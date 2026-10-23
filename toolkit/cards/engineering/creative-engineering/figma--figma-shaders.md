---
title: Figma Shaders
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-shaders
department: engineering
sub_department: creative-engineering
job: shader-engineering
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires shaders. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-shaders/SKILL.md
invoke: "figma-shaders skill"
pairs_with: [skill:ceos-shader-engineering, skill:shaders-cursor-ripples]
---
# Figma Shaders

Figma Shaders is the specialist when A Figma file/workspace exists or is explicitly requested, and the task requires shaders. Load this prerequisite only for its corresponding Figma operation. at 3RDWRONG.

## What it does

- MANDATORY prerequisite — load this skill before calling createshader or updateshader. Use when the user asks to create, author, change, fix, or iterate on a shader effect, shader fill, custom effect, custom fill, or procedural shader in Figma
- effect samples and transforms the rendered layer beneath it. Use it for blur, distortion, glow, color grading, pixelation, halftone, or other post-processing
- fill generates pixels without an input raster. Use it for gradients, patterns, noise, textures, and procedural backgrounds
- Organises the method around create workflow
- Organises the method around update workflow

## When to use

- A Figma file/workspace exists or is explicitly requested, and the task requires shaders. Load this prerequisite only for its corresponding Figma operation.

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
2. Provide the inputs and constraints above; load or invoke `figma:figma-shaders`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use figma:figma-shaders for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `skill:ceos-shader-engineering`: coordinate inputs and hand off the reviewed result.
- `skill:shaders-cursor-ripples`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Distribution is fetch; install or sign in as required before use.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
