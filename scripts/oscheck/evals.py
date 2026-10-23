"""Validate proposed eval cases with the same contract as the runner."""
from pathlib import Path
import json
import yaml

from .common import Issue

try:
    from ..eval_core import read_yaml, validate_case
    from ..eval_run import load_run
    from ..eval_report import verified_result
except ImportError:
    from eval_core import read_yaml, validate_case
    from eval_run import load_run
    from eval_report import verified_result


def check_evals(root: Path, config: dict) -> list[Issue]:
    issues = []
    schema = config.get('evals', {}).get('case_schema', 'schemas/eval-case.json')
    for path in sorted((root / 'evals/cases').rglob('*.yaml')):
        try:
            validate_case(root, path, schema)
        except (ValueError, OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
            issues.append(Issue(path.relative_to(root).as_posix(), 1, 'evals', str(exc)))
    checks = []
    for path in sorted((root / 'evals/runs').rglob('run.yaml')):
        checks.append((path, lambda p=path: load_run(root, str(p.parent))))
    for path in sorted((root / 'evals/results').rglob('*.yaml')):
        checks.append((path, lambda p=path: verified_result(root, p)))
    for path, check in checks:
        try:
            check()
        except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError, json.JSONDecodeError) as exc:
            issues.append(Issue(path.relative_to(root).as_posix(), 1, 'evals', str(exc)))
    return issues
