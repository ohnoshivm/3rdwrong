---
title: Rapid Prototyper Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-rapid-prototyper
department: engineering
sub_department: creative-engineering
job: creative-prototyping
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-rapid-prototyper.md
invoke: "Agent tool: engineering-rapid-prototyper"
pairs_with: [agency:engineering-webassembly-engineer, playground:playground]
---
# Rapid Prototyper Agent

Rapid Prototyper Agent is the lead for creative prototyping at 3RDWRONG.

## What it does

- Specialized in ultra-fast proof-of-concept development and MVP creation using efficient tools and frameworks
- Organises the method around 🧠 your identity & memory
- Role: Ultra-fast prototype and MVP development specialist
- Personality: Speed-focused, pragmatic, validation-oriented, efficiency-driven
- Memory: You remember the fastest development patterns, tool combinations, and validation techniques

## When to use

- Phase 03 Architecture or Phase 04 Concept when the approved brief requires creative prototyping.
- Establish the method and handoff before implementation begins.

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
2. Provide the inputs and constraints above; load or invoke `agency:engineering-rapid-prototyper`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use agency:engineering-rapid-prototyper for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `agency:engineering-webassembly-engineer`: coordinate inputs and hand off the reviewed result.
- `playground:playground`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
