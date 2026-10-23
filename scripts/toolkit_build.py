#!/usr/bin/env python3
"""Regenerate portable toolkit views; --check is read-only and rejects content drift."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys

import yaml

ACTIVE = {'lead', 'specialist'}
DEPARTMENTS = ['design','engineering','labs','strategy','production','media','marketing','advertising','outbound','sales','operations']
GENERATED_DIR = 'toolkit/plugins'
# Public npm launchers verified for the audited versions; other servers get a URL placeholder.
NPM_MCP = {'chrome-devtools':('chrome-devtools-mcp',[],{}),'playwright':('@playwright/mcp',[],{}),'shadcn':('shadcn',['mcp'],{}),
           'gsc':('@lukerent/google-search-console-mcp',[],{'GOOGLE_APPLICATION_CREDENTIALS':'${GOOGLE_APPLICATION_CREDENTIALS}'})}
NOTICE_START, NOTICE_END = '<!-- TOOLKIT-NOTICES:START -->', '<!-- TOOLKIT-NOTICES:END -->'


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encoded(value) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + '\n').encode()


def slug(value: str) -> str:
    return re.sub('[^a-z0-9.-]+', '-', value.lower()).strip('-')


def files_under(path: Path):
    return sorted(p for p in path.rglob('*') if (p.is_file() or p.is_symlink()) and '__pycache__' not in p.parts)


def snapshot_registry(path: Path) -> dict:
    source = yaml.safe_load(path.read_text())
    tools = source.get('tools', source.get('entries', []))
    if not isinstance(tools, list):
        raise ValueError('registry tools must be a list')
    keep = ('id','aliases','kind','role','load','department','division','sub_department','job','trigger','reason','activation')
    result = {'source_name':path.name,'source_sha256':digest(path.read_bytes()),'schema_version':source.get('schema_version',1),'tools':[]}
    for tool in tools:
        row = {k:tool[k] for k in keep if k in tool}
        row['department'] = tool.get('department') or tool.get('division') or 'operations'
        if 'load' in tool and (tool['load'] == 'active') != (tool.get('role') in ACTIVE):
            raise ValueError(f'{tool["id"]}: load {tool["load"]} contradicts role {tool.get("role")}')
        result['tools'].append(row)
    return result


def verify_vendor(repo: Path) -> tuple[list[str], list[dict]]:
    errors, records = [], []
    vendor = repo / 'toolkit/vendor'
    for package in sorted(p for p in vendor.iterdir() if p.is_dir()):
        proof = package / 'PROVENANCE.yaml'
        if not proof.is_file() or proof.is_symlink():
            errors.append(f'{proof.relative_to(repo)}: missing regular provenance file')
            continue
        provenance = yaml.safe_load(proof.read_text())
        expected = provenance.get('files', {})
        actual = {p.relative_to(package).as_posix():p for p in files_under(package) if p != proof}
        for relative in sorted(set(actual) - set(expected)):
            errors.append(f'{package.relative_to(repo)}/{relative}: unreviewed vendor file')
        for relative, entry in expected.items():
            path = package / relative
            if '..' in Path(relative).parts or Path(relative).is_absolute() or not path.resolve().is_relative_to(vendor.resolve()):
                errors.append(f'{path}: vendor path or alias escapes toolkit/vendor')
                continue
            if not path.is_file():
                errors.append(f'{path.relative_to(repo)}: missing vendored file')
                continue
            got = digest(path.read_bytes())
            if got != entry['sha256']:
                errors.append(f'{path.relative_to(repo)}: vendored file hash changed; re-import with a reviewed provenance update')
            record = {'path':path.relative_to(repo).as_posix(),'package':provenance['package'],'licence':provenance['licence'],'sha256':got,'bytes':path.stat().st_size}
            if path.is_symlink():
                record['alias_of'] = path.resolve().relative_to(repo).as_posix()
            records.append(record)
        records.append({'path':proof.relative_to(repo).as_posix(),'package':provenance['package'],'licence':provenance['licence'],'sha256':digest(proof.read_bytes()),'bytes':proof.stat().st_size})
    return errors, records


def loadable_agent(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---' not in text[3:]:
        return False
    try:
        meta = yaml.safe_load(text[4:text.index('\n---', 3)])
    except yaml.YAMLError:
        return False
    return isinstance(meta, dict) and bool(meta.get('name')) and bool(meta.get('description'))


def autolink(text: str) -> str:
    return re.sub(r'https://[^\s<>`]+?(?=[.,;)]?(?:\s|$))', lambda m: f'<{m.group(0)}>', text)


def manual_entry(package: dict) -> dict:
    reason = package.get('reason','Unknown origin; do not redistribute')
    package_id = package['id']
    url = package.get('upstream_url')
    if 'account' in reason.lower() or package_id.startswith(('account-','mcp-')):
        group = 'Account-managed connectors and skills'
        steps = 'Open the provider application, sign in with your own account, then enable this named connector/skill in Settings > Apps or Plugins. Authorise only the accounts you own. ' + (f'Provider/source: {url}.' if url else 'No verified public installer exists; use the original provider UI. Do not copy another user’s configuration.')
    elif package_id.startswith('plugin-'):
        group = 'Proprietary or separately licensed marketplaces'
        if url:
            steps = f'Review the publisher terms at {url}; sign in to the original provider and install the named plugin from its marketplace. If that repository advertises a Claude marketplace, run /plugin marketplace add {url}, then /plugin install <publisher-plugin-name>@<publisher-marketplace-name> using the names in that publisher’s manifest. The audit does not verify those catalogue names.'
        else:
            steps = 'Sign in to the provider where this plugin was purchased or enabled. Open Plugins/Marketplace, search for this exact package name and enable it under your own entitlement. No public installation command was verified.'
    else:
        group = 'Unknown origin or unverified redistribution rights'
        steps = 'Do not copy or install from the founder’s archive. Ask the original author for the source, a licence covering the installed files and a pinned public release; then rerun the licence audit before enabling this tool.'
    return {'id':package_id,'tool_ids':package.get('tool_ids',[]),'licence':package.get('licence'),'group':group,'reason':reason,'upstream_url':url,'steps':steps}


def expand_allowlist(repo: Path, copied: dict[str,str]) -> dict:
    """Reviewed exact lines, plus the same lines in byte-identical plugin copies."""
    path = repo/'toolkit/sources/secret-allowlist.json'
    reviewed = json.loads(path.read_text())['entries'] if path.exists() else []
    try:
        agency = json.loads((repo/'schemas/metadata.json').read_text())['secret_allowlist']['vendor_examples']
    except (OSError, KeyError, json.JSONDecodeError):
        agency = []
    by_source = {}
    for entry in [*reviewed, *agency]:
        if not all(isinstance(entry.get(k), str) and entry[k].strip() for k in ('path','line_sha256','label','reason')):
            raise ValueError(f'secret allowlist entry needs path, line_sha256, label and reason: {entry}')
        by_source.setdefault(entry['path'], []).append({k:entry[k] for k in ('line_sha256','label','reason')})
    # Reviewed lines in .claude/agents only seed plugin copies; that tree has its own lock.
    entries = [dict(path=e['path'],**{k:e[k] for k in ('line_sha256','label','reason')}) for e in reviewed if e['path'].startswith('toolkit/vendor/')]
    for target, source in sorted(copied.items()):
        for entry in by_source.get(source, []):
            entries.append({'path':target,**entry,'copy_of':source})
    return {'schema_version':1,'policy':'Exact reviewed lines only, bound by repository path and SHA-256 of the line; generated by scripts/toolkit_build.py from toolkit/sources/secret-allowlist.json','entries':sorted(entries,key=lambda e:(e['path'],e['line_sha256'],e['label']))}


def notices_file(repo: Path, packages: list[dict]) -> bytes:
    path = repo/'THIRD_PARTY_NOTICES.md'
    text = path.read_text() if path.exists() else '# Third-party notices\n'
    head, _, rest = text.partition(NOTICE_START)
    tail = rest.partition(NOTICE_END)[2] if NOTICE_END in rest else ''
    lines = [NOTICE_START,'','## Third-party toolkit','','Generated by `python scripts/toolkit_build.py` from `toolkit/sources/packages.json`. Each package in `toolkit/vendor/` and each copy in `toolkit/plugins/` keeps its upstream licence; the repository MIT and CC BY 4.0 licences do not apply to them. The notice files linked below are exact, unmodified copies of the installed upstream originals, kept in place in each package. `PROVENANCE.yaml` in each package records the upstream source, pinned reference, copy date and a SHA-256 for every file.','',
             '### Vendored packages','','| Package | Licence | Upstream | Original notice files |','| --- | --- | --- | --- |']
    for p in sorted((p for p in packages if p['class']=='VENDOR'), key=lambda p:p['id']):
        notices = ', '.join(f'[{Path(n).name}]({n})' for n in p.get('notices', [])) or 'None installed upstream; the licence is declared in the package material (see `PROVENANCE.yaml`)'
        upstream = f'<{p["upstream_url"]}>' if p.get('upstream_url') else 'Local installation; no public source recorded'
        lines.append(f'| `{p["id"]}` | {p["licence"]} | {upstream} | {notices} |')
    lines += ['','### Fetched at install time (not redistributed)','','`scripts/install.sh` clones these at the pinned commits into `~/.3rdwrong/fetch/`. Their licences apply to those checkouts.','','| Package | Licence | Upstream | Commit |','| --- | --- | --- | --- |']
    for p in sorted((p for p in packages if p['class']=='FETCH'), key=lambda p:p['id']):
        lines.append(f'| `{p["id"]}` | {p["licence"]} | <{p["upstream_url"]}> | `{p["installer_commit"]}` |')
    lines += ['',NOTICE_END]
    return (head.rstrip('\n')+'\n\n'+'\n'.join(lines)+'\n'+tail.lstrip('\n')).encode()


def make_outputs(repo: Path, packages: list[dict], materials: dict, registry: dict, vendor_records: list[dict]) -> dict[str,bytes]:
    outputs = {}
    aliases = {}
    for tool in registry['tools']:
        for identity in [tool['id'], *tool.get('aliases',[])]:
            aliases[identity] = tool
    items, seen, unmapped, not_loadable = [], set(), [], []
    package_map = {p['id']:p for p in packages}
    for identity, material in sorted(materials.items()):
        if identity.startswith('mcp:'):
            continue
        tool = aliases.get(identity)
        if not tool:
            unmapped.append(identity)
            tool = {'id':identity,'role':'parked','department':'operations','reason':'Absent from imported registry; library only until assigned'}
        if tool.get('role') == 'excluded':
            continue
        # Registry canonical ID collapses historical caches and duplicated providers.
        canonical_id = tool['id']
        if canonical_id in seen:
            continue
        seen.add(canonical_id)
        core = material.get('source','').startswith('skills/3w-')
        role = 'lead' if core else tool.get('role','parked')
        if role not in {'lead','specialist','bench','parked'}:
            raise ValueError(f'unknown loading role for {identity}: {role}')
        item = dict({'distribution':'vendor',**material}, id=canonical_id, aliases=[identity], department='core' if core else tool.get('department',tool.get('division','operations')), role=role,
                    name=Path(material['source']).name if core else '3w-'+slug(canonical_id))
        item['load'] = 'active' if role in ACTIVE else 'library'
        if item['load']=='active' and item['kind']=='agent' and item['distribution']=='vendor' and not loadable_agent(repo/item['source']):
            # Reference prompts without subagent frontmatter cannot load as agents.
            item['load'] = 'library'; not_loadable.append(canonical_id)
        items.append(item)
    for path in sorted((repo/'skills').glob('3w-*/SKILL.md')):
        source = path.parent.relative_to(repo).as_posix()
        if any(x.get('source')==source for x in items):
            continue
        items.append({'id':'core:'+path.parent.name,'name':path.parent.name,'source':source,'kind':'skill','package':'pack-founder-3rdwrong-skills','distribution':'vendor','department':'core','role':'lead','load':'active'})
    fetch = []
    for package in packages:
        if package['class']!='FETCH':
            continue
        commit = package.get('installer_commit')
        if not isinstance(commit,str) or not re.fullmatch('[0-9a-f]{40}',commit):
            raise ValueError(f'{package["id"]}: FETCH needs a full pinned commit')
        wanted = [x for x in items if x['package']==package['id']]
        fetch.append({'id':package['id'],'upstream_url':package['upstream_url'],'commit':commit,'licence':package['licence'],
                      'pin_basis':package.get('installer_pin_basis') or 'audit installer_commit',
                      'destination':'~/.3rdwrong/fetch/'+package['id'],'what_to_install':[{'id':x['id'],'kind':x['kind'],'role':x['role'],'candidates':x.get('candidates',[]),'upstream_name':x.get('upstream_name')} for x in wanted],
                      'runtime_setup':'Source checkout only. No third-party setup hooks are executed. Read the pinned upstream README for service credentials, native runtimes and optional runtime setup.',
                      'component_only':False})
    manual = [manual_entry(p) for p in packages if p['class']=='MANUAL']
    outputs['toolkit/fetch.yaml'] = yaml.safe_dump({'schema_version':1,'policy':'Immutable commits only; checkouts never run setup scripts automatically','packages':fetch},sort_keys=False,allow_unicode=True).encode()
    outputs['toolkit/manual.yaml'] = yaml.safe_dump({'schema_version':1,'packages':manual},sort_keys=False,allow_unicode=True).encode()
    lines = ['# Manual enablement checklist','','Generated by `python scripts/toolkit_build.py`. Account access, subscriptions and unknown rights cannot be transferred by copying files.','']
    for group in sorted({x['group'] for x in manual}):
        lines.extend(['## '+group,''])
        for entry in manual:
            if entry['group']==group:
                lines.extend(['### '+entry['id'],'',f'Licence: `{entry["licence"]}`. Reason: {autolink(entry["reason"])}','',autolink(entry['steps']),'','Tools: '+', '.join('`'+x+'`' for x in entry['tool_ids']), ''])
    outputs['toolkit/manual.md'] = ('\n'.join(lines).rstrip('\n')+'\n').encode()
    templates = {}
    for package in packages:
        if package.get('kind')!='mcp-server':
            continue
        name = slug(package['id'].removeprefix('mcp-'))
        npm = NPM_MCP.get(name)
        if npm:
            server={'command':'npx','args':['-y',f'{npm[0]}@{package["versions"][0]}',*npm[1]]}
            if npm[2]:server['env']=dict(npm[2])
        else:
            server={'type':'http','url':'${MCP_'+name.replace('-','_').replace('.','_').upper()+'_URL}'}
        templates[name+'.json'] = {'mcpServers':{name:server}}
    outputs['toolkit/install-plan.json'] = encoded({'schema_version':1,'items':items,'fetch':fetch,'templates':templates,'manual':manual})
    outputs['toolkit/coverage.json'] = encoded({'unmapped_registry_ids':unmapped,'excluded_tool_ids':{p['id']:p['excluded_tool_ids'] for p in packages if p.get('excluded_tool_ids')},'items_by_role':dict(Counter(x['role'] for x in items)),'items_by_load':dict(Counter(x['load'] for x in items)),'active_role_library_load':sorted(not_loadable)})
    # Official component paths must resolve inside the plugin root. Copies make
    # hosted marketplace cache installs independent of this repo's vendor tree.
    plugins = []
    copied = {}
    departments = list(dict.fromkeys([*DEPARTMENTS, *sorted({x['department'] for x in items if x['department']!='core'}), 'core']))
    for department in departments:
        name = '3rdwrong-'+slug(department)
        root = f'{GENERATED_DIR}/{name}'
        plugins.append({'name':name,'source':'./'+root,'description':f'3RDWRONGS {department}: active leads and specialists'})
        manifest = {'name':name,'version':'0.3.0','description':f'Active {department} skills and agents; generated from the toolkit registry','author':{'name':'3RDWRONGS'},'repository':'https://github.com/ohnoshivm/3rdwrong'}
        outputs[root+'/.claude-plugin/plugin.json'] = encoded(manifest)
        used_packages = set()
        for item in items:
            if item['department']!=department or item['load']!='active' or item['distribution']!='vendor':
                continue
            source = repo / item['source']
            if not source.exists():
                raise ValueError(f'missing plugin source: {item["source"]}')
            used_packages.add(item['package'])
            if item['kind']=='agent':
                outputs[root+'/agents/'+item['name']+'.md'] = source.read_bytes()
                copied[root+'/agents/'+item['name']+'.md'] = item['source']
            else:
                for path in files_under(source):
                    target = root+'/skills/'+item['name']+'/'+path.relative_to(source).as_posix()
                    outputs[target] = path.read_bytes()
                    copied[target] = path.resolve().relative_to(repo.resolve()).as_posix()
        notice_lines = ['# Third-party notices','','Each component retains its upstream licence. The notices below are exact copies of the installed upstream originals.','']
        for package_id in sorted(used_packages):
            package = package_map[package_id]
            notice_lines.append(f'- `{package_id}`: {package["licence"]}. '+str(package.get('upstream_url') or 'Founder-authored material')+'.')
            for n,path in enumerate(package.get('notices', [])):
                source = repo / path
                outputs[root+f'/notices/{package_id}/{n}-'+source.name] = source.read_bytes()
                copied[root+f'/notices/{package_id}/{n}-'+source.name] = source.resolve().relative_to(repo.resolve()).as_posix()
            if package_id=='pack-agency-agents' and (repo/'THIRD_PARTY_NOTICES.md').exists():
                # Only the pre-existing Agency section; avoid recursive inclusion
                # of the generated toolkit notice catalogue.
                outputs[root+'/notices/Agency-Agents.md'] = (repo/'THIRD_PARTY_NOTICES.md').read_text().split('<!-- TOOLKIT-NOTICES:START -->')[0].encode()
            if package_id=='pack-founder-3rdwrong-skills' and (repo/'LICENSE-DOCS').exists():
                outputs[root+'/notices/LICENSE-DOCS']=(repo/'LICENSE-DOCS').read_bytes()
        outputs[root+'/THIRD_PARTY_NOTICES.md'] = ('\n'.join(notice_lines)+'\n').encode()
    outputs['.claude-plugin/marketplace.json'] = encoded({'name':'3rdwrong','owner':{'name':'3RDWRONGS'},'description':'3RDWRONGS studio toolkit: one plugin per department plus the studio core skills','plugins':plugins})
    outputs['toolkit/secret-allowlist.json'] = encoded(expand_allowlist(repo, copied))
    outputs['THIRD_PARTY_NOTICES.md'] = notices_file(repo, packages)
    # Lock includes each vendored path, including aliases, generated plugin copies,
    # installation plans and portable input snapshots. It excludes itself.
    records = list(vendor_records)
    for relative, data in sorted(outputs.items()):
        if relative.startswith(GENERATED_DIR+'/'):
            name = relative.split('/')[2]
            records.append({'path':relative,'package':name,'licence':'mixed; see plugin notices','sha256':digest(data),'bytes':len(data)})
    for path in files_under(repo/'toolkit/sources'):
        records.append({'path':path.relative_to(repo).as_posix(),'package':'toolkit-metadata','licence':'MIT','sha256':digest(path.read_bytes()),'bytes':path.stat().st_size})
    by_licence = {}
    for p in packages:
        if p['class']=='VENDOR':
            row=by_licence.setdefault(p['licence'],{'packages':0,'audit_tool_ids':0,'available_tool_ids':0})
            row['packages']+=1;row['audit_tool_ids']+=p['tool_count'];row['available_tool_ids']+=p['tool_count']-len(p.get('excluded_tool_ids',[]))
    counts = {'vendor_packages':sum(p['class']=='VENDOR' for p in packages),'vendor_audit_tool_ids':sum(p['tool_count'] for p in packages if p['class']=='VENDOR'),
              'fetch_packages':len(fetch),'fetch_tool_ids':sum(p['tool_count'] for p in packages if p['class']=='FETCH'),'manual_packages':len(manual),'manual_tool_ids':sum(len(p['tool_ids']) for p in manual),
              'vendor_files':len(vendor_records),'vendor_unique_content_bytes':sum(len(data) for data in {digest((repo/r['path']).read_bytes()):(repo/r['path']).read_bytes() for r in vendor_records}.values()),
              'vendor_logical_bytes':sum(r['bytes'] for r in vendor_records),'plugins':len(plugins),'by_licence':by_licence}
    outputs['toolkit/toolkit.lock.json'] = encoded({'schema_version':1,'counts':counts,'files':sorted(records,key=lambda r:r['path']), 'generated_sha256':{k:digest(v) for k,v in sorted(outputs.items()) if not k.startswith(GENERATED_DIR+'/')}})
    security = repo/'toolkit/sources/security-review.json'
    if security.exists():
        review = json.loads(security.read_text())['findings']
        lines=['# Toolkit security and privacy review','','Every audit finding has an explicit disposition below. Values remain redacted. This is a reviewed publication filter, not a claim that regex scanning proves the absence of secrets.','',
               'MCP runtime implementations, dependencies, caches, benchmark transcripts and binaries are excluded. Literal API keys of uncertain scope and identifiable personal home paths are excluded without altering upstream files. Public copyright/contact notices and clearly fake documentation examples retain their original text.','',
               '| Finding | Package | Source | Line | Category | Decision |','| --- | --- | --- | ---: | --- | --- |']
        for h in review:
            source=h['source'].replace('|','\\|');decision=h['decision'].replace('|','\\|')
            lines.append(f'| {h["finding"]} | `{h["package"]}` | `{source}` | {h["line"]} | {h["category"]}; value redacted | {decision} |')
        decisions=Counter((h['decision'].split(':')[0],h['category']) for h in review)
        summary=['## Summary','',f'{len(review)} licence-audit findings: '+', '.join(f'{n} {d} {c}' for (d,c),n in sorted(decisions.items()))+'. '+
                 f'{len({h["source"] for h in review if h["decision"].startswith("EXCLUDE")})} distinct source files were excluded; no excluded file is present in `toolkit/vendor/`.','',
                 '## Repository secret scan: reviewed exact lines','',
                 'Hits from `scripts/validate.py` in `toolkit/vendor/` are listed below. Each is allowlisted only for its exact line (SHA-256) in that one file and scanner category, through `toolkit/secret-allowlist.json`; the plugin copies inherit the entry only while byte-identical. Credential and private-key categories have no pattern-wide or file-wide exemption, and the scan still covers `toolkit/vendor/**` and `toolkit/plugins/**`.','',
                 '| File | Line | Category | Line SHA-256 | Decision |','| --- | ---: | --- | --- | --- |']
        allow=json.loads(outputs['toolkit/secret-allowlist.json'])['entries']
        for e in allow:
            if 'copy_of' in e:continue
            text=(repo/e['path']).read_text(encoding='utf-8').splitlines()
            number=next((n for n,l in enumerate(text,1) if digest(l.encode())==e['line_sha256']),0)
            summary.append(f'| `{e["path"]}` | {number} | {e["label"]}; value redacted | `{e["line_sha256"][:16]}` | KEEP: {e["reason"]} |')
        seeds=json.loads((repo/'toolkit/sources/secret-allowlist.json').read_text())['entries'] if (repo/'toolkit/sources/secret-allowlist.json').exists() else []
        agency=sum(e['path'].startswith('.claude/agents/') for e in seeds)
        summary+=['',f'{sum("copy_of" in e for e in allow)} further entries bind the same reviewed lines in plugin copies. {agency} reviewed placeholder-address lines in `.claude/agents/` (Agency Agents, governed by their own lock) seed only their plugin copies; their justifications are in `toolkit/sources/secret-allowlist.json`.','','## Licence-audit findings','']
        head_end=lines.index('| Finding | Package | Source | Line | Category | Decision |')
        lines[head_end:head_end]=summary
        outputs['toolkit/SECURITY-REVIEW.md']=('\n'.join(lines)+'\n').encode()
    return outputs


def build(repo: Path, check: bool=False) -> list[str]:
    source=repo/'toolkit/sources'
    packages=json.loads((source/'packages.json').read_text())['packages']
    materials=json.loads((source/'materials.json').read_text())
    registry=json.loads((source/'registry.json').read_text())
    errors, records=verify_vendor(repo)
    if errors:
        return errors
    outputs=make_outputs(repo,packages,materials,registry,records)
    existing={p.relative_to(repo).as_posix() for p in files_under(repo/GENERATED_DIR)}
    obsolete=existing-set(outputs)
    for relative,data in sorted(outputs.items()):
        path=repo/relative
        if not path.is_file() or path.is_symlink() or path.read_bytes()!=data:
            if check:
                errors.append(relative+': out of date; run python scripts/toolkit_build.py')
            else:
                path.parent.mkdir(parents=True,exist_ok=True)
                if path.is_symlink():path.unlink()
                path.write_bytes(data)
    for relative in sorted(obsolete):
        if check:errors.append(relative+': obsolete generated file')
        else:(repo/relative).unlink()
    plugin_dirs={relative.split('/')[2] for relative in outputs if relative.startswith(GENERATED_DIR+'/')}
    for directory in sorted((repo/GENERATED_DIR).iterdir() if (repo/GENERATED_DIR).is_dir() else []):
        if directory.name not in plugin_dirs:
            if check:errors.append(f'{GENERATED_DIR}/{directory.name}: stale plugin directory')
            else:shutil.rmtree(directory)
    for directory in sorted((p for p in (repo/GENERATED_DIR).rglob('*') if p.is_dir()), reverse=True) if not check and (repo/GENERATED_DIR).is_dir() else []:
        if not any(directory.iterdir()):directory.rmdir()
    return errors


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1],help=argparse.SUPPRESS)
    parser.add_argument('--registry',type=Path,help='Refresh the portable registry snapshot from an audited registry YAML')
    parser.add_argument('--audit-dir',type=Path,help='Verify original audit identity; use toolkit_vendor.py for a new material import')
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args(argv)
    try:
        if args.registry:
            data=encoded(snapshot_registry(args.registry))
            path=args.repo/'toolkit/sources/registry.json'
            if args.check:
                if not path.exists() or path.read_bytes()!=data:
                    print('Registry source changed; regenerate the toolkit snapshot.');return 1
            else:path.write_bytes(data)
        if args.audit_dir:
            recorded=json.loads((args.repo/'toolkit/sources/packages.json').read_text())['audit_sha256']
            if digest((args.audit_dir/'packages.yaml').read_bytes())!=recorded:
                raise ValueError('audit changed; an explicit reviewed material re-import is required')
        errors=build(args.repo,args.check)
        for error in errors:print(error)
        print(f'Toolkit {"check" if args.check else "build"}: {len(errors)} errors.')
        return int(bool(errors))
    except (ValueError,KeyError,OSError,yaml.YAMLError) as exc:
        print(f'Toolkit error: {exc}',file=sys.stderr);return 1


if __name__=='__main__':
    raise SystemExit(main())
