"""Offline JSON Schema and semantic checks. Run via uv --with jsonschema."""
from __future__ import annotations
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

BASE = Path(__file__).resolve().parent.parent / "schemas"
schemas = {p.name: json.loads(p.read_text()) for p in BASE.glob("*.schema.json")}
registry = Registry().with_resources(
    (schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()
)


def windows(value):
    if isinstance(value, dict):
        if {"start", "end", "unit"} <= value.keys():
            assert value["start"] <= value["end"], f"Reversed window: {value}"
        for item in value.values():
            windows(item)
    elif isinstance(value, list):
        for item in value:
            windows(item)


def unique(items, key):
    values = [item[key] for item in items]
    assert len(values) == len(set(values)), f"Duplicate {key}"


examples = {}
for name, schema in schemas.items():
    Draft202012Validator.check_schema(schema)
    example = json.loads((BASE / "examples" / name.replace(".schema", ".example")).read_text())
    Draft202012Validator(schema, registry=registry).validate(example)
    windows(example)
    examples[name] = example
    print(f"PASS {name}: valid schema and example")

effects = examples["effects.schema.json"]
scroll = examples["scroll-map.schema.json"]
motion = examples["motion-spec.schema.json"]
unique(effects["effects"], "id")
unique(scroll["sections"], "id")
unique(motion["effects"], "id")
unique(motion["acceptance"], "id")
assert scroll["scope"]["start"] <= scroll["scope"]["end"]
sections = {item["id"] for item in scroll["sections"]}
effect_ids = {item["id"] for item in effects["effects"]}
for item in scroll["effects"]:
    assert item["effectId"] in effect_ids
    assert item["sectionId"] in sections
    for window in (item["in"], item["out"]):
        if window and window["unit"] == "px":
            assert scroll["scope"]["start"] <= window["start"] <= window["end"] <= scroll["scope"]["end"]
for item in effects["effects"]:
    assert item["driver"].get("sectionId") in sections
    assert set(item["evidence"]) <= {source["kind"] for source in item["sources"]}
assert effects["viewport"] == scroll["viewport"] == motion["viewport"]
owned = [p for owner in motion["ownership"] for p in owner["paths"]]
assert len(owned) == len(set(owned)), "Multiple owners for a path"
for index, p in enumerate(owned):
    for q in owned[index + 1:]:
        assert not (p.startswith(q.rstrip("/") + "/") or q.startswith(p.rstrip("/") + "/")), "Overlapping ownership"
source_ids = {}
for example in examples.values():
    def check(value):
        if isinstance(value, dict):
            if {"id", "kind", "locator"} <= value.keys():
                if value["id"] in source_ids:
                    assert source_ids[value["id"]] == value, "Evidence ID changed identity"
                source_ids[value["id"]] = value
            for item in value.values():
                check(item)
        elif isinstance(value, list):
            for item in value:
                check(item)
    check(example)

validator = Draft202012Validator(schemas["effects.schema.json"], registry=registry)
for mutation in ("bad-trigger", "missing-driver", "inference-without-probe"):
    bad = copy.deepcopy(effects)
    effect = bad["effects"][0]
    if mutation == "bad-trigger":
        effect["trigger"] = "HOVER"
    elif mutation == "missing-driver":
        del effect["driver"]
    else:
        effect["evidence"].append("inferred")
    assert list(validator.iter_errors(bad)), f"Expected rejection: {mutation}"
print("PASS semantic cross-checks and 3 invalid-instance rejection checks")
