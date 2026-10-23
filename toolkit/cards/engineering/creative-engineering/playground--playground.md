---
title: Playground
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: playground:playground
department: engineering
sub_department: creative-engineering
job: creative-prototyping
role: specialist
trigger: "The approved system needs a self-contained interactive parameter explorer."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-playground-marketplace/skills/playground
invoke: "playground skill"
pairs_with: [agency:engineering-rapid-prototyper, agency:engineering-webassembly-engineer]
---
# Playground

Playground is the specialist when The approved system needs a self-contained interactive parameter explorer. at 3RDWRONG.

## What it does

- Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic
- Organises the method around when to use this skill
- Organises the method around how to use this skill
- templates/design-playground.md — Visual design decisions (components, layouts, spacing, color, typography)
- templates/data-explorer.md — Data and query building (SQL, APIs, pipelines, regex)

## When to use

- The approved system needs a self-contained interactive parameter explorer.

## When not to use

- When the approved brief does not call for creative prototyping; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `playground:playground`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use playground:playground for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `agency:engineering-rapid-prototyper`: coordinate inputs and hand off the reviewed result.
- `agency:engineering-webassembly-engineer`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
