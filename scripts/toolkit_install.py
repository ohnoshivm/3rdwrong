#!/usr/bin/env python3
"""Install the generated toolkit plan without executing third-party setup code."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

# Department groups from the registry: Craft; Growth; Delivery + Studio. The core
# 3w-* skills install with every profile; minimal installs only them.
PROFILES = {
    'full': None,
    'design-engineering': {'design', 'engineering', 'labs'},
    'growth': {'marketing', 'advertising', 'outbound', 'sales'},
    'studio': {'strategy', 'production', 'media', 'operations'},
    'minimal': set(),
}
ACTIVE = {'lead', 'specialist'}
FETCH_TIMEOUT = int(os.environ.get('TOOLKIT_FETCH_TIMEOUT', '1800'))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_child(base: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError(f'unsafe relative path: {relative}')
    result = base / path
    if not result.resolve().is_relative_to(base.resolve()):
        raise ValueError(f'path escapes its root: {relative}')
    return result


class Installer:
    def __init__(self, repo: Path, home: Path, dry_run: bool):
        self.repo = repo.resolve()
        self.home = home.resolve()
        self.dry_run = dry_run
        self.counts: Counter = Counter()
        self.state_path = self.destination('.3rdwrong/install-state.json')
        self.state = {'schema_version': 1, 'links': {}, 'templates': {}, 'fetch': {}, 'created_dirs': []}
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text())
            self.state.setdefault('created_dirs', [])

    def destination(self, relative: str) -> Path:
        # Resolve parents only: an owned leaf symlink may legitimately point to the repo.
        parts = Path(relative).parts
        if not parts or parts[0] not in {'.claude', '.agents', '.3rdwrong'}:
            raise ValueError(f'unapproved HOME destination: {relative}')
        path = self.home / relative
        if '..' in parts or not path.parent.resolve().is_relative_to(self.home):
            raise ValueError(f'HOME parent symlink escapes HOME: {relative}')
        return path

    def ensure_dir(self, path: Path):
        # Record every directory this installer creates so uninstall can remove
        # exactly those (when empty) and never a folder the user already had.
        missing = []
        while not path.exists() and path != self.home:
            missing.append(path)
            path = path.parent
        for directory in reversed(missing):
            directory.mkdir()
            relative = directory.relative_to(self.home).as_posix()
            if relative not in self.state['created_dirs']:
                self.state['created_dirs'].append(relative)

    def selected(self, item: dict, profile: str) -> bool:
        return item.get('department') == 'core' or PROFILES[profile] is None or item.get('department') in PROFILES[profile]

    def link(self, source: Path, relative: str, category: str):
        target = self.destination(relative)
        if target.is_symlink() and target.resolve() == source.resolve():
            self.counts['unchanged'] += 1
            return
        if target.exists() or target.is_symlink():
            print(f'CONFLICT {relative}: keeping existing entry')
            self.counts['conflicts'] += 1
            return
        self.counts[category] += 1
        if self.dry_run:
            print(f'LINK {relative}')
            return
        self.ensure_dir(target.parent)
        target.symlink_to(source, target_is_directory=source.is_dir())
        self.state['links'][relative] = str(source)

    def template(self, name: str, value: dict):
        if Path(name).name != name:
            raise ValueError('unsafe template name')
        relative = f'.3rdwrong/mcp-templates/{name}'
        target = self.destination(relative)
        content = (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()
        if target.exists() or target.is_symlink():
            if target.is_symlink() or target.read_bytes() != content:
                print(f'CONFLICT {relative}: keeping existing template')
                self.counts['conflicts'] += 1
            else:
                self.counts['unchanged'] += 1
            return
        self.counts['templates'] += 1
        if not self.dry_run:
            self.ensure_dir(target.parent)
            target.write_bytes(content)
            self.state['templates'][relative] = digest(content)

    def fetch(self, package: dict) -> Path | None:
        package_id, commit = package['id'], package['commit']
        if not re.fullmatch(r'[a-z0-9][a-z0-9.-]*', package_id) or not re.fullmatch(r'[a-f0-9]{40}', commit):
            raise ValueError('FETCH requires a safe package ID and full immutable commit')
        url = package['upstream_url']
        if not re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:\.git)?', url):
            raise ValueError('FETCH URL must be a public HTTPS GitHub repository')
        relative = f'.3rdwrong/fetch/{package_id}'
        dest = self.destination(relative)
        if self.dry_run:
            print(f'FETCH {package_id} @{commit}')
            self.counts['fetch_planned'] += 1
            return None
        if dest.is_symlink():
            raise ValueError(f'FETCH destination is a symlink: {relative}')
        env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1', GIT_TERMINAL_PROMPT='0', GIT_LFS_SKIP_SMUDGE='1')
        for key in list(env):
            if key.startswith('GIT_') and key not in {'GIT_CONFIG_GLOBAL', 'GIT_CONFIG_NOSYSTEM', 'GIT_TERMINAL_PROMPT', 'GIT_LFS_SKIP_SMUDGE'}:
                del env[key]
        def git(*args, capture=False):
            return subprocess.run(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'core.fsmonitor=false', '-c', 'protocol.file.allow=never', *args], cwd=dest, env=env, check=True, text=True, stdout=subprocess.PIPE if capture else subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=FETCH_TIMEOUT)
        if dest.exists():
            if not (dest / '.git').is_dir():
                print(f'CONFLICT {relative}: not an installer checkout')
                self.counts['conflicts'] += 1
                return None
            # Never reset a user's modified checkout, including an untracked file.
            if git('status', '--porcelain', capture=True).stdout.strip():
                print(f'CONFLICT {relative}: modified checkout')
                self.counts['conflicts'] += 1
                return None
            if git('rev-parse', 'HEAD', capture=True).stdout.strip() == commit:
                self.counts['fetch_unchanged'] += 1
                return dest
            print(f'CONFLICT {relative}: existing checkout has a different pin; keeping it')
            self.counts['conflicts'] += 1
            return None
        self.ensure_dir(dest)
        print(f'FETCH {package_id} @{commit}', flush=True)
        try:
            git('init', '--quiet')
            # Request the immutable object directly; never resolve or check out moving HEAD.
            git('fetch', '--quiet', '--depth', '1', '--no-tags', url, commit)
            git('checkout', '--quiet', '--detach', commit)
            if git('rev-parse', 'HEAD', capture=True).stdout.strip() != commit:
                raise ValueError(f'FETCH pin verification failed: {package_id}')
        except Exception:
            shutil.rmtree(dest)
            raise
        self.state['fetch'][relative] = commit
        self.counts['fetch_installed'] += 1
        return dest

    def install_item(self, item: dict, tools: str, fetched: dict[str, Path]):
        if item.get('role') == 'excluded':
            return
        if item['distribution'] == 'fetch':
            root = fetched.get(item['package'])
            if root is None:
                self.counts['fetch_components_not_linked'] += 1
                return
            source = None
            for relative in item.get('candidates', []):
                candidate = safe_child(root, relative)
                if candidate.exists():
                    source = candidate
                    break
            if source is None:
                name = item.get('upstream_name') or item['id'].rsplit(':', 1)[-1]
                if item['kind'] == 'agent':
                    found = (p for p in root.rglob(name + '.md') if 'agents' in p.relative_to(root).parts)
                else:
                    found = (p.parent for p in root.rglob('SKILL.md') if p.parent.name == name)
                matches = sorted(p for p in found if '.git' not in p.relative_to(root).parts)
                source = matches[0] if matches else None
            if source is None:
                print(f'UNRESOLVED {item["id"]}: no matching component at pinned source; see toolkit/fetch.yaml')
                self.counts['unresolved'] += 1
                return
        else:
            source = safe_child(self.repo, item['source'])
        if not source.exists():
            raise ValueError(f'missing install source: {item["id"]}')
        name = item['name']
        if not re.fullmatch(r'3w-[a-z0-9][a-z0-9.-]*', name):
            raise ValueError(f'unsafe destination name: {name}')
        kind = item['kind']
        if item.get('load', 'active' if item['role'] in ACTIVE else 'library') != 'active':
            tail = f'agents/{name}.md' if kind == 'agent' else f'skills/{name}'
            self.link(source, '.claude/skills-library/3rdwrong/' + tail, 'library')
        elif kind == 'agent':
            # Codex consumes its native AGENTS.md instructions; Claude subagent format is
            # kept as a reference for Codex rather than pretending it is a native agent.
            if tools in {'claude', 'both'}:
                self.link(source, f'.claude/agents/{name}.md', 'active_agents')
            if tools == 'codex':
                self.link(source, f'.claude/skills-library/3rdwrong/agents/{name}.md', 'agent_references')
        else:
            if tools in {'claude', 'both'}:
                self.link(source, f'.claude/skills/{name}', 'active_skills')
            if tools in {'codex', 'both'}:
                self.link(source, f'.agents/skills/{name}', 'active_skills')

    def uninstall(self):
        for relative, source in list(self.state['links'].items()):
            path = self.destination(relative)
            if path.is_symlink() and os.readlink(path) == source:
                self.counts['removed_links'] += 1
                if not self.dry_run:
                    path.unlink(); del self.state['links'][relative]
            elif not self.dry_run:
                self.state['links'].pop(relative, None)
        for relative, sha in list(self.state['templates'].items()):
            path = self.destination(relative)
            if path.is_file() and not path.is_symlink() and digest(path.read_bytes()) == sha:
                self.counts['removed_templates'] += 1
                if not self.dry_run:
                    path.unlink(); del self.state['templates'][relative]
        for relative, commit in list(self.state['fetch'].items()):
            path = self.destination(relative)
            if not path.exists():
                self.state['fetch'].pop(relative)
                continue
            # A checkout with any local change or a moved HEAD may hold the user's work.
            if self.clean_checkout(path, commit):
                self.counts['removed_fetch'] += 1
                if not self.dry_run:
                    shutil.rmtree(path); del self.state['fetch'][relative]
            else:
                print(f'KEPT {relative}: modified checkout or different HEAD')
                self.counts['kept_fetch'] += 1
        if self.dry_run or self.state['links'] or self.state['templates'] or self.state['fetch']:
            return
        if self.state_path.is_file() and not self.state_path.is_symlink():
            self.state_path.unlink()
        for relative in sorted(self.state['created_dirs'], key=lambda r: r.count('/'), reverse=True):
            path = self.home / relative
            if path.is_dir() and not path.is_symlink() and not any(path.iterdir()):
                path.rmdir()
        self.state = None

    def clean_checkout(self, path: Path, commit: str) -> bool:
        try:
            def git(*args):
                return subprocess.run(['git', '-c', 'core.fsmonitor=false', *args], cwd=path, check=True, text=True, capture_output=True, timeout=60).stdout.strip()
            return (path / '.git').is_dir() and git('rev-parse', 'HEAD') == commit and git('status', '--porcelain', '--ignored') == ''
        except (OSError, subprocess.SubprocessError):
            return False

    def save(self):
        if not self.dry_run and self.state is not None:
            self.ensure_dir(self.state_path.parent)
            if self.state_path.is_symlink():
                raise ValueError('install state may not be a symlink')
            self.state_path.write_text(json.dumps(self.state, indent=2, sort_keys=True) + '\n')


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--profile', choices=PROFILES, default='full')
    parser.add_argument('--tools', choices=['claude', 'codex', 'both'], default='both')
    parser.add_argument('--uninstall', action='store_true')
    parser.add_argument('--skip-fetch', action='store_true', help='do not clone FETCH packages; their components are reported as skipped')
    args = parser.parse_args(argv)
    try:
        installer = Installer(args.repo, Path(os.environ['HOME']), args.dry_run)
        if args.uninstall:
            installer.uninstall()
        else:
            plan = json.loads((args.repo / 'toolkit/install-plan.json').read_text())
            items = [x for x in plan['items'] if installer.selected(x, args.profile)]
            # Validate all selected inputs before the first write or network request.
            for item in items:
                if item['distribution'] != 'fetch':
                    safe_child(installer.repo, item['source'])
            packages = {x['package'] for x in items if x['distribution'] == 'fetch'}
            fetched = {}
            for package in plan['fetch']:
                wanted = package['id'] in packages or (args.profile == 'full' and not package.get('component_only', False))
                if wanted and args.skip_fetch:
                    installer.counts['fetch_skipped'] += 1
                    print(f'SKIP FETCH {package["id"]} @{package["commit"]}')
                elif wanted:
                    try:
                        source = installer.fetch(package)
                    except subprocess.SubprocessError as exc:
                        # Report and continue: a failed pin is never replaced by another source.
                        print(f'FETCH FAILED {package["id"]} @{package["commit"]}: {type(exc).__name__}', file=sys.stderr)
                        installer.counts['fetch_failed'] += 1
                        continue
                    if source:
                        fetched[package['id']] = source
            for item in items:
                installer.install_item(item, args.tools, fetched)
            for name, template in plan['templates'].items():
                if args.profile != 'minimal':
                    installer.template(name, template)
            print(f'MANUAL CHECKLIST ({len(plan.get("manual", []))} packages):')
            for entry in plan.get('manual', []):
                print(f'  - {entry["id"]}: {entry["steps"]}')
        installer.save()
        print('SUMMARY ' + json.dumps(dict(sorted(installer.counts.items())), sort_keys=True))
        return 1 if installer.counts.get('unresolved') or installer.counts.get('fetch_failed') else 0
    except (ValueError, KeyError, OSError, subprocess.SubprocessError) as exc:
        print(f'ERROR {type(exc).__name__}: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
