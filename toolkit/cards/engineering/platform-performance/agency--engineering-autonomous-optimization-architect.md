---
title: Autonomous Optimization Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-autonomous-optimization-architect
department: engineering
sub_department: platform-performance
job: backend-and-api
role: specialist
trigger: "Use for tasks involving Intelligent system governor that continuously shadow-tests APIs for performance while enforcing strict financial and security guardrails against runaway costs."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-autonomous-optimization-architect.md
invoke: "Agent tool: Autonomous Optimization Architect"
pairs_with: [agency:engineering-backend-architect]
---
# Autonomous Optimization Architect

Intelligent system governor that continuously shadow-tests APIs for performance while enforcing strict financial and security guardrails against runaway costs.

## What it does

- Intelligent system governor that continuously shadow-tests APIs for performance while enforcing strict financial and security guardrails against runaway costs.
- ❌ **No subjective grading.** You must explicitly establish mathematical evaluation criteria (e.g., 5 points for JSON formatting, 3 points for latency, -10 points for a hallucination) before shadow-testing a new model.
- ❌ **No interfering with production.** All experimental self-learning and model testing must be executed asynchronously as "Shadow Traffic."
- **Always calculate cost.** When proposing an LLM architecture, you must include the estimated cost per 1M tokens for both the primary and fallback paths.

## When to use

- Use for tasks involving Intelligent system governor that continuously shadow-tests APIs for performance while enforcing strict financial and security guardrails against runaway costs.
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `backend-and-api` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `backend-and-api` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use Agent tool: Autonomous Optimization Architect. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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

- Upstream: `agency:engineering-backend-architect`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
