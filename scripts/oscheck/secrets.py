from __future__ import annotations

import re
from pathlib import Path

from .common import Issue, relative_path

SECRET_PATTERNS = [
    ("private key block", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\b(?:gh[pous]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("AWS access key", re.compile(r"\bAKIA[A-Z0-9]{16}\b")),
    ("Slack token", re.compile(r"\bxox(?:b|a|p|r|s)-[A-Za-z0-9-]{10,}\b")),
    ("OpenAI or Anthropic key", re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_-]{16,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("AI-research residue", re.compile(r"images\." + r"openai\.com")),
    ("AI-research residue", re.compile("utm_source" + r"=chatgpt\.com")),
    (
        "credential assignment",
        re.compile(r"(?i)\b(?:password|secret|token|api_key)\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    ),
]
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
PAN = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")
AADHAAR = re.compile(r"(?<!\d)(?:\d{4}[ -]?){2}\d{4}(?!\d)")
RUPEE_AMOUNT = re.compile(r"₹\s*\d[\d,]*(?:\.\d+)?")
ALLOW_MARKER = "secret-scan: allow"


def _forbidden_name(name: str) -> bool:
    lowered = name.lower()
    return (
        lowered.startswith(".env")
        or lowered.endswith((".pem", ".key"))
        or lowered.startswith("id_rsa")
    )


def check_secrets(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    allowlist = config.get("secret_allowlist", {})
    allowed_emails = {str(value).lower() for value in allowlist.get("emails", [])}
    allowed_pan = {str(value).upper() for value in allowlist.get("pan", [])}
    allowed_aadhaar = {re.sub(r"\D", "", str(value)) for value in allowlist.get("aadhaar", [])}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        rel = relative_path(root, path)
        parts = Path(rel).parts
        if ".git" in parts or ".venv" in parts or path.name == "uv.lock":
            continue
        if _forbidden_name(path.name):
            issues.append(Issue(rel, 1, "secrets", "forbidden secret-bearing filename"))
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if "\x00" in text:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if ALLOW_MARKER in line:
                continue
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    issues.append(Issue(rel, line_number, "secrets", f"possible {label} detected"))
            for match in EMAIL.finditer(line):
                value = match.group(0).lower()
                if value not in allowed_emails:
                    issues.append(Issue(rel, line_number, "secrets", "email address found", "warning"))
            for match in PAN.finditer(line):
                if match.group(0).upper() not in allowed_pan:
                    issues.append(Issue(rel, line_number, "secrets", "possible private data: PAN-like identifier detected"))
            for match in AADHAAR.finditer(line):
                digits = re.sub(r"\D", "", match.group(0))
                if digits not in allowed_aadhaar:
                    issues.append(Issue(rel, line_number, "secrets", "possible private data: Aadhaar-like identifier detected"))
            if RUPEE_AMOUNT.search(line):
                issues.append(
                    Issue(rel, line_number, "secrets", "rupee amount must not appear in the public repository")
                )
    return issues
