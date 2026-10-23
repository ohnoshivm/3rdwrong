---
title: Budget Pacing Monitor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:budget-pacing-monitor
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to \"check pacing\", \"am I over/under-spending\", \"is this campaign on track to hit budget\", or \"why did spend spike/stall mid-flight\"; returns a spend-vs-target-curve read, learning-phase status, an over/under-delivery call, and a reallocation trigger ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/budget-pacing-monitor/SKILL.md
invoke: "Claude Code: `/budget-pacing-monitor`; Codex: `budget-pacing-monitor` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Budget Pacing Monitor

Budget Pacing Monitor is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- Reads an in-flight campaign's spend against its intended target curve and returns a pacing verdict (On-track / Ahead / Behind / Stalled), the learning-phase status, an over/under-delivery call, and a reallocation trigger when the gap crosses a stated band. This is the in-flight S-lever watcher on the ROAS loop — distinct from budget-optimizer (which sets the initial allocation this skill monitors), bid-strategy-planner (which picks the bid strategy), and ad-account-auditor (which computes the RQS). It owns the spend curve, the pace read, and the reallocation trigger — not the number it started from and not the score.
- Expected output: a pacing read for one campaign or flight — cumulative spend vs the target curve (percent-to-pace), a verdict (On-track / Ahead / Behind / Stalled), the learning-phase status, an over/under-delivery call with the driver (cap-limited, bid-throttled, low-volume, dayparting), and a reallocation trigger (fire / hold) with the band that decided it. Plus a handoff summary storable under memory/ad/budget-pacing-monitor/.
- Writes: a user-facing pacing table plus a reusable pacing summary storable under memory/ad/budget-pacing-monitor/.

## When to use

- Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "check pacing", "am I over/under-spending", "is this campaign on track to hit budget", or "why did spend spike/stall mid-flight"; returns a spend-vs-target-curve read, learning-phase status, an over/under-delivery call, and a reallocation trigger .
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat this tool as authority to launch, change or fund a campaign.
- Do not use without a defined studio-demand or approved client-launch scope and the source data required by the tool.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.
- An approved campaign scope; founder approval before spend.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use Budget Pacing Monitor to Prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a pacing read for one campaign or flight — cumulative spend vs the target curve (percent-to-pace), a verdict (On-track / Ahead / Behind / Stalled), the learning-phase status, an over/under-delivery call with the driver (cap-limited, bid-throttled, low-volume, dayparting), and a reallocation trigger (fire / hold) with the band that decided it. Plus a handoff summary storable under memory/ad/budget-pacing-monitor/.
- spend is read against a target curve fixed before the check (not a bare "spent X of Y"); learning-phase status is confirmed before any over/under-delivery call is acted on; the verdict is one of the four with its percent-to-pace; and the reallocation trigger is fire/hold with the band it crossed named.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] No spend action occurs without founder approval.

## Pairs with

- `agency:marketing-growth-hacker` — same job; use when its own role or trigger applies.
- `agency:marketing-livestream-commerce-coach` — same job; use when its own role or trigger applies.
- `agency:paid-media-creative-strategist` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
