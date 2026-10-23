---
title: Launch Tier Planner
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch-tier-planner
department: marketing
sub_department: pr-awards
job: launch-planning
role: specialist
trigger: "Use for an approved studio or client launch with the specific launch phase, audience, and assets in scope."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/launch-tier-planner/SKILL.md
invoke: "Claude Code: `/launch-tier-planner`; Codex: `launch-tier-planner` skill"
pairs_with: [skill:launch, skill:launch-window-planner]
---
# Launch Tier Planner

Launch Tier Planner is a 3RDWRONG specialist for launch planning, activated only when its registry trigger applies.

## What it does

- Decides how big a launch is and what kind it is — the tier (Tier 1 flagship all-channel / Tier 2 targeted / Tier 3 changelog-level), the type (new-product / feature / relaunch / partnership), the effort that tier justifies, the KPI targets declared before launch, and the risk register with kill criteria that the day-of runbook inherits. It sits in the Research phase of the RAMP loop and feeds the RAMP R sub-items *launch tier & type declared with effort calibrated*, *risk register exists (likelihood × blast-radius, owners, kill criteria / rollback thresholds)*, and *launch KPI targets (D0/W1/M1) declared before launch*. Sizing the moment correctly is what keeps a changelog entry from burning a Tier-1 audience and a flagship from shipping with a Tier-3 kit.
- Expected output: a tier decision with the three-question rationale, a launch-type declaration (partnership launches include the partner list and co-marketing responsibility split), an effort calibration matrix (tier → channel intensity / asset scope), D0/W1/M1 KPI targets (labeled Estimated / User-provided), a risk register (likelihood × blast-radius, owner, mitigation, kill criteria / rollback thresholds), a T-8w → T+4w timeline skeleton, and the standard handoff summary.
- Writes: a user-facing tier plan + a reusable summary to memory/launch/launch-tier-planner/; the tier/type declaration and any stage/date implication go to memory/events/launches.ndjson via an authorized operation: propose request to registry-events.py for launch-registry to formalize — this skill never writes memory/launch-registry/ directly.

## When to use

- Use for an approved studio or client launch with the specific launch phase, audience, and assets in scope.
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
Use Launch Tier Planner for launch planning at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a tier decision with the three-question rationale, a launch-type declaration (partnership launches include the partner list and co-marketing responsibility split), an effort calibration matrix (tier → channel intensity / asset scope), D0/W1/M1 KPI targets (labeled Estimated / User-provided), a risk register (likelihood × blast-radius, owner, mitigation, kill criteria / rollback thresholds), a T-8w → T+4w timeline skeleton, and the standard handoff summary.
- a tier and type are declared with the three-question rationale stated; the risk register lists likelihood × blast-radius, owner, mitigation, and checkable kill criteria / rollback thresholds for each top risk; and D0/W1/M1 KPI targets exist, each labeled Estimated / User-provided against the user's own trailing baseline (never an invented benchmark).
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `skill:launch` — same job; use when its own role or trigger applies.
- `skill:launch-window-planner` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
