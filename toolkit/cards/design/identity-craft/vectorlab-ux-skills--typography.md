---
title: Typography
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:typography
department: design
sub_department: identity-craft
job: typography
role: specialist
trigger: "A supplied digital type hierarchy has a scale, weight or line-height defect."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/visual-taste/typography/SKILL.md
invoke: "Skill name: vectorlab-ux-skills:typography"
pairs_with: [agent:visual-designer]
---
# Typography

The Typography is a specialist for typography in 3RDWRONG’s identity-craft work.

## What it does

- Defines typographic scales, weight limits, and line-height pairing. Use when setting type styles, headings, body copy sizes, or fixing noisy type hierarchies.
- One typeface family for UI; a second only for marketing/display if the profile allows it.
- Create hierarchy with at most 4–5 distinct sizes on one screen (meta, secondary, body, subheading, heading).
- Prefer medium (500) for interactive labels and semibold (600) for page titles — not bold (700).

## When to use

- A supplied digital type hierarchy has a scale, weight or line-height defect.
- In practice: use it at Phase 03 Design System when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `agent:visual-designer` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Check the approved brief, source artefact and required prerequisites; record missing inputs.
2. Invoke the tool with the bounded request and supplied constraints.
3. Return its documented deliverable with evidence, unresolved points and a named next owner for independent review.

```text
Load skill `vectorlab-ux-skills:typography`. Approved direction: {{link and status}}. Job: typography. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `agent:visual-designer` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
