---
title: Webgl Laser
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:webgl-laser
department: engineering
sub_department: creative-engineering
job: generative-creative-coding
role: specialist
trigger: "The approved concept specifically calls for this effect: webgl-laser."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/effects-3d/webgl-laser/SKILL.md
invoke: "webgl-laser skill"
pairs_with: [figma:figma-generative-plugins, skill:ceos-creative-coding, skill:creating-algorithmic-art]
---
# Webgl Laser

Webgl Laser is the specialist when The approved concept specifically calls for this effect: webgl-laser. at 3RDWRONG.

## What it does

- Create a fixed full-screen WebGL laser background effect with a thin white-hot vertical core, restrained brand-colored halo, and soft smoky fog around the beam. Use only for laser background effects, not full page layout, copy, generic hero scenes, particles, or unrelated motion systems
- Apply only to the laser background effect
- Use a fixed full-screen canvas behind the DOM
- Set pointer-events: none on the canvas
- Keep page content in a higher stacking context

## When to use

- The approved concept specifically calls for this effect: webgl-laser.

## When not to use

- When the approved brief does not call for generative creative coding; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:webgl-laser`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:webgl-laser for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `figma:figma-generative-plugins`: coordinate inputs and hand off the reviewed result.
- `skill:ceos-creative-coding`: coordinate inputs and hand off the reviewed result.
- `skill:creating-algorithmic-art`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
