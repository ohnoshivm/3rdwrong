---
title: Visual Designer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:visual-designer
department: design
sub_department: identity-craft
job: typography
role: lead
trigger: ""
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/visual-designer.md
invoke: "Agent tool: visual-designer"
pairs_with: [vectorlab-ux-skills:typography]
---
# Visual Designer

The Visual Designer is 3RDWRONG’s lead for typography.

## What it does

- Executes typography, colour, spacing, grids and surface detail as a tokenised visual system and polishes it to standard.
- Its documented workflow includes: One token source of truth: spacing scale, type scale, colour roles, radii, shadows, borders, motion durations — names and values.
- Its documented workflow includes: A type ramp giving exact size, line height, letter spacing, weight and measure limit per role.

## When to use

- Phase 03 Design System, when the approved direction and the source artefact are ready for typography.
- Use it to lead this job; keep the founder’s decision and an independent check separate from its output.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `vectorlab-ux-skills:typography` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Check the approved brief, source artefact and required prerequisites; record missing inputs.
2. Invoke the tool with the bounded request and supplied constraints.
3. Return its documented deliverable with evidence, unresolved points and a named next owner for independent review.

```text
Call the Agent tool `visual-designer`. Approved direction: {{link and status}}. Job: typography. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `vectorlab-ux-skills:typography` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
