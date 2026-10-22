from __future__ import annotations

from pathlib import Path

from .common import Issue


def check_required(root: Path, config: dict) -> list[Issue]:
    return [
        Issue(path, 1, "required", "required file is missing")
        for path in config["required_files"]
        if not (root / path).exists()
    ]
