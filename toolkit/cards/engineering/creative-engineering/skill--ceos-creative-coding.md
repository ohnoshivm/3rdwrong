---
title: Ceos Creative Coding
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-creative-coding
department: engineering
sub_department: creative-engineering
job: generative-creative-coding
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-creative-coding
invoke: "ceos-creative-coding skill"
pairs_with: [figma:figma-generative-plugins, skill:creating-algorithmic-art, skill:pointer-trail-emitter]
---
# Ceos Creative Coding

Ceos Creative Coding is the lead for generative creative coding at 3RDWRONG.

## What it does

- Invents original procedural and generative visuals for the web with Canvas 2D, SVG and WebGL — noise fields, flow fields, particle systems, physics and springs, computational geometry, procedural shapes and organic animation — designed as art-directed systems, not pasted demos. Use when a site needs a custom generative background, interactive sketch, data-driven or organic visual, particle effect, procedural illustration, or when exploring a new visual technique
- Organises the method around purpose
- Organises the method around expert knowledge to apply
- Systems thinking: a generative piece = elements + rules + parameters + randomness + time + input. Expose
- Noise: value/gradient (Perlin/simplex) noise for organic variation; fractal Brownian motion (sum of octaves)

## When to use

- Phase 03 Architecture or Phase 04 Concept when the approved brief requires generative creative coding.
- Establish the method and handoff before implementation begins.

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
2. Provide the inputs and constraints above; load or invoke `skill:ceos-creative-coding`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:ceos-creative-coding for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
- `skill:creating-algorithmic-art`: coordinate inputs and hand off the reviewed result.
- `skill:pointer-trail-emitter`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
