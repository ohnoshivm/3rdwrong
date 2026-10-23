"""List documents awaiting founder review as a ranked markdown queue.

Every document whose frontmatter status is ``proposed`` or ``hypothesis`` is
listed, operating-critical areas first, then oldest ``last_reviewed`` first.
Inbox notes are excluded: they are triaged, not approved. See
business/review-queue.md for how the founder works through the queue.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.oscheck.common import as_date, markdown_files, parse_frontmatter, relative_path

ROOT = Path(__file__).resolve().parents[1]
QUEUED = ("proposed", "hypothesis")
# (label, path prefix) in priority order; the first matching prefix wins.
AREAS = [
    ("Decisions", "studio/decisions/"),
    ("Studio strategy and offers", "studio/"),
    ("Business engine", "business/"),
    ("Methods", "methods/"),
    ("Growth", "growth/"),
    ("Skills", "skills/"),
    ("Projects", "projects/"),
    ("Templates", "templates/"),
    ("Governance docs", "docs/"),
]
OTHER = "Other"


@dataclass(frozen=True)
class Entry:
    path: str
    title: str
    status: str
    area: str
    rank: int
    last_reviewed: date | None


def area_of(rel: str) -> tuple[int, str]:
    for rank, (label, prefix) in enumerate(AREAS):
        if rel.startswith(prefix):
            return rank, label
    return len(AREAS), OTHER


def collect(root: Path) -> list[Entry]:
    entries: list[Entry] = []
    for path in markdown_files(root):
        data = parse_frontmatter(path.read_text(encoding="utf-8")).data
        if not data:
            continue
        meta = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
        status = data.get("status", meta.get("status"))
        if status not in QUEUED or (data.get("type") or meta.get("type")) == "inbox":
            continue
        rel = relative_path(root, path)
        rank, area = area_of(rel)
        title = data.get("title") or data.get("name") or rel
        reviewed = as_date(data.get("last_reviewed", meta.get("last_reviewed")))
        entries.append(Entry(rel, str(title), status, area, rank, reviewed))
    # Within an area the oldest review comes first; undated documents lead.
    return sorted(entries, key=lambda e: (e.rank, e.last_reviewed or date.min, e.path))


def render(entries: list[Entry], today: date, limit: int | None = None) -> str:
    shown = entries[:limit] if limit else entries
    lines = [
        f"# Founder review queue — {today.isoformat()}",
        "",
        f"{len(entries)} documents await review ({sum(e.status == 'proposed' for e in entries)} proposed, "
        f"{sum(e.status == 'hypothesis' for e in entries)} hypothesis). Showing {len(shown)}.",
        "",
        "| # | Area | Document | Status | Last reviewed | Age (days) |",
        "| ---: | --- | --- | --- | --- | ---: |",
    ]
    for number, entry in enumerate(shown, start=1):
        reviewed = entry.last_reviewed.isoformat() if entry.last_reviewed else "never"
        age = str((today - entry.last_reviewed).days) if entry.last_reviewed else "—"
        title = entry.title.replace("|", r"\|")
        lines.append(f"| {number} | {entry.area} | [{title}]({entry.path}) | {entry.status} | {reviewed} | {age} |")
    lines += ["", "Decide each item: approve, revise, park or reject (see business/review-queue.md)."]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print the founder review queue as markdown.")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this repository)")
    parser.add_argument("--limit", type=int, help="show only the first N items (one session is usually 5-8)")
    args = parser.parse_args(argv)
    sys.stdout.write(render(collect(args.root.resolve()), date.today(), args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
