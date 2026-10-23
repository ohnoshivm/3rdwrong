"""Real local browser integration; skip only absent tool/browser prerequisites."""
from __future__ import annotations

import functools
import http.server
import json
import os
import shutil
import sys
import tempfile
import threading
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import web_qa

FIXTURE = Path(__file__).parent / "fixtures/web-qa"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@unittest.skipUnless(shutil.which("lighthouse") and shutil.which("playwright-cli"),
                     "requires lighthouse, playwright-cli and Chrome")
class WebQaIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix="3w-qa-integration-")
        cls.addClassCleanup(cls.temp.cleanup)
        # Let the OS select a free loopback port; no external network required.
        cls.server = http.server.ThreadingHTTPServer(
            ("127.0.0.1", 0), functools.partial(QuietHandler, directory=str(FIXTURE)))
        cls.addClassCleanup(cls.server.server_close)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.addClassCleanup(cls.server.shutdown)
        cls.url = f"http://127.0.0.1:{cls.server.server_port}/"
        cls.out = Path(os.environ.get("WEB_QA_INTEGRATION_OUT", str(Path(cls.temp.name) / "report")))
        cls.report = web_qa.run_harness(cls.url, cls.out, web_qa.load_budget())
        missing_browser = ("Executable doesn't exist", "not installed", "Browser was not found")
        if any(any(marker in error for marker in missing_browser) for error in cls.report["errors"]):
            raise unittest.SkipTest("Chrome/browser prerequisite missing; see harness collection errors")

    def test_full_local_run_has_real_evidence_and_no_false_field_pass(self):
        self.assertEqual(self.report["errors"], [])
        self.assertIn(self.report["status"], {"FAIL", "INCOMPLETE"})  # Host fps can fail the strict target.
        self.assertEqual(self.report["measurements"]["console_errors"], 0)
        self.assertEqual(self.report["measurements"]["active_reduced_animations"], 0)
        self.assertEqual(self.report["measurements"]["accessibility_failures"], 0)
        self.assertGreater(self.report["measurements"]["total_transfer_bytes"], 0)
        self.assertGreater(self.report["measurements"]["transfer_before_input_bytes"], 0)
        self.assertGreater(self.report["measurements"]["fps"], 0)
        for index in range(1, 4):
            self.assertEqual(json.loads((self.out / f"lighthouse-{index}.json").read_text())["configSettings"]["formFactor"], "mobile")
        for reduced in ("", "-reduced"):
            for width in (375, 768, 1440):
                path = self.out / f"screenshots-{width}{reduced}.png"
                data = path.read_bytes()
                self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
                self.assertEqual(int.from_bytes(data[16:20], "big"), width)
        self.assertIn("inp_ms", self.report["not_measured"])
        self.assertIn("reduced_motion_complete", self.report["not_measured"])

    def test_reduced_motion_detects_animation_triggered_only_deep_in_page(self):
        out = Path(self.temp.name) / "deep"
        out.mkdir()
        data = web_qa.collect_browser(self.url + "?deep=1", out)
        self.assertEqual(data["errors"], [])
        self.assertGreater(data["measurements"]["active_reduced_animations"], 0)
        for view in data["views"]:
            if view["reduced"]:
                self.assertTrue(any(s["scrollY"] > 800 for s in view["motion"]["samples"]))

    def test_browser_detects_motion_and_console_regressions(self):
        out = Path(self.temp.name) / "broken"
        out.mkdir()
        data = web_qa.collect_browser(self.url + "?broken=1", out)
        self.assertEqual(data["errors"], [])
        self.assertGreater(data["measurements"]["console_errors"], 0)
        self.assertTrue(any(row["type"] == "pageerror" for row in data["console"]))
        self.assertGreater(data["measurements"]["active_reduced_animations"], 0)


if __name__ == "__main__":
    unittest.main()
