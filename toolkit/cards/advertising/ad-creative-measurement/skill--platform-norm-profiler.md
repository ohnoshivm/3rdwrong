---
title: Platform Norm Profiler
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:platform-norm-profiler
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/platform-norm-profiler/SKILL.md
invoke: "Claude Code: `/platform-norm-profiler`; Codex: `platform-norm-profiler` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Platform Norm Profiler

Platform Norm Profiler is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- Maintains the dated, versioned per-platform norm cards the Craft phase drafts against — char limits, visible-fold cutoffs, hashtag norms, format/aspect specs, link and first-comment placement, disclosure-label mechanics, and algorithm emphases — every row labeled platform-documented (Measured, official doc) or Estimated-folklore (named source) with a last-verified date. It feeds four ECHO sub-items directly: the three C dated-norm-card items — platform adaptation, never verbatim cross-posting (C3), format specs citing the dated card (C4), and link/first-comment placement per the card (C9) — plus the E rule-digest-current item (E4). social-quality-auditor judges those items against the cards this skill keeps fresh. The anti-staleness rule is the whole point: a norm card older than its review-by date is flagged, not trusted.
- Expected output: added or refreshed organic-engagement sections in the in-scope cards under references/platforms/ (each row: value + label + source + last-verified + review-by dates), a staleness report over the cards touched, rule-snapshot pointer candidates for the active channels, and the standard handoff summary.
- Writes: the organic-engagement section of each in-scope card in references/platforms/ (the single pack, edited in place); a dated profiling log and staleness report to memory/social/platform-norm-profiler/.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat this tool as authority to launch, change or fund a campaign.
- Do not use to draft campaign creative; use the appropriate creative tool after norms are current. Source docs or a named folklore source are required for each norm.

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
Use Platform Norm Profiler to Prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- added or refreshed organic-engagement sections in the in-scope cards under references/platforms/ (each row: value + label + source + last-verified + review-by dates), a staleness report over the cards touched, rule-snapshot pointer candidates for the active channels, and the standard handoff summary.
- every in-scope card's organic-engagement rows carry a label — platform-documented (Measured, official doc URL + retrieval date) or Estimated-folklore (named source) — plus last-verified and review-by dates; every card past review-by is flagged stale; and a pointer candidate is submitted for each active channel touched.
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
