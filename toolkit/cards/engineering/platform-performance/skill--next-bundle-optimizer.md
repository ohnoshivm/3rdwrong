---
title: next-bundle-optimizer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:next-bundle-optimizer
department: engineering
sub_department: platform-performance
job: web-vitals
role: specialist
trigger: "Use for engineering/platform-performance/web-vitals when the brief specifically requires: > ."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/next-bundle-optimizer/SKILL.md
invoke: "next-bundle-optimizer skill"
pairs_with: [skill:ceos-performance-engineering]
---
# next-bundle-optimizer

>

## What it does

- >
>
## When to use

- Use for engineering/platform-performance/web-vitals when the brief specifically requires: > .
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `web-vitals` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `web-vitals` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use next-bundle-optimizer skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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

- Upstream: `skill:ceos-performance-engineering`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
