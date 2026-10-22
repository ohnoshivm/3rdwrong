from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path

import yaml


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create or update repository labels from .github/labels.yml.")
    parser.add_argument("--dry-run", action="store_true", help="print gh commands without executing them")
    args = parser.parse_args(argv)
    path = Path(".github/labels.yml")
    try:
        labels = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        print(f"cannot read {path}: {exc}", file=sys.stderr)
        return 1
    if not isinstance(labels, list):
        print(f"{path} must contain a list of labels", file=sys.stderr)
        return 1
    for label in labels:
        if not isinstance(label, dict) or not all(label.get(key) for key in ("name", "color", "description")):
            print(f"invalid label entry in {path}: each needs name, color, and description", file=sys.stderr)
            return 1
        command = [
            "gh", "label", "create", str(label["name"]), "--force",
            "--color", str(label["color"]).lstrip("#"), "--description", str(label["description"]),
        ]
        if args.dry_run:
            print(shlex.join(command))
        else:
            subprocess.run(command, check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
