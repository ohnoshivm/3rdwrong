#!/usr/bin/env python3
"""3w: 3RDWRONG project workspace CLI (standard library plus PyYAML).

Implements D-0021: cleared projects render into the public repository under a
codename; private projects render into the vault outside any git work tree.
Bundle format: templates/bundles/README.md.
"""
from __future__ import annotations

import argparse
import os
import re
import secrets
import stat
import subprocess
import sys
from datetime import date
from pathlib import Path
from string import Formatter

import yaml

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "templates" / "bundles"
CODENAME = re.compile(r"^[a-z]+-[a-z]+$")
PLACEHOLDER = re.compile(r"\{\{\s*([A-Za-z][A-Za-z0-9_]*)\s*\}\}")
BUNDLE_KEYS = ("kind", "description", "template", "target")
PRIVATE_DIRS = ("contracts", "finance", "files", "private-notes")
HOOK_MARKER = "# 3w-anonymity-guard"
# Neutral words with no client, place or product associations.
ADJECTIVES = (
    "amber", "brisk", "calm", "deep", "early", "faint", "gentle", "hollow", "idle", "keen", "late", "lucid",
    "mellow", "north", "olive", "pale", "quiet", "rapid", "slow", "still", "tidal", "upper", "vivid", "wild",
)
NOUNS = (
    "anchor", "beacon", "cedar", "delta", "ember", "fern", "harbour", "heron", "island", "juniper", "kestrel", "lantern",
    "meadow", "orchard", "pebble", "quarry", "river", "sparrow", "thistle", "tundra", "valley", "willow", "yarrow", "zephyr",
)
CLIENTS_YAML = """\
# 3RDWRONG vault: codename -> confidential client identity (D-0021).
# Never commit, paste or quote this file in the public repository.
# `bin/3w check` and the pre-commit hook block every value below in repo files.
#
# Structure (one entry per client codename, kebab-case two words):
#
# clients:
#   quiet-harbour:
#     name: Registered legal or trading name
#     aliases: [Short name, Former name, Product brand]
#     people:
#       - name: Full name
#         role: Decision-maker
#         email: person@client-domain
#         phone: "+91 ..."
#     emails: [shared inboxes]
#     domains: [client-domain, staging-domain]
#     phones: [switchboard numbers]
clients: {}
"""
VAULT_README = """\
# 3RDWRONG vault

Private store for confidential client material under D-0021. Never place this
folder inside a git work tree or a synced public location.

- clients.yaml: codename -> real names, aliases, people, emails, domains, phones.
- <codename>/contracts, finance, files, private-notes: per-project confidential material.
- <codename>/ also holds the whole workspace when a project is not cleared.

Back up with Time Machine plus an encrypted off-site copy; test a restore.
See docs/public-private-boundary.md in the repository.
"""
HOOK = f"""#!/bin/sh
{HOOK_MARKER}: installed by `bin/3w hooks install`; local only, never committed.
root="$(git rev-parse --show-toplevel)" || exit 1
if [ ! -x "$root/bin/3w" ]; then
  echo "3w anonymity guard: bin/3w not found in this checkout; guard skipped." >&2
  exit 0
fi
exec "$root/bin/3w" check --staged
"""


class CliError(Exception):
    pass


def vault_dir() -> Path:
    return Path(os.environ.get("THREEW_VAULT", "~/3rdwrong-vault")).expanduser()


