---
title: Bid Strategy Planner
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:bid-strategy-planner
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to \"pick a bid strategy\", \"set a tCPA/tROAS target\", or \"plan the learning-phase entry\"; produces a bid-strategy choice (tCPA / tROAS / max-conversions / manual CPC), the starting target math, a portfolio grouping map, and a learning-phase entry plan ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/bid-strategy-planner/SKILL.md
invoke: "Claude Code: `/bid-strategy-planner`; Codex: `bid-strategy-planner` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Bid Strategy Planner

Bid Strategy Planner is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- The source describes it as: Use when the user asks to "pick a bid strategy", "set a tCPA/tROAS target", or "plan the learning-phase entry"; produces a bid-strategy choice (tCPA / tROAS / max-conversions / manual CPC), the starting target math, a portfolio grouping map, and a learning-phase entry plan. Not for splitting the budget across campaigns — use budget-optimizer; not for in-flight pacing/scale moves — use budget-pacing-monitor; not for scoring the account — use ad-account-auditor. 出价策略/tCPA目标/tROAS/学习期.
- ~~web analytics (GA4, own-data manual export) — actual CPA/ROAS and conversion counts to replace estimated history.
- ~~ecommerce (own-data manual export) — order-level ROAS and revenue for a tROAS target instead of a benchmark range.

## When to use

- Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "pick a bid strategy", "set a tCPA/tROAS target", or "plan the learning-phase entry"; produces a bid-strategy choice (tCPA / tROAS / max-conversions / manual CPC), the starting target math, a portfolio grouping map, and a learning-phase entry plan .
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
Use Bid Strategy Planner to prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- The result follows the tool file’s stated purpose and output structure.
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
