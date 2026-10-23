---
title: Double Diamond
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:double-diamond
department: design
sub_department: experience-design
job: experience-prototyping
role: lead
trigger: ""
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/double-diamond/SKILL.md
invoke: "double-diamond skill"
pairs_with: [skill:designing-user-experience, skill:ux-storyboard]
---
# Double Diamond

The experience-design lead for `experience-prototyping` is Double Diamond, which leads a staged experience-prototyping process that moves from discovery and definition into development and delivery.

## What it does

- Frames four divergent/convergent phases.
- supports problem definition before solution development.
- connects prototypes to validation and delivery.

## When to use

- Use as lead when a scoped experience project needs a process from discovery through delivery. Use Phase 02 Discovery to frame the problem before committing to a concept.

## When not to use

- Use `skill:designing-user-experience` for detailed UX methods or `skill:ux-storyboard` to communicate an experience narrative.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved project goal, stakeholders, existing evidence, scope, constraints and decision makers.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use double-diamond skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce each phase has a question and evidence; divergent work is not mistaken for validation; human decisions are recorded. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A phase-based plan with a clear problem statement, decision gates and next evidence needed.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `skill:ux-storyboard`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- A process framework is not user research or approval. Preserve evidence labels and avoid implying that workshop activities establish truth.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
