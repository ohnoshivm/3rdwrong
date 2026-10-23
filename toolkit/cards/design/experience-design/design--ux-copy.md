---
title: UX Copy
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design:ux-copy
department: design
sub_department: experience-design
job: ux-writing
role: specialist
trigger: "An approved digital touchpoint needs labels, errors, empty states or recovery copy."
kind: plugin-skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/afe29730-8d0c-470c-801a-a52a510c0510/skills/ux-copy/SKILL.md
invoke: "/ux-copy"
pairs_with: [design-skills:ux-writing, vectorlab-ux-skills:errors, vectorlab-ux-skills:verbs]
---
# UX Copy

The experience-design specialist for `ux-writing` is UX Copy (trigger: “An approved digital touchpoint needs labels, errors, empty states or recovery copy”), which writes or reviews bounded interface copy for a specific digital touchpoint.

## What it does

- Requests screen/flow context, user state, tone and constraints.
- checks clarity and action labels.
- covers errors, empty states, confirmations, tooltips, loading and onboarding.

## When to use

- Use when an approved digital touchpoint needs labels, errors, empty states or recovery copy. Use Phase 05 Prototype while the component states are being designed.
- An approved digital touchpoint needs labels, errors, empty states or recovery copy.

## When not to use

- Use `design-skills:ux-writing` to set a cross-interface microcopy system.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Screen or flow, user intent/state, approved tone, exact behaviour and length constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use /ux-copy. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce strings explain what happens and what to do next; no unsupported behaviour or vague failure copy. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A focused set of interface strings with context and recovery action.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design-skills:ux-writing`, `vectorlab-ux-skills:errors`, `vectorlab-ux-skills:verbs`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Use the `/ux-copy` command only in its Claude plugin context. Plugin access/sign-in may be required; do not put client data in public files.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
