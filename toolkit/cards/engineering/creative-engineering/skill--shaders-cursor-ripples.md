---
title: Shaders Cursor Ripples
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:shaders-cursor-ripples
department: engineering
sub_department: creative-engineering
job: shader-engineering
role: specialist
trigger: "The approved concept specifically calls for this effect: shaders-cursor-ripples."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/effects-3d/shaders-cursor-ripples/SKILL.md
invoke: "shaders-cursor-ripples skill"
pairs_with: [figma:figma-shaders, skill:ceos-shader-engineering]
---
# Shaders Cursor Ripples

Shaders Cursor Ripples is the specialist when The approved concept specifically calls for this effect: shaders-cursor-ripples. at 3RDWRONG.

## What it does

- Add cursor-following fluid WebGPU distortion over an existing image with the Shaders library's ImageTexture and CursorRipples components. Use when a hero, gallery, or media panel needs a water-ripple mouse effect; when replacing a drifting CSS spotlight or flashlight reveal; or when a prompt says to borrow only the shader interaction from a Shaders.com reference while preserving the current brand, image, copy, and layout
- Organises the method around inspect before editing
- Find the real media wrapper, image URL, crop, overlays, z-index, and existing motion
- Confirm the wrapper has a non-zero rendered width and height
- Search for old reveal code such as data-reveal-hover, mask-image: radial-gradient, duplicated images, requestAnimationFrame, and manual pointer listeners

## When to use

- The approved concept specifically calls for this effect: shaders-cursor-ripples.

## When not to use

- When the approved brief does not call for shader engineering; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## Technology choice

**Documented** — [D-0025](../../../../studio/decisions/0025-creative-technology-selection-policy.md)
adopts the [selection policy](../../../../methods/creative-technology/selection-policy.md).
This source selects a WebGPU effect. First compare CSS/SVG, OGL or another smaller approach; retain WebGPU only for a recorded requirement with device and fallback evidence. Source availability is not a verified runtime connection. D-0023 remains binding; preserve HTML, keyboard access and reduced motion.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:shaders-cursor-ripples`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:shaders-cursor-ripples for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
- `skill:ceos-shader-engineering`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
