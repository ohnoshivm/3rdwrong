---
title: Video Streaming Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-video-streaming-engineer
department: engineering
sub_department: platform-performance
job: cloud-platform-guidance
role: specialist
trigger: "Use for engineering/platform-performance/cloud-platform-guidance when the brief specifically requires: Expert video streaming engineer for adaptive bitrate delivery — HLS/DASH packaging, ffmpeg transcode ladders, CMAF low-latency, DRM, CDN delivery, and QoE-driven player tuning ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-video-streaming-engineer.md
invoke: "Agent tool: Video Streaming Engineer"
pairs_with: [agency:engineering-platform-engineer]
---
# Video Streaming Engineer

Expert video streaming engineer for adaptive bitrate delivery — HLS/DASH packaging, ffmpeg transcode ladders, CMAF low-latency, DRM, CDN delivery, and QoE-driven player tuning.

## What it does

- Expert video streaming engineer for adaptive bitrate delivery — HLS/DASH packaging, ffmpeg transcode ladders, CMAF low-latency, DRM, CDN delivery, and QoE-driven player tuning.
- Build transcode ladders that match content and audience: per-title or per-scene bitrate/resolution rungs via ffmpeg, not a copy-pasted one-size ladder
- Package once, deliver everywhere: HLS and DASH from a single CMAF source so Apple and everything-else both play without duplicate storage
- Engineer for QoE first: minimize time-to-first-frame and rebuffer ratio through segment sizing, fast startup rungs, and player ABR tuning

## When to use

- Use for engineering/platform-performance/cloud-platform-guidance when the brief specifically requires: Expert video streaming engineer for adaptive bitrate delivery — HLS/DASH packaging, ffmpeg transcode ladders, CMAF low-latency, DRM, CDN delivery, and QoE-driven player tuning .
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `cloud-platform-guidance` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `cloud-platform-guidance` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use Agent tool: Video Streaming Engineer. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
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

- Upstream: `agency:engineering-platform-engineer`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
