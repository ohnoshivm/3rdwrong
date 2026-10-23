---
title: bulk-executor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:bulk-executor
department: operations
sub_department: planning-workflow
job: workflow-orchestration
role: specialist
trigger: "Use when the approved work needs this capability: Performs trivial repetitive mechanical work to exact instructions"
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/bulk-executor.md
invoke: "Agent tool: bulk-executor"
pairs_with: []
---
# bulk-executor

The bulk-executor tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Performs trivial repetitive mechanical work to exact instructions.

## What it does

- tools: Read, Write, Edit, Bash, Glob, Grep
- Do not delete or overwrite without the brief saying so
- If anything is unclear or requires judgment, stop and report

- ## Completion report (always end with this, ≤12 lines)

## When to use

- Use when the approved work needs this capability: Performs trivial repetitive mechanical work to exact instructions

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
Use Agent tool: bulk-executor. Job: workflow-orchestration. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
