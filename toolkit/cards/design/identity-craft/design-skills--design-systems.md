---
title: Design Systems
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-skills:design-systems
department: design
sub_department: identity-craft
job: design-system-guidelines
role: lead
trigger: ""
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-skills-marketplace/skills/design-systems/SKILL.md
invoke: "Skill name: design-skills:design-systems"
pairs_with: [agency:design-brand-guardian, design-steward:align, design-steward:canon-update]
---
# Design Systems

The Design Systems is 3RDWRONG’s lead for design-system-guidelines.

## What it does

- Build, document, and maintain design systems with design tokens, component specifications, pattern libraries, naming conventions, and governance processes. Conduct system audits, define component hierarchies, and establish shared design languages.
- More than 3 designers or 5 developers touching the same product.
- Visual audit reveals 10+ button styles, 5+ type scales, or 3+ modal implementations.
- New features take longer because teams reinvent existing patterns.

## When to use

- Phase 03 Design System, when the approved direction and the source artefact are ready for design system guidelines.
- Use it to lead this job; keep the founder’s decision and an independent check separate from its output.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For work outside this scope, route to `agency:design-brand-guardian` for its related operation; do not use this tool as a general-purpose design lead.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- Existing system, tokens or component files, plus the authority for changes.

## How to run it

1. Inspect the existing DESIGN.md, tokens, components or system context before proposing changes.
2. Run the scoped system operation in the existing design authority and preserve declared exceptions.
3. Return the diff or findings, unresolved decisions and owner for independent review.

```text
Load skill `design-skills:design-systems`. Approved direction: {{link and status}}. Job: design-system-guidelines. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
```

## What good output looks like

- It addresses the bounded request and names its source artefacts.
- Documented facts, interpretation, hypotheses and unknowns are separated.
- A next owner can act on the deliverable without mistaking it for approval.

## Quality checks

- [ ] An independent reviewer checks the result against the supplied brief and actual artefact.
- [ ] Source-backed claims are distinguishable from Interpretation, Hypothesis and Unknown.
- [ ] The handoff names open issues and next owner; no tool output is treated as approval.
- [ ] Existing tokens, component states and declared exceptions are respected or gaps are recorded.

## Pairs with

- `agency:design-brand-guardian` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `design-steward:align` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `design-steward:canon-update` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
