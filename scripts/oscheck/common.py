from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class Issue:
    path: str
    line: int
    check: str
    message: str
    severity: str = "error"

    def render(self) -> str:
        message = f"{self.severity}: {self.message}" if self.severity == "warning" else self.message
        return f"{self.path}:{self.line}: [{self.check}] {message}"


@dataclass(frozen=True)
class ParsedFrontmatter:
    data: dict[str, Any] | None
    body: str
    body_line: int
    error: str = ""
    error_line: int = 1


def parse_frontmatter(text: str) -> ParsedFrontmatter:
    text = text.removeprefix("\ufeff")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return ParsedFrontmatter(None, text, 1, "missing opening --- frontmatter delimiter", 1)
    closing = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if closing is None:
        return ParsedFrontmatter(None, "", len(lines) + 1, "missing closing --- frontmatter delimiter", 1)
    raw = "".join(lines[1:closing])
    body = "".join(lines[closing + 1 :])
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        line = mark.line + 2 if mark is not None else 2
        problem = getattr(exc, "problem", None) or "invalid YAML"
        return ParsedFrontmatter(None, body, closing + 2, f"invalid YAML: {problem}", line)
    if not isinstance(data, dict):
        return ParsedFrontmatter(None, body, closing + 2, "frontmatter must be a YAML mapping", 2)
    return ParsedFrontmatter(data, body, closing + 2)


def is_iso_date(value: object) -> bool:
    if type(value) is date:
        return True
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def as_date(value: object) -> date | None:
    if type(value) is date:
        return value
    if is_iso_date(value):
        return date.fromisoformat(str(value))
    return None


# Third-party material keeps its upstream form: no OS frontmatter, link or index
# rules apply. The secret scan still covers these trees.
THIRD_PARTY_TREES = {(".claude", "agents"), ("toolkit", "vendor"), ("toolkit", "plugins")}


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file()
        and not {".git", ".venv", "node_modules"}.intersection(path.relative_to(root).parts)
        and path.relative_to(root).parts[:2] not in THIRD_PARTY_TREES
    )


def relative_path(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def is_frontmatter_exempt(path: str, patterns: list[str]) -> bool:
    normalized = path.replace("\\", "/")
    for pattern in patterns:
        if normalized == pattern or Path(normalized).match(pattern):
            return True
        if "/" not in pattern and Path(normalized).name == pattern:
            return True
    return False


def strip_markdown_code(text: str) -> str:
    output: list[str] = []
    fence_char = ""
    fence_size = 0
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if not fence_char:
                fence_char, fence_size = marker[0], len(marker)
                output.append("")
                continue
            if marker[0] == fence_char and len(marker) >= fence_size:
                fence_char, fence_size = "", 0
            output.append("")
            continue
        if fence_char:
            output.append("")
            continue
        output.append(re.sub(r"(`+).*?\1", "", line))
    return "\n".join(output)


def extract_markdown_links(text: str) -> list[tuple[int, str]]:
    clean = strip_markdown_code(text)
    result: list[tuple[int, str]] = []
    inline = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))")
    definition = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|(\S+))", re.MULTILINE)
    for match in inline.finditer(clean):
        result.append((clean.count("\n", 0, match.start()) + 1, match.group(1) or match.group(2)))
    for match in definition.finditer(clean):
        result.append((clean.count("\n", 0, match.start()) + 1, match.group(1) or match.group(2)))
    return result


def slugify_heading(heading: str) -> str:
    heading = re.sub(r"<[^>]*>", "", heading)
    heading = re.sub(r"!?(?:\[([^\]]+)\]\([^)]*\))", r"\1", heading)
    heading = heading.replace("&amp;", "&").lower().strip()
    base = "".join(char for char in heading if char.isalnum() or char in " -_")
    return re.sub(r"\s+", "-", base).strip("-")


def heading_slugs(text: str) -> set[str]:
    clean = strip_markdown_code(text)
    seen: dict[str, int] = {}
    result: set[str] = set()
    for line in clean.splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = slugify_heading(match.group(1))
        count = seen.get(base, 0)
        slug = base if count == 0 else f"{base}-{count}"
        seen[base] = count + 1
        result.add(slug)
    return result
