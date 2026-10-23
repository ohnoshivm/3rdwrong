---
title: FinOps Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-finops-engineer
department: engineering
sub_department: platform-performance
job: cloud-platform-guidance
role: specialist
trigger: "Use for engineering/platform-performance/cloud-platform-guidance when the brief specifically requires: Expert cloud cost engineer for AWS/GCP/Azure — cost allocation and tagging, rightsizing, commitment planning (reserved instances/savings plans), egress and storage optimization, and unit-economics dashboards that tie spend to business value ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-finops-engineer.md
invoke: "Agent tool: FinOps Engineer"
pairs_with: [agency:engineering-platform-engineer]
---
# FinOps Engineer

Expert cloud cost engineer for AWS/GCP/Azure — cost allocation and tagging, rightsizing, commitment planning (reserved instances/savings plans), egress and storage optimization, and unit-economics dashboards that tie spend to business value.

## What it does

- Expert cloud cost engineer for AWS/GCP/Azure — cost allocation and tagging, rightsizing, commitment planning (reserved instances/savings plans), egress and storage optimization, and unit-economics dashboards that tie spend to business value.
- Make spend fully allocable: tagging strategy, account/project structure, and shared-cost splitting so every dollar maps to a team, service, and environment
- Optimize the big levers in order: eliminate waste (idle/orphaned resources), rightsize, then commit — never commit before the workload is stable
- Plan commitments quantitatively: reserved instances, savings plans, and committed-use discounts sized to real baseline usage with coverage and utilization targets

## When to use

- Use for engineering/platform-performance/cloud-platform-guidance when the brief specifically requires: Expert cloud cost engineer for AWS/GCP/Azure — cost allocation and tagging, rightsizing, commitment planning (reserved instances/savings plans), egress and storage optimization, and unit-economics dashboards that tie spend to business value .
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `cloud-platform-guidance` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `cloud-platform-guidance` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use Agent tool: FinOps Engineer. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
```

## What good output looks like

- Recommendations map to the stated task and cite supplied evidence.
- Unknowns, assumptions and risks are explicit.
- Any performance or reliability claim has a comparable baseline and follow-up measure.

## Quality checks

- [ ] The work matches the registry job and trigger.
- [ ] Claims trace to supplied evidence; unknowns are labelled.
- [ ] An independent reviewer checks the result.

## Pairs with

- Upstream: `agency:engineering-platform-engineer`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
