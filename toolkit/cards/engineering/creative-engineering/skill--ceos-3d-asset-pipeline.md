---
title: Ceos 3D Asset Pipeline
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-3d-asset-pipeline
department: engineering
sub_department: creative-engineering
job: realtime-3d
role: specialist
trigger: "When the approved scope specifically requires preparing and optimizing 3D assets for web delivery."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-3d-asset-pipeline
invoke: "ceos-3d-asset-pipeline skill"
pairs_with: [agent:3d-webgl-engineer, skill:3d-falling-leaves, skill:3d-high-poly-models]
---
# Ceos 3D Asset Pipeline

Ceos 3D Asset Pipeline is the specialist when When the approved scope specifically requires preparing and optimizing 3D assets for web delivery. at 3RDWRONG.

## What it does

- Produces web-ready 3D assets — Blender modelling/lookdev hand-off, baking lighting/AO, glTF/GLB export, optimisation with glTF-Transform and meshoptimizer (gltfpack), Draco/meshopt geometry compression, KTX2/Basis texture compression, animation export, and per-asset size/performance budgets. Use when bringing models or textures into a website, when a GLB is too large or slow to load, when exporting from Blender, or when setting asset budgets for a 3D site
- Organises the method around tools on this machine
- Blender 5.2 LTS (/opt/homebrew/bin/blender, Homebrew cask) — headless scripting: blender -b file.blend --python script.py
- @gltf-transform/cli and gltfpack — project dev dependencies in the immersive-3d and experimental templates
- KTX-Software (ktx/toktx) — not installed (no Homebrew formula; official macOS installer is an admin .pkg)

## When to use

- When the approved scope specifically requires preparing and optimizing 3D assets for web delivery.

## When not to use

- When the approved brief does not call for realtime 3d; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:ceos-3d-asset-pipeline`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:ceos-3d-asset-pipeline for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
```

## What good output looks like

- Addresses the registry job and trigger with a concrete artefact, recommendation or implementation handoff.
- Makes assumptions and undocumented capabilities explicit; links findings to provided evidence.
- States constraints, unresolved risks and a next action suitable for independent review.

## Quality checks

- [ ] A reviewer other than the maker checks each source-specific requirement against the brief.
- [ ] Claims are supported by the source or supplied evidence; unknowns are labelled.
- [ ] Platform, responsive behaviour, accessibility and performance constraints are checked where applicable.
- [ ] No client data or secrets are committed to a public repository.

## Pairs with

- `agent:3d-webgl-engineer`: coordinate inputs and hand off the reviewed result.
- `skill:3d-falling-leaves`: coordinate inputs and hand off the reviewed result.
- `skill:3d-high-poly-models`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
