"""Render every template bundle with its example values and check the output.

The `3w new <bundle>` CLI lives in the Delivery engine; this tiny renderer
mirrors its contract: {{variable}} placeholders, a `{vault}` target prefix.
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.oscheck.common import parse_frontmatter

BUNDLES = ROOT / "templates" / "bundles"
PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}")
TARGET_VAR = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")
MONEY = re.compile(r"[₹$€£¥]\s*\d|\b(?:INR|USD|EUR|GBP|Rs\.?)\s*\d")
OWNED = {"proposal", "sow", "change-order", "invoice", "finance-review", "weekly-review", "rates", "estimate"}


def render(text: str, values: dict[str, str]) -> str:
    return PLACEHOLDER.sub(lambda m: values[m.group(1)], text)


class BundleTests(unittest.TestCase):
    def test_owned_bundles_exist(self) -> None:
        present = {path.parent.name for path in BUNDLES.glob("*/bundle.yaml")}
        self.assertTrue(OWNED <= present, OWNED - present)

    def test_bundles_render_cleanly(self) -> None:
        config = json.loads((ROOT / "schemas" / "metadata.json").read_text(encoding="utf-8"))
        for name in sorted(OWNED):
            with self.subTest(bundle=name):
                folder = BUNDLES / name
                spec = yaml.safe_load((folder / "bundle.yaml").read_text(encoding="utf-8"))
                for key in ("kind", "description", "template", "target", "variables"):
                    self.assertIn(key, spec)
                self.assertEqual(spec["kind"], name)
                self.assertTrue(spec["template"].endswith(".tmpl"))
                template = (folder / spec["template"]).read_text(encoding="utf-8")
                declared = set(spec["variables"])
                used = set(PLACEHOLDER.findall(template))
                self.assertEqual(used, declared, "placeholders and declared variables differ")
                self.assertTrue(set(TARGET_VAR.findall(spec["target"])) - {"vault"} <= declared)
                self.assertIsNone(MONEY.search(template), "templates must not carry money amounts")
                values = {key: str(var["example"]) for key, var in spec["variables"].items()}
                output = render(template, values)
                self.assertNotIn("{{", output)
                target = spec["target"].format(vault="VAULT", **values)
                if target.endswith(".yaml"):
                    self.assertIsInstance(yaml.safe_load(output), dict)
                    self.assertTrue(target.startswith("VAULT/"), "YAML money files belong in the vault")
                    continue
                parsed = parse_frontmatter(output)
                self.assertIsNotNone(parsed.data, parsed.error)
                if target.startswith("VAULT/"):
                    self.assertIn("PRIVATE", output)
                else:
                    self.assertTrue(target.startswith("projects/stillsoil-atelier/"))
                    self.assertIn(parsed.data["type"], config["types"])
                    self.assertEqual(parsed.data["status"], "proposed")
                    self.assertIn("D-0021", output)


if __name__ == "__main__":
    unittest.main()
