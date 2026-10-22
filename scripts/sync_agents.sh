#!/usr/bin/env bash
# Reinstall upstream Claude Code agents minus the reviewed exclusions; never install globally.
set -euo pipefail
repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
upstream_url='https://github.com/msitarzewski/agency-agents'
lock_path="$repo_root/agents/agency-agents.lock.json"
cd "$repo_root"

usage() {
  printf '%s\n' 'Usage: scripts/sync_agents.sh [--upgrade [40-character-SHA]]' \
    'No arguments: reinstall the locked SHA. --upgrade: resolve upstream HEAD or use the supplied SHA.'
}
upgrade=false
case "${1:-}" in
  '') [[ $# -eq 0 ]] || { usage >&2; exit 2; } ;;
  --help|-h) usage; exit 0 ;;
  --upgrade) upgrade=true; shift; [[ $# -le 1 ]] || { usage >&2; exit 2; } ;;
  *) usage >&2; exit 2 ;;
esac
if $upgrade; then
  if [[ $# -eq 1 ]]; then
    commit_sha="$1"
  else
    commit_sha="$(git ls-remote "$upstream_url" HEAD | awk 'NR == 1 {print $1}')"
  fi
else
  commit_sha="$(uv run --locked python - "$lock_path" "$upstream_url" <<'PY'
import json, sys
from pathlib import Path
lock = json.loads(Path(sys.argv[1]).read_text())
if lock.get('upstream') != sys.argv[2]:
    raise SystemExit('Unexpected upstream URL in lock')
print(lock['commit'])
PY
)"
fi
[[ "$commit_sha" =~ ^[0-9a-f]{40}$ ]] || { printf '%s\n' 'Expected a full lowercase commit SHA' >&2; exit 2; }
stage_dir="$(mktemp -d "${TMPDIR:-/tmp}/3w-agency-sync.XXXXXX")"
trap 'rm -rf "$stage_dir"' EXIT
# All Git writes are confined to this disposable upstream clone.
git clone --quiet --no-checkout "$upstream_url" "$stage_dir/upstream"
git -C "$stage_dir/upstream" checkout --quiet --detach "$commit_sha"
[[ "$(git -C "$stage_dir/upstream" rev-parse HEAD)" == "$commit_sha" ]]

uv run --locked python - "$repo_root" "$stage_dir" "$commit_sha" "$upstream_url" <<'PY'
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path

root, stage = map(Path, sys.argv[1:3])
commit, upstream_url = sys.argv[3:5]
source = stage / 'upstream'
sys.path.insert(0, str(root))
from scripts.oscheck.agents import excluded_stems, parse_exclusions
exclusion_bytes = (root / 'agents/exclusions.txt').read_bytes()
rules = parse_exclusions(exclusion_bytes.decode('utf-8'))
tools = json.loads((source / 'tools.json').read_text())
if tools['tools']['claude-code']['format'] != 'identity':
    raise SystemExit('Claude Code render format changed; review the updater before upgrading')
divisions = list(json.loads((source / 'divisions.json').read_text())['divisions']) + ['strategy']
# Match upstream is_agent_file: a Markdown file whose first line is ---.
agents = sorted(p for division in divisions for p in (source / division).rglob('*.md')
                if p.is_file() and p.read_text().splitlines()[:1] == ['---'])
collisions = [name for name, count in Counter(p.name.casefold() for p in agents).items() if count > 1]
if not agents or collisions:
    raise SystemExit(f'Empty catalogue or colliding filenames: {collisions}')
if any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*\.md', p.name) for p in agents):
    raise SystemExit('Unexpected upstream filename; review before installing')
licence = (source / 'LICENSE').read_text()
if not licence.startswith('MIT License\n'):
    raise SystemExit('Upstream licence changed; review before upgrading')
rendered = stage / 'rendered'
subprocess.run(['bash', str(source / 'scripts/install.sh'), '--tool', 'claude-code',
                '--no-interactive', '--path', str(rendered)], cwd=source, check=True)
expected = {p.name: p.read_bytes() for p in agents}
installed = {p.name: p.read_bytes() for p in rendered.iterdir() if p.is_file()}
if expected != installed or len(installed) != len(agents):
    raise SystemExit('Installer output differs from complete upstream identity-format catalogue')
catalogue = dict(sorted((p.stem, p.relative_to(source).parts[0]) for p in agents))
excluded = excluded_stems(catalogue, rules)
installed = {name: data for name, data in installed.items() if Path(name).stem not in excluded}
for path in rendered.iterdir():
    if path.stem in excluded:
        path.unlink()
if not installed:
    raise SystemExit('Exclusions would remove every agent; review before installing')
lock_path = root / 'agents/agency-agents.lock.json'
old_lock = json.loads(lock_path.read_text()) if lock_path.exists() else {}
lock = {
    'upstream': upstream_url,
    'commit': commit,
    'date': old_lock.get('date', date.today().isoformat()) if old_lock.get('commit') == commit else date.today().isoformat(),
    'licence': 'MIT',
    'install_method': 'upstream Claude Code installer (identity format), then exclusions.txt filter',
    'install_command': 'bash scripts/install.sh --tool claude-code --no-interactive --path <repo>/.claude/agents',
    'agent_count': len(installed),
    'included_count': len(installed),
    'excluded_count': len(excluded),
    'upstream_agent_count': len(agents),
    'exclusions_file': 'agents/exclusions.txt',
    'exclusions_sha256': hashlib.sha256(exclusion_bytes).hexdigest(),
    'catalogue': catalogue,
    'division_counts': dict(sorted(Counter(division for stem, division in catalogue.items() if stem not in excluded).items())),
    'files': {f'.claude/agents/{name}': hashlib.sha256(data).hexdigest()
              for name, data in sorted(installed.items())},
}
claude = root / '.claude'
claude.mkdir(exist_ok=True)
destination = claude / 'agents'
if destination.is_symlink() or any(p.is_symlink() for p in destination.rglob('*')):
    raise SystemExit('Refusing to replace a symlinked agent catalogue')
if destination.exists():
    current = {p.relative_to(root).as_posix() for p in destination.rglob('*') if p.is_file()}
    extras = current - set(old_lock.get('files', {}))
    if extras:
        raise SystemExit(f'Unlisted local files would be removed; review them first: {sorted(extras)}')
# Stage on the same filesystem so the directory replacement uses atomic renames.
with tempfile.TemporaryDirectory(prefix='.agents-sync-', dir=claude) as work_dir:
    work = Path(work_dir)
    candidate = work / 'agents'
    shutil.copytree(rendered, candidate)
    previous = work / 'previous'
    if destination.exists():
        os.replace(destination, previous)
    try:
        os.replace(candidate, destination)
        lock_path.parent.mkdir(exist_ok=True)
        pending_lock = lock_path.with_suffix('.json.tmp')
        pending_lock.write_text(json.dumps(lock, indent=2) + '\n')
        os.replace(pending_lock, lock_path)
    except BaseException:
        if destination.exists():
            shutil.rmtree(destination)
        if previous.exists():
            os.replace(previous, destination)
        raise
notice = '# Third-party notices\n\n## Agency Agents\n\n'
notice += f'Files in `.claude/agents/` originate from [{upstream_url}]({upstream_url}), pinned by [the agent lock](agents/agency-agents.lock.json).\n\n'
notice += 'The following is the upstream `LICENSE`, reproduced verbatim.\n\n```text\n' + licence.rstrip('\n') + '\n```\n'
(root / 'THIRD_PARTY_NOTICES.md').write_text(notice)
print(f'Installed {len(installed)} included / {len(excluded)} excluded of {len(agents)} agents at {commit}; filename collisions: 0; lock regenerated.')
PY
