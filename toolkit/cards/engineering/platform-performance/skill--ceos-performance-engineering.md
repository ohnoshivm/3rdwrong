---
title: ceos-performance-engineering
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-performance-engineering
department: engineering
sub_department: platform-performance
job: web-vitals
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-performance-engineering
invoke: "ceos-performance-engineering skill"
pairs_with: []
---
# ceos-performance-engineering

Measures and fixes performance of creative, animated and WebGL websites — Core Web Vitals (LCP, INP, CLS), DevTools performance traces, main-thread long tasks, GPU/frame-time stability, memory leaks, bundle and asset weight, loading strategy, adaptive quality and progressive enhancement. Use when a site feels slow or janky, before launch, when setting budgets, when adding heavy 3D/video/fonts, or when someone claims it's "fast" without numbers.

## What it does

- Measures and fixes performance of creative, animated and WebGL websites — Core Web Vitals (LCP, INP, CLS), DevTools performance traces, main-thread long tasks, GPU/frame-time stability, memory leaks, bundle and asset weight, loading strategy, adaptive quality and progressive enhancement. Use when a site feels slow or janky, before launch, when setting budgets, when adding heavy 3D/video/fonts, or when someone claims it's "fast" without numbers.

## When to use

- Phase 05 Build, when measured evidence shows a need for web vitals work.
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
Use ceos-performance-engineering skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
```

## What good output looks like

- Studio web budget (founder instruction): LCP ≤ 2.0 s; ≤ 2 MB before first interaction; INP ≤ 200 ms; CLS ≤ 0.1; 60 fps; honour reduced motion.
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
