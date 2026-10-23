---
title: IoT Fleet Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-iot-fleet-engineer
department: engineering
sub_department: platform-performance
job: deployment-and-release
role: specialist
trigger: "Use for tasks involving Expert IoT and edge fleet engineer."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-iot-fleet-engineer.md
invoke: "Agent tool: IoT Fleet Engineer"
pairs_with: [agency:engineering-devops-automator]
---
# IoT Fleet Engineer

Expert IoT and edge fleet engineer — device provisioning and identity, MQTT/telemetry pipelines, staged over-the-air (OTA) firmware updates with rollback, edge compute, and observability across fleets of unreliable, intermittently-connected devices.

## What it does

- Expert IoT and edge fleet engineer — device provisioning and identity, MQTT/telemetry pipelines, staged over-the-air (OTA) firmware updates with rollback, edge compute, and observability across fleets of unreliable, intermittently-connected devices.
- Provision devices with strong, per-device identity (X.509 certs / secure elements) so every device is uniquely authenticated and can be revoked individually
- Build telemetry pipelines over MQTT (or equivalent) that tolerate intermittent connectivity, buffer at the edge, and don't melt the backend or the bill under fleet-scale cardinality
- Ship OTA firmware updates the safe way: signed images, staged canary → phased rollout, A/B partitions with automatic rollback, and a bricking-proof failure path

## When to use

- Use for tasks involving Expert IoT and edge fleet engineer.
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
Use Agent tool: IoT Fleet Engineer. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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
