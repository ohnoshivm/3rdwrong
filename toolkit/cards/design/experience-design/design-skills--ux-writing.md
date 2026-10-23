---
title: UX Writing
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-skills:ux-writing
department: design
sub_department: experience-design
job: ux-writing
role: lead
trigger: ""
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-skills-marketplace/skills/ux-writing
invoke: "ux-writing skill (Claude Code plugin `design-skills`)"
pairs_with: [design:ux-copy, vectorlab-ux-skills:verbs, vectorlab-ux-skills:errors]
---
# UX Writing

The experience-design lead for `ux-writing` is UX Writing, which leads consistent, clear and accessible microcopy across an approved interface.

## What it does

- Applies purposeful, concise, conversational and clear standards.
- covers actions, errors, success, empty states, forms and notifications.
- sets voice and tone guidance.

## When to use

- Use when an approved interface needs a consistent microcopy specification across component states. Use Phase 05 Prototype, before strings are frozen for implementation.

## When not to use

- Use `design:ux-copy` for a bounded touchpoint, or `vectorlab-ux-skills:errors` for failure-state recovery copy.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved strategy and product voice, user goal, UI states, character/platform limits and terminology.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ux-writing skill (Claude Code plugin `design-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce each state has concise, accurate copy, clear action and consistent terminology; uncertainty is flagged. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A component-state copy specification with terminology, variants and rationale.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design:ux-copy`, `vectorlab-ux-skills:verbs`, `vectorlab-ux-skills:errors`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Copy quality guidance is not audience research. Do not invent product behaviour or claim comprehension without testing.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
