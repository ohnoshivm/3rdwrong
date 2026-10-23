---
title: Design Elevation
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-skills:design-elevation
department: design
sub_department: identity-craft
job: composition-layout
role: specialist
trigger: "The concept is already approved and a bounded artefact needs formal hierarchy and craft refinement."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-skills-marketplace/skills/design-elevation/SKILL.md
invoke: "Skill name: design-skills:design-elevation"
pairs_with: [figma:figma-create-new-file, figma:figma-use, mcp:stitch]
---
# Design Elevation

The Design Elevation is a specialist for composition and layout in 3RDWRONG’s identity-craft work.

## What it does

- Comprehensive design elevation system that automatically transforms functional visual outputs into polished, professional designs. Use when creating ANY visual output including presentations (pptx), spreadsheets (xlsx), dashboards, reports, HTML artifacts, PDFs, web pages, or data visualizations. Applies systematic design thinking grounded in Tailwind CSS as the canonical design token system. Structures decisions through functional patterns (what users interact with) and perceptual patterns (how the design feels), following Alla Kholmatova's design systems framework. Triggers on ALL requests for visual content creation, ensuring outputs look hand-crafted rather than template-based.
- Colors from Tailwind's palette (gray, blue, emerald, amber, rose, violet, etc.).
- Spacing from Tailwind's scale (1 = 0.25rem/4px, 2 = 0.5rem/8px, 4 = 1rem/16px, etc.).
- Typography from Tailwind's type scale (text-xs through text-9xl).

## When to use

- The concept is already approved and a bounded artefact needs formal hierarchy and craft refinement.
- In practice: use it at Phase 04 Concept or Phase 05 Application when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `figma:figma-create-new-file` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.

## How to run it

1. Check the approved brief, source artefact and required prerequisites; record missing inputs.
2. Invoke the tool with the bounded request and supplied constraints.
3. Return its documented deliverable with evidence, unresolved points and a named next owner for independent review.

```text
Load skill `design-skills:design-elevation`. Approved direction: {{link and status}}. Job: composition-layout. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `figma:figma-create-new-file` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `figma:figma-use` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `mcp:stitch` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
