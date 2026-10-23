#!/usr/bin/env python3
"""One-time, explicit import of audited local material. Normal builds need no Mac paths."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

import yaml

SKIP = {'.git', 'node_modules', '__pycache__', '.venv', '.cache', 'dist', 'build', 'coverage', 'benchmarks', 'bench', '.DS_Store', 'screenshots', 'recordings', '.gitignore', '.gitattributes'}
NOTICE = re.compile(r'(?i)^(?:licen[cs]e|notice|copyright|third.party.notices)(?:[._-].*)?$')
PERSONAL = re.compile(r'(?:/Users/([^\s/`"<>]+)|/home/([^\s/`"<>]+))')
EXAMPLE_USERS = {'user','username','you','name','alice','me','u','x','data','vercel-sandbox','...','<user>','<username>'}
EMAIL = re.compile(r'(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}')
# These are code references, environment names or clearly fake tutorial literals.
CREDENTIAL_SAFE = re.compile(r'(?i)process\.env|os\.environ|accessToken:\s*mapboxAccessToken|\$\{|your[_-]|example|placeholder|<[^>]+>|test[_-]|dummy|changeme|FAKE')
ACCOUNT_IDS = {'plugin-account-synced-'+x+'-marketplace' for x in ('agency-mcp','design-skills','design-steward','design-superpowers','superdesign','superpowers','vectorlab-ux-skills')}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def portable(value: str) -> str:
    value = value.replace(str(Path.home()), '~')
    value = re.sub(r'(?<=/synced/)[^/]+', 'ACCOUNT', value)
    value = re.sub(r'(?<=/ACCOUNT/)[0-9a-f-]{36}(?:~g\d+)?', 'PLUGIN', value)
    return value


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + '\n')


def rejected(path: Path, text: str, findings: list[dict]) -> str | None:
    if path.name.startswith('.env') or path.suffix.lower() in {'.pem', '.key', '.pyc', '.map', '.lock'}:
        return 'secret-bearing filename, cache or generated lock/map'
    if '\x00' in text:
        return 'binary content'
    # Real identifiable home paths are excluded, even if committed upstream.
    if any((m.group(1) or m.group(2)).rstrip('.,);:') not in EXAMPLE_USERS for m in PERSONAL.finditer(text)):
        return 'identifiable personal home path; excluded unchanged'
    if re.search(r'-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----', text):
        return 'private-key-shaped content; excluded conservatively'
    if re.search(r'\b(?:AIza[0-9A-Za-z_-]{35}|gh[pous]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b', text):
        return 'credential-shaped literal; excluded conservatively'
    if re.search(r'(?i)(?:api[-_]?key|access[-_]?token)=[0-9a-f]{20,}', text):
        return 'literal API/search key; public scope unverified, excluded'
    # Do not publish local account settings, telemetry or user/session payloads.
    if path.name in {'settings.local.json', 'auth.json', 'credentials.json', '.mcp.json', '.lsp.json'}:
        return 'account/server configuration is represented by a template instead'
    for finding in findings:
        if finding['category'] in {'credential-assignment','service-api-token','private-key'}:
            lines = text.splitlines()
            line = lines[finding['line']-1] if len(lines) >= finding['line'] else ''
            if not CREDENTIAL_SAFE.search(line):
                return 'audit credential indicator without a provably fake value; excluded'
    return None


def selected_files(root: Path):
    if root.is_file():
        yield root, Path('agents') / root.name
        return
    if (root / 'SKILL.md').is_file():
        for path in sorted(root.rglob('*')):
            if path.is_file() and not SKIP.intersection(path.relative_to(root).parts):
                yield path, Path('skills') / root.name / path.relative_to(root)
        return
    if root.name == 'agents':
        for path in sorted(root.rglob('*.md')):
            yield path, Path('agents') / path.relative_to(root)
        return
    # Broad plugin boundaries: only skill trees, agent prompts, command/hook text,
    # manifests and supporting scripts; no MCP server src or runtime bundles.
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if SKIP.intersection(rel.parts) or not path.is_file():
            continue
        top = rel.parts[0]
        if NOTICE.match(path.name):
            yield path, rel
        elif top in {'skills','agents','commands','hooks','scripts','.claude-plugin','.codex-plugin'}:
            if top != 'agents' or path.suffix == '.md':
                yield path, rel
        elif 'skills' in rel.parts[:-1] or (path.suffix == '.md' and 'agents' in rel.parts[:-1]):
            yield path, rel
        elif top == '.codex-marketplace' and ('skills' in rel.parts or NOTICE.match(path.name)):
            yield path, rel


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit-dir', type=Path, required=True)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    repo, audit = args.repo, args.audit_dir
    packages = yaml.safe_load((audit / 'packages.yaml').read_text())['packages']
    local = json.loads((audit / 'local-evidence.json').read_text())
    hits = json.loads((audit / 'secret-scan.json').read_text())['hits']
    hits_by_path = {}
    for h in hits:
        hits_by_path.setdefault(h['path'], []).append(h)
    base = repo / 'toolkit'
    if (base / 'vendor').exists():
        raise SystemExit('Refusing to replace an existing vendor snapshot. Move it aside for an explicitly reviewed re-import.')
    (base / 'vendor').mkdir(parents=True)
    normalized, source_map, materials = [], {}, {}
    canonical = {}
    exclusions = {}
    review = []
    for package in packages:
        package_id = package['id']
        action = package['class']
        reason = package['reason']
        account_decision = None
        if package_id in ACCOUNT_IDS:
            evidence = [e for e in package['licence_evidence'] if e.get('licence') in {'MIT','Apache-2.0'} and e.get('path') and Path(e['path']).is_file()]
            if evidence:
                action = 'VENDOR';reason = 'Founder 2026-10-23 account-synced permissive exception; installed licence verified'
                account_decision = 'VENDOR: installed licence file/declaration travels with material'
            else:
                action = 'MANUAL';account_decision = 'MANUAL: no installed licence file/declaration verified'
        if package_id in {'mcp-chrome-devtools','mcp-gsc'}:
            action = 'FETCH';reason = 'MCP implementation excluded from vendor; pinned public source only'
        if package_id == 'pack-agency-agents':
            action = 'EXISTING';reason = 'Already vendored under .claude/agents and agents/agency-agents.lock.json'
        if package_id == 'pack-founder-3rdwrong-skills':
            action = 'EXISTING';reason = 'Original skills already in skills/3w-*; installed directly from canonical repo files'
        if package_id == 'archive-master-of-20261021-untraced':
            action = 'MANUAL';reason = 'Explicitly excluded: unknown origin archive; parent handles separately'
        record = {k: package.get(k) for k in ('id','kind','upstream_url','pinned_ref','versions','licence','tool_ids','tool_count','installer_commit','installer_pin_basis','licence_scope','pin_status')}
        record.update({'class': action, 'audit_class': package['class'], 'reason': reason, 'notices': [], 'account_decision': account_decision})
        if action == 'FETCH' and not record.get('installer_commit'):
            pin = next((x for x in package.get('pinned_ref',[]) if re.fullmatch('[a-f0-9]{40}',x)), None)
            if not pin:
                slug = package['upstream_url'].replace('https://github.com/','')
                pin = subprocess.check_output(['gh','api',f'repos/{slug}/commits','--jq','.[0].sha'], text=True).strip()
            record['installer_commit'] = pin
            record['installer_pin_basis'] = 'explicit public installation snapshot; not proof of installed identity'
        normalized.append(record)
        if action != 'VENDOR':
            continue
        if package['licence'] == 'none-found' and package_id == 'pack-founder-local-agents':
            record['licence'] = 'CC-BY-4.0'
            record['reason'] += '; founder-owned written material follows repository documentation licence'
        dest = base / 'vendor' / package_id
        dest.mkdir()
        provenance = {'package': package_id, 'upstream_url': package['upstream_url'], 'pinned_ref': package.get('pinned_ref') or package.get('versions') or ['unresolved'], 'licence': record['licence'], 'evidence_path': 'toolkit/sources/packages.json#'+package_id, 'copied_from': [portable(x) for x in package['material_roots']], 'copied_on': str(date.today()), 'files': {}, 'notices': [], 'excluded': []}
        candidates = []
        for root_string in package['material_roots']:
            root = Path(root_string)
            if not root.exists():
                provenance['excluded'].append({'source':portable(root_string),'reason':'source missing at import'})
                continue
            candidates.extend(selected_files(root))
        # Exact original notices from every audited installed evidence location,
        # including upstream ancestor licences outside the narrow skill slice.
        for e in package['licence_evidence']:
            path = Path(e.get('path',''))
            if path.is_file() and (NOTICE.match(path.name) or e.get('source') in {'manifest','readme-licence-section'}):
                candidates.append((path, Path('notices') / (sha(path.read_bytes())[:12]+'-'+path.name)))
        if package_id == 'pack-founder-local-agents':
            candidates.append((repo / 'LICENSE-DOCS', Path('LICENSE-DOCS')))
        used = {}
        for path, relative in candidates:
            try:
                data = path.read_bytes(); text = data.decode('utf-8')
            except (OSError,UnicodeDecodeError):
                provenance['excluded'].append({'source': portable(str(path)), 'reason':'binary/non-UTF8 or unreadable; never distributed'})
                continue
            finding_list = hits_by_path.get(str(path), [])
            why = rejected(path, text, finding_list)
            if why:
                exclusions[str(path)] = why
                provenance['excluded'].append({'source': portable(str(path)), 'reason':why})
                continue
            digest = sha(data)
            if str(relative).casefold() in used and used[str(relative).casefold()] != digest:
                relative = relative.parent / (relative.stem + '-' + digest[:10] + relative.suffix)
            used[str(relative).casefold()] = digest
            target = dest / relative
            if target.exists() or target.is_symlink():
                source_map[str(path)] = target.relative_to(repo).as_posix()
                source_map[str(path.resolve())] = target.relative_to(repo).as_posix()
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            key = (digest, path.stat().st_mode & 0o111)
            # Notices remain exact regular files in each package. Other identical
            # files have one canonical repo copy and relative aliases.
            alias = canonical.get(key) if not NOTICE.match(path.name) else None
            if alias:
                target.symlink_to(os.path.relpath(alias, target.parent))
            else:
                target.write_bytes(data)
                target.chmod(0o755 if path.stat().st_mode & 0o111 else 0o644)
                canonical.setdefault(key, target)
            rel_repo = target.relative_to(repo).as_posix()
            source_map[str(path)] = rel_repo
            source_map[str(path.resolve())] = rel_repo
            provenance['files'][relative.as_posix()] = {'sha256':digest,'copied_from':portable(str(path))}
            if alias:
                provenance['files'][relative.as_posix()]['alias_of'] = alias.relative_to(repo).as_posix()
            if NOTICE.match(path.name) or relative.parts[0]=='notices':
                provenance['notices'].append(relative.as_posix())
                record['notices'].append(rel_repo)
        (dest / 'PROVENANCE.yaml').write_text(yaml.safe_dump(provenance, sort_keys=False, allow_unicode=True))
        print(package_id, len(provenance['files']), 'files', len(provenance['excluded']), 'excluded')
    by_id = {x['id']:x for x in normalized}
    membership = {t:p['id'] for p in packages for t in p['tool_ids']}
    for tool in local:
        tool_id = tool['tool_id']; package_id = membership[tool_id]; record=by_id[package_id]
        path = Path(tool.get('resolved_path') or '')
        source = source_map.get(str(path)) or source_map.get(str(path.resolve()))
        kind = 'agent' if tool['kind'] in {'agent','upstream-agent'} else 'skill'
        if record['class']=='EXISTING':
            if package_id=='pack-agency-agents':
                source = '.claude/agents/' + path.name
            elif path.name=='SKILL.md':
                source = 'skills/' + path.parent.name + '/SKILL.md'
        if source:
            materials[tool_id] = {'package':package_id,'source':str(Path(source).parent) if kind=='skill' else source,'kind':kind,'distribution':'vendor'}
        elif record['class']=='FETCH':
            name = path.parent.name if path.name=='SKILL.md' else tool_id.rsplit(':',1)[-1]
            candidates = []
            text_path = str(path)
            for marker in ('/skills/','/plugins/','/external_plugins/'):
                if marker in text_path:
                    candidates.append(marker.strip('/')+'/'+text_path.split(marker,1)[1].removesuffix('/SKILL.md'))
            materials[tool_id] = {'package':package_id,'kind':kind,'distribution':'fetch','upstream_name':name,'candidates':candidates}
        elif record['class']=='VENDOR':
            record.setdefault('excluded_tool_ids',[]).append(tool_id)
    for n,h in enumerate(hits,1):
        path = Path(h['path']); source=source_map.get(str(path)) or source_map.get(str(path.resolve()))
        reason=exclusions.get(str(path))
        if source:
            if h['category']=='email-address':
                decision='KEEP: upstream public attribution/support/example address; original notice retained where applicable'
            elif h['category']=='personal-path':
                decision='KEEP: generic tutorial username or documented sandbox path, not an identifiable personal path'
            else:
                decision='KEEP: environment lookup or clearly fake tutorial placeholder; no literal live credential'
        else:
            decision='EXCLUDE: '+(reason or 'outside the permitted material slice, or package is FETCH/MANUAL/already vendored')
        review.append({'finding':n,'package':h['package_id'],'source':portable(h['path']),'line':h['line'],'category':h['category'],'value':'[REDACTED]','decision':decision,'vendored_path':source})
    # Portable source snapshots are sufficient to regenerate every public view.
    dump(base / 'sources/packages.json', {'audit_generated_at':yaml.safe_load((audit/'packages.yaml').read_text())['audit']['generated_at'], 'audit_sha256':sha((audit/'packages.yaml').read_bytes()), 'packages':normalized})
    dump(base / 'sources/materials.json', materials)
    dump(base / 'sources/security-review.json', {'findings':review,'policy':'Every audit finding resolved by exact file selection; values omitted.'})
    print('TOTAL',len([p for p in normalized if p['class']=='VENDOR']),len(materials),'mapped tools')


if __name__=='__main__':
    main()
