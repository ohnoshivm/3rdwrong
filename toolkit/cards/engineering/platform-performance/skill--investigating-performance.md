---
title: investigating-performance
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:investigating-performance
department: engineering
sub_department: platform-performance
job: runtime-diagnostics
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/investigating-performance/SKILL.md
invoke: "investigating-performance skill"
pairs_with: []
---
# investigating-performance

Use when something is too slow, uses too much memory or CPU, degrades under load, or times out — and before making any change intended to speed something up. Triggers include "this is slow", "optimize this", "high latency", "p99", "memory leak", "it's fine locally but not in production", "the query takes forever", "reduce bundle size", and any request to make code faster.

## What it does

- Use when something is too slow, uses too much memory or CPU, degrades under load, or times out — and before making any change intended to speed something up. Triggers include "this is slow", "optimize this", "high latency", "p99", "memory leak", "it's fine locally but not in production", "the query takes forever", "reduce bundle size", and any request to make code faster.
- Not for "this is obviously the slow part" — obvious is what makes it worth measuring
- Not for "the fix is cheap anyway" — a cheap fix to a non-bottleneck is pure risk with zero payoff
- Not for changes you would make on style grounds regardless. Make them; just don't call it performance work

## When to use

- Phase 05 Build, when measured evidence shows a need for runtime diagnostics work.
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
Use investigating-performance skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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

- Upstream: the relevant project owner.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
