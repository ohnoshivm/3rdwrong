---
title: Taste Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: stitch-utilities:taste-design
department: design
sub_department: identity-craft
job: composition-layout
role: specialist
trigger: "An approved Stitch project needs a restrained semantic design-system prompt; its preset aesthetics remain subordinate to the concept."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-google-labs-code-stitch-skills-stitch-utilities-0337446dadde/skills/taste-design/SKILL.md
invoke: "Skill name: stitch-utilities:taste-design"
pairs_with: [design-skills:design-elevation, figma:figma-create-new-file, figma:figma-use]
---
# Taste Design

The Taste Design is a specialist for composition and layout in 3RDWRONG’s identity-craft work.

## What it does

- Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance.
- Access to Google Stitch via [labs.google.com/stitch](https://labs.google.com/stitch).
- Optionally: Stitch MCP Server for programmatic integration with Cursor, Antigravity, or Gemini CLI.
- **Density:** "Art Gallery Airy" (1–3) → "Daily App Balanced" (4–7) → "Cockpit Dense" (8–10).

## When to use

- An approved Stitch project needs a restrained semantic design-system prompt; its preset aesthetics remain subordinate to the concept.
- In practice: use it at Phase 04 Concept or Phase 05 Application when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `design-skills:design-elevation` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Check the approved brief, source artefact and required prerequisites; record missing inputs.
2. Invoke the tool with the bounded request and supplied constraints.
3. Return its documented deliverable with evidence, unresolved points and a named next owner for independent review.

```text
Load skill `stitch-utilities:taste-design`. Approved direction: {{link and status}}. Job: composition-layout. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `design-skills:design-elevation` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `figma:figma-create-new-file` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `figma:figma-use` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
