---
title: Interaction Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-skills:interaction-design
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A digital application has a named gesture, state-machine or error-prevention problem."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-skills-marketplace/skills/interaction-design
invoke: "interaction-design skill (Claude Code plugin `design-skills`)"
pairs_with: [skill:designing-user-experience, skill:ceos-interaction-architecture, vectorlab-ux-skills:forms]
---
# Interaction Design

The experience-design specialist for `interaction-architecture` is Interaction Design (trigger: “A digital application has a named gesture, state-machine or error-prevention problem”), which specifies how a digital product responds to user input across triggers, rules, feedback and loops.

## What it does

- Uses a four-part microinteraction framework.
- considers product posture and user flow.
- addresses edge cases, error prevention and modes.

## When to use

- Use when a digital application has a named gesture, state-machine or error-prevention problem. Use Phase 05 interaction specification before implementation.
- A digital application has a named gesture, state-machine or error-prevention problem.

## When not to use

- Use `skill:designing-user-experience` for end-to-end UX, or `vectorlab-ux-skills:forms` for a form-specific validation problem.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- User goal, trigger, current behaviour, constraints, states and failure cases.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use interaction-design skill (Claude Code plugin `design-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce a compact interaction specification that covers normal, interrupted and error paths without unnecessary modes. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A named interaction with trigger, rules, feedback, loop/mode and exceptional states.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `skill:ceos-interaction-architecture`, `vectorlab-ux-skills:forms`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not add motion for decoration; honour reduced motion, keyboard and touch. Validate the proposed behaviour against real use.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
