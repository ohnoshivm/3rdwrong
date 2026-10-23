---
title: Launch Monitor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch-monitor
department: marketing
sub_department: pr-awards
job: launch-measurement
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/launch-monitor/SKILL.md
invoke: "Claude Code: `/launch-monitor`; Codex: `launch-monitor` skill"
pairs_with: [skill:launch-feedback-synthesizer, skill:launch-retro-analyzer]
---
# Launch Monitor

Launch Monitor is 3RDWRONG’s lead for launch measurement in pr awards.

## What it does

- Watches the launch window — T-0 through T+30 — so traction is verifiable while it happens, not reconstructed afterwards. It is the first Prove-phase skill in the RAMP loop: its pre-launch mode verifies measurement instrumentation on every launch surface (the direct upstream of the P1 veto — untagged surfaces make traction unverifiable), and its window mode feeds the RAMP P sub-items for instrumentation, per-channel attribution reconciled against own analytics, KPI actuals vs targets at D0/W1/M1, spike-vs-sustain retention, and owned-capture rate. The live watch itself is the evidence behind the M live-monitoring-coverage sub-item.
- Expected output: a pre-launch instrumentation verification report (per-surface UTM/event pass-fail) or a window telemetry read — polling log, flamewar/anomaly alerts, D0/W1/M1 KPI snapshot vs targets, spike-vs-sustain and owned-capture reads — every number labeled Measured / User-provided / Estimated, plus the standard handoff summary.
- Writes: snapshots + a reusable summary to memory/launch/launch-monitor/; the outcome-snapshot facts (peak rank, D0/W1/M1 actuals, window close) are submitted to memory/events/launches.ndjson via an authorized operation: propose request to registry-events.py — this skill never writes memory/launch-registry/ directly.

## When to use

- Use as lead for launch measurement when the studio has an approved brief for this deliverable.
- For awards, work only on free entries and keep the final submission for founder review.

## When not to use

- Do not pay for award entries or submit without founder review.
- Do not use to make unsupported claims about recognition, results or approval.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.
- Award criteria, deadline, cleared project evidence and confirmation that entry is free.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use Launch Monitor for launch measurement at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a pre-launch instrumentation verification report (per-surface UTM/event pass-fail) or a window telemetry read — polling log, flamewar/anomaly alerts, D0/W1/M1 KPI snapshot vs targets, spike-vs-sustain and owned-capture reads — every number labeled Measured / User-provided / Estimated, plus the standard handoff summary.
- instrumentation is verified per surface against the current manifest (pre-launch actions are explicitly not-yet-due, not missing); every window/outcome snapshot binds to the measurement contract and matched receipts for actions that are due or attempted; missing/partial/unknown due receipts keep the affected lane and close join open; actuals vs targets preserve truth/reference labels; and every alert names its threshold and KPI target.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `skill:launch-feedback-synthesizer` — same job; use when its own role or trigger applies.
- `skill:launch-retro-analyzer` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
