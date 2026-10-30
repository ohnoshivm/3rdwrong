---
title: "Reconciled hand-off formats, version 2.0"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Reconciled hand-off formats, version 2.0

These are JSON Schema draft 2020-12 schemas. `effects.schema.json` describes an
inventory; `scroll-map.schema.json` describes section geometry and native-scroll
windows; `motion-spec.schema.json` adds the build boundary and acceptance checks.
Local relative `$ref`s resolve against this folder; no network lookup is needed.
Schema `$id` URLs are identifiers, not deployed endpoints.

Examples under `examples/` summarise documented Oryzo facts in our words. They
are deliberately small teaching instances, not complete motion specifications
or new measurements. Source locators point to the curated case notes; the raw
third-party bundles and captures are excluded. Credits: oryzo.ai by Lusion.
DPR in examples describes capture context, not renderer DPR (capped at 1.5).

Windows declare units and may be null for a phase that does not apply. `from`
and `to` can be numbers, vectors, colours or strings; the property/unit gives
them meaning. A driver names the scalar and formula; values outside [0,1] are
valid section coordinates. Effect-local normalised progress is clamped.
An `inferred` evidence tag requires a confirmationProbe. Sources name evidence
kind and locator; they never contain source or shader dumps.

Validate examples with a draft-2020-12 validator. For this checkout, run
`uv run --with jsonschema python agent-system/scripts/validate-schemas.py`.
The helper validates schemas/examples offline and checks cross-field invariants.

JSON Schema cannot express all cross-field comparisons. Also check unique IDs,
source-ID consistency, window start ≤ end, scope bounds, valid effect/section
references, matching viewport units and single-writer ownership. A null window
means unknown/not applicable; status and notes must explain which. Schemas
validate the hand-off's shape, not the truth of its evidence.
