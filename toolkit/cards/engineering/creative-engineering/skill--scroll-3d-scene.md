---
title: Scroll 3D Scene
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:scroll-3d-scene
department: engineering
sub_department: creative-engineering
job: realtime-3d
role: specialist
trigger: "The approved identity application specifically needs scroll-driven 3D with one scroll owner."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/scroll-3d-scene/SKILL.md
invoke: "scroll-3d-scene skill"
pairs_with: [agent:3d-webgl-engineer, skill:3d-falling-leaves, skill:3d-high-poly-models]
---
# Scroll 3D Scene

Scroll 3D Scene is the specialist when The approved identity application specifically needs scroll-driven 3D with one scroll owner. at 3RDWRONG.

## What it does

- Wire up scroll-driven 3D — smooth scrolling with Lenis, scroll-linked timelines and camera moves with GSAP ScrollTrigger, or in-canvas scrolling with drei ScrollControls. Use when the user wants the 3D scene to react to scrolling, a cinematic scroll story, scroll-pinned sections, or camera that moves as the user scrolls
- Approach A — Lenis + GSAP ScrollTrigger: normal DOM page scrolls; scroll drives 3D. Best for marketing/story pages mixing HTML and 3D
- Approach B — drei ScrollControls: scroll lives inside the Canvas over a virtual track. Best for pure 3D experiences
- Organises the method around approach a — lenis + gsap scrolltrigger
- Organises the method around approach b — drei scrollcontrols

## When to use

- The approved identity application specifically needs scroll-driven 3D with one scroll owner.

## When not to use

- When the approved brief does not call for realtime 3d; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## Technology choice

**Documented** — [D-0025](../../../../studio/decisions/0025-creative-technology-selection-policy.md)
adopts the [selection policy](../../../../methods/creative-technology/selection-policy.md).
Use native scrolling with ScrollTrigger first. Lenis or ScrollControls needs a recorded reason; choose one scroll owner and check current package APIs rather than copying legacy install commands. D-0023 remains binding; preserve HTML, keyboard access and reduced motion.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:scroll-3d-scene`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:scroll-3d-scene for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `agent:3d-webgl-engineer`: coordinate inputs and hand off the reviewed result.
- `skill:3d-falling-leaves`: coordinate inputs and hand off the reviewed result.
- `skill:3d-high-poly-models`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Distribution is manual; install or sign in as required before use.
- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Treat GPU work as a measured budget: record frame time, draw calls, memory and device tier; reduce quality or disable the effect on constrained devices. Exact numeric budget: Not documented unless the source specifies one.
- Provide a non-WebGL/static fallback and honour prefers-reduced-motion; keep motion purposeful and preserve usable content when animation is off.
