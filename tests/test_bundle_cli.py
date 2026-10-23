"""Exercise shipped bundles through bin/3w, never through a mirror renderer.

A list-only variable loader, ignored --set codename, or missing output file
breaks this contract. All writes and Git operations stay in temporary copies.
"""
from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}")


class ShippedBundleCliTests(unittest.TestCase):
    def test_every_bundle_renders_with_declared_examples(self) -> None:
        with tempfile.TemporaryDirectory(prefix="threew-bundles-") as tmp:
            base = Path(tmp).resolve()
            repo = base / "repo"
            repo.mkdir()
            for directory in ("bin", "scripts", "templates", "schemas"):
                shutil.copytree(ROOT / directory, repo / directory, ignore=shutil.ignore_patterns("__pycache__"))
            for name in ("pyproject.toml", "uv.lock", ".python-version"):
                shutil.copy2(ROOT / name, repo / name)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            specs = sorted((repo / "templates/bundles").glob("*/bundle.yaml"))
            self.assertEqual({p.parent.name for p in specs}, {
                "project-identity", "project-digital", "proposal", "sow", "change-order",
                "invoice", "finance-review", "weekly-review", "rates", "estimate",
                "case-study", "content-brief", "discovery-notes", "outreach-sequence", "win-loss",
            })
            for spec_path in specs:
                spec = yaml.safe_load(spec_path.read_text())
                raw = spec.get("variables", [])
                self.assertIsInstance(raw, list, spec_path)
                variables = {item["name"]: item for item in raw}
                values = {name: str(item["example"]) for name, item in variables.items()}
                modes = ("--cleared", "--private") if spec["kind"] == "project" else (
                    ("--cleared",) if spec["target"].startswith("projects/") else (None,)
                )
                for mode in modes:
                    name = spec_path.parent.name
                    with self.subTest(bundle=name, mode=mode):
                        vault = base / (name + (mode or "-vault"))
                        vault.mkdir()
                        env = {**os.environ, "THREEW_VAULT": str(vault),
                               "UV_PROJECT_ENVIRONMENT": sys.prefix, "UV_NO_SYNC": "1",
                               "PYTHONDONTWRITEBYTECODE": "1"}
                        command = [str(repo / "bin/3w"), "new", name]
                        if mode:
                            command.append(mode)
                        for key, value in values.items():
                            command.extend(("--set", f"{key}={value}"))
                        result = subprocess.run(command, cwd=repo, env=env, text=True, capture_output=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        pattern = spec["target"]
                        if mode == "--private":
                            pattern = "{vault}/" + pattern.removeprefix("projects/")
                        target = Path(pattern.format(vault=vault, **values))
                        if not target.is_absolute():
                            target = repo / target
                        self.assertTrue(target.exists(), f"missing expected output: {target}")
                        outputs = sorted(target.rglob("*")) if target.is_dir() else [target]
                        outputs = [p for p in outputs if p.is_file()]
                        self.assertTrue(outputs)
                        required = set(values) | {"bundle", "title", "clearance"}
                        for path in outputs:
                            unresolved = set(PLACEHOLDER.findall(path.read_text())) & required
                            self.assertFalse(unresolved, f"{path}: {unresolved}")
                        if name in {"project-identity", "project-digital"}:
                            self.assertEqual(len(outputs), 10 if name == "project-digital" else 9)
                            if name == "project-digital":
                                stack = (target / "stack-decision.md").read_text()
                                self.assertIn("## Final decision before production build", stack)
                                self.assertIn(f"codename: {values['codename']}", stack)
                            text = (target / "README.md").read_text()
                            self.assertIn(f"codename: {values['codename']}", text)
                            self.assertIn("private: vault only" if mode == "--private" else "cleared:", text)
                        if target.is_dir():
                            shutil.rmtree(target)
                        else:
                            target.unlink()
                        location = mode or ("vault" if spec["target"].startswith("{vault}/") else "repo")
                        print(f"BUNDLE OK {name} {location}: {len(outputs)} files", flush=True)
