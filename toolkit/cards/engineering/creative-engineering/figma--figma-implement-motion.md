---
title: Figma Implement Motion
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-implement-motion
department: engineering
sub_department: creative-engineering
job: motion-implementation
role: specialist
trigger: "Use for engineering/creative-engineering/motion-implementation when the brief specifically requires: Translates Figma motion and animations into production-ready application code ."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-implement-motion/SKILL.md
invoke: "figma-implement-motion skill"
pairs_with: [agent:motion-director, nateherk-design:scroll-craft, skill:animation-systems]
---
# Figma Implement Motion

Figma Implement Motion is the specialist when Use for engineering/creative-engineering/motion-implementation when the brief specifically requires: Translates Figma motion and animations into production-ready application code . at 3RDWRONG.

## What it does

- Translates Figma motion and animations into production-ready application code. Use when implementing animation/motion from a Figma design — user mentions "implement this motion", "add animation from Figma", "animate this component", provides a Figma URL whose node is animated, or when getdesigncontext returns motion data or instructs you to call getmotioncontext
- Organises the method around skill boundaries
- Use this skill when the deliverable is motion code in the user's repository
- If the user asks to create/edit animations inside Figma itself, switch to figma-use (upstream reference `../figma-use/SKILL.md`) and follow that skill instead
- Organises the method around prerequisites

## When to use

- Use for engineering/creative-engineering/motion-implementation when the brief specifically requires: Translates Figma motion and animations into production-ready application code .

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
2. Provide the inputs and constraints above; load or invoke `figma:figma-implement-motion`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use figma:figma-implement-motion for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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
- `nateherk-design:scroll-craft`: coordinate inputs and hand off the reviewed result.
- `skill:animation-systems`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Distribution is fetch; install or sign in as required before use.
- Motion must serve the concept, preserve readable content and honour prefers-reduced-motion; test keyboard and touch behaviour.
