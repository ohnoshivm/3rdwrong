"""Shared, dependency-light evaluation contracts. Only PyYAML is third-party."""
from __future__ import annotations

import hashlib
import json
import math
import re
import unicodedata
from pathlib import Path

import yaml

VERDICTS = (
    'Strong enough to advance',
    'Promising but structurally unresolved',
    'Technically sound but conceptually weak',
    'Distinctive but commercially inappropriate',
    'Rejected, with explicit reasons',
)
LABELS = ('Documented', 'Interpretation', 'Hypothesis', 'Unknown')
ROOT = Path(__file__).resolve().parents[1]


class EvalError(ValueError):
    """An actionable contract error, safe to display without a traceback."""


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate mapping keys rather than silently changing scores."""


def _mapping(loader, node, deep=False):
    keys = [loader.construct_object(key, deep=deep) for key, _ in node.value]
    try:
        if len(keys) != len(set(keys)):
            raise EvalError('duplicate YAML key')
    except TypeError as exc:
        raise EvalError('YAML mapping keys must be scalar') from exc
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_yaml(path: Path) -> dict:
    data = yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueLoader)
    if not isinstance(data, dict):
        raise EvalError(f'{path.name}: expected a YAML mapping')
    return data


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding='utf-8')
    temporary.replace(path)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_path(root: Path, value: str) -> Path:
    if not isinstance(value, str) or Path(value).is_absolute() or '..' in Path(value).parts:
        raise EvalError('inputs must be relative repository paths without traversal')
    path = root / value
    if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
        raise EvalError(f'input must be an existing repository file: {value}')
    return path


def identifier(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*', value):
        raise EvalError('identifier must contain lowercase letters, numbers and hyphens only')
    return value


def registry(root: Path) -> list[dict]:
    return json.loads((root / 'toolkit/sources/registry.json').read_text())['tools']


def schema_errors(value, schema: dict, at='case') -> list[str]:
    """Validate the JSON Schema subset used by eval-case.json, without jsonschema."""
    errors = []
    kind = schema.get('type')
    valid = {
        'object': isinstance(value, dict), 'array': isinstance(value, list),
        'string': isinstance(value, str),
        'number': type(value) in (int, float) and math.isfinite(value),
    }
    if kind and not valid[kind]:
        return [f'{at}: expected {kind}']
    if 'const' in schema and (type(value) is not type(schema['const']) or value != schema['const']):
        errors.append(f'{at}: must equal {schema["const"]!r}')
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{at}: unsupported value')
    if kind == 'object':
        # YAML commonly parses anchor keys as integers; JSON object keys are strings.
        normalized = {str(k): v for k, v in value.items()}
        if len(normalized) != len(value):
            errors.append(f'{at}: duplicate normalised keys')
        for key in schema.get('required', []):
            if key not in normalized:
                errors.append(f'{at}: missing {key}')
        for key, item in normalized.items():
            if key in schema.get('properties', {}):
                errors.extend(schema_errors(item, schema['properties'][key], f'{at}.{key}'))
            elif schema.get('additionalProperties') is False:
                errors.append(f'{at}: unknown field {key}')
    elif kind == 'array':
        if len(value) < schema.get('minItems', 0):
            errors.append(f'{at}: list must not be empty')
        for index, item in enumerate(value):
            errors.extend(schema_errors(item, schema['items'], f'{at}[{index}]'))
    elif kind == 'string' and len(value.strip()) < schema.get('minLength', 0):
        errors.append(f'{at}: text must not be empty')
    elif kind == 'number':
        if value < schema.get('minimum', -math.inf) or value > schema.get('maximum', math.inf):
            errors.append(f'{at}: number outside allowed range')
        if value <= schema.get('exclusiveMinimum', -math.inf):
            errors.append(f'{at}: weight must be positive')
    return errors


def validate_case(root: Path, path: Path, schema_path='schemas/eval-case.json', *, storage: Path | None = None) -> dict:
    storage = storage or root
    if not path.resolve().is_relative_to(storage.resolve()):
        raise EvalError('case must remain inside the repository')
    case = read_yaml(path)
    schema = json.loads((root / schema_path).read_text())
    errors = schema_errors(case, schema)
    if errors:
        raise EvalError('; '.join(errors))
    for key in ('id', 'job', 'department'):
        identifier(case[key])
    expected = storage / 'evals/cases' / case['department'] / case['job'] / (case['id'] + '.yaml')
    if path.resolve() != expected.resolve():
        raise EvalError('case path must match department/job/id')
    if not any(t['department'] == case['department'] and t['job'] == case['job'] for t in registry(root)):
        raise EvalError('case department/job must exist in the registry')
    for name in case['inputs']:
        repo_path(storage / 'evals' if storage != root else root, name)
    if len(case['inputs']) != len(set(case['inputs'])):
        raise EvalError('duplicate input paths')
    for field in ('rubric', 'disqualifiers'):
        ids = [identifier(item['id']) for item in case[field]]
        if len(ids) != len(set(ids)):
            raise EvalError(f'duplicate {field} ids')
    if not math.isclose(sum(c['weight'] for c in case['rubric']), 1.0, abs_tol=1e-9):
        raise EvalError('rubric weights must sum to 1')
    return case


def canonical_model(value: str, *, demo: bool = False) -> str:
    """Resolve supported model spellings to conservative families; fail closed.

    Dated versions, provider routing prefixes and size/runtime variants cannot
    establish independence within one family. Unmapped deployment aliases need
    an explicit, reviewed resolver update rather than operator assertion.
    """
    if not isinstance(value, str):
        raise EvalError('model identifier must be text')
    name = unicodedata.normalize('NFKC', value).strip().casefold().split('/')[-1]
    if demo and name in {'unknown', 'historical-unknown'}:
        return 'unknown'
    name = re.sub(r'[-@:]\d{4}-?\d{2}-?\d{2}$', '', name)
    patterns = (
        (r'(?:gpt|codex)-(\d+(?:\.\d+)?)(?:-(?:sol|astra|luna|mini|nano|pro|chat|codex|latest))*', 'openai/gpt'),
        (r'(o[134])(?:-(?:mini|pro|latest))*', 'openai/o'),
        (r'gemini-(\d+(?:\.\d+)?)(?:-(?:pro|flash|lite|preview|latest))*', 'google/gemini'),
    )
    for pattern, prefix in patterns:
        match = re.fullmatch(pattern, name)
        if match:
            return prefix
    # Both Claude naming orders are in common use: opus-4-1 and 3-7-sonnet.
    for pattern in (r'claude-(opus|sonnet|haiku)-(\d+)(?:[.-](\d+))?',
                    r'claude-(\d+)(?:[.-](\d+))?-(opus|sonnet|haiku)'):
        match = re.fullmatch(pattern, name)
        if match:
            return 'anthropic/claude'
    raise EvalError(f'unresolved model alias: {value!r}; use a supported explicit model id')
