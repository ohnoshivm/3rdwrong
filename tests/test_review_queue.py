from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import review_queue


def doc(status: str, reviewed: str, doc_type: str = "guide", title: str = "Doc") -> str:
    return f"---\ntitle: {title}\ntype: {doc_type}\nstatus: {status}\nowner: founder\nlast_reviewed: {reviewed}\n---\n# {title}\n"


class ReviewQueueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        files = {
            "templates/old.md": doc("proposed", "2026-01-01", "template", "Old template"),
            "business/new.md": doc("proposed", "2026-10-20", title="New business"),
            "business/older.md": doc("hypothesis", "2026-09-01", title="Older business"),
            "studio/decisions/0099-x.md": doc("proposed", "2026-10-22", "decision", "Decision"),
            "studio/approved.md": doc("approved", "2026-10-01", title="Approved"),
            "inbox/note.md": "---\ntitle: Note\ntype: inbox\nstatus: proposed\ncaptured: 2026-10-01\n---\n# Note\n",
            "skills/3w-x/SKILL.md": "---\nname: 3w-x\nmetadata:\n  type: skill\n  status: proposed\n  last_reviewed: 2026-10-02\n---\n# 3w-x\n",
            "taste/a.md": doc("hypothesis", "2026-05-01", title="Taste | note"),
        }
        for rel, text in files.items():
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_ranks_by_area_then_age_and_filters(self) -> None:
        paths = [entry.path for entry in review_queue.collect(self.root)]
        self.assertEqual(
            paths,
            [
                "studio/decisions/0099-x.md",
                "business/older.md",
                "business/new.md",
                "skills/3w-x/SKILL.md",
                "templates/old.md",
                "taste/a.md",
            ],
        )

    def test_render_markdown(self) -> None:
        entries = review_queue.collect(self.root)
        text = review_queue.render(entries, date(2026, 10, 23), limit=2)
        self.assertIn("6 documents await review (4 proposed, 2 hypothesis). Showing 2.", text)
        self.assertIn("| 1 | Decisions | [Decision](studio/decisions/0099-x.md) | proposed | 2026-10-22 | 1 |", text)
        self.assertNotIn("Old template", text)
        full = review_queue.render(entries, date(2026, 10, 23))
        self.assertIn(r"Taste \| note", full)


if __name__ == "__main__":
    unittest.main()
