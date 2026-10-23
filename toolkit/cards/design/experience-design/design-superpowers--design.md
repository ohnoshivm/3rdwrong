---
title: Design with an Existing System
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-superpowers:design
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "An existing design system must be used to design a new scoped screen or flow."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-superpowers-marketplace/skills/design
invoke: "/design"
pairs_with: [frontend-design:frontend-design, vectorlab-ux-skills:page-patterns]
---
# Design with an Existing System

The experience-design specialist for `ui-design` is Design with an Existing System (trigger: “An existing design system must be used to design a new scoped screen or flow”), which routes a scoped feature or screen through an existing design system and its component patterns.

## What it does

- Detects design-system maturity.
- uses existing components and patterns.
- routes component selection and layout composition.

## When to use

- Use when an existing design system must be used to design a new scoped screen or flow. Use Phase 05 Prototype after confirming the system is the approved one.
- An existing design system must be used to design a new scoped screen or flow.

## When not to use

- Use `frontend-design:frontend-design` when the work needs original visual direction rather than system composition.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved screen goal, existing design-system docs/components, flow and content.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use /design. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce named components and variants map to the screen requirements; alternatives and system gaps are explicit. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A screen/flow composition using named existing system components, or an explicit gap list.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `frontend-design:frontend-design`, `vectorlab-ux-skills:page-patterns`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- The source describes a router and asks first in some flows; follow its maturity detection and do not invent components or system rules.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
