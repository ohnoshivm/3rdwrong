---
title: Behavioral Nudge Engine
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:product-behavioral-nudge-engine
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires interaction architecture expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/product-behavioral-nudge-engine.md
invoke: "Claude Code Agent tool: Behavioral Nudge Engine"
pairs_with: [skill:designing-user-experience, skill:ai-wayfinders]
---
# Behavioral Nudge Engine

The experience-design specialist for `interaction-architecture` is Behavioral Nudge Engine (trigger: “When the approved scope specifically requires interaction architecture expertise”), which explores low-friction prompts and cadence patterns for a product interaction, grounded in stated user preferences.

## What it does

- Breaks large queues into small actions.
- proposes preference-aware cadence and channel patterns.
- drafts opt-out and completion feedback.

## When to use

- Use only when the approved experience includes a behaviour-change or reminder moment. Use Phase 04 Concept to design the intervention before implementation.
- When the approved scope specifically requires interaction architecture expertise.

## When not to use

- Use `skill:ai-wayfinders` for helping users start an AI task, or `skill:designing-user-experience` for general onboarding and journey structure.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- A user goal, evidence about user preferences and context, permitted channel and frequency constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use Claude Code Agent tool: Behavioral Nudge Engine. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce one useful next action, user-controlled cadence and clear pause/opt-out path; no assumed efficacy. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A proposed nudge sequence with user choice, off-ramps and assumptions made explicit.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `skill:ai-wayfinders`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Its source asserts success metrics and user-specific learning. Treat those as proposed product measures, not demonstrated results. Do not use pressure or manipulative defaults.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
