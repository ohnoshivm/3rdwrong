from __future__ import annotations

from pathlib import Path

from .common import Issue

try:
    from ..build_index import index_is_current
except ImportError:
    from build_index import index_is_current


def check_index(root: Path, config: dict) -> list[Issue]:
    if index_is_current(root):
        return []
    return [Issue("INDEX.md", 1, "index", "index is stale; run `uv run python scripts/build_index.py`")]
