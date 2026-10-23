"""Private project storage and append-only preparation events (D-0021)."""
from __future__ import annotations

import json
import os
from pathlib import Path

try:
    from .eval_core import EvalError
    from .threew import CODENAME, inside_git_worktree
except ImportError:
    from eval_core import EvalError
    from threew import CODENAME, inside_git_worktree


def private_path(root: Path, path: Path, boundary: Path | None = None) -> Path:
    path = path.expanduser().resolve()
    repository = root.resolve()
    # Case-fold as well as resolving symlinks and .., even on case-sensitive
    # test hosts. A case variant must never become an alternate public target.
    folded, repo = str(path).casefold(), str(repository).casefold()
    if folded == repo or folded.startswith(repo + os.sep) or inside_git_worktree(path):
        raise EvalError('project material must stay outside the public repository and any Git worktree')
    if boundary is not None and not path.is_relative_to(boundary.resolve()):
        raise EvalError('project material must stay within its vault evals directory')
    return path


def project_root(root: Path, codename: str) -> Path:
    if not isinstance(codename, str) or not CODENAME.fullmatch(codename):
        raise EvalError('codename must be two lowercase words joined by a hyphen')
    vault = private_path(root, Path(os.environ.get('THREEW_VAULT', '~/3rdwrong-vault')))
    project = private_path(root, vault / codename, vault)
    private_path(root, project / 'evals', project)
    return project


def anchor_path(root: Path, codename: str) -> Path:
    base = project_root(root, codename) / 'evals'
    return private_path(root, base / 'preparations.jsonl', base)


def append_project_anchor(root: Path, run: dict) -> None:
    path = anchor_path(root, run['project'])
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    event = {'run_id': run['run_id'], 'codename': run['project'],
             'case_sha256': run['case_sha256'], 'timestamp': run['created_at'],
             'creation_sha256': run['creation_sha256']}
    # Append only: no runner command edits/truncates existing events. O_APPEND
    # plus one write preserves prior entries; fsync anchors before prepare returns.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW, 0o600)
    try:
        import fcntl
        fcntl.flock(fd, fcntl.LOCK_EX)
        events = [json.loads(line) for line in path.read_text().splitlines()]
        if any(e['run_id'] == run['run_id'] for e in events):
            raise EvalError('private run id already anchored; never reuse it')
        os.write(fd, (json.dumps(event, sort_keys=True) + '\n').encode())
        os.fsync(fd)
    finally:
        os.close(fd)


def verify_project_anchor(root: Path, run: dict) -> None:
    events = [json.loads(line) for line in anchor_path(root, run['project']).read_text().splitlines()]
    matches = [e for e in events if e['run_id'] == run['run_id']]
    if len(matches) != 1 or matches[0] != {
            'run_id': run['run_id'], 'codename': run['project'],
            'case_sha256': run['case_sha256'], 'timestamp': run['created_at'],
            'creation_sha256': run['creation_sha256']}:
        raise EvalError('private preparation anchor missing or changed')
