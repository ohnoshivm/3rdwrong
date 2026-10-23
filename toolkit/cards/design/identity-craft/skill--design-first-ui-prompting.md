---
title: Design First UI Prompting
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:design-first-ui-prompting
department: design
sub_department: identity-craft
job: handover-specs
role: specialist
trigger: "When the approved scope specifically requires writing a design-first prompt for a UI generation workflow."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/design-first-ui-prompting/SKILL.md
invoke: "Skill name: skill:design-first-ui-prompting"
pairs_with: [design:design-handoff, agency:engineering-technical-writer, design-steward:brief]
---
# Design First UI Prompting

The Design First UI Prompting is a specialist for handover specifications in 3RDWRONG’s identity-craft work.

## What it does

- Use when you need design-first, spec-driven, skimmable prompts for UI generation. Covers prompt structure, constraints, variations, typography/spacing rules, and iteration workflow for consistent UI outputs.
- What are we making? (e.g., landing page hero / onboarding / dashboard / carousel slide).
- What’s the success criteria? (clarity, conversion, vibe).
- Size/aspect: (e.g., 1080x1350).

## When to use

- When the approved scope specifically requires writing a design-first prompt for a UI generation workflow.
- In practice: use it at Phase 06 Handoff when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `design:design-handoff` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Collect the approved design artefact, implementation constraints and known decisions.
2. Create the scoped handoff with explicit acceptance criteria and evidence locations.
3. Return open decisions and route implementation questions to the named owner.

```text
Load skill `skill:design-first-ui-prompting`. Approved direction: {{link and status}}. Job: handover-specs. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `design:design-handoff` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:engineering-technical-writer` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `design-steward:brief` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- Distribution is fetch; confirm installation, sign-in and applicable licence limits before use.
- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
