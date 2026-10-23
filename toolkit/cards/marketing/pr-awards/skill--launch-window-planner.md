---
title: Launch Window Planner
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch-window-planner
department: marketing
sub_department: pr-awards
job: launch-planning
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/launch-window-planner/SKILL.md
invoke: "Claude Code: `/launch-window-planner`; Codex: `launch-window-planner` skill"
pairs_with: [skill:launch, skill:launch-tier-planner]
---
# Launch Window Planner

Launch Window Planner is 3RDWRONG’s lead for launch planning in pr awards.

## What it does

- Picks when to launch — the timing lever of the RAMP loop Research phase. It scans industry-event and conference cycles, maps the competitor launch calendar, pads for store-review latency, chooses a launch-week vs rolling format, and defines the embargo window (lift moment + timezone). It feeds the RAMP-R timing sub-item ("timing window chosen deliberately — event cycles, competitor calendar, review-latency buffers") and the RAMP-M embargo-coordination sub-item ("embargo & partner commitments coordinated against one authoritative date/stage") per ramp-benchmark.md. It works one lever — timing — and hands off.
- Expected output: a candidate-window comparison table (conflict / tailwind / risk per window), a launch-week vs rolling format call with rationale, store-review buffer padding (labeled Estimated), an embargo window definition (lift moment + timezone + committed parties), and the standard handoff summary.
- Writes: the window comparison + recommendation to memory/launch/launch-window-planner/; the chosen window, buffer, and embargo facts are submitted to memory/events/launches.ndjson via an authorized operation: propose request to registry-events.py for launch-registry to formalize — this skill never writes memory/launch-registry/ directly.

## When to use

- Use as lead for launch planning when the studio has an approved brief for this deliverable.
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
Use Launch Window Planner for launch planning at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a candidate-window comparison table (conflict / tailwind / risk per window), a launch-week vs rolling format call with rationale, store-review buffer padding (labeled Estimated), an embargo window definition (lift moment + timezone + committed parties), and the standard handoff summary.
- at least two candidate windows are compared with conflict / tailwind / risk columns; the launch-week vs rolling call is stated with its tradeoff; the embargo window names a lift moment + timezone (or embargo is marked not-applicable); and every timing input is labeled Measured / User-provided / Estimated with its source — platform timing lore is never presented as a rule.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `skill:launch` — same job; use when its own role or trigger applies.
- `skill:launch-tier-planner` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
