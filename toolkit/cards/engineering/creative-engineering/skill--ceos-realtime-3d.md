---
title: Ceos Realtime 3D
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-realtime-3d
department: engineering
sub_department: creative-engineering
job: realtime-3d
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-realtime-3d
invoke: "ceos-realtime-3d skill"
pairs_with: [agent:3d-webgl-engineer, skill:3d-falling-leaves, skill:3d-high-poly-models]
---
# Ceos Realtime 3D

Ceos Realtime 3D is the lead for realtime 3d at 3RDWRONG.

## What it does

- Architects and art-directs realtime 3D for websites with Three.js, React Three Fiber or OGL — scene graph, cameras and camera direction, PBR materials and lighting, environment maps, textures and colour management, render targets and post-processing, instancing, GPU memory and disposal, render-loop ownership, DOM/canvas coordination, adaptive quality and mobile. Use when building a WebGL/3D hero or scene, choosing three vs R3F vs OGL, fixing a 3D scene that looks cheap or runs slowly, or syncing 3D with scroll and HTML
- Organises the method around purpose
- Organises the method around choosing the library
- three.js: default for websites; mature, large ecosystem (loaders, PMREM, post, TSL/WebGPU renderer)
- R3F (+ drei): when the app is React and scenes are component-shaped; keep the frame loop in useFrame, avoid

## When to use

- Phase 03 Architecture or Phase 04 Concept when the approved brief requires realtime 3d.
- Establish the method and handoff before implementation begins.

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
2. Provide the inputs and constraints above; load or invoke `skill:ceos-realtime-3d`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:ceos-realtime-3d for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
