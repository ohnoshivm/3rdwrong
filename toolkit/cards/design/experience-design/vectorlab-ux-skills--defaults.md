---
title: Interaction Defaults
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:defaults
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A defined form or preferences flow needs useful defaults or draft persistence."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/interaction/defaults
invoke: "defaults skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [vectorlab-ux-skills:forms, vectorlab-ux-skills:labels]
---
# Interaction Defaults

The experience-design specialist for `interaction-architecture` is Interaction Defaults (trigger: “A defined form or preferences flow needs useful defaults or draft persistence”), which reduces repetitive form work with useful inferred defaults and protects drafts across navigation.

## What it does

- Recommends defaults from known context.
- covers draft persistence.
- avoids blank dropdowns when a justified default exists.

## When to use

- Use when a defined form or preferences flow needs useful defaults or draft persistence. Use Phase 05 Prototype while form behaviour is specified.
- A defined form or preferences flow needs useful defaults or draft persistence.

## When not to use

- Use `vectorlab-ux-skills:forms` for validation and field reduction.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Defined form/preferences flow, known reliable context, persistence boundaries and privacy requirements.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use defaults skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce defaults are explainable and editable; drafts survive the intended navigation without exposing private data. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A defined default and persistence rule with an explicit override and recovery path.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `vectorlab-ux-skills:forms`, `vectorlab-ux-skills:labels`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not infer sensitive preferences or silently commit an action. Confirm the project UX profile before changing an existing surface.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
