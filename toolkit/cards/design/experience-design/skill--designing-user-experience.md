---
title: Designing User Experience
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:designing-user-experience
department: design
sub_department: experience-design
job: interaction-architecture
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/designing-user-experience/SKILL.md
invoke: "designing-user-experience skill"
pairs_with: [skill:ceos-interaction-architecture, skill:double-diamond, agent:ui-ux-architect]
---
# Designing User Experience

The experience-design lead for `interaction-architecture` is Designing User Experience, which leads user-centred product experience work from problem framing through flows, interaction and usability evaluation.

## What it does

- Structures discovery and definition.
- maps user journeys and information.
- designs interaction and feedback.
- proposes prototypes and validation.

## When to use

- Use as lead for Phase 02 Discovery / Phase 04 Concept when the experience problem, journey or interaction model needs definition.

## When not to use

- Use `skill:ceos-interaction-architecture` for detailed website input/focus/state specifications and `skill:double-diamond` for a staged project process.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved strategy and goals, known research, audience/context, constraints, content and decision owner.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use designing-user-experience skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce user needs and assumptions are separated; journeys reach the goal; critical states and validation are explicit. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A traceable UX brief with journeys, interaction decisions, prototype question and validation plan.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-interaction-architecture`, `skill:double-diamond`, `agent:ui-ux-architect`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not invent research or user findings. Mark assumptions and use real research for audience claims; maker and checker remain separate.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
