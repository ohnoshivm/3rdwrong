from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import yaml

try:
    from .oscheck.common import parse_frontmatter
except ImportError:
    from oscheck.common import parse_frontmatter


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create a document from a repository template.")
    parser.add_argument("template_path")
    parser.add_argument("dest_path")
    parser.add_argument("--title")
    args = parser.parse_args(argv)
    template = Path(args.template_path)
    destination = Path(args.dest_path)
    if destination.exists() or destination.is_symlink():
        print(f"refusing to overwrite: {destination}", file=sys.stderr)
        return 1
    try:
        template_text = template.read_text(encoding="utf-8")
        schema = json.loads((Path.cwd() / "schemas" / "metadata.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read template or metadata schema: {exc}", file=sys.stderr)
        return 1
    parsed = parse_frontmatter(template_text)
    if parsed.data is None:
        print(f"invalid template frontmatter: {parsed.error}", file=sys.stderr)
        return 1
    metadata = parsed.data
    if metadata.get("type") != "template":
        print("template frontmatter must set type: template", file=sys.stderr)
        return 1
    doc_type = metadata.get("template_for")
    if not isinstance(doc_type, str) or doc_type not in set(schema["types"]):
        print("template_for must name a valid document type", file=sys.stderr)
        return 1
    metadata["type"] = doc_type
    metadata.pop("template_for", None)
    metadata["status"] = "reference" if doc_type in {"research", "reference-study"} else "proposed"
    metadata["last_reviewed"] = date.today().isoformat()
    metadata["title"] = args.title or metadata.get("title") or "Untitled document"
    frontmatter = yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True).rstrip()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(f"---\n{frontmatter}\n---\n{parsed.body}", encoding="utf-8")
    print(f"Created {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
