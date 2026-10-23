---
title: Scroll Craft
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: nateherk-design:scroll-craft
department: engineering
sub_department: creative-engineering
job: motion-implementation
role: specialist
trigger: "When the approved scope specifically requires use when creating motion or time-based visual work."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-nateherk-nateherk-design-0.3.0/skills/scroll-craft
invoke: "scroll-craft skill"
pairs_with: [agent:motion-director, figma:figma-implement-motion, skill:animation-systems]
---
# Scroll Craft

Scroll Craft is the specialist when When the approved scope specifically requires use when creating motion or time-based visual work. at 3RDWRONG.

## What it does

- >
- Organises the method around what this is not
- Organises the method around nate's standing hero preference
- Organises the method around approved collection standard
- Organises the method around step 0: the brief and creative authority

## When to use

- When the approved scope specifically requires use when creating motion or time-based visual work.

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
2. Provide the inputs and constraints above; load or invoke `nateherk-design:scroll-craft`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use nateherk-design:scroll-craft for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
- `skill:animation-systems`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Motion must serve the concept, preserve readable content and honour prefers-reduced-motion; test keyboard and touch behaviour.
