from __future__ import annotations

from pathlib import Path

from .common import Issue


def check_skill_graph(root: Path, config: dict) -> list[Issue]:
    try:
        from ..build_skill_graph import stale_outputs
    except ImportError:
        from build_skill_graph import stale_outputs
    try:
        return [Issue(path.split(':', 1)[0], 1, 'skill-graph', path.split(': ', 1)[1]) for path in stale_outputs(root)]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [Issue('skill-graph/README.md', 1, 'skill-graph', f'cannot verify skill graph: {exc}')]
