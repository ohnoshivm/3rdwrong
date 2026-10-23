from __future__ import annotations

import json
import math
import subprocess
import sys
import tempfile
import unittest

import yaml
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import web_qa


class BudgetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def budget(self, text):
        path = self.root / "budget.yaml"
        path.write_text(text)
        return path

    def test_default_and_stricter_partial_override(self):
        default = web_qa.load_budget()
        self.assertEqual(default["limits"]["lcp_ms"], 2000)
        self.assertEqual(default["limits"]["transfer_before_input_bytes"], 2_000_000)
        strict = web_qa.load_budget(self.budget("limits:\n  lcp_ms: 1800\n  fps: 65\n"))
        self.assertEqual(strict["limits"]["lcp_ms"], 1800)
        self.assertEqual(strict["limits"]["inp_ms"], 200)

    def test_looser_requires_actual_founder_record(self):
        path = self.budget("limits:\n  lcp_ms: 2500\nexception:\n  record: approval.md\n  metrics: [lcp_ms]\n")
        with self.assertRaises(ValueError):
            web_qa.load_budget(path)
        record = self.root / "approval.md"
        record.write_text("---\nstatus: proposed\napproved_by: founder\napproved_on: 2026-10-23\n---\n")
        with self.assertRaises(ValueError):
            web_qa.load_budget(path)
        record.write_text("---\nstatus: approved\napproved_by: founder\napproved_on: 2026-10-23\n---\nFounder exception for lcp_ms.\n")
        with self.assertRaises(ValueError):
            web_qa.load_budget(path)

    def test_canonical_exception_requires_committed_exact_project_scope(self):
        decisions = self.root / "studio/decisions"
        decisions.mkdir(parents=True)
        record = decisions / "exception.md"
        metadata = {"status": "approved", "approved_by": "founder", "approved_on": "2026-10-23",
                    "qa_exception": {"project": "fictional-test", "limits": {"lcp_ms": 2500}}}
        content = "---\n" + yaml.safe_dump(metadata) + "---\nFictional test approval.\n"
        record.write_text(content)
        path = self.budget("limits:\n  lcp_ms: 2500\nexception:\n"
                           "  record: studio/decisions/exception.md\n  project: fictional-test\n  metrics: [lcp_ms]\n")
        trusted = subprocess.CompletedProcess([], 0, content.encode(), b"")
        with patch.object(web_qa, "ROOT", self.root), patch.object(web_qa.subprocess, "run", return_value=trusted):
            self.assertEqual(web_qa.load_budget(path)["limits"]["lcp_ms"], 2500)
            for mutation in ("project", "limit", "future", "uncommitted", "traversal", "symlink"):
                record.write_text(content)
                budget = yaml.safe_load(path.read_text())
                budget["exception"]["project"] = "fictional-test"
                budget["exception"]["record"] = "studio/decisions/exception.md"
                changed = yaml.safe_load(yaml.safe_dump(metadata))
                if mutation == "project":
                    budget["exception"]["project"] = "other-project"
                elif mutation == "limit":
                    changed["qa_exception"]["limits"]["lcp_ms"] = 2400
                elif mutation == "future":
                    changed["approved_on"] = "2999-01-01"
                elif mutation == "traversal":
                    budget["exception"]["record"] = "studio/decisions/../decisions/exception.md"
                elif mutation == "symlink":
                    (decisions / "alias.md").symlink_to(path)
                    budget["exception"]["record"] = "studio/decisions/alias.md"
                changed_content = "---\n" + yaml.safe_dump(changed) + "---\nFictional test approval.\n"
                record.write_text(changed_content)
                path.write_text(yaml.safe_dump(budget))
                committed = content if mutation == "uncommitted" else changed_content
                if mutation == "uncommitted":
                    record.write_text(content + "unreviewed change")
                with patch.object(web_qa.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, committed.encode(), b"")):
                    with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                        web_qa.load_budget(path)

    def test_invalid_budgets_are_rejected(self):
        for text in ("[]", "limits: []", "limits:\n  typo: 1", "limits:\n  fps: 0",
                     "limits:\n  lcp_ms: true", "limits:\n  lcp_ms: .nan",
                     "limits:\n  cls: -1", "limits:\n  lcp_ms: '2000'", "limits:\n  inp_ms: 201"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                web_qa.load_budget(self.budget(text))

    def test_boundaries_missing_nonfinite_and_minimum(self):
        self.assertEqual(web_qa.compare(2000, 2000), "PASS")
        self.assertEqual(web_qa.compare(2001, 2000), "FAIL")
        self.assertEqual(web_qa.compare(59, 60, minimum=True), "FAIL")
        self.assertEqual(web_qa.compare(60, 60, minimum=True), "PASS")
        for missing in (None, math.nan, math.inf, True, "0"):
            self.assertEqual(web_qa.compare(missing, 2000), "NOT_MEASURED")


def lhr(lcp=1900, cls=0, tbt=0, size=1500):
    return {"lighthouseVersion": "13.5.0", "audits": {
        "largest-contentful-paint": {"numericValue": lcp},
        "cumulative-layout-shift": {"numericValue": cls},
        "total-blocking-time": {"numericValue": tbt},
        "total-byte-weight": {"numericValue": size},
        "network-requests": {"details": {"items": [
            {"rendererStartTime": 0, "transferSize": 1000, "finished": True},
            {"rendererStartTime": 1200, "transferSize": 500, "finished": True}]}},
        "metrics": {"details": {"items": [{"observedLoad": 1000}]}},
        "image-alt": {"score": 0, "scoreDisplayMode": "binary", "title": "Image alt"},
    }, "categories": {"accessibility": {"auditRefs": [{"id": "image-alt"}]}}}


class ReportTests(unittest.TestCase):
    def test_missing_tools_write_incomplete_report_and_cli_exit(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(web_qa.shutil, "which", return_value=None):
            out = Path(tmp) / "out"
            code = web_qa.main(["run", "http://localhost/", "--out", str(out)])
            self.assertEqual(code, 2)
            report = json.loads((out / "report.json").read_text())
            self.assertEqual(report["status"], "INCOMPLETE")
            self.assertEqual(report["lab_status"], "INCOMPLETE")
            self.assertTrue(all(row["status"] == "NOT_MEASURED" for row in report["checks"]))
            self.assertEqual(len(report["errors"]), 2)
            self.assertEqual(web_qa.main(["run", "http://localhost/", "--out", str(out)]), 2)

    def test_repository_output_and_symlink_are_refused_before_collection(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            alias = Path(tmp) / "alias"
            alias.symlink_to(repo, target_is_directory=True)
            with patch.object(web_qa, "ROOT", repo), patch.object(web_qa.shutil, "which", return_value=None):
                for target in (repo / "projects/client/qa", alias / "qa"):
                    with self.subTest(target=target), self.assertRaises(ValueError):
                        web_qa.run_harness("http://localhost/", target, web_qa.load_budget())
                self.assertEqual(list(repo.iterdir()), [])

    def test_malformed_lighthouse_shapes_keep_structured_incomplete_report(self):
        shapes = [[], {"audits": []}, {"audits": {"largest-contentful-paint": []}},
                  {"audits": {}, "categories": []}]
        for ref in ({}, None, {"id": []}, "bad"):
            run = lhr()
            run["categories"]["accessibility"]["auditRefs"] = [ref]
            shapes.append(run)
        malformed_mode = lhr()
        malformed_mode['audits']['image-alt']['scoreDisplayMode'] = []
        shapes.append(malformed_mode)
        malformed_runtime = {"runtimeError": "crash", "categories": []}
        shapes.append(malformed_runtime)
        for run in shapes:
            with self.subTest(run=run), tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "out"
                def lighthouse(argv, **kwargs):
                    dest = next(arg.split("=", 1)[1] for arg in argv if arg.startswith("--output-path="))
                    Path(dest).write_text(json.dumps(run))
                with patch.object(web_qa.shutil, "which", return_value="lighthouse"), \
                     patch.object(web_qa, "command", side_effect=lighthouse), \
                     patch.object(web_qa, "collect_browser", side_effect=RuntimeError("not collected")):
                    self.assertEqual(web_qa.main(["run", "http://localhost/", "--out", str(out)]), 2)
                report = json.loads((out / "report.json").read_text())
                self.assertEqual(report["status"], "INCOMPLETE")
                self.assertTrue(any("Lighthouse run" in err for err in report["errors"]))
                self.assertIsNone(report["measurements"]["accessibility_failures"])

    def test_rejects_non_http_and_embedded_credentials(self):
        with tempfile.TemporaryDirectory() as tmp:
            for url in ("file:///etc/passwd", "http://user:secret@localhost/", "--help", "https://"):
                with self.subTest(url=url), self.assertRaises(ValueError):
                    web_qa.run_harness(url, Path(tmp) / "out", web_qa.load_budget())

    def test_threew_qa_routes_to_harness(self):
        from scripts import threew
        with patch.object(web_qa, "run_args", return_value=2) as run:
            self.assertEqual(threew.main(["qa", "run", "http://localhost/", "--out", "/tmp/qa-test"]), 2)
            self.assertEqual(run.call_args.args[0].url, "http://localhost/")

    def test_threew_script_from_another_working_directory(self):
        result = subprocess.run([sys.executable, str(web_qa.ROOT / "scripts/threew.py"),
                                 "qa", "run", "--help"], cwd=tempfile.gettempdir(),
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--budget", result.stdout)

    def test_three_run_median_and_worst_accessibility_count(self):
        data = web_qa.summarise_lighthouse([lhr(3000), lhr(1800), lhr(1900)])
        self.assertEqual(data["lcp_ms"], 1900)
        self.assertEqual(data["cls"], 0)
        self.assertEqual(data["transfer_before_input_bytes"], 1000)
        self.assertEqual(data["accessibility_failures"], 1)

    def test_missing_run_or_audit_cannot_pass(self):
        data = web_qa.summarise_lighthouse([lhr(), lhr()])
        self.assertIsNone(data["lcp_ms"])
        broken = lhr()
        del broken["audits"]["largest-contentful-paint"]
        self.assertIsNone(web_qa.summarise_lighthouse([lhr(), broken, lhr()])["lcp_ms"])
        broken = lhr()
        broken["audits"]["image-alt"]["scoreDisplayMode"] = "error"
        broken["audits"]["image-alt"]["score"] = None
        self.assertIsNone(web_qa.summarise_lighthouse([lhr(), broken, lhr()])["accessibility_failures"])

    def test_unfinished_initial_request_is_not_a_zero_byte_pass(self):
        broken = lhr()
        broken["audits"]["network-requests"]["details"]["items"][0]["finished"] = False
        data = web_qa.summarise_lighthouse([lhr(), broken, lhr()])
        self.assertIsNone(data["transfer_before_input_bytes"])

    def test_each_measured_line_cites_relevant_evidence(self):
        report = web_qa.make_report("http://localhost/", web_qa.load_budget(),
            {"lcp_ms": 1900, "fps": 60}, ["lighthouse-1.json", "browser.json"], [])
        rows = {row["id"]: row for row in report["checks"]}
        self.assertEqual(rows["lcp_ms"]["evidence"], ["lighthouse-1.json"])
        self.assertEqual(rows["fps"]["evidence"], ["browser.json"])
        self.assertEqual(rows["inp_ms"]["evidence"], [])

    def test_reports_distinguish_lab_pass_from_launch_and_link_evidence(self):
        report = web_qa.make_report("http://localhost/", web_qa.load_budget(),
            {"lcp_ms": 1900, "cls": 0, "tbt_ms": 0, "fps": 60,
             "transfer_before_input_bytes": 1000, "accessibility_failures": 0,
             "console_errors": 0, "active_reduced_animations": 0},
            ["browser.json", "screenshots/375.png"], [])
        self.assertEqual(report["status"], "INCOMPLETE")
        self.assertEqual(report["lab_status"], "PASS")
        rows = {row["id"]: row for row in report["checks"]}
        self.assertEqual(rows["inp_ms"]["status"], "NOT_MEASURED")
        self.assertEqual(rows["reduced_motion_complete"]["status"], "NOT_MEASURED")
        with tempfile.TemporaryDirectory() as tmp:
            web_qa.write_report(Path(tmp), report)
            saved = json.loads((Path(tmp) / "report.json").read_text())
            self.assertEqual(saved["status"], "INCOMPLETE")
            markdown = (Path(tmp) / "report.md").read_text()
            self.assertIn("[screenshots/375.png](screenshots/375.png)", markdown)
            self.assertIn("NOT_MEASURED", markdown)
            self.assertIn("lab estimate", markdown)

    def test_failures_and_collection_errors_block(self):
        report = web_qa.make_report("http://localhost/", web_qa.load_budget(),
            {"lcp_ms": 3000}, [], ["Playwright unavailable"])
        self.assertEqual(report["status"], "FAIL")
        report = web_qa.make_report("http://localhost/", web_qa.load_budget(), {}, [], ["missing"])
        self.assertEqual(report["lab_status"], "INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
