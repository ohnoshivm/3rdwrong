"""Collect pre-launch lab evidence; never turn proxies into field acceptance.

Run with uv run python scripts/web_qa.py run URL --out PRIVATE_DIRECTORY.
Only PyYAML is required in Python; Lighthouse and Playwright CLI run as tools.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import statistics
import subprocess
import sys
import tempfile
import uuid
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUDGET = ROOT / "methods/digital-experience/qa-budget.yaml"
# Immutable ceiling: editing the distributed YAML cannot silently waive D-0023.
DEFAULTS = {
    "lcp_ms": 2000, "inp_ms": 200, "cls": 0.1,
    "transfer_before_input_bytes": 2_000_000, "fps": 60, "tbt_ms": 200,
    "accessibility_failures": 0, "console_errors": 0, "active_reduced_animations": 0,
}
LABELS = {
    "lcp_ms": "LCP median, mobile lab (ms)",
    "inp_ms": "INP mobile p75, field (ms)",
    "cls": "CLS median, mobile lab",
    "transfer_before_input_bytes": "Transfer before input, load approximation (bytes)",
    "fps": "Scroll frame rate, lab estimate (fps)",
    "tbt_ms": "TBT median, lab responsiveness proxy (ms)",
    "accessibility_failures": "Failed Lighthouse accessibility audits (maximum across runs)",
    "console_errors": "Console errors and uncaught exceptions across browser probes",
    "active_reduced_animations": "Active reduced-motion CSS/WAAPI animations and playing media",
}
LIMITS = [
    "Lighthouse uses three cold mobile runs with default simulated mobile throttling; "
    "medians are lab observations, not mobile p75 field data.",
    "INP is NOT_MEASURED. TBT is a load responsiveness proxy, not an INP value. "
    "Collect mobile p75 INP using RUM/CrUX when available, and script representative "
    "click/type journeys with Event Timing for pre-launch interaction evidence.",
    "Pre-input transfer approximates an input at the load event: sum full transferSize "
    "of Lighthouse network requests whose rendererStartTime <= observedLoad (both ms). "
    "No user input is sent during Lighthouse. Full requests can overcount bytes crossing "
    "the cutoff; after-load requests and later user input are outside this approximation. "
    "Total transfer is the median Lighthouse total-byte-weight over its observation window.",
    "Accessibility uses Lighthouse accessibility audits (including its axe-based checks), "
    "not a separate axe scan. Count failed audit IDs, not DOM violations. Manual audits, "
    "keyboard, screen reader and complete WCAG 2.2 AA conformance are not verified.",
    "Reduced motion is emulated before navigation at all three widths. Poll running/pending "
    "document.getAnimations() and playing audio/video for 1.5 seconds at top, midpoint and three-quarter scroll depth; "
    "non-zero is flagged. Canvas/WebGL, GIFs, cross-origin frames, JS style updates, "
    "later/interaction-triggered motion and equivalent fallback content need manual review. "
    "Zero detected motion never proves a complete fallback.",
    "Frame rate is a two-second requestAnimationFrame scripted scroll lab estimate on the "
    "host at 375 CSS px, without mobile CPU/GPU throttling. It measures callback cadence, "
    "not compositor/GPU output or 60 fps on a mid-range phone. No scroll range means not measured.",
    "Screenshots at 375/768/1440 CSS px (900 px height, DPR 1) are evidence for human "
    "inspection, not automatic visual approval. The studio 390/834, reflow 320, large 1920 "
    "widths, other browsers/devices and functional journeys still need separate QA.",
    "Only this URL and the sampled states are checked. Independent review, security, "
    "consent, production build tests, launch/rollback and founder/client approval remain required.",
]


def number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def load_budget(path: Path | None = None) -> dict:
    path = (path or DEFAULT_BUDGET).resolve()
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("limits", {}), dict):
        raise ValueError("budget must be a mapping with a limits mapping")
    if set(raw) - {"status", "source", "limits", "exception"}:
        raise ValueError("unknown budget keys")
    limits = DEFAULTS | raw.get("limits", {})
    for key, value in limits.items():
        if key not in DEFAULTS or not number(value) or value < 0 or (key == "fps" and value == 0):
            raise ValueError(f"invalid budget limit: {key}")
    looser = [key for key, value in limits.items()
              if (value < DEFAULTS[key] if key == "fps" else value > DEFAULTS[key])]
    exception = None
    if looser:
        proposed = raw.get("exception")
        if not isinstance(proposed, dict) or not isinstance(proposed.get("metrics"), list):
            raise ValueError("looser limits require exception.record and exception.metrics")
        if not set(looser).issubset(proposed["metrics"]) or not isinstance(proposed.get("record"), str):
            raise ValueError("founder exception must cover every loosened metric")
        reference = Path(proposed["record"])
        if reference.is_absolute() or ".." in reference.parts:
            raise ValueError("exception record must be a repository-relative decision path without traversal")
        record = (ROOT / reference).resolve()
        decisions = (ROOT / "studio/decisions").resolve()
        if not record.is_relative_to(decisions) or record.suffix != ".md" or not record.is_file():
            raise ValueError("founder exception must name a canonical studio/decisions Markdown record")
        # Only committed, unchanged decisions are trusted; caller-written frontmatter is not approval.
        committed = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{reference.as_posix()}"],
                                   capture_output=True, check=False)
        if committed.returncode or committed.stdout != record.read_bytes():
            raise ValueError("founder exception must be committed and unchanged in the trusted repository")
        content = record.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        metadata = yaml.safe_load(parts[1]) if content.startswith("---\n") and len(parts) == 3 else None
        if (not isinstance(metadata, dict) or metadata.get("status") != "approved"
                or metadata.get("approved_by") != "founder"):
            raise ValueError("exception record needs status: approved and approved_by: founder")
        try:
            approved = date.fromisoformat(str(metadata.get("approved_on")))
            if approved > date.today():
                raise ValueError("future approval")
        except ValueError as exc:
            raise ValueError("exception record needs a valid approved_on date") from exc
        scope = metadata.get("qa_exception")
        project = proposed.get("project")
        if (not isinstance(project, str) or not project.strip() or not isinstance(scope, dict)
                or scope.get("project") != project or not isinstance(scope.get("limits"), dict)
                or any(scope["limits"].get(key) != limits[key] for key in looser)):
            raise ValueError("founder decision must authorise this project codename and exact loosened limits")
        exception = {"record": str(record), "metrics": proposed["metrics"],
                     "approved_on": str(metadata["approved_on"]),
                     "sha256": hashlib.sha256(content.encode()).hexdigest()}
    return {"path": str(path), "limits": limits, "exception": exception}


def compare(value: object, limit: float, *, minimum: bool = False) -> str:
    if not number(value) or value < 0:
        return "NOT_MEASURED"
    return "PASS" if (value >= limit if minimum else value <= limit) else "FAIL"


def validate_lighthouse(run: object) -> dict:
    """Validate containers before aggregation; malformed evidence is never a pass."""
    if not isinstance(run, dict):
        raise ValueError("malformed Lighthouse report: expected object")
    if run.get("runtimeError"):
        return run
    audits = run.get("audits")
    categories = run.get("categories")
    if (not isinstance(audits, dict) or any(not isinstance(v, dict) for v in audits.values())
            or not isinstance(categories, dict) or not isinstance(categories.get("accessibility"), dict)):
        raise ValueError("malformed Lighthouse audits/categories")
    if any(not isinstance(audit.get("scoreDisplayMode", ""), str) for audit in audits.values()):
        raise ValueError("malformed Lighthouse scoreDisplayMode")
    refs = categories["accessibility"].get("auditRefs")
    if (not isinstance(refs, list) or not refs
            or any(not isinstance(ref, dict) or not isinstance(ref.get("id"), str)
                   or ref["id"] not in audits for ref in refs)):
        raise ValueError("malformed Lighthouse accessibility auditRefs")
    return run


def summarise_lighthouse(runs: list[dict]) -> dict:
    """Require all three valid observations per metric; never median a partial run."""
    metrics = {"lcp_ms": "largest-contentful-paint", "cls": "cumulative-layout-shift",
               "tbt_ms": "total-blocking-time", "total_transfer_bytes": "total-byte-weight"}
    values: dict[str, list] = {key: [] for key in (*metrics, "transfer_before_input_bytes", "accessibility_failures")}
    for run in runs:
        try:
            validate_lighthouse(run)
        except ValueError:
            run = {"runtimeError": "malformed report"}
        audits = run.get("audits", {}) if not run.get("runtimeError") else {}
        for key, audit in metrics.items():
            values[key].append(audits.get(audit, {}).get("numericValue"))
        try:
            cutoff = audits["metrics"]["details"]["items"][0]["observedLoad"]
            requests = audits["network-requests"]["details"]["items"]
            if not number(cutoff) or cutoff <= 0 or not requests:
                raise ValueError("missing load/network observation")
            initial = 0
            for request in requests:
                start, size = request.get("rendererStartTime"), request.get("transferSize")
                if not number(start) or not number(size) or size < 0:
                    raise ValueError("incomplete request timing/size")
                if start <= cutoff:
                    if request.get("finished") is not True:
                        raise ValueError("unfinished initial request")
                    initial += size
            values["transfer_before_input_bytes"].append(initial)
        except (KeyError, IndexError, TypeError, ValueError, AttributeError):
            values["transfer_before_input_bytes"].append(None)
        refs = [] if run.get("runtimeError") else run["categories"]["accessibility"]["auditRefs"]
        count = 0
        valid = bool(refs) and bool(audits)
        for ref in refs:
            audit = audits.get(ref["id"], {})
            mode = audit.get("scoreDisplayMode")
            if mode in {"manual", "notApplicable", "informative"}:
                continue
            if mode == "error" or not number(audit.get("score")):
                valid = False
            elif audit["score"] < 1:
                count += 1
        values["accessibility_failures"].append(count if valid else None)
    return {key: ((max(items) if key == "accessibility_failures" else statistics.median(items))
                  if len(items) == 3 and all(number(v) and v >= 0 for v in items) else None)
            for key, items in values.items()}


def make_report(url: str, budget: dict, measurements: dict, evidence: list[str], errors: list[str]) -> dict:
    checks = [{"id": key, "label": LABELS[key], "value": measurements.get(key), "limit": limit,
               "operator": ">=" if key == "fps" else "<=",
               "status": compare(measurements.get(key), limit, minimum=key == "fps")}
              for key, limit in budget["limits"].items()]
    browser_metrics = {"fps", "console_errors", "active_reduced_animations"}
    for row in checks:
        row["evidence"] = ([] if row["status"] == "NOT_MEASURED" else
                           [path for path in evidence if (path == "browser.json" if row["id"] in browser_metrics
                                                          else path.startswith("lighthouse-"))])
    # These D-0023 requirements cannot be certified by the automated lab probes.
    for key, label, limit in (
        ("field_lcp_ms", "LCP mobile p75, field (ms)", budget["limits"]["lcp_ms"]),
        ("field_cls", "CLS mobile p75, field", budget["limits"]["cls"]),
        ("device_fps", "60 fps target on reference mid-range phone", budget["limits"]["fps"]),
        ("reduced_motion_complete", "Complete equivalent reduced-motion fallback", "manual review"),
    ):
        checks.append({"id": key, "label": label, "value": None, "limit": limit,
                       "operator": "required", "status": "NOT_MEASURED", "evidence": []})
    lab = [row for row in checks if row["id"] in DEFAULTS and row["id"] != "inp_ms"]
    lab_status = ("FAIL" if any(row["status"] == "FAIL" for row in lab) else
                  "INCOMPLETE" if errors or any(row["status"] == "NOT_MEASURED" for row in lab) else "PASS")
    return {"schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
            "url": url, "status": "FAIL" if lab_status == "FAIL" else "INCOMPLETE",
            "lab_status": lab_status, "budget": budget, "measurements": measurements,
            "checks": checks, "evidence": evidence, "errors": errors, "limits": LIMITS,
            "not_measured": [row["id"] for row in checks if row["status"] == "NOT_MEASURED"]}


def private_output(out: Path) -> Path:
    out = out.expanduser().resolve()
    if out.is_relative_to(ROOT.resolve()):
        raise ValueError("QA evidence must stay outside the public repository, including symlink targets")
    return out


def write_report(out: Path, report: dict) -> None:
    out = private_output(out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "report.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    lines = ["# 3RDWRONG web delivery QA", "", f"URL: {cell(report['url'])}", "",
             f"Collected: {report['created_at']}", "",
             f"Result: **{report['status']}**. Automated lab gates: **{report['lab_status']}**.", "",
             "This report does not approve launch. NOT_MEASURED blocks an acceptance claim.", "",
             "| Check | Observed | Budget | Result | Evidence |", "| --- | --- | --- | --- | --- |"]
    for row in report["checks"]:
        lines.append(f"| {cell(row['label'])} | {cell(row['value']) if row['value'] is not None else 'not measured'} "
                     f"| {row['operator']} {cell(row['limit'])} | {row['status']} "
                     f"| {', '.join(f'[{p}]({p})' for p in row['evidence']) or 'none'} |")
    lines += ["", "Total transfer (median Lighthouse observation, bytes): "
              + str(report["measurements"].get("total_transfer_bytes", "not measured")), "",
              "## Evidence", ""]
    lines += [f"- [{p}]({p})" for p in report["evidence"]] or ["No evidence collected."]
    lines += ["", "## Collection errors", ""]
    lines += [f"- {cell(error)}" for error in report["errors"]] or ["None."]
    lines += ["", "## Methods and limits", ""]
    lines += [f"- {limit}" for limit in report["limits"]]
    lines += ["", "Budget and any founder exception record/hash are included in report.json.", ""]
    (out / "report.md").write_text("\n".join(lines), encoding="utf-8")


def command(argv: list[str], *, cwd: Path, timeout: int = 180) -> str:
    result = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=timeout, check=False)
    if result.returncode:
        raise RuntimeError(f"{argv[0]} exited {result.returncode}: {(result.stderr or result.stdout)[-2000:]}")
    if "### Error" in result.stdout:
        raise RuntimeError(result.stdout[-2000:])
    return result.stdout.strip()


def collect_browser(url: str, out: Path) -> dict:
    cli = shutil.which("playwright-cli")
    if not cli:
        raise RuntimeError("playwright-cli unavailable; install @playwright/cli and Chrome")
    session = f"3w-qa-{uuid.uuid4().hex[:10]}"
    with tempfile.TemporaryDirectory(prefix="3w-web-qa-") as tmp:
        cwd = Path(tmp)
        script = (ROOT / "scripts/web_qa_browser.js").read_text(encoding="utf-8")
        script = script.replace("__WEB_QA_CONFIG__", json.dumps({"url": url, "out": str(out)}))
        source = cwd / "probe.js"
        source.write_text(script, encoding="utf-8")
        prefix = [cli, f"-s={session}"]
        try:
            command([*prefix, "open", "about:blank", "--browser=chrome"], cwd=cwd, timeout=60)
            raw = command([*prefix, "--raw", "run-code", f"--filename={source}"], cwd=cwd)
            result = json.loads(raw)
            result["playwrightCliVersion"] = command([cli, "--version"], cwd=cwd, timeout=20)
            return result
        finally:
            try:
                command([*prefix, "close"], cwd=cwd, timeout=20)
            except (RuntimeError, OSError, subprocess.TimeoutExpired):
                pass


def run_harness(url: str, out: Path, budget: dict) -> dict:
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("URL must be http(s), without embedded credentials")
    out = private_output(out)
    # Never mix screenshots from a prior build with current measurements.
    if out.exists() and any(out.iterdir()):
        raise ValueError("--out must be a new or empty directory")
    out.mkdir(parents=True, exist_ok=True)
    errors, evidence, runs = [], [], []
    lighthouse = shutil.which("lighthouse")
    if not lighthouse:
        errors.append("lighthouse unavailable; no performance/accessibility observations")
    else:
        for index in range(1, 4):
            target = out / f"lighthouse-{index}.json"
            try:
                command([lighthouse, url, "--quiet", "--output=json", f"--output-path={target}",
                         "--only-categories=performance,accessibility", "--form-factor=mobile",
                         "--throttling-method=simulate", "--chrome-flags=--headless"], cwd=out)
                run = json.loads(target.read_text(encoding="utf-8"))
                evidence.append(target.name)
                validate_lighthouse(run)
                runs.append(run)
                if run.get("runtimeError"):
                    errors.append(f"Lighthouse run {index}: {run['runtimeError']}")
            except (RuntimeError, OSError, ValueError, subprocess.TimeoutExpired) as exc:
                errors.append(f"Lighthouse run {index}: {exc}")
    measurements = summarise_lighthouse(runs)
    try:
        browser = collect_browser(url, out)
        (out / "browser.json").write_text(json.dumps(browser, indent=2) + "\n", encoding="utf-8")
        evidence.append("browser.json")
        evidence.extend(browser["screenshots"])
        measurements.update(browser["measurements"])
        errors.extend(browser.get("errors", []))
    except (RuntimeError, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as exc:
        errors.append(f"Playwright: {exc}")
        evidence.extend(sorted(path.name for path in out.glob("screenshots-*.png")))
    report = make_report(url, budget, measurements, evidence, errors)
    report["tools"] = {"lighthouse_versions": [run.get("lighthouseVersion") for run in runs],
                       "lighthouse_profiles": [run.get("configSettings") for run in runs]}
    write_report(out, report)
    return report


def add_run_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("url")
    parser.add_argument("--out", type=Path, help="new/empty directory outside the repo; default: private temporary directory")
    parser.add_argument("--budget", type=Path, help="project YAML; defaults to the studio budget")


def run_args(args: argparse.Namespace) -> int:
    try:
        args.out = args.out or Path(tempfile.mkdtemp(prefix="3w-web-qa-evidence-"))
        report = run_harness(args.url, args.out, load_budget(args.budget))
    except (ValueError, OSError, yaml.YAMLError) as exc:
        print(f"web-qa: {exc}", file=sys.stderr)
        return 2
    print(f"{report['status']} (lab {report['lab_status']}): {args.out.resolve() / 'report.md'}")
    return 1 if report["status"] == "FAIL" else 2  # Field/manual requirements remain unverified.


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    add_run_arguments(commands.add_parser("run", help="collect and compare private lab evidence"))
    return run_args(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
