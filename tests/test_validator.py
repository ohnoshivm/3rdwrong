from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.new_doc import main as new_doc_main
from scripts.oscheck.common import is_iso_date, parse_frontmatter, slugify_heading
from scripts.oscheck.decisions import check_decisions
from scripts.oscheck.frontmatter import check_frontmatter
from scripts.oscheck.links import check_links
from scripts.oscheck.required import check_required
from scripts.oscheck.secrets import check_secrets
from scripts.oscheck.skills import check_skills
from scripts.oscheck.stale import check_stale
from scripts.sync_labels import main as sync_labels_main
from scripts.validate import main as validate_main


SECTIONS = [
    "Purpose",
    "When to use",
    "When not to use",
    "Inputs",
    "Dependencies",
    "Procedure",
    "Evidence requirements",
    "Output",
    "Quality checks",
    "Failure conditions",
    "Human review",
    "Example",
]


def metadata() -> dict:
    return {
        "types": [
            "strategy", "decision", "research", "reference-study", "principle",
            "method", "checklist", "template", "skill", "project", "experiment",
            "guide", "policy", "inbox",
        ],
        "statuses": [
            "approved", "proposed", "hypothesis", "experimental", "rejected",
            "superseded", "reference",
        ],
        "decision_statuses": [
            "approved", "proposed", "hypothesis", "experimental", "rejected", "superseded",
        ],
        "default_review_every_days": {"guide": 180, "skill": 90},
        "required_files": [],
        "frontmatter_exempt_globs": [],
        "required_skill_sections": SECTIONS,
        "required_decision_sections": [
            "Decision", "Status", "Rationale", "Alternatives considered", "Evidence",
            "Consequences", "Revision triggers",
        ],
        "secret_allowlist": {"emails": [], "pan": [], "aadhaar": []},
    }


def write_metadata(root: Path, data: dict | None = None) -> dict:
    config = data or metadata()
    (root / "schemas").mkdir(parents=True, exist_ok=True)
    (root / "schemas" / "metadata.json").write_text(json.dumps(config), encoding="utf-8")
    return config


def doc_frontmatter(**changes: object) -> str:
    values: dict[str, object] = {
        "title": "Example document",
        "type": "guide",
        "status": "proposed",
        "owner": "founder",
        "last_reviewed": "2026-10-22",
    }
    values.update(changes)
    import yaml

    return "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n\n# Example document\n\nBody.\n"


def decision_doc(number: int = 1, **changes: object) -> str:
    values: dict[str, object] = {
        "id": f"D-{number:04d}",
        "title": "Example decision",
        "type": "decision",
        "status": "proposed",
        "date": "2026-10-22",
        "owner": "founder",
        "last_reviewed": "2026-10-22",
    }
    values.update(changes)
    import yaml

    body = "\n\n".join(f"## {heading}\n\nNotes." for heading in metadata()["required_decision_sections"])
    return "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n\n# Example decision\n\n" + body + "\n"


def skill_doc(name: str = "demo-skill", sections: list[str] | None = None) -> str:
    import yaml

    frontmatter = {
        "name": name,
        "description": "A concise skill description.",
        "metadata": {
            "type": "skill",
            "status": "experimental",
            "owner": "founder",
            "last_reviewed": "2026-10-22",
            "version": "0.1.0",
        },
    }
    section_names = SECTIONS if sections is None else sections
    body = "\n\n".join(f"## {heading}\n\nNotes." for heading in section_names)
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False) + "---\n\n# Demo skill\n\n" + body + "\n"


class ValidatorChecksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.config = write_metadata(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def put(self, relative: str, content: str = "") -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_frontmatter_parser_returns_mapping_and_body(self) -> None:
        parsed = parse_frontmatter(doc_frontmatter())
        self.assertEqual(parsed.data["title"], "Example document")
        self.assertIn("# Example document", parsed.body)
        self.assertEqual(parsed.error, "")

    def test_frontmatter_parser_reports_missing_delimiters(self) -> None:
        parsed = parse_frontmatter("# Plain\n")
        self.assertIsNone(parsed.data)
        self.assertTrue(parsed.error)

    def test_iso_date_rejects_timestamp_values(self) -> None:
        parsed = parse_frontmatter("---\nlast_reviewed: 2026-10-22T12:00:00Z\n---\n")
        self.assertIsNotNone(parsed.data)
        self.assertFalse(is_iso_date(parsed.data["last_reviewed"]))

    def test_frontmatter_check_accepts_valid_metadata_and_rejects_bad_date(self) -> None:
        self.put("good.md", doc_frontmatter())
        self.put("bad.md", doc_frontmatter(last_reviewed="22-10-2026"))
        issues = check_frontmatter(self.root, self.config)
        self.assertEqual(sum(issue.path == "good.md" for issue in issues), 0)
        self.assertTrue(any(issue.path == "bad.md" and "ISO" in issue.message for issue in issues))

    def test_frontmatter_requires_approval_fields(self) -> None:
        self.put("draft.md", doc_frontmatter(status="approved"))
        issues = check_frontmatter(self.root, self.config)
        self.assertTrue(any("approved_by" in issue.message for issue in issues))
        self.assertTrue(any("approved_on" in issue.message for issue in issues))

    def test_frontmatter_requires_sources_for_research(self) -> None:
        source = {"title": "Primary source", "url": "https://example.org/source", "accessed": "2026-10-22"}
        self.put("research.md", doc_frontmatter(type="research", status="reference", sources=[source]))
        self.put("incomplete.md", doc_frontmatter(type="principle", sources=[]))
        issues = check_frontmatter(self.root, self.config)
        self.assertFalse(any(issue.path == "research.md" for issue in issues))
        self.assertTrue(any(issue.path == "incomplete.md" and "sources" in issue.message for issue in issues))

    def test_frontmatter_rejects_unknown_enums_and_template_target(self) -> None:
        self.put("unknown.md", doc_frontmatter(type="unlisted"))
        self.put("template.md", doc_frontmatter(type="template", template_for="unlisted"))
        issues = check_frontmatter(self.root, self.config)
        self.assertTrue(any(issue.path == "unknown.md" and "unknown type" in issue.message for issue in issues))
        self.assertTrue(any(issue.path == "template.md" and "template_for" in issue.message for issue in issues))

    def test_frontmatter_allows_version_and_unknown_extra_keys(self) -> None:
        self.put("versioned.md", doc_frontmatter(version="1.2.3", custom_note="kept"))
        self.assertEqual(check_frontmatter(self.root, self.config), [])

    def test_frontmatter_requires_version_to_be_a_string(self) -> None:
        self.put("bad-version.md", doc_frontmatter(version=3))
        issues = check_frontmatter(self.root, self.config)
        self.assertTrue(any("version" in issue.message and "string" in issue.message for issue in issues))

    def test_inbox_frontmatter_has_relaxed_requirements(self) -> None:
        self.put("inbox/note.md", doc_frontmatter(
            title="Quick note", type="inbox", status="proposed", captured="2026-10-22",
            owner=None, last_reviewed=None,
        ).replace("owner: null\n", "").replace("last_reviewed: null\n", ""))
        self.assertEqual(check_frontmatter(self.root, self.config), [])

    def test_inbox_requires_captured_date_and_proposed_status(self) -> None:
        self.put("inbox/note.md", doc_frontmatter(
            title="Quick note", type="inbox", status="experimental", captured="not-a-date",
        ))
        issues = check_frontmatter(self.root, self.config)
        self.assertTrue(any("captured" in issue.message for issue in issues))
        self.assertTrue(any("status 'proposed'" in issue.message for issue in issues))

    def test_heading_slugging_matches_github_style(self) -> None:
        self.assertEqual(slugify_heading("A **Small** Test: (v2)"), "a-small-test-v2")
        self.assertEqual(slugify_heading("Evidence requirements"), "evidence-requirements")

    def test_decision_index_accepts_linked_contiguous_record(self) -> None:
        decision = self.put("studio/decisions/0001-example.md", decision_doc())
        index = self.put("studio/decisions/README.md", "# Decisions\n\n[Example](0001-example.md) — D-0001 — proposed.\n")
        issues = check_decisions(self.root, self.config)
        self.assertEqual(issues, [])
        self.assertTrue(decision.exists() and index.exists())

    def test_decision_check_catches_index_omission_and_number_gap(self) -> None:
        self.put("studio/decisions/0002-example.md", decision_doc(2))
        self.put("studio/decisions/README.md", "# Decisions\n")
        issues = check_decisions(self.root, self.config)
        self.assertTrue(any("contiguous" in issue.message for issue in issues))
        self.assertTrue(any("listed" in issue.message for issue in issues))

    def test_decision_check_rejects_reference_status_and_missing_section(self) -> None:
        content = decision_doc(status="reference").replace("## Evidence", "## Evidence removed")
        self.put("studio/decisions/0001-example.md", content)
        self.put("studio/decisions/README.md", "# Decisions\n\n[Example](0001-example.md)\n")
        issues = check_decisions(self.root, self.config)
        self.assertTrue(any("status" in issue.message for issue in issues))
        self.assertTrue(any("Evidence" in issue.message for issue in issues))

    def test_decision_superseded_by_must_resolve(self) -> None:
        first = decision_doc(status="superseded", superseded_by="D-0002")
        second = decision_doc(2)
        self.put("studio/decisions/0001-first.md", first)
        self.put("studio/decisions/0002-second.md", second)
        self.put("studio/decisions/README.md", "[First](0001-first.md)\n[Second](0002-second.md)\n")
        self.assertEqual(check_decisions(self.root, self.config), [])
        self.put("studio/decisions/0001-first.md", decision_doc(status="superseded", superseded_by="D-9999"))
        issues = check_decisions(self.root, self.config)
        self.assertTrue(any("superseded_by target" in issue.message for issue in issues))

    def test_skill_check_accepts_sections_and_resolving_symlink(self) -> None:
        skill = self.put("skills/demo-skill/SKILL.md", skill_doc())
        aliases = self.root / ".claude" / "skills"
        aliases.mkdir(parents=True)
        (aliases / "demo-skill").symlink_to("../../skills/demo-skill")
        self.assertTrue(skill.exists())
        self.assertEqual(check_skills(self.root, self.config), [])

    def test_skill_check_catches_missing_section_and_non_symlink_alias(self) -> None:
        self.put("skills/demo-skill/SKILL.md", skill_doc(sections=SECTIONS[:-1]))
        aliases = self.put(".claude/skills/demo-skill", "not a symlink")
        issues = check_skills(self.root, self.config)
        self.assertTrue(any("Example" in issue.message for issue in issues))
        self.assertTrue(any("symlink" in issue.message for issue in issues))
        self.assertTrue(aliases.exists())

    def test_links_accept_existing_file_and_anchor_but_reject_missing_target(self) -> None:
        self.put("target.md", "# A Section\n")
        self.put("source.md", "[valid](target.md#a-section)\n[bad](missing.md)\n")
        issues = check_links(self.root, self.config)
        self.assertTrue(any("missing.md" in issue.message for issue in issues))
        self.assertFalse(any("target.md#a-section" in issue.message for issue in issues))

    def test_links_ignore_fenced_and_inline_code(self) -> None:
        self.put("source.md", "`[inline](absent.md)`\n\n```markdown\n[code](also-absent.md)\n```\n")
        self.assertEqual(check_links(self.root, self.config), [])

    def test_links_reject_missing_heading_anchor(self) -> None:
        self.put("target.md", "# Existing heading\n")
        self.put("source.md", "[bad](target.md#not-here)\n")
        issues = check_links(self.root, self.config)
        self.assertTrue(any("anchor '#not-here'" in issue.message for issue in issues))

    def test_required_files_reports_absent_schema_entries(self) -> None:
        self.config["required_files"] = ["README.md", "studio/README.md"]
        write_metadata(self.root, self.config)
        issues = check_required(self.root, self.config)
        self.assertEqual({issue.path for issue in issues}, {"README.md", "studio/README.md"})

    def test_required_files_accepts_existing_schema_entries(self) -> None:
        self.put("README.md", "# Ready\n")
        self.config["required_files"] = ["README.md"]
        self.assertEqual(check_required(self.root, self.config), [])

    def test_secret_check_flags_synthetic_tokens_and_personal_data(self) -> None:
        gh_token = "gh" + "p_" + "A" * 36
        openai_key = "sk" + "-" + "B" * 24
        aws_key = "AK" + "IA" + "C" * 16
        email = "tester" + "@" + "example" + ".org"
        pan = "ABCDE" + "1234" + "F"
        aadhaar = "123456" + "789012"
        slack_token = "xo" + "xb" + "-" + "D" * 16
        google_key = "AI" + "za" + "E" * 35
        credential = "password" + " = '" + "Q" * 10 + "'"
        private_key = "-----BEGIN " + "PRIVATE KEY-----"
        self.put(
            "sample.txt",
            f"{gh_token}\n{openai_key}\n{aws_key}\n{slack_token}\n{google_key}\n"
            f"{credential}\n{private_key}\n{email}\n{pan}\n{aadhaar}\n",
        )
        issues = check_secrets(self.root, self.config)
        self.assertTrue(any(issue.severity == "error" and "GitHub" in issue.message for issue in issues))
        self.assertTrue(any(issue.severity == "error" and "private data" in issue.message for issue in issues))
        self.assertTrue(any(issue.severity == "warning" and "email" in issue.message for issue in issues))
        self.assertTrue(any("Slack" in issue.message for issue in issues))
        self.assertTrue(any("Google" in issue.message for issue in issues))
        self.assertTrue(any("assignment" in issue.message for issue in issues))
        self.assertTrue(any("private key" in issue.message for issue in issues))

    def test_secret_check_clean_text_has_no_findings(self) -> None:
        self.put("clean.txt", "No credentials or identifying details are included.\n")
        self.assertEqual(check_secrets(self.root, self.config), [])

    def test_secret_check_flags_ai_research_residue(self) -> None:
        residue_host = "images" + "." + "openai" + "." + "com"
        tracking_query = "utm_source" + "=" + "chatgpt" + "." + "com"
        self.put("research.md", f"https://{residue_host}/asset\n?{tracking_query}\n")
        issues = check_secrets(self.root, self.config)
        self.assertTrue(any("AI-research residue" in issue.message for issue in issues))
        self.assertEqual(sum(issue.severity == "error" for issue in issues), 2)

    def test_secret_check_errors_on_rupee_amount_everywhere(self) -> None:
        rupee = chr(0x20B9)
        self.put("docs/pricing.md", f"Example {rupee}12,000\n")
        self.put("studio/pricing.md", doc_frontmatter(status="hypothesis") + f"\nTest {rupee}12,000\n")
        self.put("INDEX.md", f"Indexed price {rupee}12,000\n")
        issues = check_secrets(self.root, self.config)
        self.assertEqual(sum(issue.severity == "error" and "rupee amount" in issue.message for issue in issues), 3)

    def test_secret_check_rejects_forbidden_filenames(self) -> None:
        self.put(".env.example", "configuration template\n")
        issues = check_secrets(self.root, self.config)
        self.assertTrue(any("forbidden secret-bearing filename" in issue.message for issue in issues))

    def test_secret_check_respects_allow_comment_and_config_allowlist(self) -> None:
        allowed_email = "team" + "@" + "3rdwrongs" + ".studio"
        self.config["secret_allowlist"]["emails"] = [allowed_email]
        write_metadata(self.root, self.config)
        pan = "ABCDE" + "1234" + "F"
        self.put("sample.txt", f"{pan} # secret-scan: allow\n{allowed_email}\n")
        self.assertEqual(check_secrets(self.root, self.config), [])

    def test_stale_check_warns_without_error(self) -> None:
        self.put("old.md", doc_frontmatter(last_reviewed="2020-01-01", review_every_days=1))
        issues = check_stale(self.root, self.config, today=date(2026, 10, 22))
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "warning")

    def test_stale_check_accepts_current_review(self) -> None:
        self.put("current.md", doc_frontmatter(last_reviewed="2026-10-22", review_every_days=30))
        self.assertEqual(check_stale(self.root, self.config, today=date(2026, 10, 22)), [])

    def test_stale_check_warns_for_inbox_capture_older_than_thirty_days(self) -> None:
        self.put("inbox/old.md", doc_frontmatter(
            title="Old note", type="inbox", status="proposed", captured="2026-09-20",
            owner=None, last_reviewed=None,
        ).replace("owner: null\n", "").replace("last_reviewed: null\n", ""))
        issues = check_stale(self.root, self.config, today=date(2026, 10, 22))
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "warning")
        self.assertIn("inbox note has been waiting", issues[0].message)

    def test_validator_cli_returns_one_and_summary_for_error(self) -> None:
        self.config["required_files"] = ["missing.md"]
        write_metadata(self.root, self.config)
        stdout = io.StringIO()
        with patch("scripts.validate.ROOT", self.root), redirect_stdout(stdout):
            result = validate_main(["--check", "required"])
        self.assertEqual(result, 1)
        self.assertIn("missing.md:1: [required]", stdout.getvalue())
        self.assertIn("Validation complete: 1 error, 0 warnings.", stdout.getvalue())

    def test_validator_cli_stale_warning_does_not_fail(self) -> None:
        self.put("old.md", doc_frontmatter(last_reviewed="2020-01-01", review_every_days=1))
        write_metadata(self.root, self.config)
        stdout = io.StringIO()
        with patch("scripts.validate.ROOT", self.root), patch("scripts.oscheck.stale.date") as mocked_date:
            mocked_date.today.return_value = date(2026, 10, 22)
            with redirect_stdout(stdout):
                result = validate_main(["--check", "stale"])
        self.assertEqual(result, 0)
        self.assertIn("[stale] warning:", stdout.getvalue())
        self.assertIn("Validation complete: 0 errors, 1 warning.", stdout.getvalue())

    def test_new_doc_copies_template_and_refuses_overwrite(self) -> None:
        self.put("template.md", doc_frontmatter(type="template", template_for="research", status="proposed"))
        old_cwd = Path.cwd()
        stdout = io.StringIO()
        stderr = io.StringIO()
        os.chdir(self.root)
        try:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                result = new_doc_main(["template.md", "new.md", "--title", "New study"])
            self.assertEqual(result, 0)
            parsed = parse_frontmatter((self.root / "new.md").read_text(encoding="utf-8"))
            self.assertEqual(parsed.data["type"], "research")
            self.assertEqual(parsed.data["status"], "reference")
            self.assertNotIn("template_for", parsed.data)
            self.assertEqual(parsed.data["title"], "New study")
            with redirect_stderr(stderr):
                self.assertEqual(new_doc_main(["template.md", "new.md"]), 1)
        finally:
            os.chdir(old_cwd)

    def test_sync_labels_dry_run_prints_gh_commands(self) -> None:
        labels = [{"name": "type: docs", "color": "BFD4F2", "description": "Documentation"}]
        import yaml

        self.put(".github/labels.yml", yaml.safe_dump(labels, sort_keys=False))
        old_cwd = Path.cwd()
        output = io.StringIO()
        os.chdir(self.root)
        try:
            with redirect_stdout(output):
                self.assertEqual(sync_labels_main(["--dry-run"]), 0)
        finally:
            os.chdir(old_cwd)
        self.assertIn("gh label create 'type: docs' --force", output.getvalue())


if __name__ == "__main__":
    unittest.main()
