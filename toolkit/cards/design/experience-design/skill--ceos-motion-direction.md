---
title: Motion Direction
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-motion-direction
department: design
sub_department: experience-design
job: motion-principles
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-motion-direction
invoke: "ceos-motion-direction skill"
pairs_with: [skill:ceos-interaction-architecture, skill:animate, vectorlab-ux-skills:motion]
---
# Motion Direction

The experience-design lead for `motion-principles` is Motion Direction, which purpose, tokens, choreography, implementation approach and reduced-motion alternative.

## What it does

- Chooses CSS, WAAPI, GSAP, Motion or Lenis by task.
- defines reusable timing/easing and scene choreography.
- addresses cleanup, interruption and performance verification.

## When to use

- Use for Phase 05 Motion when a site needs coordinated motion direction, a motion spec, or diagnosis of jank.

## When not to use

- Use `skill:ceos-interaction-architecture` to define the interaction model first; use `skill:animate` for a bounded interaction.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved concept, interaction inventory, target platform, motion goal, reduced-motion and performance constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ceos-motion-direction skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce every move has purpose; one scroll engine; content works without motion/js; verification is planned. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A coherent motion specification with triggers, timings, easing, interruption, reduced-motion and performance notes.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-interaction-architecture`, `skill:animate`, `vectorlab-ux-skills:motion`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Motion only when concept needs it. Honour reduced motion, keyboard/touch and cleanup; validate performance rather than assuming it.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
