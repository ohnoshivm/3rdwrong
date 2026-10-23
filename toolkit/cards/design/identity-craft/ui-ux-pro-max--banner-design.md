---
title: Banner Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: ui-ux-pro-max:banner-design
department: design
sub_department: identity-craft
job: composition-layout
role: specialist
trigger: "An explicitly agreed identity application needs a banner composition at specified dimensions."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-ui-ux-pro-max-skill-ui-ux-pro-max-2.13.0/.claude/skills/banner-design/SKILL.md
invoke: "Skill name: ui-ux-pro-max:banner-design"
pairs_with: [design-skills:design-elevation, figma:figma-create-new-file, figma:figma-use]
---
# Banner Design

The Banner Design is a specialist for composition and layout in 3RDWRONG’s identity-craft work.

## What it does

- Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. Actions: design, create, generate banner. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, website hero, print. Styles: minimalist, gradient, bold typography, photo-based, illustrated, geometric, retro, glassmorphism, 3D, neon, duotone, editorial, collage.
- User requests banner, cover, or header design.
- Social media cover/header creation.
- Ad banner or display ad design.

## When to use

- An explicitly agreed identity application needs a banner composition at specified dimensions.
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
Load skill `ui-ux-pro-max:banner-design`. Approved direction: {{link and status}}. Job: composition-layout. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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
