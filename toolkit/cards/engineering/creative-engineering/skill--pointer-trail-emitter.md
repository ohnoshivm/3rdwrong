---
title: Pointer Trail Emitter
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:pointer-trail-emitter
department: engineering
sub_department: creative-engineering
job: generative-creative-coding
role: specialist
trigger: "The approved concept specifically calls for this effect: pointer-trail-emitter."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/effects-3d/pointer-trail-emitter/SKILL.md
invoke: "pointer-trail-emitter skill"
pairs_with: [figma:figma-generative-plugins, skill:ceos-creative-coding, skill:creating-algorithmic-art]
---
# Pointer Trail Emitter

Pointer Trail Emitter is the specialist when The approved concept specifically calls for this effect: pointer-trail-emitter. at 3RDWRONG.

## What it does

- Build a cursor trail whose spacing stays constant at any hand speed, by emitting motes per unit of distance travelled rather than on a timer, so a flick draws the same continuous ribbon as a crawl instead of breaking into scattered dots. Covers sub-segment placement, the ring-buffer ordering trap, the idle breath a distance emitter needs, anchoring the trail to the screen in a 3-D scene, scaling scatter against the plane it hangs on, coasting instead of stopping dead, touch and reduced-motion fallbacks, and why moving the emitter to a DOM overlay to raise its z-index costs more than it buys. Use for cursor wisps, pointer sparks, embers, magic trails, comet tails, plankton, dust, or any mote trail that must stay legible however fast the hand moves
- Organises the method around emit by distance, not by time
- Organises the method around place each mote where it is owed
- Organises the method around take the ring-buffer slot before advancing it
- Organises the method around lag the emitter behind the pointer

## When to use

- The approved concept specifically calls for this effect: pointer-trail-emitter.

## When not to use

- When the approved brief does not call for generative creative coding; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:pointer-trail-emitter`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:pointer-trail-emitter for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
```

## What good output looks like

- Addresses the registry job and trigger with a concrete artefact, recommendation or implementation handoff.
- Makes assumptions and undocumented capabilities explicit; links findings to provided evidence.
- States constraints, unresolved risks and a next action suitable for independent review.

## Quality checks

- [ ] A reviewer other than the maker checks each source-specific requirement against the brief.
- [ ] Claims are supported by the source or supplied evidence; unknowns are labelled.
- [ ] Platform, responsive behaviour, accessibility and performance constraints are checked where applicable.
- [ ] No client data or secrets are committed to a public repository.

## Pairs with

- `figma:figma-generative-plugins`: coordinate inputs and hand off the reviewed result.
- `skill:ceos-creative-coding`: coordinate inputs and hand off the reviewed result.
- `skill:creating-algorithmic-art`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Motion must serve the concept, preserve readable content and honour prefers-reduced-motion; test keyboard and touch behaviour.
