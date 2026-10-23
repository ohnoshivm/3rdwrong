---
title: Analytics Tracking
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:analytics
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/skills/analytics/SKILL.md
invoke: "Claude Code: `/analytics`; Codex: `analytics` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Analytics Tracking

Analytics Tracking is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- The source describes it as: When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4," "Google Analytics," "conversion tracking," "event tracking," "UTM parameters," "tag manager," "GTM," "analytics implementation," "tracking plan," "how do I measure this," "track conversions," "Mixpanel," "Segment," "are my events firing," or "analytics isn't working." Use this whenever someone asks how to know if something is working or wants to measure marketing results. For choosing attribution models, comparing multi-touch/MMM/incrementality, or reconciling conflicting numbers across tools, see attribution. For A/B test measurement, see ab-testing. Rate metrics divide matching closed windows — never full-period spend by partial-period results.
- Every event should inform a decision.
- Quality > quantity of events.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat analytics setup as authority to launch, change or fund an advertising campaign.
- Do not use without an approved measurement question, site/property context and the access or exports the tool requires.

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
Use Analytics Tracking for an approved studio-demand or client-launch measurement task. Site/property and access status: {details}. Business question and events: {brief}. Existing analytics stack and implementation constraints: {details}. Return the source-documented setup/review and state what remains unverified.
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
