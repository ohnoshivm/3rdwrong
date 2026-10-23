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
GROWTH_BUNDLES = {
    "case-study": "repo",
    "content-brief": "repo",
    "discovery-notes": "vault",
    "outreach-sequence": "vault",
    "win-loss": "vault",
}
REQUIRED_KEYS = {"kind", "description", "template", "target", "variables"}
PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}")
TARGET_FIELD = re.compile(r"\{([A-Za-z0-9_]+)\}")


def load_bundle(name: str) -> dict:
    return yaml.safe_load((BUNDLES / name / "bundle.yaml").read_text(encoding="utf-8"))


def template_files(name: str, spec: dict) -> list[Path]:
    path = BUNDLES / name / spec["template"]
    return sorted(path.rglob("*.tmpl")) if path.is_dir() else [path]


def render(name: str, values: dict[str, str]) -> dict[str, str]:
    """Render a bundle the way `3w new` does: {{var}} in files, {var} in the target."""
    spec = load_bundle(name)
    target = TARGET_FIELD.sub(lambda m: "{vault}" if m.group(1) == "vault" else values[m.group(1)], spec["target"])
    out = {}
    for path in template_files(name, spec):
        text = PLACEHOLDER.sub(lambda m: values[m.group(1)], path.read_text(encoding="utf-8"))
        out[target] = text
    return out


class GrowthBundleTests(unittest.TestCase):
    def test_bundle_metadata(self) -> None:
        for name, side in GROWTH_BUNDLES.items():
            with self.subTest(bundle=name):
                spec = load_bundle(name)
                self.assertTrue(REQUIRED_KEYS <= spec.keys(), f"missing keys: {REQUIRED_KEYS - spec.keys()}")
                self.assertEqual(spec["template"].endswith(".tmpl") or (BUNDLES / name / spec["template"]).is_dir(), True)
                for path in template_files(name, spec):
                    self.assertTrue(path.is_file(), f"template missing: {path}")
                self.assertIsInstance(spec["variables"], list)
                for variable in spec["variables"]:
                    self.assertTrue({"name", "example"} <= variable.keys(), variable)
                self.assertEqual(spec["target"].startswith("{vault}/"), side == "vault")

    def test_placeholders_declared(self) -> None:
        for name in GROWTH_BUNDLES:
            with self.subTest(bundle=name):
                spec = load_bundle(name)
                declared = {v["name"] for v in spec["variables"]}
                used = set(TARGET_FIELD.findall(spec["target"])) - {"vault"}
                for path in template_files(name, spec):
                    used |= set(PLACEHOLDER.findall(path.read_text(encoding="utf-8")))
                self.assertFalse(used - declared, f"undeclared: {sorted(used - declared)}")

    def test_render_resolves_everything(self) -> None:
        schema = json.loads((ROOT / "schemas" / "metadata.json").read_text(encoding="utf-8"))
        for name, side in GROWTH_BUNDLES.items():
            with self.subTest(bundle=name):
                values = {v["name"]: str(v["example"]) for v in load_bundle(name)["variables"]}
                for target, text in render(name, values).items():
                    self.assertNotIn("{{", text)
                    self.assertNotIn("}}", text)
                    self.assertNotRegex(target, r"\{(?!vault\})")
                    if side == "repo":
                        parsed = parse_frontmatter(text)
                        self.assertEqual(parsed.error, "")
                        data = parsed.data
                        for key in ("title", "type", "status", "owner", "last_reviewed"):
                            self.assertIn(key, data)
                        self.assertIn(data["type"], schema["types"])
                        self.assertEqual(data["status"], "proposed")


if __name__ == "__main__":
    unittest.main()
