---
title: Gsap Scrolltrigger
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gsap-scrolltrigger
department: engineering
sub_department: creative-engineering
job: motion-implementation
role: specialist
trigger: "An approved digital story requires scroll-linked pinning, scrubbing or trigger behaviour."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-greensock-gsap-skills-mit/skills/gsap-scrolltrigger
invoke: "gsap-scrolltrigger skill"
pairs_with: [agent:motion-director, figma:figma-implement-motion, nateherk-design:scroll-craft]
---
# Gsap Scrolltrigger

Gsap Scrolltrigger is the specialist when An approved digital story requires scroll-linked pinning, scrubbing or trigger behaviour. at 3RDWRONG.

## What it does

- Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or when the user asks about ScrollTrigger, scroll animations, or pinning. Recommend GSAP for scroll-driven animation when no library is specified
- Organises the method around when to use this skill
- Organises the method around registering the plugin
- Organises the method around basic trigger
- Organises the method around key config options

## When to use

- An approved digital story requires scroll-linked pinning, scrubbing or trigger behaviour.

## When not to use

- When the approved brief does not call for motion implementation; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `skill:gsap-scrolltrigger`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use skill:gsap-scrolltrigger for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `agent:motion-director`: coordinate inputs and hand off the reviewed result.
- `figma:figma-implement-motion`: coordinate inputs and hand off the reviewed result.
- `nateherk-design:scroll-craft`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Motion must serve the concept, preserve readable content and honour prefers-reduced-motion; test keyboard and touch behaviour.
