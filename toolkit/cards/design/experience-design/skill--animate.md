---
title: Animate
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:animate
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "When defining motion purpose, timing, easing, choreography, and reduced-motion behavior."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/animate
invoke: "animate skill"
pairs_with: [skill:ceos-motion-direction, vectorlab-ux-skills:motion]
---
# Animate

The experience-design specialist for `motion-principles` is Animate (trigger: “When defining motion purpose, timing, easing, choreography, and reduced-motion behavior”), which guides purposeful interface animation with specific motion patterns and implementation considerations.

## What it does

- Reviews animation purpose and user feedback.
- helps select motion approach.
- includes reduced-motion handling and performance considerations.

## When to use

- Use when defining motion purpose, timing, easing, choreography, and reduced-motion behavior. Use Phase 05 Motion before implementation.
- When defining motion purpose, timing, easing, choreography, and reduced-motion behavior.

## When not to use

- Use `skill:ceos-motion-direction` for a full motion system, or `vectorlab-ux-skills:motion` for duration/easing tokens.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Interaction trigger, purpose, affected elements, platform and reduced-motion requirements.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use animate skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce motion clarifies hierarchy, continuity or feedback; reduced-motion path preserves meaning. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A short motion spec tied to a state change, trigger and fallback.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-motion-direction`, `vectorlab-ux-skills:motion`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Keep motion proportional to the concept; accessibility and browser performance still need review.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
