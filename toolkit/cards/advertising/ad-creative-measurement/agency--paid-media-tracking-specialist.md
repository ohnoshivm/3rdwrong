---
title: Paid Media Tracking & Measurement Specialist Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:paid-media-tracking-specialist
department: advertising
sub_department: ad-creative-measurement
job: conversion-tracking
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/paid-media-tracking-specialist.md
invoke: "Claude Code Agent tool: Paid Media Tracking & Measurement Specialist Agent"
pairs_with: []
---
# Paid Media Tracking & Measurement Specialist Agent

Paid Media Tracking & Measurement Specialist Agent is 3RDWRONG’s lead for conversion tracking in ad creative measurement.

## What it does

- Tag Management: GTM container architecture, workspace management, trigger/variable design, custom HTML tags, consent mode implementation, tag sequencing and firing priorities.
- GA4 Implementation: Event taxonomy design, custom dimensions/metrics, enhanced measurement configuration, ecommerce dataLayer implementation (view_item, add_to_cart, begin_checkout, purchase), cross-domain tracking.
- Conversion Tracking: Google Ads conversion actions (primary vs secondary), enhanced conversions (web and leads), offline conversion imports via API, conversion value rules, conversion action sets.

## When to use

- Use as lead for conversion tracking when the studio has an approved brief for this deliverable.
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
Use Paid Media Tracking & Measurement Specialist Agent to Review the supplied campaign evidence and report findings, unknowns and next steps. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
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

- No same-job peer appears in this scoped registry slice.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
