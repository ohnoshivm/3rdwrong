from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

from .common import Issue, as_date, markdown_files, parse_frontmatter, relative_path


def check_stale(root: Path, config: dict, today: date | None = None) -> list[Issue]:
    today = today or date.today()
    defaults = config["default_review_every_days"]
    issues: list[Issue] = []
    for path in markdown_files(root):
        rel = relative_path(root, path)
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed.data is None:
            continue
        data = parsed.data
        if data.get("type") == "inbox":
            captured = as_date(data.get("captured"))
            if captured is not None and captured + timedelta(days=30) < today:
                issues.append(
                    Issue(rel, 2, "stale", f"inbox note has been waiting {today - captured} days; triage or remove it", "warning")
                )
            continue
        if rel.startswith("skills/") and path.name == "SKILL.md":
            data = data.get("metadata", {})
        reviewed = as_date(data.get("last_reviewed")) if isinstance(data, dict) else None
        if reviewed is None:
            continue
        doc_type = "skill" if rel.startswith("skills/") and path.name == "SKILL.md" else parsed.data.get("type")
        if not isinstance(doc_type, str):
            continue
        interval = data.get("review_every_days") or defaults.get(doc_type)
        if isinstance(interval, int) and not isinstance(interval, bool) and reviewed + timedelta(days=interval) < today:
            issues.append(Issue(rel, 2, "stale", f"review overdue; last reviewed {reviewed.isoformat()} (every {interval} days)", "warning"))
    return issues
