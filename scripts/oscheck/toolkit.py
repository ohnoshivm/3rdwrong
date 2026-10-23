from __future__ import annotations

from pathlib import Path

import yaml

from .common import Issue

try:
    from ..toolkit_build import build
except ImportError:
    from toolkit_build import build


def check_toolkit(root: Path, config: dict) -> list[Issue]:
    """Vendored hashes, generated plugins, plans and notices must match toolkit/sources."""
    if not (root / "toolkit/sources/packages.json").is_file():
        return []
    try:
        errors = build(root, check=True)
    except (ValueError, KeyError, OSError, yaml.YAMLError) as exc:
        return [Issue("toolkit/toolkit.lock.json", 1, "toolkit", f"cannot verify toolkit: {exc}")]
    issues = []
    for error in errors:
        path, _, message = error.partition(": ")
        issues.append(Issue(path, 1, "toolkit", message or "toolkit check failed"))
    return issues
