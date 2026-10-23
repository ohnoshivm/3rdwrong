---
title: Verb-First Actions
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:verbs
department: design
sub_department: experience-design
job: ux-writing
role: specialist
trigger: "An approved interface needs verb-first action labels."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/voice/verbs
invoke: "verbs skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [design-skills:ux-writing, design:ux-copy]
---
# Verb-First Actions

The experience-design specialist for `ux-writing` is Verb-First Actions (trigger: “An approved interface needs verb-first action labels”), which makes buttons and action links state clearly what activation will do.

## What it does

- Uses strong imperative verbs.
- avoids vague labels such as OK, Submit and Proceed.
- keeps action names consistent across a flow.

## When to use

- Use when an approved interface needs verb-first action labels. Use Phase 05 Prototype during microcopy review.
- An approved interface needs verb-first action labels.

## When not to use

- Use `design-skills:ux-writing` for broader copy rules or `design:ux-copy` for a single touchpoint.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Action outcomes, interface context, approved terminology and character limits.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use verbs skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce each label starts with a clear action and accurately predicts the result. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A set of action labels mapped to the result each action causes.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design-skills:ux-writing`, `design:ux-copy`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Never use a clearer verb to disguise an irreversible action; label the consequence and require confirmation where needed.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
