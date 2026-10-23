---
title: Onboarding
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:onboarding
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/skills/onboarding/SKILL.md
invoke: "onboarding skill"
pairs_with: [skill:designing-user-experience, skill:ai-wayfinders]
---
# Onboarding

The experience-design specialist for `interaction-architecture` is Onboarding (trigger: “Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope”), which optimises post-signup onboarding, first-run experience, activation and time-to-value.

## What it does

- Assesses product context, activation definition and current post-signup flow.
- defines a minimum path to value.
- focuses each session on one outcome and favours doing over tutorial-only instruction.

## When to use

- Use only when an approved, named onboarding content or lifecycle task is explicitly in scope. Use Phase 05 Prototype after the onboarding goal and first-success action are approved.
- Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.

## When not to use

- Use `skill:ai-wayfinders` for onboarding into an AI feature or `skill:designing-user-experience` for broader journey design.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved audience and product capabilities, first-success action, required data and optionality.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use onboarding skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce each step supports a real user goal; skip/exit is clear; no unverified promises. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- An onboarding sequence with purpose, step, user action and exit/skip path.
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

- Registry trigger refers to marketing scope and conflicts with the design job; source is a Codex-local skill. Do not widen into campaigns or lifecycle execution.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
