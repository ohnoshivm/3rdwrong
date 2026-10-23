---
title: Frontend Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: frontend-design:frontend-design
department: design
sub_department: experience-design
job: ui-design
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-frontend-design-a0b04d9ddcca/skills/frontend-design
invoke: "frontend-design skill"
pairs_with: [skill:designing-frontend-interfaces, skill:designing-user-experience, skill:ceos-motion-direction]
---
# Frontend Design

The experience-design lead for `ui-design` is Frontend Design, which leads distinctive visual design for new or reshaped interfaces, grounded in the specific subject and brief.

## What it does

- Establishes a compact token system.
- plans palette, type and layout before code.
- checks for generic defaults and self-critiques rendered work.

## When to use

- Use for Phase 04 Concept / Phase 05 Prototype when choosing distinctive digital visual direction before implementation.

## When not to use

- Use `skill:designing-user-experience` for flows and non-trivial state, and `building-accessible-interfaces` before shipping.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Subject, audience, interface goal, constraints, brand/strategy, content and real references.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use frontend-design skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce design decisions trace to the brief; one intentional memorable feature; responsive, keyboard, reduced-motion and visual checks are covered. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A brief-specific art direction and token block, then a refined interface that has been visually inspected.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-frontend-interfaces`, `skill:designing-user-experience`, `skill:ceos-motion-direction`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Avoid generic templates and rejected own-identity look (D-0006). References inspire only; inspect actual renders. The source provides process guidance, not proof of quality.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
