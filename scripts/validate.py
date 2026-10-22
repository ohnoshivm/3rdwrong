from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Callable

try:
    from .oscheck.agents import check_agents
    from .oscheck.common import Issue
    from .oscheck.decisions import check_decisions
    from .oscheck.frontmatter import check_frontmatter
    from .oscheck.index import check_index
    from .oscheck.links import check_links
    from .oscheck.required import check_required
    from .oscheck.secrets import check_secrets
    from .oscheck.skills import check_skills
    from .oscheck.stale import check_stale
except ImportError:
    from oscheck.agents import check_agents
    from oscheck.common import Issue
    from oscheck.decisions import check_decisions
    from oscheck.frontmatter import check_frontmatter
    from oscheck.index import check_index
    from oscheck.links import check_links
    from oscheck.required import check_required
    from oscheck.secrets import check_secrets
    from oscheck.skills import check_skills
    from oscheck.stale import check_stale

ROOT = Path(__file__).resolve().parents[1]
CHECKS: dict[str, Callable[[Path, dict], list[Issue]]] = {
    "frontmatter": check_frontmatter,
    "decisions": check_decisions,
    "skills": check_skills,
    "agents": check_agents,
    "links": check_links,
    "required": check_required,
    "secrets": check_secrets,
    "index": check_index,
}
ALL_CHECKS = (*CHECKS, "stale")


def run_checks(root: Path, config: dict, selected: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    for name in selected:
        if name == "stale":
            issues.extend(check_stale(root, config))
        else:
            issues.extend(CHECKS[name](root, config))
    return sorted(issues, key=lambda issue: (issue.path, issue.line, issue.check, issue.message))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate 3RDWRONGS OS documents and repository policy.")
    parser.add_argument("--check", choices=ALL_CHECKS, action="append", help="run only this check; repeat to run several")
    parser.add_argument("--stale", action="store_true", help="include the warning-only review-cadence report")
    args = parser.parse_args(argv)
    root = ROOT
    schema_path = root / "schemas" / "metadata.json"
    try:
        config = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        issue = Issue("schemas/metadata.json", 1, "required", f"cannot read metadata schema: {exc}")
        print(issue.render())
        print("Validation complete: 1 error, 0 warnings.")
        return 1
    selected = list(args.check or CHECKS)
    if args.stale and "stale" not in selected:
        selected.append("stale")
    issues = run_checks(root, config, selected)
    for issue in issues:
        print(issue.render())
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    print(f"Validation complete: {errors} error{'s' if errors != 1 else ''}, {warnings} warning{'s' if warnings != 1 else ''}.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
