---
title: Figma Generative Plugins
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-generative-plugins
department: engineering
sub_department: creative-engineering
job: generative-creative-coding
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires generative plugins. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-generative-plugins/SKILL.md
invoke: "figma-generative-plugins skill"
pairs_with: [skill:ceos-creative-coding, skill:creating-algorithmic-art, skill:pointer-trail-emitter]
---
# Figma Generative Plugins

Figma Generative Plugins is the specialist when A Figma file/workspace exists or is explicitly requested, and the task requires generative plugins. Load this prerequisite only for its corresponding Figma operation. at 3RDWRONG.

## What it does

- MANDATORY prerequisite — load this skill before calling creategenerativeplugin or updategenerativeplugin. Use when the user asks to create, author, change, fix, or extend a reusable generative Figma plugin
- Organises the method around preflight
- Plugins run in the Figma Design editor
- Every plugin must provide functional UI for its core workflow. A plugin with no configurable inputs still needs a clear primary action and useful status or validation feedback
- Organises the method around create workflow

## When to use

- A Figma file/workspace exists or is explicitly requested, and the task requires generative plugins. Load this prerequisite only for its corresponding Figma operation.

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
2. Provide the inputs and constraints above; load or invoke `figma:figma-generative-plugins`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use figma:figma-generative-plugins for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
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

- `skill:ceos-creative-coding`: coordinate inputs and hand off the reviewed result.
- `skill:creating-algorithmic-art`: coordinate inputs and hand off the reviewed result.
- `skill:pointer-trail-emitter`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
- Distribution is fetch; install or sign in as required before use.
