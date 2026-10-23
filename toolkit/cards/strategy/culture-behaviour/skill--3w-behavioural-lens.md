---
title: Behavioural lens
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-behavioural-lens
department: strategy
sub_department: culture-behaviour
job: behavioural-theory
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-behavioural-lens/SKILL.md
invoke: "3w-behavioural-lens skill"
pairs_with: [agency:academic-psychologist, agency:academic-statistician, agency:research-synthesist]
---
# Behavioural lens

The studio's lead tool for behavioural theory: cited mechanisms turned into testable hypotheses, with an ethics screen. Registered job lead; the skill remains experimental.

## What it does

- States the behaviour as actor, context and observable action.
- Maps candidate mechanisms with primary source, studied context and replication status.
- Writes if-then-because hypotheses with the cheapest honest test.
- Rejects levers that rely on deception, pressure or exploiting vulnerability.

## When to use

- Identity 02 Diagnosis and 03 Strategy, digital stage 02, when a decision rests on how people notice, choose or act.
- Whenever a psychology claim enters a brief (perception-to-identity map rule).

## When not to use

- Profiling a named person or making clinical statements.
- Designing dark patterns or pressure tactics.
- When sourced audience evidence already answers the question — use `agency:research-synthesist`.

## Inputs it needs

- The decision and the behaviour that matters.
- Existing evidence with sources.
- Audience, market, culture and language context.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-behavioural-lens skill. Decision: {{decision}}. Behaviour: {{actor, context, action}}. Evidence: {{sources}}. Return the mechanism table with primary sources, hypotheses with tests, rejected levers and unknowns.
```

## What good output looks like

- Every mechanism has a primary source, context and replication note.
- Hypotheses are observable and testable.
- Rejected levers listed with reasons.

## Quality checks

- [ ] Behaviour separated from attitudes.
- [ ] No mechanism without a source.
- [ ] Contested findings flagged.
- [ ] No manipulative lever survives.

## Pairs with

- Specialists by explicit call: `agency:academic-psychologist` (theory depth), `agency:academic-statistician` (test design).
- Downstream: the strategy owner and `skill:3w-creative-direction`.

## Limits and cautions

- Experimental skill; transfer from studied contexts is Interpretation or Hypothesis.
- Not a substitute for research with people.
