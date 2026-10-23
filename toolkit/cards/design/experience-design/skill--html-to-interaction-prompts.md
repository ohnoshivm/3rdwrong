---
title: HTML to Interaction Prompts
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:html-to-interaction-prompts
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/visual-design/html-to-interaction-prompts/SKILL.md
invoke: "html-to-interaction-prompts skill"
pairs_with: [skill:ceos-interaction-architecture, skill:ceos-motion-direction]
---
# HTML to Interaction Prompts

The experience-design specialist for `motion-principles` is HTML to Interaction Prompts (trigger: “When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference”), which turns supplied html or interface structure into prompts describing possible interaction behaviours.

## What it does

- Examines supplied UI structure.
- extracts visible controls and states.
- frames interaction ideas as prompts for further design work.

## When to use

- Use when identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference. Use Phase 05 Motion / Interaction discovery on supplied HTML.
- When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference.

## When not to use

- Use `skill:ceos-interaction-architecture` for a complete interaction model or `skill:ceos-motion-direction` for motion decisions.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- HTML or rendered interface, purpose, user tasks and constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use html-to-interaction-prompts skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce prompts identify actual elements and unresolved behaviour; inferred behaviour is labelled rather than asserted. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A set of scoped interaction questions/prompts tied to real elements in the supplied HTML.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-interaction-architecture`, `skill:ceos-motion-direction`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Prompts are exploratory, not implementation specifications. Do not copy reference identity or assume unobservable behaviour.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
