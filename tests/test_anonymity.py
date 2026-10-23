from __future__ import annotations

import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.oscheck import anonymity
from scripts.oscheck.anonymity import check_anonymity, load_deny_terms, scan_repository, scan_staged, scan_text
from scripts.validate import run_checks

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "schemas" / "metadata.json").read_text(encoding="utf-8"))
REC = "projects/quiet-harbour/brief.md"

# label -> (lines that must be caught, lines that must pass)
CASES = {
    "email address": (
        ["Write to founder@realclient.in", "cc: Ops.Team@client-domain.co.uk"],  # secret-scan: allow
        ["studio@example.com", "a@stillsoil.example", "no address here", "user@users.noreply.github.com"],  # secret-scan: allow
    ),
    "phone number": (
        ["+91 98765 43210", "+91-98765-43210", "call 9876543210", "landline 022 2345 6789", "+44 20 7946 0958"],
        ["2026-10-23", "version 1.2.3", "between 2 and 6 weeks", "D-0021", "1440, 834 and 390 px", "LCP 2500 ms"],
    ),
    "currency amount": (
        ["fee ₹50,000", "₹ 1.2", "Rs. 2000", "rs 500", "INR 5000", "$1,200", "€300", "£45", "5,00,000 INR", "12 lakh", "2 crore", "USD 900"],  # secret-scan: allow
        ["price on request", "$HOME", "money stays in the vault", "Rs without digits", "₹ symbol only", "3 hours"],
    ),
    "GSTIN": (["GSTIN 27ABCDE1234F1Z5"], ["27 ABCDE"]),
    "PAN": (["PAN ABCDE1234F"], ["WCAG 2.2 AA", "ABCDE-1234"]),  # secret-scan: allow
    "IFSC code": (["IFSC HDFC0001234"], ["HDFC1001234", "L0 Lead"]),
    "Aadhaar-like number": (["1234 5678 9012", "1234-5678-9012", "123456789012"], ["1234 5678", "2026-10-23"]),  # secret-scan: allow
}


def labels(line: str, rel: str = REC) -> set[str]:
    return {issue.message.split(" in a public")[0] for issue in scan_text(rel, line)}


class GenericPatternTests(unittest.TestCase):
    def test_every_pattern_positive_and_negative(self) -> None:
        for label, (positives, negatives) in CASES.items():
            for line in positives:
                with self.subTest(label=label, line=line):
                    self.assertIn(label, labels(line))
            for line in negatives:
                with self.subTest(label=label, negative=line):
                    self.assertNotIn(label, labels(line))

    def test_generic_checks_only_apply_to_guarded_paths(self) -> None:
        self.assertEqual(scan_text("methods/lifecycle.md", "Contact founder@realclient.in for ₹500"), [])  # secret-scan: allow
        self.assertEqual(len(scan_text(REC, "Contact founder@realclient.in for ₹500")), 2)  # secret-scan: allow

    def test_studio_domain_allowlist(self) -> None:
        anonymity.STUDIO_EMAIL_DOMAINS.add("studio.test-domain.in")
        self.addCleanup(anonymity.STUDIO_EMAIL_DOMAINS.discard, "studio.test-domain.in")
        self.assertEqual(scan_text(REC, "hello@studio.test-domain.in"), [])  # secret-scan: allow


class TreeTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.project = self.root / "projects" / "quiet-harbour"
        self.project.mkdir(parents=True)
        (self.project / "README.md").write_text("# Quiet Harbour\n\nAnonymised record.\n", encoding="utf-8")

    def test_clean_tree_passes(self) -> None:
        self.assertEqual(check_anonymity(self.root, CONFIG), [])

    def test_non_text_files_are_blocked(self) -> None:
        for name in ("moodboard.png", "contract.pdf", "notes.docx", "export.csv"):
            (self.project / name).write_bytes(b"\x89PNG")
        (self.project / "data.yaml").write_text("a: 1\n", encoding="utf-8")
        (self.project / ".DS_Store").write_bytes(b"\x00")
        flagged = sorted(Path(i.path).name for i in check_anonymity(self.root, CONFIG))
        self.assertEqual(flagged, ["contract.pdf", "export.csv", "moodboard.png", "notes.docx"])

    def test_validator_runs_anonymity_check(self) -> None:
        (self.project / "brief.md").write_text("Budget ₹ 4,00,000\n", encoding="utf-8")  # secret-scan: allow
        issues = run_checks(self.root, CONFIG, ["anonymity"])
        self.assertEqual([(i.path, i.line, i.check) for i in issues], [("projects/quiet-harbour/brief.md", 1, "anonymity")])

    def test_repository_examples_pass(self) -> None:
        self.assertEqual(check_anonymity(ROOT, CONFIG), [])


class DenyListTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        base = Path(temp.name)
        self.vault = base / "vault"
        self.vault.mkdir()
        (self.vault / "clients.yaml").write_text(
            """clients:
  quiet-harbour:
    name: Monsoon Leaf Company
    aliases: [MLC Teas]
    people:
      - name: Asha Verma
        role: Founder
        email: asha@monsoonleaf.in  # secret-scan: allow
        phone: "+91 98111 22334"
    emails: [hello@monsoonleaf.in]  # secret-scan: allow
    domains: [monsoonleaf.in]
    phones: ["022 4000 1111"]
""",
            encoding="utf-8",
        )
        self.root = base / "repo"
        (self.root / "docs").mkdir(parents=True)
        self.deny = load_deny_terms(self.vault)

    def test_terms_loaded_from_every_field(self) -> None:
        sources = {source for source, _ in self.deny}
        self.assertEqual(sources, {
            "quiet-harbour.name", "quiet-harbour.aliases", "quiet-harbour.emails", "quiet-harbour.domains",
            "quiet-harbour.phones", "quiet-harbour.people.name", "quiet-harbour.people.email", "quiet-harbour.people.phone",
        })

    def test_each_term_blocked_anywhere_without_echoing_it(self) -> None:
        leaks = [
            "We met monsoon leaf company today.",
            "MLC Teas launch",
            "Asha Verma approved",
            "see monsoonleaf.in",
            "mail hello@monsoonleaf.in",  # secret-scan: allow
            "call 98111 22334",
            "office 02240001111",
        ]
        for line in leaks:
            with self.subTest(line=line):
                issues = scan_text("docs/notes.md", line, self.deny)
                self.assertTrue(issues)
                self.assertTrue(all("deny-listed" in i.message for i in issues))
                for _, term in self.deny:
                    self.assertFalse(any(term.lower() in i.render().lower() for i in issues))

    def test_clean_text_and_partial_words_pass(self) -> None:
        for line in ("Monsoon season planning", "The Leaf motif", "Ashan", "2026-10-23"):
            with self.subTest(line=line):
                self.assertEqual(scan_text("docs/notes.md", line, self.deny), [])

    def test_repository_scan_and_cli(self) -> None:
        (self.root / "docs" / "clean.md").write_text("Nothing to see.\n", encoding="utf-8")
        self.assertEqual(scan_repository(self.root, self.deny), [])
        (self.root / "docs" / "leak.md").write_text("Draft for Asha Verma\n", encoding="utf-8")
        self.assertEqual([i.path for i in scan_repository(self.root, self.deny)], ["docs/leak.md"])
        with redirect_stdout(io.StringIO()) as out:
            code = anonymity.main(["--root", str(self.root), "--vault", str(self.vault)])
        self.assertEqual(code, 1)
        self.assertIn("deny-list on", out.getvalue())
        self.assertNotIn("Asha", out.getvalue())

    def test_missing_vault_disables_deny_list(self) -> None:
        self.assertEqual(load_deny_terms(self.vault / "absent"), [])

    def test_staged_mode_scans_only_staged_blobs(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / "docs" / "staged.md").write_text("Asha Verma\n", encoding="utf-8")
        (self.root / "docs" / "unstaged.md").write_text("MLC Teas\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", "docs/staged.md"], check=True)
        (self.root / "docs" / "staged.md").write_text("cleaned in working tree\n", encoding="utf-8")
        self.assertEqual([i.path for i in scan_staged(self.root, self.deny)], ["docs/staged.md"])


if __name__ == "__main__":
    unittest.main()
