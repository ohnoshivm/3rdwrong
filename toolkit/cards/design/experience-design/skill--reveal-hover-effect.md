---
title: Reveal Hover Effect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:reveal-hover-effect
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "The approved concept specifically calls for this effect: reveal-hover-effect."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/effects-3d/reveal-hover-effect/SKILL.md
invoke: "reveal-hover-effect skill"
pairs_with: [skill:ceos-interaction-architecture, skill:ceos-motion-direction]
---
# Reveal Hover Effect

The experience-design specialist for `interaction-architecture` is Reveal Hover Effect (trigger: “The approved concept specifically calls for this effect: reveal-hover-effect”), which applies a specific hover-reveal interaction pattern when it is explicitly part of the approved concept.

## What it does

- Layers aligned base and reveal images with a feathered radial mask.
- Tracks and eases pointer position with requestAnimationFrame; collapses the mask on pointer exit.
- Defaults to CSS masks to avoid per-frame canvas data URLs and includes touch/keyboard alternatives.

## When to use

- Use only when the approved concept specifically calls for this effect: reveal-hover-effect. Use Phase 05 Prototype after the visual concept is approved.
- The approved concept specifically calls for this effect: reveal-hover-effect.

## When not to use

- Use `skill:ceos-interaction-architecture` to define accessible equivalent interaction paths.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved visual concept, target element, revealed content and touch/keyboard requirements.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use reveal-hover-effect skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce reveal is discoverable and has equivalent focus/touch behaviour; no essential content is hover-only. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A bounded hover effect with its target, trigger, reveal and fallback specified.
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

- Effect source is a local manual skill; inspect its specific requirements. Hover cannot be the only input path; motion respects reduced motion.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
