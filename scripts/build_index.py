from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    from .oscheck.common import markdown_files, parse_frontmatter, relative_path
except ImportError:
    from oscheck.common import markdown_files, parse_frontmatter, relative_path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY_LIMIT = 140


def _plain_text(value: str) -> str:
    value = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[`*_~]", "", value)
    return " ".join(value.split()).replace("|", r"\|")


def _summary(body: str, frontmatter_summary: object) -> str:
    if isinstance(frontmatter_summary, str) and frontmatter_summary.strip():
        prose = frontmatter_summary
    else:
        lines = body.splitlines()
        h1_index = next(
            (index for index, line in enumerate(lines) if re.match(r"^\s{0,3}#\s+", line)),
            -1,
        )
        prose_lines: list[str] = []
        in_fence = False
        for line in lines[h1_index + 1 :]:
            if re.match(r"^\s{0,3}(`{3,}|~{3,})", line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            stripped = line.strip()
            if not stripped:
                if prose_lines:
                    break
                continue
            if stripped.startswith(("#", ">", "- ", "* ", "+ ", "|")) or re.match(r"\d+\.\s", stripped):
                if prose_lines:
                    break
                continue
            prose_lines.append(stripped)
        prose = " ".join(prose_lines)

    prose = _plain_text(prose)
    if not prose:
        return "—"
    first_sentence = re.split(r"(?<=[.!?])\s+", prose, maxsplit=1)[0]
    if len(first_sentence) > SUMMARY_LIMIT:
        first_sentence = first_sentence[: SUMMARY_LIMIT - 3].rstrip() + "..."
    return first_sentence


def _document_row(root: Path, path: Path) -> tuple[str, str, str, str, str, str] | None:
    text = path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)
    if parsed.data is None:
        return None
    data = parsed.data
    rel = relative_path(root, path)
    is_skill = rel.startswith("skills/") and path.name == "SKILL.md"
    nested = data.get("metadata", {}) if is_skill else {}
    if not isinstance(nested, dict):
        nested = {}
    title = data.get("title") or data.get("name") or path.stem
    doc_type = nested.get("type", data.get("type", "—"))
    status = nested.get("status", data.get("status", "—"))
    reviewed = nested.get("last_reviewed", data.get("last_reviewed", "—"))
    summary = _summary(parsed.body, data.get("summary"))
    return (
        rel,
        str(title),
        str(doc_type),
        str(status),
        str(reviewed) if reviewed is not None else "—",
        summary,
    )


def build_index(root: Path = ROOT) -> str:
    groups: dict[str, list[tuple[str, str, str, str, str, str]]] = defaultdict(list)
    for path in markdown_files(root):
        row = _document_row(root, path)
        if row is None:
            continue
        parts = Path(row[0]).parts
        area = parts[0] if len(parts) > 1 else "Root"
        groups[area].append(row)

    lines = [
        "# Knowledge index",
        "",
        "Generated from Markdown frontmatter. Read this index to locate current knowledge, then follow links to canonical documents.",
        "",
    ]
    for area in sorted(groups, key=lambda value: (value == "Root", value.casefold())):
        lines.extend([f"## {area}", "", "| Path | Title | Type | Status | Last reviewed | Summary |", "| --- | --- | --- | --- | --- | --- |"])
        for rel, title, doc_type, status, reviewed, summary in sorted(groups[area], key=lambda row: row[0].casefold()):
            safe_title = title.replace("|", r"\|")
            lines.append(f"| [{rel}]({rel}) | {safe_title} | {doc_type} | {status} | {reviewed} | {summary} |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def index_is_current(root: Path = ROOT) -> bool:
    index_path = root / "INDEX.md"
    try:
        return index_path.read_text(encoding="utf-8") == build_index(root)
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the Markdown knowledge index.")
    parser.add_argument("--check", action="store_true", help="fail if INDEX.md is missing or out of date")
    args = parser.parse_args(argv)
    index_path = ROOT / "INDEX.md"
    expected = build_index(ROOT)
    if args.check:
        if index_is_current(ROOT):
            print("INDEX.md is current.")
            return 0
        print("INDEX.md is stale; run `uv run python scripts/build_index.py`.")
        return 1
    index_path.write_text(expected, encoding="utf-8")
    print(f"Wrote INDEX.md ({sum(1 for line in expected.splitlines() if line.startswith('| ['))} documents).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
