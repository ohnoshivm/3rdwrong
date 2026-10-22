from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

from .common import Issue, as_date, is_frontmatter_exempt, is_iso_date, markdown_files, parse_frontmatter, relative_path


def check_frontmatter(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    types = set(config["types"])
    statuses = set(config["statuses"])
    exempt = config["frontmatter_exempt_globs"]
    default_required = ("title", "type", "status", "owner", "last_reviewed")
    for path in markdown_files(root):
        rel = relative_path(root, path)
        if is_frontmatter_exempt(rel, exempt) or (rel.startswith("skills/") and path.name == "SKILL.md"):
            continue
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed.data is None:
            issues.append(Issue(rel, parsed.error_line, "frontmatter", parsed.error))
            continue
        data = parsed.data
        doc_type = data.get("type")
        required = ("title", "type", "status", "captured") if doc_type == "inbox" else default_required
        for key in required:
            if key not in data or data[key] in (None, ""):
                issues.append(Issue(rel, 2, "frontmatter", f"missing required key '{key}'"))
        if data.get("title") is not None and not isinstance(data["title"], str):
            issues.append(Issue(rel, 2, "frontmatter", "'title' must be a string"))
        if data.get("type") is not None and (not isinstance(data["type"], str) or data["type"] not in types):
            issues.append(Issue(rel, 2, "frontmatter", f"unknown type '{data['type']}'"))
        if data.get("status") is not None and (not isinstance(data["status"], str) or data["status"] not in statuses):
            issues.append(Issue(rel, 2, "frontmatter", f"unknown status '{data['status']}'"))
        if "last_reviewed" in data and not is_iso_date(data["last_reviewed"]):
            issues.append(Issue(rel, 2, "frontmatter", "'last_reviewed' must be an ISO date (YYYY-MM-DD)"))
        if "captured" in data and not is_iso_date(data["captured"]):
            issues.append(Issue(rel, 2, "frontmatter", "'captured' must be an ISO date (YYYY-MM-DD)"))
        if "version" in data and (not isinstance(data["version"], str) or not data["version"].strip()):
            issues.append(Issue(rel, 2, "frontmatter", "'version' must be a non-empty string"))
        if "review_every_days" in data and (
            isinstance(data["review_every_days"], bool)
            or not isinstance(data["review_every_days"], int)
            or data["review_every_days"] < 1
        ):
            issues.append(Issue(rel, 2, "frontmatter", "'review_every_days' must be a positive integer"))
        if data.get("status") == "approved":
            if not isinstance(data.get("approved_by"), str) or not data["approved_by"].strip():
                issues.append(Issue(rel, 2, "frontmatter", "approved status requires a named 'approved_by'"))
            if not is_iso_date(data.get("approved_on")):
                issues.append(Issue(rel, 2, "frontmatter", "approved status requires ISO date 'approved_on'"))
        if data.get("status") == "superseded" and not data.get("superseded_by"):
            issues.append(Issue(rel, 2, "frontmatter", "superseded status requires 'superseded_by'"))
        if doc_type == "inbox" and data.get("status") != "proposed":
            issues.append(Issue(rel, 2, "frontmatter", "inbox notes must use status 'proposed'"))
        if isinstance(doc_type, str) and doc_type in {"research", "reference-study", "principle"}:
            sources = data.get("sources")
            if not isinstance(sources, list) or not sources:
                issues.append(Issue(rel, 2, "frontmatter", "this type requires a non-empty 'sources' list"))
            else:
                for index, source in enumerate(sources, start=1):
                    if not isinstance(source, dict):
                        issues.append(Issue(rel, 2, "frontmatter", f"source {index} must be a mapping"))
                        continue
                    for key in ("title", "url", "accessed"):
                        if not source.get(key):
                            issues.append(Issue(rel, 2, "frontmatter", f"source {index} requires '{key}'"))
                    url = source.get("url")
                    if url and (not isinstance(url, str) or urlparse(url).scheme != "https"):
                        issues.append(Issue(rel, 2, "frontmatter", f"source {index} URL must use https"))
                    if source.get("accessed") and not is_iso_date(source["accessed"]):
                        issues.append(Issue(rel, 2, "frontmatter", f"source {index} 'accessed' must be an ISO date"))
            if doc_type in {"research", "reference-study"} and data.get("status") != "reference":
                issues.append(Issue(rel, 2, "frontmatter", "research and reference-study documents use status 'reference'"))
        if data.get("type") == "template" and (
            not isinstance(data.get("template_for"), str) or data["template_for"] not in types
        ):
            issues.append(Issue(rel, 2, "frontmatter", "template requires 'template_for' set to a valid type"))
        if "date" in data and data["date"] is not None and not is_iso_date(data["date"]):
            issues.append(Issue(rel, 2, "frontmatter", "'date' must be an ISO date (YYYY-MM-DD)"))
        if "approved_on" in data and data["approved_on"] is not None and not is_iso_date(data["approved_on"]):
            issues.append(Issue(rel, 2, "frontmatter", "'approved_on' must be an ISO date (YYYY-MM-DD)"))
    return issues
