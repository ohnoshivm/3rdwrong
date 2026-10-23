---
title: Labs benchmark
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-labs-benchmark
department: labs
sub_department: experiments
job: research-benchmarks
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-labs-benchmark/SKILL.md
invoke: "3w-labs-benchmark skill"
pairs_with: [agency:academic-statistician, skill:3w-engine-validation]
---
# Labs benchmark

The studio's lead tool for research benchmarks: a reproducible comparison of techniques, libraries, models or workflows tied to a real decision. Proposed lead; the registry change is pending.

## What it does

- Fixes a decision threshold before measuring.
- Uses one shared fixture, recorded environments and at least five alternating runs per option.
- Reports medians and spread; blinds judged metrics and has a non-maker score them.
- Labels the conclusion and states limits and a re-run trigger.

## When to use

- Choosing between rendering approaches, animation libraries, image formats, build tools or AI models for studio work.
- Before a choice is written into the house engine or a method.

## When not to use

- As a project performance gate — use the launch-readiness checklist.
- To validate a single kit — use `skill:3w-engine-validation`.
- To publish rankings as marketing claims.

## Inputs it needs

- The decision and its owner.
- Two or more options with versions and licences.
- A realistic fixture with provenance (no client material).
- The metrics and threshold that would change the decision.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-labs-benchmark skill. Decision: {{decision, owner}}. Options: {{A vX, B vY}}. Fixture: {{path}}. Metrics and threshold: {{…}}. Run at least five alternating runs per environment and return the benchmark record.
```

## What good output looks like

- Results table with median, spread and n for each metric.
- Conclusion labelled Documented only for what was measured here.
- Explicit limits and a re-run trigger.

## Quality checks

- [ ] Threshold recorded before results.
- [ ] Fixtures and scripts are rerunnable from the repo.
- [ ] Judged metrics blinded and scored by a non-maker.
- [ ] No client data in fixtures.

## Pairs with

- Challenge: `agency:academic-statistician` for sample and inference questions.
- Downstream: the method or kit the result informs; `skill:3w-engine-validation` for kits.

## Limits and cautions

- Experimental skill; one benchmark is evidence for its fixture and environments only.
- Vendor claims are quoted separately, never merged with own measurements.
- Founder approval before publication outside the repo.
