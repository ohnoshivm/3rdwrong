from __future__ import annotations

from pathlib import Path
from urllib.parse import unquote, urlsplit

from .common import Issue, extract_markdown_links, heading_slugs, markdown_files, relative_path


def check_links(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    for source in markdown_files(root):
        source_rel = relative_path(root, source)
        text = source.read_text(encoding="utf-8")
        for line, target in extract_markdown_links(text):
            target = target.strip()
            if not target or "{{" in target or "}}" in target:
                continue
            parts = urlsplit(target)
            if parts.scheme in {"http", "https", "mailto"} or target.startswith("//"):
                continue
            if parts.scheme:
                continue
            fragment = unquote(parts.fragment)
            raw_path = unquote(parts.path)
            target_path = (source.parent / raw_path).resolve() if raw_path else source.resolve()
            try:
                target_path.relative_to(root.resolve())
            except ValueError:
                issues.append(Issue(source_rel, line, "links", f"relative link escapes repository: '{target}'"))
                continue
            if not target_path.exists():
                issues.append(Issue(source_rel, line, "links", f"target does not exist: '{target}'"))
                continue
            if fragment and target_path.is_file() and target_path.suffix.lower() in {".md", ".markdown"}:
                anchors = heading_slugs(target_path.read_text(encoding="utf-8"))
                if fragment not in anchors:
                    issues.append(Issue(source_rel, line, "links", f"anchor '#{fragment}' not found in '{raw_path or source.name}'"))
    return issues
