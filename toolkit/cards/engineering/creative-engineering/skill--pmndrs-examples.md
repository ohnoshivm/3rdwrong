---
title: Pmndrs Examples
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:pmndrs-examples
department: engineering
sub_department: creative-engineering
job: realtime-3d
role: specialist
trigger: "An existing React Three Fiber project needs a pinned example of a specific approved scene mechanism."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/pmndrs-examples
invoke: "pmndrs-examples skill"
pairs_with: [agent:3d-webgl-engineer, skill:3d-falling-leaves, skill:3d-high-poly-models]
---
# Pmndrs Examples

Pmndrs Examples is the specialist when An existing React Three Fiber project needs a pinned example of a specific approved scene mechanism. at 3RDWRONG.

## What it does

- Search and adapt pinned pmndrs examples for Three.js, React Three Fiber, drei, or WebGL scene work; use only when implementing those renderers
- The source does not document further capabilities in the inspected section

## When to use

- An existing React Three Fiber project needs a pinned example of a specific approved scene mechanism.

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
2. Provide the inputs and constraints above; load or invoke `skill:pmndrs-examples`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:pmndrs-examples for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
