---
title: Campaign Planner
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:campaign-planner
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to \"plan an influencer campaign\", \"build a campaign blueprint\", \"track or close a creator campaign\", or \"record a late campaign correction\"; produces the plan and, when requested, a non-canonical evidence tracker with scoped identity, publication, reconciliation, close, and reopen receipts ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/campaign-planner/SKILL.md
invoke: "Claude Code: `/campaign-planner`; Codex: `campaign-planner` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Campaign Planner

Campaign Planner is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- The source describes it as: Use when the user asks to "plan an influencer campaign", "build a campaign blueprint", "track or close a creator campaign", or "record a late campaign correction"; produces the plan and, when requested, a non-canonical evidence tracker with scoped identity, publication, reconciliation, close, and reopen receipts. Not for individual creator briefs — use brief-generator; not for overall product launches without creators — use launch-tier-planner; not for sending, publishing, amplifying, or paying — use the owning execution workflow. 达人营销策划/种草方案/活动追踪与关账.
- The selected mode is explicit: plan-only completes §§1–9, tracker-only completes only §10 from its required existing inputs, and both completes §§1–9 before §10.
- In a plan-authoring mode, objectives, strategy, influencer mix, deliverables, timeline, budget allocation, contingency, and KPIs are concrete only where the user supplied them or a compatible source-dated planning anchor supports them. Every unsupported required choice stays NEEDS_INPUT; the skill never fills it from a repository default. The §8 measurement design is execution-locked only when its campaign/plan binding, immutable plan hash/version, authorization, non-empty creator scope, and unique per-creator/deliverable checkpoints are present; otherwise report the exact lock inputs as NEEDS_INPUT/DONE_WITH_CONCERNS and do not create a close-eligible tracker.

## When to use

- Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "plan an influencer campaign", "build a campaign blueprint", "track or close a creator campaign", or "record a late campaign correction"; produces the plan and, when requested, a non-canonical evidence tracker with scoped identity, publication, reconciliation, close, and reopen receipts .
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
Use Campaign Planner to prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
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
