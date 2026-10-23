---
title: XR Cockpit Interaction Specialist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:xr-cockpit-interaction-specialist
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires interaction architecture expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/xr-cockpit-interaction-specialist.md
invoke: "Claude Code Agent tool: XR Cockpit Interaction Specialist"
pairs_with: [agency:xr-interface-architect, skill:ceos-interaction-architecture]
---
# XR Cockpit Interaction Specialist

The experience-design specialist for `interaction-architecture` is XR Cockpit Interaction Specialist (trigger: “When the approved scope specifically requires interaction architecture expertise”), which designs fixed-perspective cockpit controls and feedback for a specifically scoped seated xr experience.

## What it does

- Plans cockpit control placement.
- considers gesture, voice, gaze and physical inputs.
- proposes constrained control mechanics and feedback.

## When to use

- Use only when approved scope explicitly includes an XR cockpit or seated simulation. Use Phase 05 Prototype before committing the spatial controls.
- When the approved scope specifically requires interaction architecture expertise.

## When not to use

- Use `agency:xr-interface-architect` for broader spatial interface architecture.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- XR platform and input hardware, seated task, cockpit content, comfort and accessibility constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use Claude Code Agent tool: XR Cockpit Interaction Specialist. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce a control map with input, state, feedback and fallback for each control, plus unknowns requiring xr testing. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A cockpit interaction proposal tied to the target device, user posture and tested comfort constraints.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `agency:xr-interface-architect`, `skill:ceos-interaction-architecture`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Source suggests A-Frame/Three.js prototypes and comfort tuning but gives no measurable comfort threshold. Require real device testing; do not infer safety.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
