---
title: XR Interface Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:xr-interface-architect
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires interaction architecture expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/xr-interface-architect.md
invoke: "Claude Code Agent tool: XR Interface Architect"
pairs_with: [agency:xr-cockpit-interaction-specialist, skill:ceos-interaction-architecture]
---
# XR Interface Architect

The experience-design specialist for `interaction-architecture` is XR Interface Architect (trigger: “When the approved scope specifically requires interaction architecture expertise”), which structures discoverable and comfortable spatial interfaces for a defined ar/vr/xr experience.

## What it does

- Plans HUDs, panels and interaction zones.
- maps gaze, touch, controller and gesture inputs.
- outlines comfort and learnability validation.

## When to use

- Use only when the approved scope explicitly requires spatial or immersive interaction architecture. Use Phase 04 Concept to map orientation and actions before prototype.
- When the approved scope specifically requires interaction architecture expertise.

## When not to use

- Use `agency:xr-cockpit-interaction-specialist` for cockpit-only control ergonomics.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- XR platform, user context, task sequence, input modalities and accessibility requirements.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use Claude Code Agent tool: XR Interface Architect. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce a spatial layout and flow with orientation cues, discoverable actions and non-gesture alternatives. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A spatial flow and layout proposal with input fallbacks and validation questions.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `agency:xr-cockpit-interaction-specialist`, `skill:ceos-interaction-architecture`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Source describes specialist expertise but no standardised XR thresholds. Validate comfort and learnability with target users and hardware.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
