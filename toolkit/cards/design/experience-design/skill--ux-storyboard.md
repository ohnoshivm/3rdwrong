---
title: UX Storyboard
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ux-storyboard
department: design
sub_department: experience-design
job: experience-prototyping
role: specialist
trigger: "When the approved scope specifically requires representing user needs, journeys, or experience narratives."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/ux-storyboard/SKILL.md
invoke: "ux-storyboard skill"
pairs_with: [skill:designing-user-experience, skill:double-diamond, figma:video-interaction-mapper]
---
# UX Storyboard

The experience-design specialist for `experience-prototyping` is UX Storyboard (trigger: “When the approved scope specifically requires representing user needs, journeys, or experience narratives”), which creates a visual sequence that communicates a user scenario and experience over time.

## What it does

- Defines a scenario/persona, visual panels and captions.
- supports creation from research, a journey map or a new concept.
- distinguishes storyboards from journey maps.

## When to use

- Use when the approved scope specifically requires representing user needs, journeys, or experience narratives. Use Phase 03 Definition to make a proposed experience concrete.
- When the approved scope specifically requires representing user needs, journeys, or experience narratives.

## When not to use

- Use `figma:video-interaction-mapper` when a supplied recording needs extraction; use `skill:designing-user-experience` for a validated journey.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved user evidence or explicitly hypothetical persona, scenario, goal, sequence and audience for the storyboard.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ux-storyboard skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce the story is understandable without visuals; panels show actions and consequences; source vs hypothesis is clear. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A sequence with context, user actions and experience changes, with invented details labelled.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `skill:double-diamond`, `figma:video-interaction-mapper`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not invent research findings. Clearly label fictional scenarios and keep client-identifying information out of the public repo.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
