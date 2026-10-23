---
title: Forms
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:forms
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "An approved form needs field reduction or blur-validation behaviour."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/interaction/forms
invoke: "forms skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [vectorlab-ux-skills:labels, vectorlab-ux-skills:defaults, vectorlab-ux-skills:errors]
---
# Forms

The experience-design specialist for `interaction-architecture` is Forms (trigger: “An approved form needs field reduction or blur-validation behaviour”), which reduces form friction with fewer fields, blur-first validation and an actionable submit path.

## What it does

- Promotes field reduction.
- validates on blur and clears corrected errors.
- avoids dead disabled-submit states.

## When to use

- Use when an approved form needs field reduction or blur-validation behaviour. Use Phase 05 Prototype before implementation.
- An approved form needs field reduction or blur-validation behaviour.

## When not to use

- Use `vectorlab-ux-skills:labels` for persistent labels and `vectorlab-ux-skills:defaults` for justified prefilled values.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved form goal, fields, validation rules, submission behaviour and privacy constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use forms skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce every field is necessary and labelled; errors appear at an appropriate time and clear after correction. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A form specification with field rationale, validation timing and correction path.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `vectorlab-ux-skills:labels`, `vectorlab-ux-skills:defaults`, `vectorlab-ux-skills:errors`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not make submission inaccessible via a disabled control with no explanation; check keyboard and screen-reader behaviour.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
