---
title: DS Make
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-superpowers:ds-make
department: design
sub_department: identity-craft
job: design-system-guidelines
role: specialist
trigger: "A specified enterprise token, component or pattern needs creation or a versioned change."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-superpowers-marketplace/skills/ds-make/SKILL.md
invoke: "Skill name: design-superpowers:ds-make"
pairs_with: [design-skills:design-systems, agency:design-brand-guardian, design-steward:align]
---
# DS Make

The DS Make is a specialist for design system guidelines in 3RDWRONG’s identity-craft work.

## What it does

- Use when creating, updating, versioning, or deprecating design system tokens, components, or patterns. Activates for /ds-make, "new component", "add token", "create a variant", "update a component", "bump version", "deprecate X", "semver", "scaffold design system", "token naming", "breaking change".
- **L0 (Greenfield):** Scaffold a new DS from scratch. A DESIGN.md gives the richest input, but its absence is **not a hard gate** — judge by the request:.
- **L2 (DS exists):** Extend the existing DS. Load `.ds-context.md` for library keys and token collections before acting.
- `${CLAUDE_PLUGIN_ROOT}/skills/shared/knowledge/core-principles.md` (L1 — always).

## When to use

- A specified enterprise token, component or pattern needs creation or a versioned change.
- In practice: use it at Phase 03 Design System when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `design-skills:design-systems` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- Existing system, tokens or component files, plus the authority for changes.

## How to run it

1. Inspect the existing DESIGN.md, tokens, components or system context before proposing changes.
2. Run the scoped system operation in the existing design authority and preserve declared exceptions.
3. Return the diff or findings, unresolved decisions and owner for independent review.

```text
Load skill `design-superpowers:ds-make`. Approved direction: {{link and status}}. Job: design-system-guidelines. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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

- `design-skills:design-systems` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:design-brand-guardian` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `design-steward:align` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
