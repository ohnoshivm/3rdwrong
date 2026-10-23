from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from .common import Issue, is_iso_date, parse_frontmatter, relative_path, strip_markdown_code

CARD_FIELDS = (
    'title', 'type', 'status', 'owner', 'last_reviewed', 'tool_id', 'department',
    'sub_department', 'job', 'role', 'trigger', 'kind', 'availability',
    'distribution', 'source', 'invoke', 'pairs_with',
)
CARD_SECTIONS = (
    'What it does', 'When to use', 'When not to use', 'Inputs it needs',
    'How to run it', 'What good output looks like', 'Quality checks',
    'Pairs with', 'Limits and cautions',
)
ACTIVE_ROLES = {'lead', 'specialist'}


def load_registry(root: Path) -> tuple[list[dict], dict[str, dict]]:
    """Resolve both canonical IDs and aliases without silently shadowing tools."""
    data = json.loads((root / 'toolkit/sources/registry.json').read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('tools'), list):
        raise ValueError('registry must contain a tools list')
    tools = data['tools']
    by_id: dict[str, dict] = {}
    canonical: set[str] = set()
    for tool in tools:
        if not isinstance(tool, dict) or not all(isinstance(tool.get(k), str) and tool[k] for k in
                ('id', 'department', 'sub_department', 'job', 'role')):
            raise ValueError('registry tools require string id, department, sub_department, job and role')
        for key in ('department', 'sub_department'):
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', tool[key]):
                raise ValueError(f"registry {key} must be a slug for '{tool['id']}'")
        if tool['id'] in canonical:
            raise ValueError(f"duplicate registry id '{tool['id']}'")
        canonical.add(tool['id'])
        aliases = tool.get('aliases', [])
        if not isinstance(aliases, list) or any(not isinstance(a, str) or not a for a in aliases):
            raise ValueError(f"invalid aliases for '{tool['id']}'")
        for identity in (tool['id'], *aliases):
            if identity in by_id and by_id[identity]['id'] != tool['id']:
                raise ValueError(f"ambiguous registry alias '{identity}'")
            by_id[identity] = tool
    return tools, by_id


def card_paths(root: Path) -> list[Path]:
    # Only the generated folder README is not a tool card. Include misplaced
    # files at any depth so the path rule cannot be bypassed.
    return sorted(p for p in (root / 'toolkit/cards').rglob('*.md')
                  if p != root / 'toolkit/cards/README.md' and p.is_file())


def card_slug(identity: str) -> str:
    return re.sub(r'[^a-z0-9-]', '-', identity.lower().replace(':', '--'))


def read_cards(root: Path, by_id: dict[str, dict]) -> dict[str, tuple[Path, dict, str]]:
    cards = {}
    for path in card_paths(root):
        parsed = parse_frontmatter(path.read_text(encoding='utf-8'))
        identity = (parsed.data or {}).get('tool_id')
        if isinstance(identity, str) and identity in by_id:
            cards.setdefault(by_id[identity]['id'], (path, parsed.data, parsed.body))
    return cards


