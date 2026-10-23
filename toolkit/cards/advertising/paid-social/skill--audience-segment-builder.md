---
title: Audience Segment Builder
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:audience-segment-builder
department: advertising
sub_department: paid-social
job: audience-targeting
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/audience-segment-builder/SKILL.md
invoke: "Claude Code: `/audience-segment-builder`; Codex: `audience-segment-builder` skill"
pairs_with: []
---
# Audience Segment Builder

Audience Segment Builder is 3RDWRONG’s lead for audience targeting in paid social.

## What it does

- Turns the user's own customer/CRM/GA4 export into seed audiences, value-based lookalike SEED lists, exclusion/suppression segments, and a cross-platform funnel-stage targeting map. It defines who the audiences are and how they are seeded and suppressed — campaign-architect then consumes these segments into account structure and match types; this skill does not build campaigns, and it is distinct from organic keyword-research, which reads SERP intent rather than paid segments.
- Expected output: a set of named audiences in four buckets — (1) seed audiences grouped by trait/behavior, (2) value-based lookalike SEED lists (the high-value seed rows themselves, not a platform key), (3) exclusion/suppression segments (existing customers, recent purchasers, bad-fit), and (4) a funnel-stage targeting map reusable across platforms — with notes that inform the ROAS A (Audience) dimension, plus the standard handoff summary.
- Writes: a user-facing segment plan and reusable summary to memory/ad/audience-segment-builder/.

## When to use

- Use as lead for audience targeting when the studio has an approved brief for this deliverable.
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
Use Audience Segment Builder to Prepare a bounded recommendation for this approved campaign task. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a set of named audiences in four buckets — (1) seed audiences grouped by trait/behavior, (2) value-based lookalike SEED lists (the high-value seed rows themselves, not a platform key), (3) exclusion/suppression segments (existing customers, recent purchasers, bad-fit), and (4) a funnel-stage targeting map reusable across platforms — with notes that inform the ROAS A (Audience) dimension, plus the standard handoff summary.
- each audience is named and grounded in an exported column; value-based seeds are ranked by the user's own value field; exclusion segments cover existing customers and recent purchasers (window stated); the funnel-stage map is platform-neutral; and the ROAS A relevance of each bucket is noted (or flagged NEEDS_INPUT).
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
