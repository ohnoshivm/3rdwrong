---
title: Karpathy guidelines
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:karpathy-guidelines
department: engineering
sub_department: engineering-qa-security
job: code-review
role: specialist
trigger: "Use when any build agent writes, reviews or refactors code, to avoid overcomplication, make surgical changes, surface assumptions and define verifiable success criteria."
kind: skill
availability: both
distribution: fetch
source: ~/.3rdwrong/fetch/pack-forrestchang-andrej-karpathy-skills-mit/skills/karpathy-guidelines (pinned 2c606141936f1eeef17fa3043a72095b4765b9c2)
invoke: "karpathy-guidelines skill"
pairs_with: [engineering:code-review, skill:verification-before-completion, skill:test-driven-development]
---
# Karpathy guidelines

A behavioural guideline for coding agents: avoid overcomplication, make surgical changes, surface assumptions and define verifiable success criteria before editing. Every build agent loads it for code work.

## What it does

- Asks for the smallest change that solves the stated problem.
- Makes assumptions explicit before editing, rather than hidden.
- Requires a verifiable success criterion before work starts.
- Biases toward caution on non-trivial work; leaves trivial tasks to judgement.

## When to use

- Any build, refactor or code review by a build agent in this studio.
- Before an edit that touches more than one file or changes behaviour.

## When not to use

- Trivial one-line edits where the guideline adds overhead; use judgement.
- Design or copy work: use the design specialists.
- Security review: use `skill:security-review` or the security specialists.

## Inputs it needs

- The task, the files it touches, and the acceptance criterion.

## How to run it

1. State the assumptions and the success criterion in one short list.
2. Make the smallest change that meets the criterion.
3. Verify against the criterion with a command or a test, then report what was checked.

```text
Use the karpathy-guidelines skill. Task: {task}. Acceptance criterion: {command or test}. List assumptions first. Make the smallest change that meets the criterion, touch only the files named, and report the verification output.
```

## What good output looks like

- Assumptions listed before edits; a diff limited to the task.
- A verification result for the stated criterion, not a claim that it passes.

## Quality checks

- [ ] Assumptions are visible in the change record.
- [ ] No unrelated refactor or speculative abstraction in the diff.
- [ ] A reviewer other than the maker checks the criterion.

## Pairs with

- `engineering:code-review`: review of the resulting diff.
- `skill:verification-before-completion`: the evidence gate before completion.
- `skill:test-driven-development`: tests-first for logic.

## Limits and cautions

- MIT declared in the upstream README and SKILL.md; the pinned checkout has no LICENSE file. Flagged for review before wide use.
- Guidance, not a test. It does not replace running the code.
