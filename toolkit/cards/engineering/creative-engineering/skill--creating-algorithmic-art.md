---
title: Creating Algorithmic Art
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:creating-algorithmic-art
department: engineering
sub_department: creative-engineering
job: generative-creative-coding
role: specialist
trigger: "When the approved scope specifically requires creating original procedural or generative visual systems."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/creating-algorithmic-art/SKILL.md
invoke: "creating-algorithmic-art skill"
pairs_with: [figma:figma-generative-plugins, skill:ceos-creative-coding, skill:pointer-trail-emitter]
---
# Creating Algorithmic Art

Creating Algorithmic Art is the specialist when When the approved scope specifically requires creating original procedural or generative visual systems. at 3RDWRONG.

## What it does

- Use when creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Triggers include requests for generative art, algorithmic art, flow fields, particle systems, or any art created through code. Always create original algorithmic art — never copy existing artists' work to avoid copyright violations
- Organises the method around algorithmic philosophy creation
- Computational processes, emergent behavior, mathematical beauty
- Seeded randomness, noise fields, organic systems
- Particles, flows, fields, forces

## When to use

- When the approved scope specifically requires creating original procedural or generative visual systems.

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
2. Provide the inputs and constraints above; load or invoke `skill:creating-algorithmic-art`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:creating-algorithmic-art for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
- `skill:pointer-trail-emitter`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
