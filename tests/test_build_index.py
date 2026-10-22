from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.build_index import build_index, main as build_index_main
from scripts.oscheck.index import check_index


class BuildIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def put(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_build_index_groups_docs_and_uses_summary_fallbacks(self) -> None:
        self.put(
            "studio/strategy.md",
            "---\ntitle: Studio strategy\ntype: strategy\nstatus: proposed\nlast_reviewed: 2026-10-22\nsummary: Explicit summary. Extra sentence.\n---\n\n# Studio strategy\n\nFallback prose is ignored.\n",
        )
        self.put(
            "skills/demo/SKILL.md",
            "---\nname: demo\ndescription: Demo skill.\nmetadata:\n  type: skill\n  status: experimental\n  last_reviewed: 2026-10-22\n---\n\n# Demo skill\n\nThis skill has a concise purpose. A second sentence.\n",
        )
        self.put("inbox/note.md", "---\ntitle: Captured note\ntype: inbox\nstatus: proposed\ncaptured: 2026-10-22\n---\n\n# Captured note\n\nA rough observation for triage.\n")
        self.put("README.md", "# Not indexed without frontmatter\n")

        first = build_index(self.root)
        self.assertEqual(first, build_index(self.root))
        self.assertLess(first.index("## inbox"), first.index("## skills"))
        self.assertLess(first.index("## skills"), first.index("## studio"))
        self.assertIn("[studio/strategy.md](studio/strategy.md)", first)
        self.assertIn("Explicit summary.", first)
        self.assertIn("This skill has a concise purpose.", first)
        self.assertIn("A rough observation for triage.", first)
        self.assertNotIn("README.md", first)

    def test_build_index_excludes_vendor_agents_even_with_frontmatter(self) -> None:
        self.put(".claude/agents/vendor.md", "---\nname: Vendor\n---\n\n# Vendor\n\nUpstream persona.\n")
        self.assertNotIn("vendor", build_index(self.root).lower())

    def test_build_index_truncates_summaries_to_about_140_characters(self) -> None:
        long_summary = "A" * 200
        self.put(
            "docs/long.md",
            f"---\ntitle: Long\ntype: guide\nstatus: proposed\nsummary: {long_summary}\n---\n\n# Long\n\nBody.\n",
        )
        index = build_index(self.root)
        self.assertIn("A" * 137 + "...", index)
        self.assertNotIn("A" * 138, index)

    def test_build_index_check_fails_when_stale_and_passes_when_current(self) -> None:
        source = self.put("docs/guide.md", "---\ntitle: Guide\ntype: guide\nstatus: proposed\n---\n\n# Guide\n\nA guide.\n")
        output = io.StringIO()
        with patch("scripts.build_index.ROOT", self.root), redirect_stdout(output):
            self.assertEqual(build_index_main(["--check"]), 1)
        self.assertIn("INDEX.md is stale", output.getvalue())

        (self.root / "INDEX.md").write_text(build_index(self.root), encoding="utf-8")
        output = io.StringIO()
        with patch("scripts.build_index.ROOT", self.root), redirect_stdout(output):
            self.assertEqual(build_index_main(["--check"]), 0)
        self.assertIn("INDEX.md is current", output.getvalue())
        self.assertTrue(source.exists())

    def test_validator_index_check_detects_stale_output(self) -> None:
        self.put("guide.md", "---\ntitle: Guide\ntype: guide\nstatus: proposed\n---\n\n# Guide\n\nA guide.\n")
        self.put("INDEX.md", "stale\n")
        self.assertTrue(check_index(self.root, {})[0].check == "index")
        (self.root / "INDEX.md").write_text(build_index(self.root), encoding="utf-8")
        self.assertEqual(check_index(self.root, {}), [])


if __name__ == "__main__":
    unittest.main()
