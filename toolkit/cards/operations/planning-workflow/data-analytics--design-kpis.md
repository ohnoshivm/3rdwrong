---
title: design-kpis
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: data-analytics:design-kpis
department: operations
sub_department: planning-workflow
job: process-improvement
role: specialist
trigger: "When defining operating metrics for the studio or a contracted client engagement."
kind: plugin-skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/data-analytics/1.0.11/skills/design-kpis/SKILL.md
invoke: "design-kpis skill"
pairs_with: []
---
# design-kpis

The design-kpis tool supports 3RDWRONG specialist when When defining operating metrics for the studio or a contracted client engagement..

## What it does

- Design KPI frameworks, set targets, and develop measurement plans that help teams make product or business decisions
- Follow the shared Data instructions (upstream reference `../../shared/shared-skill-instructions.md`) throughout this workflow
- Product Analytics: Event instrumentation, behavioral measures, and experiment guardrails
- Use $analyze-data-quality first when the task is to reconcile existing metrics, dashboards, tables, owners, or sources of truth

## When to use

- When defining operating metrics for the studio or a contracted client engagement.

## When not to use

- When the brief needs a different job than `process-improvement`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use design-kpis skill. Job: process-improvement. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
```

## What good output looks like

- Addresses the stated outcome and follows the source instructions.
- Separates documented evidence from assumptions and names unresolved inputs.
- Includes a useful next action or handoff where the source calls for one.

## Quality checks

- [ ] A reviewer confirms claims against source evidence.
- [ ] Assumptions and missing inputs are explicit.
- [ ] The result is reviewed by someone other than its maker when it is used to check work.

## Pairs with

- No registry pairings are documented. Handoff: share the brief, output and open questions with the next tool selected for the project.

## Limits and cautions

- Capabilities are limited to those stated in the tool file; details not stated there are Not documented.
- Distribution/access: follow the installed package and access rules.
- Keep client data out of the public repository (D-0021).
- Apply evidence labels: Documented, Interpretation, Hypothesis or Unknown; preserve human review for consequential decisions.
