---
title: Interface Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:interface-design
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When shaping multi-state product UI or defining resilient interaction patterns for a studio-owned app or site."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-dammyjay93-interface-design-mit/skills/interface-design
invoke: "interface-design skill"
pairs_with: [frontend-design:frontend-design, skill:ceos-interaction-architecture, vectorlab-ux-skills:page-patterns]
---
# Interface Design

The experience-design specialist for `interaction-architecture` is Interface Design (trigger: “When shaping multi-state product UI or defining resilient interaction patterns for a studio-owned app or site”), which shapes resilient multi-state product interfaces and implementation-aware component patterns.

## What it does

- Covers visual design principles and component construction.
- includes interaction states and responsive considerations.
- provides implementation-oriented direction.

## When to use

- Use when shaping multi-state product UI or defining resilient interaction patterns for a studio-owned app or site. Use Phase 05 Prototype for a component with several meaningful states.
- When shaping multi-state product UI or defining resilient interaction patterns for a studio-owned app or site.

## When not to use

- Use `frontend-design:frontend-design` for distinctive art direction and `skill:ceos-interaction-architecture` for end-to-end journeys.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Product goal, existing system, screen context, state inventory, content and platform constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use interface-design skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce the design handles loading, empty, error and success as relevant and fits the existing product system. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A screen or component specification that accounts for its states and constraints.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `frontend-design:frontend-design`, `skill:ceos-interaction-architecture`, `vectorlab-ux-skills:page-patterns`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Apply only the source-supported patterns; verify visual output and accessibility independently.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
