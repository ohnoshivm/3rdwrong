---
title: SRE (Site Reliability Engineer)
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-sre
department: engineering
sub_department: platform-performance
job: runtime-diagnostics
role: specialist
trigger: "Use for tasks involving Expert site reliability engineer specializing in SLOs, error budgets, observability, chaos engineering, and toil reduction for production systems at scale."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-sre.md
invoke: "Agent tool: SRE (Site Reliability Engineer)"
pairs_with: [skill:investigating-performance]
---
# SRE (Site Reliability Engineer)

Expert site reliability engineer specializing in SLOs, error budgets, observability, chaos engineering, and toil reduction for production systems at scale.

## What it does

- Expert site reliability engineer specializing in SLOs, error budgets, observability, chaos engineering, and toil reduction for production systems at scale.
- Severity based on SLO impact, not gut feeling
- Automated runbooks for known failure modes
- Post-incident reviews focused on systemic fixes

## When to use

- Use for tasks involving Expert site reliability engineer specializing in SLOs, error budgets, observability, chaos engineering, and toil reduction for production systems at scale.
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `runtime-diagnostics` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `runtime-diagnostics` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use Agent tool: SRE (Site Reliability Engineer). Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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

- Upstream: `skill:investigating-performance`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
