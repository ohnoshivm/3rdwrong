---
title: Design Handoff
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design:design-handoff
department: design
sub_department: identity-craft
job: handover-specs
role: lead
trigger: ""
kind: plugin-skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/afe29730-8d0c-470c-801a-a52a510c0510/skills/design-handoff/SKILL.md
invoke: "Skill name: design:design-handoff"
pairs_with: [agency:engineering-technical-writer, design-steward:brief, figma:figma-spec]
---
# Design Handoff

The Design Handoff is 3RDWRONG’s lead for handover specifications.

## What it does

- Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component props, interaction states, responsive breakpoints, edge cases, and animation details.
- Exact measurements (padding, margins, widths).
- Design token references (colors, typography, spacing).
- Responsive breakpoints and behavior.

## When to use

- Phase 06 Handoff, when the approved direction and the source artefact are ready for handover specs.
- Use it to lead this job; keep the founder’s decision and an independent check separate from its output.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `agency:engineering-technical-writer` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Collect the approved design artefact, implementation constraints and known decisions.
2. Create the scoped handoff with explicit acceptance criteria and evidence locations.
3. Return open decisions and route implementation questions to the named owner.

```text
Load skill `design:design-handoff`. Approved direction: {{link and status}}. Job: handover-specs. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `agency:engineering-technical-writer` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `design-steward:brief` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `figma:figma-spec` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is manual; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
