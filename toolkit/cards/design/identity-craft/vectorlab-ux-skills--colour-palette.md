---
title: Colour Palette
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:colour-palette
department: design
sub_department: identity-craft
job: colour
role: specialist
trigger: "A digital palette needs role/distribution checks after the human colour direction is approved."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/visual-taste/colour-palette/SKILL.md
invoke: "Skill name: vectorlab-ux-skills:colour-palette"
pairs_with: [design-skills:design-systems]
---
# Colour Palette

The Colour Palette is a specialist for colour in 3RDWRONG’s identity-craft work.

## What it does

- Applies 60-30-10 colour distribution and elevation via borders then soft shadows. Use when choosing surfaces, accents, borders, shadows, or dark-mode depth.
- reference/elevation-tokens.md.
- **A list, table, or board is an L1 surface.** It must have a 1px subtle border, **or** a one-step background shift **and** hairline row/column dividers. A table of text on L0 canvas is a fail.
- **“Borders rare” / paper profiles still require hairlines on lists.** Stripping decorative card chrome is fine. Stripping the table frame is not.

## When to use

- A digital palette needs role/distribution checks after the human colour direction is approved.
- In practice: use it at Phase 03 Design System when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this job, route to the relevant design lead and keep this tool within the registered scope.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Check the approved brief, source artefact and required prerequisites; record missing inputs.
2. Invoke the tool with the bounded request and supplied constraints.
3. Return its documented deliverable with evidence, unresolved points and a named next owner for independent review.

```text
Load skill `vectorlab-ux-skills:colour-palette`. Approved direction: {{link and status}}. Job: colour. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
```

## What good output looks like

- It addresses the bounded request and names its source artefacts.
- Documented facts, interpretation, hypotheses and unknowns are separated.
- A next owner can act on the deliverable without mistaking it for approval.

## Quality checks

- [ ] An independent reviewer checks the result against the supplied brief and actual artefact.
- [ ] Source-backed claims are distinguishable from Interpretation, Hypothesis and Unknown.
- [ ] The handoff names open issues and next owner; no tool output is treated as approval.

## Pairs with

- `design-skills:design-systems` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
