---
title: Launch Retro Analyzer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch-retro-analyzer
department: marketing
sub_department: pr-awards
job: launch-measurement
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/launch-retro-analyzer/SKILL.md
invoke: "Claude Code: `/launch-retro-analyzer`; Codex: `launch-retro-analyzer` skill"
pairs_with: [skill:launch-feedback-synthesizer, skill:launch-monitor]
---
# Launch Retro Analyzer

Launch Retro Analyzer is a 3RDWRONG specialist for launch measurement, activated only when its registry trigger applies.

## What it does

- Runs the structured D1/W1/M1 retrospective after a launch: the per-channel actual-vs-target read, the 5-Whys on the single largest miss, the keep / kill / change call per channel, and the 3-5 learnings that change the next launch. It sits in the Prove phase of the RAMP loop (Research → Assemble → Mobilize → Prove) and feeds the RAMP P retro sub-items — retro completed (channel actual-vs-target, 5-Whys on misses, keep/kill) and learnings promoted to memory + the launch-registry outcome snapshot — plus the P attribution discipline that own UTM-attributed analytics, not platform self-reported numbers, are the truth column. See ramp-benchmark.md.
- Expected output: a D1/W1/M1 launch retrospective bound to the current manifest, complete action-receipt set, and predeclared measurement contract — a per-channel actual-vs-target table, one 5-Whys chain, keep / kill / change decisions, 3-5 learning entries, an outcome proposal, and the standard handoff summary. Missing receipts or an incomplete measurement window keep the retro provisional.
- Writes: the user-facing retro + a reusable summary to memory/launch/launch-retro-analyzer/; the outcome snapshot to memory/events/launches.ndjson via an authorized operation: propose request to registry-events.py for launch-registry to attach to the launch dossier — never memory/launch-registry/ records directly.

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
Use Launch Retro Analyzer for launch measurement at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a D1/W1/M1 launch retrospective bound to the current manifest, complete action-receipt set, and predeclared measurement contract — a per-channel actual-vs-target table, one 5-Whys chain, keep / kill / change decisions, 3-5 learning entries, an outcome proposal, and the standard handoff summary. Missing receipts or an incomplete measurement window keep the retro provisional.
- every required current-manifest action has a matching terminal receipt; the measurement contract/window and actual-vs-target evidence are complete and labeled; one 5-Whys chain exists; every channel carries a reasoned keep/kill/change call; and 3-5 learnings plus the bound outcome proposal are delivered. Missing receipts, targets, or window evidence produce retro_status: PROVISIONAL | NEEDS_INPUT, never a closed launch.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `skill:launch-feedback-synthesizer` — same job; use when its own role or trigger applies.
- `skill:launch-monitor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
