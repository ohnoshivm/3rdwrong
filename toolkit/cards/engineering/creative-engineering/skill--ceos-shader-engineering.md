---
title: Ceos Shader Engineering
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-shader-engineering
department: engineering
sub_department: creative-engineering
job: shader-engineering
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-shader-engineering
invoke: "ceos-shader-engineering skill"
pairs_with: [figma:figma-shaders, skill:shaders-cursor-ripples]
---
# Ceos Shader Engineering

Ceos Shader Engineering is the lead for shader engineering at 3RDWRONG.

## What it does

- Writes, debugs and optimises GPU shaders for the web — GLSL ES 3.0 and WGSL, Three.js ShaderMaterial/onBeforeCompile and TSL (WebGPU), coordinate spaces, procedural noise and textures, signed distance fields and raymarching, vertex displacement, image and page transitions, GPGPU particles, multi-pass/ping-pong rendering, precision and cross-browser fallbacks. Use when a visual effect needs a custom shader, when building transitions, distortion, fluid or particle simulations, raymarched forms, or when a shader is slow, banding, or broken on some GPUs
- Organises the method around purpose
- Organises the method around core knowledge
- Organises the method around implementation standards
- Uniforms named by meaning (uProgress, uPointer, uTime), time in seconds, all animation driven from JS state

## When to use

- Phase 03 Architecture or Phase 04 Concept when the approved brief requires shader engineering.
- Establish the method and handoff before implementation begins.

## When not to use

- When the approved brief does not call for shader engineering; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:ceos-shader-engineering`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:ceos-shader-engineering for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `figma:figma-shaders`: coordinate inputs and hand off the reviewed result.
- `skill:shaders-cursor-ripples`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
