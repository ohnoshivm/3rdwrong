#!/usr/bin/env python3
"""Build a proposed leaderboard; demos never nominate a registry lead."""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
import json
from pathlib import Path
import sys

import yaml

try:
    from .eval_core import ROOT, EvalError, canonical_model, digest, read_yaml, registry
    from .eval_run import load_run, verify_creation
    from .eval_provenance import locations, verify_provenance
except ImportError:
    from eval_core import ROOT, EvalError, canonical_model, digest, read_yaml, registry
    from eval_run import load_run, verify_creation
    from eval_provenance import locations, verify_provenance


def verified_result(root: Path, path: Path) -> dict:
    run = read_yaml(path)
    if run.get('project'):
        raise EvalError('project runs are never leaderboard evidence')
    folder, expected = locations(root, run)
    if path.absolute() != expected:
        raise EvalError('result class/location changed; refusing leaderboard eligibility')
    _, stored = load_run(root, str(folder))
    verify_creation(folder, run)
    verify_provenance(root, folder, run)
    if (stored['state'] != 'scored' or run.get('state') != 'scored'
            or any(run.get(k) != v for k, v in stored.items())
            or (folder / 'result.sha256').read_text().strip() != digest(path.read_bytes())):
        raise EvalError('result provenance changed; refusing leaderboard eligibility')
    judge = canonical_model(run['judge_model'])
    if any(judge == canonical_model(c['maker_model'], demo=run['demo']) for c in run['candidates'].values()):
        raise EvalError('judge family must differ from every maker family')
    return run


def build_report(root: Path, today: date | None = None) -> str:
    today = today or date.today()
    tools = registry(root)
    leads = defaultdict(list)
    for tool in tools:
        if tool['role'] == 'lead':
            leads[(tool['department'], tool['job'])].append(tool['id'])
    jobs = set()
    for path in (root / 'evals/cases').rglob('*.yaml'):
        case = read_yaml(path)
        jobs.add((case['department'], case['job']))
    groups = defaultdict(list)
    demos = []
    provisional = []
    current_registry = digest((root / 'toolkit/sources/registry.json').read_bytes())
    for path in sorted((root / 'evals/results').rglob('*.yaml')):
        run = verified_result(root, path)
        key = (run['department'], run['job'])
        jobs.add(key)
        for slot, score in run['scores'].items():
            row = {'tool': run['candidates'][slot]['tool_id'], 'run': run, 'score': score, 'slot': slot}
            if run['demo']:
                demos.append(row)
            elif not run.get('human_spot_check'):
                provisional.append(row)
            else:
                groups[key].append(row)
    lines = ['---', 'title: Quality Lab leaderboard', 'type: guide', 'status: proposed',
             'owner: founder', f'last_reviewed: {today.isoformat()}', 'review_every_days: 90',
             '---', '', '# Quality Lab leaderboard', '',
             '**Documented:** generated from stored evaluation records and the current registry.',
             '**Interpretation:** scores compare these frozen cases only; a lead change requires founder review.',
             'Demo scores are pipeline demonstrations, not quality verdicts. Only non-demo, human-checked runs enter quality means.',
             'Failed and disqualified attempts remain in the mean; disqualified tools cannot be nominated as best performer.',
             '', '| Department / job | Current registry lead | Best eligible performer | Mean / 5 | Runs | Last run | Review |',
             '| --- | --- | --- | --- | --- | --- | --- |']
    detail = []
    for key in sorted(jobs):
        by_tool = defaultdict(list)
        for row in groups[key]:
            by_tool[row['tool']].append(row)
        rankings = []
        for tool, rows in by_tool.items():
            mean = sum(r['score']['weighted_score'] for r in rows) / len(rows)
            last = max(r['run']['scored_at'][:10] for r in rows)
            dq = any(r['score']['disqualifiers'] for r in rows)
            eligible = not dq and all(r['score']['passes'] for r in rows)
            rankings.append((mean, tool, len(rows), last, eligible))
            detail.append(f'| {key[0]} / {key[1]} | `{tool}` | {mean:.2f} | {len(rows)} | {last} | {"Eligible" if eligible else "Below bar / disqualified"} |')
        candidates = sorted((r for r in rankings if r[4]), key=lambda r: (-r[0], r[1]))
        if not candidates:
            lines.append(f'| {key[0]} / {key[1]} | {", ".join(leads[key]) or "Human craft gap / no registry lead"} | No eligible quality evidence | — | {len(groups[key])} | — | Bake-off required |')
            continue
        best = candidates[0]
        tied = [r[1] for r in candidates if abs(r[0] - best[0]) < 1e-9]
        flags = []
        if len(tied) > 1:
            flags.append('TIE — no sole winner')
        elif best[1] not in leads[key]:
            flags.append('DISAGREEMENT — founder review')
        if any((today - date.fromisoformat(r['run']['created_at'][:10])).days >= 90 for r in groups[key]):
            flags.append('RETEST — 90 days')
        if any(r['run']['registry_sha256'] != current_registry for r in groups[key]):
            flags.append('RETEST — registry changed; inspect tool versions and new candidates')
        lines.append(f'| {key[0]} / {key[1]} | {", ".join(leads[key]) or "Human craft gap / no registry lead"} | {", ".join(tied)} | {best[0]:.2f} | {best[2]} | {best[3]} | {"; ".join(flags) or "Evidence current; human selection required"} |')
    lines += ['', '## Per-tool quality evidence', '',
              '| Department / job | Tool | Mean / 5 | Runs | Last run | Eligibility |',
              '| --- | --- | --- | --- | --- | --- |', *detail]
    if not detail:
        lines += ['| — | No non-demo human-checked runs | — | 0 | — | Unknown |']
    lines += ['', '## Pipeline demonstrations', '',
              'These numbers only demonstrate storage, weighting and report rendering. They cannot select or validate a lead.', '',
              '| Job | Run | Tool | Slot | Demo score / 5 |', '| --- | --- | --- | --- | --- |']
    for row in demos:
        lines.append(f'| {row["run"]["job"]} | {row["run"]["run_id"]} | `{row["tool"]}` | {row["slot"]} | {row["score"]["weighted_score"]:.2f} |')
    if not demos:
        lines.append('| — | No demonstrations | — | — | — |')
    lines += ['', '## Awaiting human spot-check', '']
    for row in provisional:
        lines.append(f'- {row["run"]["job"]} / {row["run"]["run_id"]} / slot {row["slot"]}: excluded from lead evidence.')
    if not provisional:
        lines.append('None recorded.')
    lines += ['', '**Unknown:** runtime tool updates are not discoverable from these files. The operator must trigger a fresh',
              'bake-off after a tool/model/prompt update or a new candidate, even when the registry hash is unchanged.',
              'See [Quality Lab](README.md) for paired-case comparison and re-test rules.', '']
    return '\n'.join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        report = build_report(args.root.resolve())
        output = args.root / 'evals/LEADERBOARD.md'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding='utf-8')
        print(output)
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError, json.JSONDecodeError) as exc:
        print(f'eval-report: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
