---
title: Empty States
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:empty-states
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A defined empty or filtered-zero state needs a next action."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/feedback/empty-states
invoke: "empty-states skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [design-skills:ux-writing, vectorlab-ux-skills:errors]
---
# Empty States

The experience-design specialist for `interaction-architecture` is Empty States (trigger: “A defined empty or filtered-zero state needs a next action”), which designs actionable empty and filtered-zero states with a clear next action.

## What it does

- Explains what belongs in the space and why.
- distinguishes first-use, cleared and filtered-zero cases.
- helps a user recover from no results.

## When to use

- Use when a defined empty or filtered-zero state needs a next action. Use Phase 05 Prototype when specifying empty, first-use or no-results states.
- A defined empty or filtered-zero state needs a next action.

## When not to use

- Use `design-skills:ux-writing` for a broader copy system or `vectorlab-ux-skills:errors` for failures.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Exact empty condition, user goal, product capability, tone and next action.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use empty-states skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce the state explains the absence without blame and gives an appropriate action; filtered-zero offers a way back. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- State-specific copy and one relevant action for each empty condition.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design-skills:ux-writing`, `vectorlab-ux-skills:errors`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not use decorative illustration as a substitute for direction; confirm project voice and accessibility profile.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
