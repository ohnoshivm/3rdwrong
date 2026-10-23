---
title: hands-free
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-steward:hands-free
department: operations
sub_department: planning-workflow
job: project-planning
role: specialist
trigger: "Use when the approved work needs this capability: Plan a multi-step outcome as a resumable, evidence-backed plan. Use for hands-free planning; use execute to run and resume to continue interrupted work"
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-steward-marketplace/components/hands-free/skills/hands-free
invoke: "hands-free skill"
pairs_with: []
---
# hands-free

The hands-free tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Plan a multi-step outcome as a resumable, evidence-backed plan. Use for hands-free planning; use execute to run and resume to continue interrupted work.

## What it does

- Turn the requested outcome into a bounded plan with observable acceptance criteria
- Read current project guidance, existing plans, and user decisions. For a small
- Write `.hands-free/<run-id>/plan.json` using `../../references/execution.md`
- If asked to plan, deliver the plan. If asked to implement/run, continue through

## When to use

- Use when the approved work needs this capability: Plan a multi-step outcome as a resumable, evidence-backed plan. Use for hands-free planning; use execute to run and resume to continue interrupted work

## When not to use

- When the brief needs a different job than `project-planning`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use hands-free skill. Job: project-planning. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
