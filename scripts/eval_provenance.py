"""Derive studio run authority from committed cases, never local run manifests."""
from __future__ import annotations

from pathlib import Path
import re
import subprocess

import yaml

try:
    from .eval_core import EvalError, digest, identifier, read_yaml
    from .eval_storage import project_root, verify_project_anchor, private_path
except ImportError:
    from eval_core import EvalError, digest, identifier, read_yaml
    from eval_storage import project_root, verify_project_anchor, private_path


def git(root: Path, *args: str) -> bytes:
    try:
        result = subprocess.run(['git', '-C', str(root), *args], capture_output=True,
                                timeout=15, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise EvalError('cannot read committed case history') from exc
    if result.returncode:
        raise EvalError('cannot read committed case history or verify ancestor of HEAD')
    return result.stdout


def complete_history(root: Path) -> None:
    if (Path(git(root, 'rev-parse', '--show-toplevel').decode().strip()).resolve() != root.resolve()
            or git(root, 'rev-parse', '--is-shallow-repository').strip() != b'false'):
        raise EvalError('committed case requires complete Git history at the repository root')


def case_at(root: Path, relative: str, commit: str) -> tuple[dict, bytes]:
    if (not isinstance(commit, str) or not re.fullmatch(r'[0-9a-f]{40,64}', commit)
            or Path(relative).is_absolute() or '..' in Path(relative).parts):
        raise EvalError('invalid committed case reference')
    complete_history(root)
    git(root, 'merge-base', '--is-ancestor', commit, 'HEAD')
    raw = git(root, 'show', f'{commit}:{relative}')
    # Use the duplicate-key rejecting loader for history too.
    try:
        from .eval_core import UniqueLoader
    except ImportError:
        from eval_core import UniqueLoader
    case = yaml.load(raw, Loader=UniqueLoader)
    if not isinstance(case, dict) or case.get('class') not in {'evidence', 'demo'}:
        raise EvalError('committed case must declare class: evidence or demo')
    expected = f'evals/cases/{identifier(case["department"])}/{identifier(case["job"])}/{identifier(case["id"])}.yaml'
    if relative != expected:
        raise EvalError('committed case id/path disagree')
    history = git(root, 'log', '--full-history', '-m', '--format=%H', 'HEAD', '--', relative).decode().splitlines()
    if not history:
        raise EvalError('committed case history unavailable')
    for revision in history:
        # Deletion commits have no blob; list the tree rather than swallowing a
        # failed show (which could hide a transport/history failure).
        if not git(root, 'ls-tree', revision, '--', relative).strip():
            continue
        earlier = yaml.load(git(root, 'show', f'{revision}:{relative}'), Loader=UniqueLoader)
        if not isinstance(earlier, dict) or earlier.get('class') != case['class']:
            raise EvalError('case class changed since its first commit; create a new case id')
    return case, raw


def committed_case(root: Path, path: Path) -> tuple[dict, str, bytes]:
    complete_history(root)
    relative = path.relative_to(root).as_posix()
    commit = git(root, 'log', '-1', '--format=%H', 'HEAD', '--', relative).decode().strip()
    if not commit:
        raise EvalError('prepare requires a committed case, including for demos')
    case, raw = case_at(root, relative, commit)
    if path.read_bytes() != raw:
        raise EvalError('case has uncommitted changes; commit the studio case before preparing')
    return case, commit, raw


def locations(root: Path, run: dict) -> tuple[Path, Path]:
    project = run.get('project')
    base = project_root(root, project) if project else root
    kind, prefix = ('demos', 'demo-') if run['demo'] else ('evidence', 'evidence-')
    if project:
        kind, prefix = 'project', 'project-'
    run_id, job = identifier(run['run_id']), identifier(run['job'])
    if not run_id.startswith(prefix):
        raise EvalError('run id disagrees with derived case class')
    paths = (base / 'evals/runs' / kind / job / run_id,
             base / 'evals/results' / kind / job / (run_id + '.yaml'))
    for path in paths:
        if path.resolve() != path.absolute() or not path.resolve().is_relative_to(base.resolve()):
            raise EvalError('run and result paths must be canonical, without symlinks')
        if project:
            private_path(root, path, base / 'evals')
    return paths


def verify_provenance(root: Path, folder: Path, run: dict) -> str:
    if run.get('project'):
        base = project_root(root, run['project'])
        private_path(root, folder, base / 'evals')
        verify_project_anchor(root, run)
        case = read_yaml(folder / 'case.yaml')
        kind = case.get('class')
        raw = (folder / 'case.yaml').read_bytes()
    else:
        case, raw = case_at(root, run['case_path'], run['case_commit'])
        kind = case['class']
        if (folder / 'case.yaml').read_bytes() != raw:
            raise EvalError('case snapshot differs from committed case')
        if [item['source'] for item in run['inputs']] != case['inputs']:
            raise EvalError('input inventory differs from committed case')
        for item in run['inputs']:
            source = item['source']
            if Path(source).is_absolute() or '..' in Path(source).parts:
                raise EvalError('unsafe committed input path')
            expected = digest(git(root, 'show', f'{run["case_commit"]}:{source}'))
            if item['sha256'] != expected or digest((folder / item['snapshot']).read_bytes()) != expected:
                raise EvalError('input snapshot differs from committed case inputs')
    if (kind not in {'evidence', 'demo'} or type(run.get('demo')) is not bool
            or run['demo'] != (kind == 'demo') or run.get('class', kind) != kind
            or run.get('case_id') != case['id'] or run['job'] != case['job']
            or run['department'] != case['department'] or run['case_sha256'] != digest(raw)):
        raise EvalError('informational run class/id disagrees with derived case')
    if kind == 'evidence' and len(run['candidates']) < 2:
        raise EvalError('evidence needs at least two candidates')
    expected_folder, _ = locations(root, run)
    if folder.absolute() != expected_folder:
        raise EvalError('run location disagrees with derived case class')
    return kind
