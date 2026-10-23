---
title: Improve Animations
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:improve-animations
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/improve-animations
invoke: "improve-animations skill"
pairs_with: [skill:ceos-motion-direction, skill:find-animation-opportunities]
---
# Improve Animations

The experience-design specialist for `motion-principles` is Improve Animations (trigger: “When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference”), which reviews existing animation and proposes focused changes to make it clearer and more coherent.

## What it does

- Inspects an existing animation.
- diagnoses timing, easing or pattern problems.
- proposes improvements grounded in the supplied example.

## When to use

- Use when identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference. Use Phase 07 Validation on an existing motion implementation.
- When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference.

## When not to use

- Use `skill:ceos-motion-direction` for system-level direction or `skill:vectorlab-ux-skills:motion` for token consistency.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Existing animation or recording, desired communication, interaction context and reduced-motion setting.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use improve-animations skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce recommendations fix an observed issue, preserve user intent and avoid ornamental movement. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A before/after motion recommendation with rationale and reduced-motion consideration.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-motion-direction`, `skill:find-animation-opportunities`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not claim smoothness/performance without measurement; inspect reduced-motion and keyboard/touch operation.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
