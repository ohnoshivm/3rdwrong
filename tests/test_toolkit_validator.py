"""Toolkit validator wiring: third-party trees skip OS rules but never the secret scan."""
from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.oscheck.common import markdown_files
from scripts.oscheck.secrets import check_secrets
from scripts.oscheck.toolkit import check_toolkit

KEY_LINE = 'token = "abcdefgh12345678"'  # secret-scan: allow (fake fixture)


class ToolkitValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ("vendor/a", "plugins/p"):
            path = self.root / "toolkit" / name / "doc.md"
            path.parent.mkdir(parents=True)
            path.write_text(KEY_LINE + "\n")

    def allow(self, **entry: str) -> None:
        base = {"path": "toolkit/vendor/a/doc.md", "line_sha256": hashlib.sha256(KEY_LINE.encode()).hexdigest(), "label": "credential assignment", "reason": "fake"}
        base.update(entry)
        (self.root / "toolkit/secret-allowlist.json").write_text(json.dumps({"entries": [base]}))

    def secret_paths(self) -> list[str]:
        return sorted(issue.path for issue in check_secrets(self.root, {}))

    def test_third_party_markdown_is_skipped_by_document_checks(self) -> None:
        (self.root / "notes.md").write_text("# Notes\n")
        self.assertEqual([p.name for p in markdown_files(self.root)], ["notes.md"])

    def test_secret_scan_still_covers_toolkit_trees(self) -> None:
        self.assertEqual(self.secret_paths(), ["toolkit/plugins/p/doc.md", "toolkit/vendor/a/doc.md"])

    def test_reviewed_line_is_bound_to_path_hash_and_label(self) -> None:
        self.allow()
        self.assertEqual(self.secret_paths(), ["toolkit/plugins/p/doc.md"])
        (self.root / "toolkit/vendor/a/doc.md").write_text(KEY_LINE + " \n")
        self.assertEqual(self.secret_paths(), ["toolkit/plugins/p/doc.md", "toolkit/vendor/a/doc.md"])

    def test_wrong_label_or_missing_reason_does_not_suppress(self) -> None:
        self.allow(label="email address")
        self.assertIn("toolkit/vendor/a/doc.md", self.secret_paths())
        self.allow(reason="")
        self.assertIn("toolkit/secret-allowlist.json", self.secret_paths())
        self.assertIn("toolkit/vendor/a/doc.md", self.secret_paths())

    def test_allowlist_cannot_cover_paths_outside_toolkit(self) -> None:
        self.allow(path="studio/doc.md")
        self.assertIn("toolkit/secret-allowlist.json", self.secret_paths())

    def test_toolkit_check_is_inert_without_sources(self) -> None:
        self.assertEqual(check_toolkit(self.root, {}), [])


if __name__ == "__main__":
    unittest.main()
