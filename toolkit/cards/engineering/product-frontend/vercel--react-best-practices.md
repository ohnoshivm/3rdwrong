---
title: Vercel React Best Practices
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vercel:react-best-practices
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: React best-practices reviewer for TSX files ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-vercel-0.50.0/skills/react-best-practices
invoke: "react-best-practices skill"
pairs_with: [agent:frontend-architect, skill:vercel-composition-patterns]
---
# Vercel React Best Practices

Vercel React Best Practices is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Reviews TSX after multiple component edits
- Checks structure, hooks, accessibility, performance and TypeScript
- Has path/import signals and CSS-in-JS warning

## When to use

- Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: React best-practices reviewer for TSX files .
- Independent review after multi-TSX edits

## When not to use

- Not implementation lead or browser QA
- For broader UX review use QA reviewer
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Changed TSX and review scope
- Project conventions and criteria

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `react-best-practices skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `vercel:react-best-practices` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Prioritised file-specific findings
- No invented execution claims and maker/checker separation

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `skill:vercel-composition-patterns` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Condensed checklist, not full test suite
- clean checklist does not prove responsive rendering
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
