---
title: Press Media Relations
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:press-media-relations
department: marketing
sub_department: pr-awards
job: earned-media
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/press-media-relations/SKILL.md
invoke: "Claude Code: `/press-media-relations`; Codex: `press-media-relations` skill"
pairs_with: [skill:launch-asset-packager, skill:launch-monitor]
---
# Press Media Relations

Press Media Relations is 3RDWRONG’s earned-media lead for approved studio and client launches.

## What it does

- Runs the media and analyst motion of a launch: a three-tier media list sized to the launch tier, embargo terms and a pitch timing skeleton keyed to the authoritative launch date, a press-release draft in standard structure, and an analyst briefing outline. It sits in the Mobilize phase of the RAMP loop and feeds two RAMP-M sub-items — *embargo & partner commitments coordinated against one authoritative date/stage* and *media/analyst/community activation right-sized and personalized under embargo sequence* (ramp-benchmark.md). It works one lever — the media/analyst channel — and hands off: the pitch sequence goes to the outreach engine for execution, and every date/stage commitment is judged against the launch-registry record, never against a date this skill picks.
- Expected output: a three-tier media/analyst list (Tier 1 exclusive candidates, Tier 2 vertical press, Tier 3 communities and newsletters) with a per-contact angle, embargo terms plus a pitch timing skeleton (cadence labeled Estimated; lift moment from the launch-registry record), a press-release draft with zero fabricated quotes or numbers, an analyst briefing outline, and the standard handoff summary.
- Writes: the media plan + release/briefing drafts to memory/launch/press-media-relations/; embargo and exclusive commitments to memory/events/launches.ndjson via an authorized operation: propose request to registry-events.py (the registry formalizes them — this skill never writes memory/launch-registry/ records directly); any unsubstantiated product/comparative claim to memory/events/claims.ndjson via an authorized operation: propose request to registry-events.py marked [needs source].

## When to use

- Use as lead for earned media when the studio has an approved brief for this deliverable.
- Awards submissions are not documented as this tool’s function; if a separate approved entry is in scope, it must be free and founder reviewed.

## When not to use

- Do not treat earned-media planning as award-submission support; do not pay entry fees.
- Do not use to make unsupported claims about recognition, results or approval.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.
- Launch tier, authoritative launch date/stage, approved claims and message house, target verticals and source material for the release.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use Press Media Relations for earned media at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a three-tier media/analyst list (Tier 1 exclusive candidates, Tier 2 vertical press, Tier 3 communities and newsletters) with a per-contact angle, embargo terms plus a pitch timing skeleton (cadence labeled Estimated; lift moment from the launch-registry record), a press-release draft with zero fabricated quotes or numbers, an analyst briefing outline, and the standard handoff summary.
- the three tiers are populated and right-sized to the launch tier with one named angle per Tier-1/Tier-2 contact; embargo terms and the timing skeleton reference the launch-registry date (or the missing record is flagged as an open loop); and the press-release draft contains no invented quote or number — every claim traces to the ledger or carries [needs source].
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `agency:marketing-pr-communications-manager` — specialist for approved launch communications; activate only on its trigger.
- `skill:launch-asset-packager` — build the press kit assets this media plan links to.
- `skill:launch-monitor` — track the post-launch coverage echo after outreach.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
