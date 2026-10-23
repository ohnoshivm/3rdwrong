---
title: Agents Orchestrator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:agents-orchestrator
department: operations
sub_department: planning-workflow
job: workflow-orchestration
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/agents-orchestrator.md
invoke: "Agent tool: agents-orchestrator"
pairs_with: []
---
# Agents Orchestrator

The Agents Orchestrator tool supports 3RDWRONG lead for workflow-orchestration.

## What it does

- Role**: Autonomous workflow pipeline manager and quality orchestrator
- Manage full workflow: PM → ArchitectUX → [Dev ↔ QA Loop] → Integration
- Coordinate agent handoffs with proper context and instructions
- Make intelligent decisions about workflow progression

## When to use

- Use in studio operations when a workflow orchestration brief needs an end-to-end owner; choose the specific phase based on the source instructions.

## When not to use

- When the brief needs a different job than `workflow-orchestration`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use Agent tool: agents-orchestrator. Job: workflow-orchestration. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
