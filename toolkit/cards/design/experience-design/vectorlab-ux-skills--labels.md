---
title: Visible Form Labels
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:labels
department: design
sub_department: experience-design
job: ux-writing
role: specialist
trigger: "A supplied form is missing persistent visible labels."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/voice/labels
invoke: "labels skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [vectorlab-ux-skills:forms, design-skills:ux-writing]
---
# Visible Form Labels

The experience-design specialist for `ux-writing` is Visible Form Labels (trigger: “A supplied form is missing persistent visible labels”), which ensures every form input has a persistent visible label.

## What it does

- Separates field labels from placeholders.
- keeps labels present on focus.
- checks accessible input naming.

## When to use

- Use when a supplied form is missing persistent visible labels. Use Phase 05 Prototype before handoff.
- A supplied form is missing persistent visible labels.

## When not to use

- Use `vectorlab-ux-skills:forms` for the full form and validation pattern.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Form fields, data requested, format hints, existing voice and layout.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use labels skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce every input has a visible persistent label; placeholders only give format examples. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A field-to-label specification with format hints separated from names.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `vectorlab-ux-skills:forms`, `design-skills:ux-writing`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Check actual programmatic label association and focus; visual text alone does not prove screen-reader accessibility.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
