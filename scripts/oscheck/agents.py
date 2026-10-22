"""Check the pinned, unmodified upstream Claude Code agent catalogue."""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from .common import Issue, is_iso_date, relative_path

LOCK = 'agents/agency-agents.lock.json'
UPSTREAM = 'https://github.com/msitarzewski/agency-agents'
EXCLUSIONS = 'agents/exclusions.txt'
SLUG = r'[a-z0-9]+(?:-[a-z0-9]+)*'


def parse_exclusions(text: str) -> list[tuple[str, str]]:
    rules: list[tuple[str, str]] = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(rf'\s*(division|agent):({SLUG})\s+#\s*(\S.*)', line)
        if not match:
            raise ValueError(f'exclusions line {number}: expected division:<name> or agent:<file-stem> followed by # reason')
        rule = (match[1], match[2])
        if rule in rules:
            raise ValueError(f'exclusions line {number}: duplicate {rule[0]}:{rule[1]}')
        rules.append(rule)
    return rules


def excluded_stems(catalogue: dict[str, str], rules: list[tuple[str, str]]) -> set[str]:
    excluded: set[str] = set()
    for kind, value in rules:
        if kind == 'division':
            matches = {stem for stem, division in catalogue.items() if division == value}
        else:
            matches = {value} if value in catalogue else set()
        if not matches:
            raise ValueError(f'unknown exclusion {kind}:{value}')
        excluded.update(matches)
    return excluded


def check_agents(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    try:
        lock = json.loads((root / LOCK).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [Issue(LOCK, 1, 'agents', f'cannot read agent lock: {exc}')]
    if not isinstance(lock, dict):
        return [Issue(LOCK, 1, 'agents', 'agent lock must be a JSON object')]
    for key, valid in (
        ('upstream', lock.get('upstream') == UPSTREAM),
        ('commit', bool(re.fullmatch(r'[0-9a-f]{40}', str(lock.get('commit', ''))))),
        ('date', is_iso_date(lock.get('date'))),
        ('licence', lock.get('licence') == 'MIT'),
        ('install_method', isinstance(lock.get('install_method'), str) and bool(lock['install_method'].strip())),
        ('install_command', isinstance(lock.get('install_command'), str) and bool(lock['install_command'].strip())),
    ):
        if not valid:
            issues.append(Issue(LOCK, 1, 'agents', f'invalid or missing {key}'))
    files = lock.get('files')
    if not isinstance(files, dict) or not files:
        return issues + [Issue(LOCK, 1, 'agents', 'files must be a non-empty path-to-sha256 mapping')]
    try:
        exclusion_bytes = (root / EXCLUSIONS).read_bytes()
        rules = parse_exclusions(exclusion_bytes.decode('utf-8'))
    except (OSError, ValueError) as exc:
        return issues + [Issue(EXCLUSIONS, 1, 'agents', f'cannot read exclusions: {exc}')]
    if hashlib.sha256(exclusion_bytes).hexdigest() != lock.get('exclusions_sha256'):
        issues.append(Issue(EXCLUSIONS, 1, 'agents', 'exclusions hash differs from lock; run scripts/sync_agents.sh'))
    catalogue = lock.get('catalogue')
    if not isinstance(catalogue, dict) or not catalogue or any(
        not re.fullmatch(SLUG, stem) or not isinstance(division, str) or not re.fullmatch(SLUG, division)
        for stem, division in catalogue.items()
    ):
        return issues + [Issue(LOCK, 1, 'agents', 'catalogue must map upstream file stems to divisions')]
    try:
        excluded = excluded_stems(catalogue, rules)
    except ValueError as exc:
        return issues + [Issue(EXCLUSIONS, 1, 'agents', str(exc))]
    expected_files = {f'.claude/agents/{stem}.md' for stem in catalogue.keys() - excluded}
    if set(files) != expected_files:
        issues.append(Issue(LOCK, 1, 'agents', 'file list must include every included agent and no excluded agents'))
    counts = {
        'included_count': len(expected_files),
        'excluded_count': len(excluded),
        'upstream_agent_count': len(catalogue),
    }
    for key, expected_count in counts.items():
        if type(lock.get(key)) is not int or lock[key] != expected_count:
            issues.append(Issue(LOCK, 1, 'agents', f'{key} does not match catalogue and exclusions count'))
    expected_divisions = dict(sorted(Counter(division for stem, division in catalogue.items() if stem not in excluded).items()))
    if lock.get('division_counts') != expected_divisions:
        issues.append(Issue(LOCK, 1, 'agents', 'division counts do not match included agents'))
    count = lock.get('agent_count')
    if type(count) is not int or count < 1 or count != len(files):
        issues.append(Issue(LOCK, 1, 'agents', 'agent count must match the lock file count'))
    directory = root / '.claude' / 'agents'
    if directory.is_symlink():
        return issues + [Issue('.claude/agents', 1, 'agents', 'agent directory must not be a symlink')]
    actual = {
        relative_path(root, path): path
        for path in directory.rglob('*')
        if path.is_file() or path.is_symlink()
    }
    if len(actual) != count:
        issues.append(Issue(LOCK, 1, 'agents', 'installed agent count does not match lock'))
    for stem in sorted(excluded):
        rel = f'.claude/agents/{stem}.md'
        if rel in actual:
            issues.append(Issue(rel, 1, 'agents', 'excluded agent must not be installed'))
    for rel, expected in files.items():
        valid_path = bool(re.fullmatch(r'\.claude/agents/[a-z0-9]+(?:-[a-z0-9]+)*\.md', rel))
        if not valid_path:
            issues.append(Issue(LOCK, 1, 'agents', f'invalid agent path: {rel}'))
        if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
            issues.append(Issue(LOCK, 1, 'agents', f'invalid sha256 for {rel}'))
        if not valid_path:
            continue
        path = actual.get(rel)
        if path is None:
            issues.append(Issue(rel, 1, 'agents', 'locked agent is missing'))
        elif path.is_symlink():
            issues.append(Issue(rel, 1, 'agents', 'agent must not be a symlink'))
        else:
            try:
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
            except OSError as exc:
                issues.append(Issue(rel, 1, 'agents', f'cannot read agent: {exc}'))
                continue
            if digest != expected:
                issues.append(Issue(rel, 1, 'agents', 'agent hash differs from lock; reinstall with scripts/sync_agents.sh'))
    for extra in sorted(actual.keys() - files.keys()):
        issues.append(Issue(extra, 1, 'agents', 'unlisted agent file; regenerate from upstream'))
    return issues