def inside_git_worktree(path: Path) -> bool:
    probe = path.expanduser().resolve()
    while not probe.exists():
        probe = probe.parent
    try:
        result = subprocess.run(
            ["git", "-C", str(probe), "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True
        )
    except OSError:
        return False
    return result.returncode == 0 and result.stdout.strip() == "true"


def require_safe_vault(vault: Path) -> None:
    if inside_git_worktree(vault):
        raise CliError(f"vault {vault} is inside a git work tree; set THREEW_VAULT to a path outside any repository")


def load_bundle(name: str, bundles: Path | None = None) -> tuple[dict, dict[str, Path], bool]:
    """Return (metadata, {output relative path: source .tmpl}, single_file)."""
    bundles = bundles or BUNDLES
    directory = bundles / name
    if not re.fullmatch(r"[a-z0-9-]+", name) or not (directory / "bundle.yaml").is_file():
        available = sorted(p.parent.name for p in bundles.glob("*/bundle.yaml"))
        raise CliError(f"unknown bundle '{name}'; available: {', '.join(available)}")
    try:
        meta = yaml.safe_load((directory / "bundle.yaml").read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise CliError(f"{name}/bundle.yaml: invalid YAML: {exc}") from exc
    if not isinstance(meta, dict) or any(not isinstance(meta.get(key), str) for key in BUNDLE_KEYS):
        raise CliError(f"{name}/bundle.yaml needs string keys: {', '.join(BUNDLE_KEYS)}")
    variables = meta.get("variables") or []
    if not isinstance(variables, list) or any(not isinstance(v, dict) or "name" not in v or "example" not in v for v in variables):
        raise CliError(f"{name}/bundle.yaml: 'variables' must be a list of {{name, description?, example}}")
    meta["variables"] = {str(v["name"]): v for v in variables}
    source = (directory / meta["template"]).resolve()
    if not source.is_relative_to(directory.resolve()) or not source.exists():
        raise CliError(f"{name}/bundle.yaml: template '{meta['template']}' not found in the bundle")
    if source.is_file():
        return meta, {source.name.removesuffix(".tmpl"): source}, True
    files = {p.relative_to(source).as_posix().removesuffix(".tmpl"): p for p in sorted(source.rglob("*.tmpl"))}
    if not files:
        raise CliError(f"{name}/bundle.yaml: template folder '{meta['template']}' has no .tmpl files")
    return meta, files, False


def render(text: str, values: dict[str, str]) -> str:
    """Replace known variables; leave other {{placeholders}} for humans to fill."""
    return PLACEHOLDER.sub(lambda m: values.get(m.group(1), m.group(0)), text)


def codename_taken(codename: str, root: Path, vault: Path) -> bool:
    return (root / "projects" / codename).exists() or (vault / codename).exists()


def new_codename(root: Path, vault: Path) -> str:
    rng = secrets.SystemRandom()
    for _ in range(200):
        codename = f"{rng.choice(ADJECTIVES)}-{rng.choice(NOUNS)}"
        if not codename_taken(codename, root, vault):
            return codename
    raise CliError("could not find a free codename; pass --codename")


def render_bundle(
    bundle: str,
    *,
    codename: str | None = None,
    cleared: bool = False,
    private: bool = False,
    values: dict[str, str] | None = None,
    root: Path = ROOT,
    vault: Path | None = None,
    bundles: Path | None = None,
    today: date | None = None,
) -> Path:
    """Render a bundle; returns the created file (single-file bundle) or folder."""
    vault = (vault or vault_dir()).expanduser()
    meta, files, single = load_bundle(bundle, bundles)
    declared = meta["variables"]
    unknown = sorted(set(values or {}) - set(declared))
    if unknown:
        raise CliError(f"unknown variable(s) {', '.join(unknown)}; '{bundle}' declares: {', '.join(declared) or 'none'}")
    pattern = meta["target"]
    fields = {field for _, field, _, _ in Formatter().parse(pattern) if field}
    is_project = meta["kind"] == "project"
    if pattern.startswith("{vault}/"):
        if cleared:
            raise CliError(f"'{bundle}' renders into the vault; --cleared does not apply")
    elif "codename" in fields or is_project:
        if cleared == private:
            raise CliError("choose --cleared (the contract permits anonymised publication) or --private (vault only)")
        if private:
            pattern = "{vault}/" + pattern.removeprefix("projects/")
    elif cleared or private:
        raise CliError(f"'{bundle}' is not a client record; --cleared and --private do not apply")
    in_vault = pattern.startswith("{vault}/")
    if codename is None:
        codename = (values or {}).get("codename")
    if codename is None and ("codename" in fields or is_project):
        if not is_project:
            raise CliError(f"'{bundle}' needs --codename (the client's existing codename)")
        codename = new_codename(root, vault)
    if codename is not None and not CODENAME.fullmatch(codename):
        raise CliError(f"codename '{codename}' must be two lowercase words joined by a hyphen, e.g. quiet-harbour")
    filled = {"date": (today or date.today()).isoformat(), "bundle": bundle, **(values or {})}
    if codename:
        filled.update(codename=codename, title=codename.replace("-", " ").title())
    if cleared or private:
        filled["clearance"] = "private: vault only" if private else "cleared: contract permits anonymised publication"
    missing = sorted(fields - set(filled) - {"vault"})
    if missing:
        hints = ", ".join(f"--set {m}={declared.get(m, {}).get('example', '...')}" for m in missing)
        raise CliError(f"target '{meta['target']}' needs: {hints}")
    unsafe = sorted(f for f in fields - {"vault"} if re.search(r"[/\\]|\.\.", filled[f]))
    if unsafe:
        raise CliError(f"target variable(s) {', '.join(unsafe)} must not contain path separators or '..'")
    # Cleared project workspaces also create private sidecar directories.
    # Validate their vault before writing any public or private output.
    if in_vault or (is_project and vault.is_dir()):
        require_safe_vault(vault)
    if in_vault:
        if not vault.is_dir():
            raise CliError(f"vault {vault} does not exist; run `bin/3w vault init` first")
    base = (vault if in_vault else root).resolve()
    relative = pattern.removeprefix("{vault}/").format(vault=str(vault), **filled)
    target = (base / relative).resolve()
    if not target.is_relative_to(base) or target == base:
        raise CliError(f"target '{relative}' must stay inside the {'vault' if in_vault else 'repository'}")
    if single and not relative.endswith("/"):
        outputs = {target: next(iter(files.values()))}
    else:
        outputs = {target / rel: source for rel, source in files.items()}
    if is_project and codename:
        other = (root / "projects" / codename) if in_vault else (vault / codename / "README.md")
        if target.exists() or other.exists():
            raise CliError(f"codename '{codename}' already has a workspace; refusing to overwrite")
    existing = [str(path) for path in outputs if path.exists()]
    if existing:
        raise CliError(f"refusing to overwrite {', '.join(existing)}")
    for destination, source in outputs.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("x", encoding="utf-8") as handle:
            handle.write(render(source.read_text(encoding="utf-8"), filled))
    if is_project and codename and (private or vault.is_dir()):
        for name in PRIVATE_DIRS:
            (vault / codename / name).mkdir(parents=True, exist_ok=True)
    return target


def init_vault(vault: Path | None = None) -> Path:
    vault = vault or vault_dir()
    require_safe_vault(vault)
    vault.mkdir(parents=True, exist_ok=True)
    vault.chmod(0o700)
    for name, content in (("clients.yaml", CLIENTS_YAML), ("README.md", VAULT_README)):
        path = vault / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            path.chmod(0o600)
    return vault


def install_hook(repo: Path = ROOT) -> Path:
    try:
        hooks = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--git-path", "hooks"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        raise CliError(f"{repo} is not a git work tree") from exc
    hook = (repo / hooks / "pre-commit").resolve()
    if hook.exists() and HOOK_MARKER not in hook.read_text(encoding="utf-8", errors="replace"):
        raise CliError(f"{hook} already exists; add `bin/3w check --staged` to it by hand instead of overwriting")
    hook.parent.mkdir(parents=True, exist_ok=True)
    hook.write_text(HOOK, encoding="utf-8")
    hook.chmod(hook.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return hook


def run_check(staged: bool, root: Path = ROOT, vault: Path | None = None) -> int:
    vault = vault or vault_dir()
    if vault.exists():
        require_safe_vault(vault)
    guard = [sys.executable, "-m", "scripts.oscheck.anonymity", "--root", str(root), "--vault", str(vault)]
    if staged:
        return subprocess.call([*guard, "--staged"], cwd=ROOT)
    validator = subprocess.call([sys.executable, str(root / "scripts" / "validate.py")], cwd=root)
    return max(validator, subprocess.call(guard, cwd=ROOT))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="3w", description="3RDWRONG project workspaces, vault and anonymity guard (D-0021).")
    commands = parser.add_subparsers(dest="command", required=True)
    new = commands.add_parser("new", help="render a template bundle into a project workspace")
    new.add_argument("bundle")
    new.add_argument("--codename", help="kebab-case two-word codename; generated when omitted")
    where = new.add_mutually_exclusive_group()
    where.add_argument("--cleared", action="store_true", help="public repo: contract permits anonymised publication")
    where.add_argument("--private", action="store_true", help="render the whole workspace into the vault")
    new.add_argument("--set", action="append", default=[], metavar="NAME=VALUE", help="fill a declared variable; repeatable")
    vault = commands.add_parser("vault", help="manage the private vault")
    vault.add_argument("action", choices=["init"])
    check = commands.add_parser("check", help="run the repository validator, then the anonymity guard")
    check.add_argument("--staged", action="store_true", help="guard staged files only (used by the pre-commit hook)")
    hooks = commands.add_parser("hooks", help="manage local git hooks")
    hooks.add_argument("action", choices=["install"])
    args = parser.parse_args(argv)
    try:
        if args.command == "new":
            pairs = [item.partition("=") for item in args.set]
            if any(not sep or not name for name, sep, _ in pairs):
                raise CliError("--set expects NAME=VALUE")
            target = render_bundle(
                args.bundle, codename=args.codename, cleared=args.cleared, private=args.private,
                values={name: value for name, _, value in pairs},
            )
            shown = target.relative_to(ROOT) if target.is_relative_to(ROOT) else target
            print(f"Created {shown}{'/' if target.is_dir() else ''}")
            if args.cleared:
                print("Next: record the real client under this codename in the vault's clients.yaml,")
                print("then run `uv run python scripts/build_index.py` and `bin/3w check`.")
            return 0
        if args.command == "vault":
            print(f"Vault ready at {init_vault()}")
            return 0
        if args.command == "hooks":
            print(f"Installed {install_hook()}")
            return 0
        return run_check(args.staged)
    except CliError as exc:
        print(f"3w: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
