---
title: 3D High Resolution Textures
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3d-high-resolution-textures
department: engineering
sub_department: creative-engineering
job: realtime-3d
role: specialist
trigger: "Use for engineering/creative-engineering/realtime-3d when the brief specifically requires: Build sharp, physically coherent high-resolution materials for 3D rendering with appropriate PBR maps, texel density, UV direction, mipmaps, anisotropic filtering, and progressive asset delivery ."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills/3d-high-resolution-textures/SKILL.md
invoke: "3d-high-resolution-textures skill"
pairs_with: [agent:3d-webgl-engineer, skill:3d-falling-leaves, skill:3d-high-poly-models]
---
# 3D High Resolution Textures

3D High Resolution Textures is the specialist when Use for engineering/creative-engineering/realtime-3d when the brief specifically requires: Build sharp, physically coherent high-resolution materials for 3D rendering with appropriate PBR maps, texel density, UV direction, mipmaps, anisotropic filtering, and progressive asset delivery . at 3RDWRONG.

## What it does

- Build sharp, physically coherent high-resolution materials for 3D rendering with appropriate PBR maps, texel density, UV direction, mipmaps, anisotropic filtering, and progressive asset delivery. Use for detailed wood, stone, fabric, foliage, and architectural close-ups without excessive download or GPU memory costs
- Organises the method around choose resolution from the view
- Organises the method around build a coherent pbr material
- Organises the method around preserve detail during sampling
- Organises the method around deliver detail progressively

## When to use

- Use for engineering/creative-engineering/realtime-3d when the brief specifically requires: Build sharp, physically coherent high-resolution materials for 3D rendering with appropriate PBR maps, texel density, UV direction, mipmaps, anisotropic filtering, and progressive asset delivery .

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
2. Provide the inputs and constraints above; load or invoke `skill:3d-high-resolution-textures`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:3d-high-resolution-textures for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
