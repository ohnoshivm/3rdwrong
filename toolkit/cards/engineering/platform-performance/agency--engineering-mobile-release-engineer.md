---
title: Mobile Release Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-mobile-release-engineer
department: engineering
sub_department: platform-performance
job: deployment-and-release
role: specialist
trigger: "Use for tasks involving Expert mobile release and distribution engineer for iOS and Android."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-mobile-release-engineer.md
invoke: "Agent tool: Mobile Release Engineer"
pairs_with: [agency:engineering-devops-automator]
---
# Mobile Release Engineer

Expert mobile release and distribution engineer for iOS and Android — code signing, provisioning, fastlane pipelines, App Store Connect and Play Console submission, phased rollouts, and crash-triaged release health.

## What it does

- Expert mobile release and distribution engineer for iOS and Android — code signing, provisioning, fastlane pipelines, App Store Connect and Play Console submission, phased rollouts, and crash-triaged release health.
- Own code signing end to end: iOS certificates, provisioning profiles, and capabilities; Android keystores and Play App Signing — automated, versioned, and never living on one engineer's laptop
- Build reproducible release pipelines with fastlane (or equivalent) that go from tagged commit to store-ready artifact with no manual clicking
- Navigate store submission: App Store Connect and Play Console metadata, review-guideline compliance, privacy declarations, and the rejection-appeal path

## When to use

- Use for tasks involving Expert mobile release and distribution engineer for iOS and Android.
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
Use Agent tool: Mobile Release Engineer. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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
