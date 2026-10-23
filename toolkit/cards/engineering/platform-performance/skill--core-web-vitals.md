---
title: core-web-vitals
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:core-web-vitals
department: engineering
sub_department: platform-performance
job: web-vitals
role: specialist
trigger: "a focused LCP, INP, or CLS diagnosis is requested and field/lab evidence is available."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/core-web-vitals/SKILL.md
invoke: "core-web-vitals skill"
pairs_with: [skill:ceos-performance-engineering]
---
# core-web-vitals

Optimize Core Web Vitals (LCP, INP, CLS) for better page experience using field and lab evidence. Use when asked to "improve Core Web Vitals", "fix LCP", "reduce CLS", "optimize INP", "page experience optimization", or "fix layout shifts".

## What it does

- Optimize Core Web Vitals (LCP, INP, CLS) for better page experience using field and lab evidence. Use when asked to "improve Core Web Vitals", "fix LCP", "reduce CLS", "optimize INP", "page experience optimization", or "fix layout shifts".

## When to use

- a focused LCP, INP, or CLS diagnosis is requested and field/lab evidence is available.
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
Use core-web-vitals skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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
