---
title: Stitch Build Loop
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: stitch-utilities:stitch-loop
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use when the approved work needs this capability: Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern"
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-google-labs-code-stitch-skills-stitch-utilities-0337446dadde/skills/stitch-loop
invoke: "stitch-loop skill"
pairs_with: [stitch-build:react-components, agent:frontend-architect]
---
# Stitch Build Loop

Stitch Build Loop is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Uses baton-based iterative website work with Stitch MCP
- Reads task, generates/integrates page and writes next baton
- Requires project, DESIGN.md and SITE.md

## When to use

- Use when the approved work needs this capability: Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern
- When project intentionally uses Stitch baton loop
- Phase 05

## When not to use

- For ordinary one-off build use `agent:frontend-architect`
- Not without Stitch project and baton
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Current `.stitch/next-prompt.md`
- DESIGN.md and SITE.md
- Target page and Stitch tools

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `stitch-loop skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `stitch-utilities:stitch-loop` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Integrated page and updated next baton
- Design system block and filename preserved

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `stitch-build:react-components` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Source requires updating baton before finish
- protect client data and credentials
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
