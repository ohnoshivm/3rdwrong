---
title: setup-deploy
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:setup-deploy
department: engineering
sub_department: platform-performance
job: deployment-and-release
role: specialist
trigger: "Use for tasks involving Configure deployment settings for /land-and-deploy."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/creative-engineering-os/library/skills/setup-deploy/SKILL.md
invoke: "setup-deploy skill"
pairs_with: [agency:engineering-devops-automator]
---
# setup-deploy

|

## What it does

- |
- If it was present and **errored** (not absent), retry the SAME call **once** — only if no answer could have surfaced (a missing-result error can arrive after the user saw the question; retrying would double-prompt, so if it may have reached them, treat it as pending and don't retry).
- Then branch on `SESSION_KIND` (echoed by the preamble; empty/absent ⇒ `interactive`):

## When to use

- Use for tasks involving Configure deployment settings for /land-and-deploy.
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `deployment-and-release` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `deployment-and-release` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use setup-deploy skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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

- Upstream: `agency:engineering-devops-automator`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