def check_cards(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    try:
        tools, by_id = load_registry(root)
    except (OSError, ValueError, TypeError) as exc:
        return [Issue('toolkit/sources/registry.json', 1, 'cards', f'cannot read registry: {exc}')]
    covered: dict[str, str] = {}
    required = config.get('cards', {}).get('required_fields', CARD_FIELDS)
    for path in card_paths(root):
        rel = relative_path(root, path)
        text = path.read_text(encoding='utf-8')
        parsed = parse_frontmatter(text)
        if len(text.splitlines()) > 90:
            issues.append(Issue(rel, 1, 'cards', 'card exceeds 90 lines; keep it readable in two minutes', 'warning'))
        if parsed.data is None:
            issues.append(Issue(rel, parsed.error_line, 'cards', parsed.error))
            continue
        data = parsed.data
        for key in required:
            if key not in data:
                issues.append(Issue(rel, 2, 'cards', f"missing required key '{key}'"))
            elif key not in {'pairs_with', 'last_reviewed'} and (
                    not isinstance(data[key], str) or (not data[key].strip() and key != 'trigger')):
                issues.append(Issue(rel, 2, 'cards', f"'{key}' must be a non-empty string"))
        if data.get('type') != 'tool-card':
            issues.append(Issue(rel, 2, 'cards', "type must be 'tool-card'"))
        status = data.get('status')
        if not isinstance(status, str) or status not in config.get('statuses', ['proposed']):
            issues.append(Issue(rel, 2, 'cards', f"invalid status '{status}'"))
        if status == 'approved' and (not isinstance(data.get('approved_by'), str)
                or not data['approved_by'].strip() or not is_iso_date(data.get('approved_on'))):
            issues.append(Issue(rel, 2, 'cards', 'approved status requires named approved_by and ISO approved_on'))
        if not is_iso_date(data.get('last_reviewed')):
            issues.append(Issue(rel, 2, 'cards', 'last_reviewed must be an ISO date (YYYY-MM-DD)'))
        for key, choices in (
            ('availability', {'claude', 'codex', 'both', 'mcp', 'repo', 'claude-managed'}),
            ('distribution', {'vendor', 'fetch', 'manual', 'repo'}),
        ):
            if not isinstance(data.get(key), str) or data[key] not in choices:
                issues.append(Issue(rel, 2, 'cards', f"invalid {key}; expected one of {', '.join(sorted(choices))}"))
        pairs = data.get('pairs_with')
        if not isinstance(pairs, list):
            issues.append(Issue(rel, 2, 'cards', 'pairs_with must be a list of registry ids'))
        else:
            for identity in pairs:
                if not isinstance(identity, str) or identity not in by_id:
                    issues.append(Issue(rel, 2, 'cards', f"unknown pairs_with id '{identity}'"))
        identity = data.get('tool_id')
        tool = by_id.get(identity) if isinstance(identity, str) else None
        if tool is None:
            issues.append(Issue(rel, 2, 'cards', f"unknown tool_id '{identity}'"))
        else:
            canonical = tool['id']
            if canonical in covered:
                issues.append(Issue(rel, 2, 'cards', f"duplicate card for '{canonical}'; already in {covered[canonical]}"))
            covered[canonical] = rel
            for key in ('department', 'sub_department', 'job', 'role'):
                if data.get(key) != tool[key]:
                    issues.append(Issue(rel, 2, 'cards', f"{key} '{data.get(key)}' does not match; registry value is '{tool[key]}'"))
            if tool['role'] not in ACTIVE_ROLES:
                issues.append(Issue(rel, 2, 'cards', f"no card allowed for registry role '{tool['role']}' ({canonical})"))
            if tool['role'] == 'specialist' and not str(data.get('trigger') or '').strip():
                issues.append(Issue(rel, 2, 'cards', 'specialist trigger must not be empty'))
            expected = f"toolkit/cards/{tool['department']}/{tool['sub_department']}/{card_slug(identity)}.md"
            if rel != expected:
                issues.append(Issue(rel, 1, 'cards', f'card path must be {expected}'))
        clean = strip_markdown_code(parsed.body)
        if len(re.findall(r'^ {0,3}#\s+\S', clean, re.MULTILINE)) != 1:
            issues.append(Issue(rel, parsed.body_line, 'cards', 'card must have exactly one H1'))
        headings = re.findall(r'^ {0,3}##\s+(.+?)\s*#*\s*$', clean, re.MULTILINE)
        required_headings = [h for h in headings if h in CARD_SECTIONS]
        if required_headings != list(CARD_SECTIONS):
            issues.append(Issue(rel, parsed.body_line, 'cards', 'required H2 sections must appear once in order: ' + '; '.join(CARD_SECTIONS)))
    missing: dict[str, list[str]] = defaultdict(list)
    for tool in tools:
        if tool['role'] in ACTIVE_ROLES and tool['id'] not in covered:
            missing[tool['department']].append(tool['id'])
    settings = config.get('cards', {})
    strict = settings.get('strict_departments', [])
    for department, identities in sorted(missing.items()):
        severity = 'error' if settings.get('strict', False) or department in strict else 'warning'
        issues.append(Issue('toolkit/cards', 1, 'cards',
            f"{department}: missing {len(identities)} lead/specialist card(s): {', '.join(sorted(identities))}", severity))
    return issues


def check_handbook(root: Path, config: dict) -> list[Issue]:
    try:
        from ..build_handbook import build_handbook, stale_outputs
    except ImportError:
        from build_handbook import build_handbook, stale_outputs
    try:
        expected = build_handbook(root)
        return [Issue(path, 1, 'handbook', 'generated handbook is stale; run `uv run python scripts/build_handbook.py`')
                for path in stale_outputs(root, expected)]
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return [Issue('handbook/README.md', 1, 'handbook', f'cannot verify handbook: {exc}')]
