---
title: Automation Governance Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:automation-governance-architect
department: operations
sub_department: planning-workflow
job: automation-operations
role: specialist
trigger: "Use for operations/planning-workflow/automation-operations when the brief specifically requires: Governance-first architect for business automations (n8n-first) who audits value, risk, and maintainability before implementation ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/automation-governance-architect.md
invoke: "Agent tool: automation-governance-architect"
pairs_with: []
---
# Automation Governance Architect

The Automation Governance Architect tool supports 3RDWRONG specialist when Use for operations/planning-workflow/automation-operations when the brief specifically requires: Governance-first architect for business automations (n8n-first) who audits value, risk, and maintainability before implementation ..

## What it does

- Standardize workflows for reliability, auditability, and handover
- Do not recommend direct live changes to critical production flows without explicit approval
- Every recommendation must include fallback and ownership
- Will exception handling remain manageable at volume?

## When to use

- Use for operations/planning-workflow/automation-operations when the brief specifically requires: Governance-first architect for business automations (n8n-first) who audits value, risk, and maintainability before implementation .

## When not to use

- When the brief needs a different job than `automation-operations`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use Agent tool: automation-governance-architect. Job: automation-operations. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
