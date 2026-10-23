from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import threew
from scripts.oscheck.anonymity import check_anonymity
from scripts.oscheck.common import parse_frontmatter
from scripts.oscheck.frontmatter import check_frontmatter

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "schemas" / "metadata.json").read_text(encoding="utf-8"))
TODAY = date(2026, 10, 23)


def git_init(path: Path) -> None:
    subprocess.run(["git", "init", "-q", str(path)], check=True)


class ThreewTestCase(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.base = Path(temp.name).resolve()
        self.root = self.base / "repo"
        (self.root / "projects").mkdir(parents=True)
        self.vault = self.base / "vault"

    def create(self, bundle: str = "project-digital", **kwargs) -> Path:
        kwargs.setdefault("root", self.root)
        kwargs.setdefault("vault", self.vault)
        kwargs.setdefault("today", TODAY)
        return threew.render_bundle(bundle, **kwargs)


class BundleTests(ThreewTestCase):
    def test_public_render_substitutes_variables_and_strips_tmpl(self) -> None:
        target = self.create(codename="quiet-harbour", cleared=True)
        self.assertEqual(target, self.root / "projects" / "quiet-harbour")
        files = sorted(p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file())
        self.assertEqual(files, [
            "README.md", "brief.md", "decisions.md", "feedback.md", "handover.md",
            "qa/README.md", "retro.md", "risks.md", "status/README.md",
        ])
        readme = (target / "README.md").read_text(encoding="utf-8")
        data = parse_frontmatter(readme).data
        self.assertEqual(data["codename"], "quiet-harbour")
        self.assertEqual(data["offer"], "Digital Experience")
        self.assertIn("cleared", data["clearance"])
        self.assertIn("# Quiet Harbour", readme)
        self.assertIn("../../methods/digital-experience/README.md", readme)
        for path in target.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for auto in ("{{codename}}", "{{title}}", "{{date}}", "{{offer}}", "{{method_path}}", "{{clearance}}"):
                self.assertNotIn(auto, text, path)

    def test_rendered_files_pass_frontmatter_and_anonymity_checks(self) -> None:
        for bundle, codename in (("project-identity", "amber-heron"), ("project-digital", "still-meadow")):
            self.create(bundle, codename=codename, cleared=True)
        self.assertEqual(check_frontmatter(self.root, CONFIG), [])
        self.assertEqual(check_anonymity(self.root, CONFIG), [])

    def test_digital_bundle_inherits_base_and_overrides_qa(self) -> None:
        identity = self.create("project-identity", codename="amber-heron", cleared=True)
        digital = self.create("project-digital", codename="still-meadow", cleared=True)
        self.assertIn("identity-system-testing.md", (identity / "qa/README.md").read_text(encoding="utf-8"))
        digital_qa = (digital / "qa/README.md").read_text(encoding="utf-8")
        self.assertIn("LCP p75", digital_qa)
        self.assertEqual(
            (identity / "feedback.md").read_text(encoding="utf-8").replace("Amber Heron", "X").replace("amber-heron", "x"),
            (digital / "feedback.md").read_text(encoding="utf-8").replace("Still Meadow", "X").replace("still-meadow", "x"),
        )

    def test_unknown_bundle_lists_available(self) -> None:
        with self.assertRaisesRegex(threew.CliError, "project-digital"):
            self.create("nope", cleared=True)

    def test_bundle_metadata_is_validated(self) -> None:
        bundles = self.base / "bundles"
        (bundles / "broken").mkdir(parents=True)
        (bundles / "broken" / "bundle.yaml").write_text("kind: note\ndescription: x\ntarget: notes/x.md\n", encoding="utf-8")
        with self.assertRaisesRegex(threew.CliError, "template"):
            self.create("broken", bundles=bundles)
        (bundles / "broken" / "bundle.yaml").write_text(
            "kind: note\ndescription: x\ntemplate: missing.md.tmpl\ntarget: notes/x.md\n", encoding="utf-8")
        with self.assertRaisesRegex(threew.CliError, "not found"):
            self.create("broken", bundles=bundles)


class SharedFormatTests(ThreewTestCase):
    """Bundles in the Business engine's format: single-file and folder templates, repo and vault targets."""

    def setUp(self) -> None:
        super().setUp()
        self.bundles = self.base / "bundles"

    def bundle(self, name: str, target: str, variables: list[dict], files: dict[str, str], template: str) -> None:
        directory = self.bundles / name
        for rel, text in files.items():
            (directory / rel).parent.mkdir(parents=True, exist_ok=True)
            (directory / rel).write_text(text, encoding="utf-8")
        meta = {"kind": name, "description": f"{name} fixture", "template": template, "target": target, "variables": variables}
        (directory / "bundle.yaml").write_text(yaml.safe_dump(meta), encoding="utf-8")

    def run_cli(self, *argv: str) -> tuple[int, str]:
        err = io.StringIO()
        with patch.object(threew, "BUNDLES", self.bundles), patch.object(threew, "ROOT", self.root), \
                patch.dict(os.environ, {"THREEW_VAULT": str(self.vault)}), redirect_stdout(io.StringIO()), redirect_stderr(err):
            code = threew.main(list(argv))
        return code, err.getvalue()

    def test_vault_target_single_file_via_cli(self) -> None:
        self.bundle(
            "invoice", "{vault}/{codename}/finance/invoice-{number}.md",
            [{"name": "number", "description": "Invoice number", "example": "001"}, {"name": "amount", "example": "see rates"}],
            {"invoice.md.tmpl": "# Invoice {{number}} for {{codename}}\n\nAmount: {{amount}}\nDue: {{due}}\n"},
            "invoice.md.tmpl",
        )
        code, err = self.run_cli("new", "invoice", "--codename", "quiet-harbour", "--set", "number=007")
        self.assertEqual(code, 2)
        self.assertIn("vault init", err)
        threew.init_vault(self.vault)
        code, err = self.run_cli("new", "invoice", "--codename", "quiet-harbour")
        self.assertEqual(code, 2)
        self.assertIn("--set number=001", err)
        code, err = self.run_cli("new", "invoice", "--codename", "quiet-harbour", "--set", "number=007", "--set", "amount=X")
        self.assertEqual((code, err), (0, ""))
        created = self.vault / "quiet-harbour" / "finance" / "invoice-007.md"
        self.assertEqual(created.read_text(encoding="utf-8"), "# Invoice 007 for quiet-harbour\n\nAmount: X\nDue: {{due}}\n")
        self.assertEqual(list((self.root / "projects").iterdir()), [])
        code, err = self.run_cli("new", "invoice", "--codename", "quiet-harbour", "--set", "number=007")
        self.assertEqual(code, 2)
        self.assertIn("refusing to overwrite", err)
        for argv, message in (
            (("new", "invoice", "--set", "number=008"), "--codename"),
            (("new", "invoice", "--codename", "quiet-harbour", "--set", "nope=1"), "unknown variable"),
            (("new", "invoice", "--codename", "quiet-harbour", "--cleared", "--set", "number=009"), "--cleared does not apply"),
            (("new", "invoice", "--codename", "quiet-harbour", "--set", "number=../../x"), "path separators"),
        ):
            with self.subTest(argv=argv):
                code, err = self.run_cli(*argv)
                self.assertEqual(code, 2)
                self.assertIn(message, err)

    def test_vault_target_without_codename(self) -> None:
        self.bundle("rates", "{vault}/rates.yaml", [], {"rates.yaml.tmpl": "updated: {{date}}\n"}, "rates.yaml.tmpl")
        threew.init_vault(self.vault)
        target = self.create("rates", bundles=self.bundles)
        self.assertEqual(target, (self.vault / "rates.yaml").resolve())
        self.assertEqual(target.read_text(encoding="utf-8"), f"updated: {TODAY.isoformat()}\n")

    def test_repo_target_single_file_and_folder(self) -> None:
        self.bundle(
            "change-order", "projects/{codename}/change-order-{ref}.md", [{"name": "ref", "example": "CO-01"}],
            {"change-order.md.tmpl": "# {{ref}}\n"}, "change-order.md.tmpl",
        )
        with self.assertRaisesRegex(threew.CliError, "--cleared"):
            self.create("change-order", codename="quiet-harbour", values={"ref": "co-01"}, bundles=self.bundles)
        target = self.create("change-order", codename="quiet-harbour", cleared=True, values={"ref": "co-01"}, bundles=self.bundles)
        self.assertEqual(target, (self.root / "projects/quiet-harbour/change-order-co-01.md").resolve())
        self.bundle("guide", "notes/{slug}/", [{"name": "slug", "example": "x"}],
                    {"files/a.md.tmpl": "{{slug}}\n", "files/sub/b.md.tmpl": "b\n"}, "files/")
        folder = self.create("guide", values={"slug": "demo"}, bundles=self.bundles)
        self.assertEqual(sorted(p.relative_to(folder).as_posix() for p in folder.rglob("*.md")), ["a.md", "sub/b.md"])
        with self.assertRaisesRegex(threew.CliError, "do not apply"):
            self.create("guide", cleared=True, values={"slug": "other"}, bundles=self.bundles)


class CodenameAndRoutingTests(ThreewTestCase):
    def test_codename_rules(self) -> None:
        for bad in ("Quiet-Harbour", "quiet", "quiet-harbour-bay", "quiet_harbour", "quiet-2", "../escape"):
            with self.subTest(bad=bad), self.assertRaises(threew.CliError):
                self.create(codename=bad, cleared=True)

    def test_generated_codename_is_two_words_from_word_lists(self) -> None:
        target = self.create(cleared=True)
        first, second = target.name.split("-")
        self.assertIn(first, threew.ADJECTIVES)
        self.assertIn(second, threew.NOUNS)

    def test_requires_cleared_or_private(self) -> None:
        with self.assertRaisesRegex(threew.CliError, "--cleared"):
            self.create(codename="quiet-harbour")
        with self.assertRaises(threew.CliError):
            self.create(codename="quiet-harbour", cleared=True, private=True)
        self.assertEqual(list((self.root / "projects").iterdir()), [])

    def test_refuses_to_overwrite(self) -> None:
        target = self.create(codename="quiet-harbour", cleared=True)
        (target / "brief.md").write_text("edited", encoding="utf-8")
        with self.assertRaisesRegex(threew.CliError, "refusing to overwrite"):
            self.create(codename="quiet-harbour", cleared=True)
        self.assertEqual((target / "brief.md").read_text(encoding="utf-8"), "edited")
        threew.init_vault(self.vault)
        with self.assertRaisesRegex(threew.CliError, "refusing to overwrite"):
            self.create(codename="quiet-harbour", private=True)

    def test_private_renders_into_vault_only(self) -> None:
        threew.init_vault(self.vault)
        target = self.create(codename="pale-river", private=True)
        self.assertEqual(target, self.vault / "pale-river")
        self.assertTrue((target / "README.md").is_file())
        for name in threew.PRIVATE_DIRS:
            self.assertTrue((target / name).is_dir(), name)
        self.assertIn("private", (target / "README.md").read_text(encoding="utf-8"))
        self.assertEqual(list((self.root / "projects").iterdir()), [])
        with self.assertRaisesRegex(threew.CliError, "refusing to overwrite"):
            self.create(codename="pale-river", cleared=True)

    def test_private_requires_initialised_vault(self) -> None:
        with self.assertRaisesRegex(threew.CliError, "vault init"):
            self.create(codename="pale-river", private=True)

    def test_cleared_creates_private_folders_when_vault_exists(self) -> None:
        threew.init_vault(self.vault)
        (self.vault / "quiet-harbour" / "contracts").mkdir(parents=True)
        self.create(codename="quiet-harbour", cleared=True)
        self.assertTrue((self.vault / "quiet-harbour" / "finance").is_dir())
        self.assertFalse((self.vault / "quiet-harbour" / "README.md").exists())


class VaultTests(ThreewTestCase):
    def test_vault_init_skeleton_and_no_overwrite(self) -> None:
        vault = threew.init_vault(self.vault)
        self.assertEqual(oct(vault.stat().st_mode & 0o777), "0o700")
        clients = yaml.safe_load((vault / "clients.yaml").read_text(encoding="utf-8"))
        self.assertEqual(clients, {"clients": {}})
        (vault / "clients.yaml").write_text("clients: {kept: {}}\n", encoding="utf-8")
        threew.init_vault(self.vault)
        self.assertIn("kept", (vault / "clients.yaml").read_text(encoding="utf-8"))

    def test_vault_inside_git_work_tree_is_refused(self) -> None:
        git_init(self.base / "somerepo")
        inside = self.base / "somerepo" / "nested" / "vault"
        self.assertTrue(threew.inside_git_worktree(inside))
        self.assertFalse(threew.inside_git_worktree(self.vault))
        with self.assertRaisesRegex(threew.CliError, "git work tree"):
            threew.init_vault(inside)
        with self.assertRaisesRegex(threew.CliError, "git work tree"):
            self.create(codename="pale-river", private=True, vault=inside)

    def test_env_var_sets_vault(self) -> None:
        previous = os.environ.get("THREEW_VAULT")
        os.environ["THREEW_VAULT"] = str(self.vault)
        try:
            self.assertEqual(threew.vault_dir(), self.vault)
        finally:
            if previous is None:
                os.environ.pop("THREEW_VAULT")
            else:
                os.environ["THREEW_VAULT"] = previous


class HookTests(ThreewTestCase):
    def test_hook_install_into_temp_repo(self) -> None:
        repo = self.base / "hookrepo"
        git_init(repo)
        hook = threew.install_hook(repo)
        self.assertEqual(hook, (repo / ".git" / "hooks" / "pre-commit").resolve())
        self.assertTrue(os.access(hook, os.X_OK))
        text = hook.read_text(encoding="utf-8")
        self.assertIn(threew.HOOK_MARKER, text)
        self.assertIn("bin/3w\" check --staged", text)
        threew.install_hook(repo)  # idempotent for its own hook

    def test_hook_install_refuses_foreign_hook_and_non_repo(self) -> None:
        repo = self.base / "hookrepo"
        git_init(repo)
        foreign = repo / ".git" / "hooks" / "pre-commit"
        foreign.write_text("#!/bin/sh\necho mine\n", encoding="utf-8")
        with self.assertRaisesRegex(threew.CliError, "already exists"):
            threew.install_hook(repo)
        self.assertIn("echo mine", foreign.read_text(encoding="utf-8"))
        with self.assertRaisesRegex(threew.CliError, "not a git work tree"):
            threew.install_hook(self.base)

    def test_hook_blocks_staged_leak_end_to_end(self) -> None:
        repo = self.base / "hookrepo"
        git_init(repo)
        (repo / "bin").mkdir()
        wrapper = repo / "bin" / "3w"
        wrapper.write_text(f"#!/bin/sh\nexec {sys.executable} -m scripts.oscheck.anonymity --root \"$(git rev-parse --show-toplevel)\" --vault /nonexistent --staged\n", encoding="utf-8")
        wrapper.chmod(0o755)
        threew.install_hook(repo)
        (repo / "projects" / "quiet-harbour").mkdir(parents=True)
        (repo / "projects" / "quiet-harbour" / "brief.md").write_text("Contact: owner@realclient.in\n", encoding="utf-8")  # secret-scan: allow
        env = {**os.environ, "PYTHONPATH": str(ROOT), "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",  # secret-scan: allow
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com"}  # secret-scan: allow
        subprocess.run(["git", "-C", str(repo), "add", "-A"], check=True)
        result = subprocess.run(["git", "-C", str(repo), "commit", "-qm", "leak"], capture_output=True, text=True, env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("email address", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
