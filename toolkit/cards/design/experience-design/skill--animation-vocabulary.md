---
title: Animation Vocabulary
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:animation-vocabulary
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "When defining motion purpose, timing, easing, choreography, and reduced-motion behavior."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/animation-vocabulary
invoke: "animation-vocabulary skill"
pairs_with: [skill:ceos-motion-direction, skill:improve-animations]
---
# Animation Vocabulary

The experience-design specialist for `motion-principles` is Animation Vocabulary (trigger: “When defining motion purpose, timing, easing, choreography, and reduced-motion behavior”), which provides a shared vocabulary for describing animation and communicating motion decisions.

## What it does

- Maps a vague motion description to a precise term in its glossary.
- Disambiguates close terms and offers one or two alternatives when useful.
- Stays within the glossary and says when no exact term matches.

## When to use

- Use when defining motion purpose, timing, easing, choreography, and reduced-motion behavior, especially when a team lacks shared terms.
- When defining motion purpose, timing, easing, choreography, and reduced-motion behavior.

## When not to use

- Use `skill:ceos-motion-direction` to turn vocabulary into a system or `skill:improve-animations` to revise existing motion.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Motion examples or target interaction, audience/team and desired communication context.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use animation-vocabulary skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce terms are used consistently and each maps to an observable movement rather than subjective praise. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A small glossary or annotated motion description that collaborators can use consistently.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-motion-direction`, `skill:improve-animations`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Vocabulary does not itself specify implementation, usability or accessibility; translate terms into measurable behaviours.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
