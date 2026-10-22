from __future__ import annotations

import re
from pathlib import Path

from .common import Issue, as_date, extract_markdown_links, parse_frontmatter, relative_path

FILENAME = re.compile(r"^(\d{4})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")
ID = re.compile(r"^D-(\d{4})$")


def _h2_headings(body: str) -> list[tuple[int, str]]:
    return [
        (line_number, match.group(1).strip())
        for line_number, line in enumerate(body.splitlines(), start=1)
        if (match := re.match(r"^ {0,3}##\s+(.+?)\s*#*\s*$", line))
    ]


def check_decisions(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    directory = root / "studio" / "decisions"
    index = directory / "README.md"
    files = sorted(path for path in directory.glob("*.md") if path.name != "README.md") if directory.exists() else []
    records: list[tuple[int, Path, dict, str]] = []
    for path in files:
        rel = relative_path(root, path)
        match = FILENAME.fullmatch(path.name)
        if not match:
            issues.append(Issue(rel, 1, "decisions", "filename must match NNNN-lowercase-slug.md"))
            number = -1
        else:
            number = int(match.group(1))
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed.data is None:
            issues.append(Issue(rel, parsed.error_line, "decisions", parsed.error))
            continue
        data = parsed.data
        id_match = ID.fullmatch(str(data.get("id", "")))
        if not id_match or int(id_match.group(1)) != number:
            issues.append(Issue(rel, 2, "decisions", "id must match the filename number (for example D-0001)"))
        if data.get("type") != "decision":
            issues.append(Issue(rel, 2, "decisions", "decision record requires type 'decision'"))
        if not isinstance(data.get("status"), str) or data["status"] not in set(config["decision_statuses"]):
            issues.append(Issue(rel, 2, "decisions", f"invalid decision status '{data.get('status', '')}'"))
        if as_date(data.get("date")) is None:
            issues.append(Issue(rel, 2, "decisions", "decision requires ISO date 'date'"))
        actual = _h2_headings(parsed.body)
        actual_names = [name for _, name in actual]
        cursor = 0
        for required in config["required_decision_sections"]:
            try:
                cursor = actual_names.index(required, cursor) + 1
            except ValueError:
                issues.append(Issue(rel, 1, "decisions", f"required H2 section missing or out of order: '{required}'"))
                break
        records.append((number, path, data, rel))

    numbered = [number for number, _, _, _ in records if number > 0]
    if numbered:
        expected = list(range(1, max(numbered) + 1))
        if sorted(numbered) != expected:
            missing = sorted(set(expected) - set(numbered))
            issues.append(Issue("studio/decisions/README.md", 1, "decisions", f"decision numbering must be contiguous from 0001; missing {', '.join(f'{n:04d}' for n in missing)}"))

    if records and not index.exists():
        issues.append(Issue("studio/decisions/README.md", 1, "decisions", "decision index is missing"))
    index_links: set[str] = set()
    if index.exists():
        index_text = index.read_text(encoding="utf-8")
        for _, target in extract_markdown_links(index_text):
            if "{{" in target:
                continue
            index_links.add(Path(target.split("#", 1)[0]).name)
    for _, path, data, rel in records:
        if path.name not in index_links:
            issues.append(Issue("studio/decisions/README.md", 1, "decisions", f"decision '{path.name}' is not listed as a link"))
        if data.get("status") == "superseded":
            successor = str(data.get("superseded_by", ""))
            target_exists = False
            if successor in {str(record_data.get("id", "")) for _, _, record_data, _ in records}:
                target_exists = True
            else:
                candidate_paths = [root / successor, path.parent / successor, directory / Path(successor).name]
                target_exists = any(candidate.exists() for candidate in candidate_paths)
            if not target_exists:
                issues.append(Issue(rel, 2, "decisions", f"superseded_by target does not exist: '{successor}'"))
    return issues
