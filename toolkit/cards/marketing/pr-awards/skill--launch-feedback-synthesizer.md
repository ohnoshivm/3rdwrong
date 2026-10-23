---
title: Launch Feedback Synthesizer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch-feedback-synthesizer
department: marketing
sub_department: pr-awards
job: launch-measurement
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/launch-feedback-synthesizer/SKILL.md
invoke: "Claude Code: `/launch-feedback-synthesizer`; Codex: `launch-feedback-synthesizer` skill"
pairs_with: [skill:launch-monitor, skill:launch-retro-analyzer]
---
# Launch Feedback Synthesizer

Launch Feedback Synthesizer is a 3RDWRONG specialist for launch measurement, activated only when its registry trigger applies.

## What it does

- Triages the feedback a launch generates — channel comments, store reviews, feedback-board posts, support tickets — into themes, runs each theme through a visible status loop, and turns shipped changes and happy users into compliant social proof. This is the feedback lever of the RAMP Prove phase: it feeds the P feedback-loop sub-item (themes, status transitions, requester notification) and the P social-proof-pipeline sub-item (no incentivized store reviews) of the RAMP benchmark. It works one lever and hands off — launch-readiness-auditor rolls the P dimension into the RAMP profile result; this skill never computes it.
- Expected output: a feedback theme digest (per theme: frequency, severity, representative quotes), a status-loop spec (transitions, duplicate-merge rule, notification rules), "you asked, we shipped" announcement material for completed themes, a social-proof harvest protocol with a platform compliance matrix, and the standard handoff summary.
- Writes: a user-facing digest + a reusable summary to memory/launch/launch-feedback-synthesizer/; the theme snapshot is submitted to memory/events/launches.ndjson via an authorized operation: propose request to registry-events.py for launch-registry to formalize — this skill never writes memory/launch-registry/ records directly; unadjudicated product/comparative claims found in feedback go to memory/events/claims.ndjson via an authorized operation: propose request to registry-events.py.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
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
Use Launch Feedback Synthesizer for launch measurement at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a feedback theme digest (per theme: frequency, severity, representative quotes), a status-loop spec (transitions, duplicate-merge rule, notification rules), "you asked, we shipped" announcement material for completed themes, a social-proof harvest protocol with a platform compliance matrix, and the standard handoff summary.
- themes are clustered with frequency (Measured from the exports), severity, and at least one verbatim quote each; the status loop states its transitions, the duplicate-merge rule, and the notification rule (all subscribers minus the actor; unchanged status = no-op); and the harvest protocol includes a platform compliance matrix with store reviews marked never-incentivized.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `skill:launch-monitor` — same job; use when its own role or trigger applies.
- `skill:launch-retro-analyzer` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
