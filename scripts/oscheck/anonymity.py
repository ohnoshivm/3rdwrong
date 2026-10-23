"""Anonymity guard for D-0021: public project records stay anonymised.

Generic checks run in CI over the operating-record paths below. Deny-list mode
also loads the private vault's clients.yaml (never committed) and blocks every
real client name, alias, person, domain, email and phone in any tracked,
untracked-but-not-ignored or staged file.

Run from the repository root: ``python -m scripts.oscheck.anonymity [--staged]``.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from .common import Issue

# Operating records: client project workspaces. Declared in docs/public-private-boundary.md.
GUARDED_PREFIXES = ("projects/",)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json"}
# Add the studio's own mail domain here once the founder confirms it.
STUDIO_EMAIL_DOMAINS: set[str] = set()
EXAMPLE_EMAIL_DOMAINS = {"example.com", "example.org", "example.net", "users.noreply.github.com"}
RESERVED_TLDS = (".example", ".test", ".invalid", ".localhost")

EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@([A-Z0-9.-]+\.[A-Z]{2,})\b", re.IGNORECASE)
PHONE_CANDIDATE = re.compile(r"(?<![\w.])\+?\(?\d[\d\s().-]{6,18}\d(?!\w)")
INDIAN_MOBILE = re.compile(r"(?<![\w+])[6-9]\d{9}(?!\w)")
CURRENCY = re.compile(
    r"(?:₹|\bRs\.?|\bINR|\bUSD|\bEUR|\bGBP|\$|€|£)\s?\d"
    r"|\d\s?(?:INR|USD|EUR|GBP|lakhs?|crores?)\b",
    re.IGNORECASE,
)
GSTIN = re.compile(r"\b\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b")
PAN = re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b")
IFSC = re.compile(r"\b[A-Z]{4}0[A-Z0-9]{6}\b")
AADHAAR = re.compile(r"(?<![\w+])\d{4}[ -]?\d{4}[ -]?\d{4}(?!\w)")
PATTERNS = (
    ("currency amount", CURRENCY),
    ("GSTIN", GSTIN),
    ("PAN", PAN),
    ("IFSC code", IFSC),
    ("Aadhaar-like number", AADHAAR),
)
DENY_FIELDS = ("name", "aliases", "emails", "domains", "phones")


def _email_allowed(domain: str) -> bool:
    domain = domain.lower()
    return domain in STUDIO_EMAIL_DOMAINS | EXAMPLE_EMAIL_DOMAINS or domain.endswith(RESERVED_TLDS)


def _is_phone(raw: str) -> bool:
    digits = re.sub(r"\D", "", raw)
    if raw.startswith("+"):
        return 8 <= len(digits) <= 15
    return (len(digits) == 10 and digits[0] in "6789") or (len(digits) == 11 and digits[0] == "0")


def is_guarded(rel: str) -> bool:
    return rel.startswith(GUARDED_PREFIXES)


def generic_line_issues(line: str) -> list[str]:
    found = ["email address" for m in EMAIL.finditer(line) if not _email_allowed(m.group(1))]
    if INDIAN_MOBILE.search(line) or any(_is_phone(m.group(0).strip()) for m in PHONE_CANDIDATE.finditer(line)):
        found.append("phone number")
    found.extend(label for label, pattern in PATTERNS if pattern.search(line))
    return found


def load_deny_terms(vault: Path) -> list[tuple[str, str]]:
    """Return (source, term) pairs from <vault>/clients.yaml; source never contains the term."""
    import yaml

    path = vault / "clients.yaml"
    if not path.is_file():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    clients = data.get("clients") or {}
    if not isinstance(clients, dict):
        raise ValueError(f"{path}: 'clients' must be a mapping of codename to record")
    terms: list[tuple[str, str]] = []

    def add(source: str, value: object) -> None:
        values = value if isinstance(value, list) else [value]
        terms.extend((source, str(item).strip()) for item in values if item and str(item).strip())

    for codename, record in clients.items():
        record = record or {}
        for field in DENY_FIELDS:
            add(f"{codename}.{field}", record.get(field))
        for person in record.get("people") or []:
            if isinstance(person, dict):
                for field in ("name", "email", "phone"):
                    add(f"{codename}.people.{field}", person.get(field))
    return terms


def _deny_matchers(terms: list[tuple[str, str]]):
    matchers = []
    for source, term in terms:
        digits = re.sub(r"\D", "", term)
        if source.endswith(("phones", "phone")) and len(digits) >= 7:
            tail = digits[-10:]
            matchers.append((source, lambda line, tail=tail: any(
                re.sub(r"\D", "", m.group(0)).endswith(tail) for m in PHONE_CANDIDATE.finditer(line)
            ) or tail in re.sub(r"\D", "", line)))
        elif len(term) >= 3:
            pattern = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE)
            matchers.append((source, lambda line, pattern=pattern: bool(pattern.search(line))))
    return matchers


def scan_text(rel: str, text: str, deny: list[tuple[str, str]] | None = None, generic: bool | None = None) -> list[Issue]:
    generic = is_guarded(rel) if generic is None else generic
    matchers = _deny_matchers(deny or [])
    issues: list[Issue] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if generic:
            issues.extend(Issue(rel, number, "anonymity", f"{label} in a public project record; keep it in the vault") for label in generic_line_issues(line))
        for source, matches in matchers:
            if matches(line):
                issues.append(Issue(rel, number, "anonymity", f"deny-listed client term from the vault ({source})"))
    return issues


def scan_blob(rel: str, data: bytes, deny: list[tuple[str, str]] | None = None) -> list[Issue]:
    if is_guarded(rel) and Path(rel).suffix.lower() not in TEXT_SUFFIXES:
        return [Issue(rel, 1, "anonymity", "non-text file in a public project record; client files belong in the vault")]
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return []
    return scan_text(rel, text, deny)


def _git(root: Path, *args: str) -> bytes | None:
    try:
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout


def repo_files(root: Path, prefixes: tuple[str, ...] = ()) -> list[str]:
    """Tracked plus untracked-but-not-ignored files; plain walk outside git."""
    listed = _git(root, "ls-files", "-z", "-co", "--exclude-standard", "--", *prefixes)
    if listed is not None:
        return sorted({p for p in listed.decode("utf-8").split("\0") if p and (root / p).is_file()})
    bases = [root / p for p in prefixes] or [root]
    return sorted(
        path.relative_to(root).as_posix()
        for base in bases if base.exists()
        for path in base.rglob("*")
        if path.is_file() and path.name != ".DS_Store" and ".git" not in path.relative_to(root).parts
    )


def check_anonymity(root: Path, config: dict) -> list[Issue]:
    """Validator entry point: generic checks over guarded paths; no vault in CI."""
    issues: list[Issue] = []
    for rel in repo_files(root, GUARDED_PREFIXES):
        issues.extend(scan_blob(rel, (root / rel).read_bytes()))
    return issues


def scan_repository(root: Path, deny: list[tuple[str, str]]) -> list[Issue]:
    issues: list[Issue] = []
    for rel in repo_files(root):
        if is_guarded(rel) or deny:
            issues.extend(scan_blob(rel, (root / rel).read_bytes(), deny))
    return issues


def scan_staged(root: Path, deny: list[tuple[str, str]]) -> list[Issue]:
    names = _git(root, "diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR")
    if names is None:
        raise RuntimeError("cannot list staged files; is this a git work tree?")
    issues: list[Issue] = []
    for rel in filter(None, names.decode("utf-8").split("\0")):
        if is_guarded(rel) or deny:
            issues.extend(scan_blob(rel, _git(root, "show", f":{rel}") or b"", deny))
    return issues


def default_vault() -> Path:
    return Path(os.environ.get("THREEW_VAULT", "~/3rdwrong-vault")).expanduser()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Anonymity guard for public project records (D-0021).")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--staged", action="store_true", help="scan staged blobs only (pre-commit)")
    parser.add_argument("--vault", type=Path, default=None, help="vault path; default THREEW_VAULT or ~/3rdwrong-vault")
    args = parser.parse_args(argv)
    vault = args.vault or default_vault()
    try:
        deny = load_deny_terms(vault)
        issues = scan_staged(args.root, deny) if args.staged else scan_repository(args.root, deny)
    except (ValueError, RuntimeError, OSError) as exc:
        print(f"anonymity guard: error: {exc}", file=sys.stderr)
        return 2
    for issue in issues:
        print(issue.render())
    mode = f"deny-list on ({len(deny)} terms)" if deny else "deny-list off (no vault clients.yaml)"
    scope = "staged files" if args.staged else "working tree"
    print(f"Anonymity guard ({scope}, {mode}): {len(issues)} issue{'s' if len(issues) != 1 else ''}.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
