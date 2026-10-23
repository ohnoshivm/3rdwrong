---
title: Product Feed Optimizer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:product-feed-optimizer
department: advertising
sub_department: search-programmatic
job: shopping-feeds
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/product-feed-optimizer/SKILL.md
invoke: "Claude Code: `/product-feed-optimizer`; Codex: `product-feed-optimizer` skill"
pairs_with: []
---
# Product Feed Optimizer

Product Feed Optimizer is 3RDWRONG’s lead for shopping feeds in search programmatic.

## What it does

- Audits and rewrites the Shopping / Performance Max product feed — title and description patterns, required and recommended attributes, GTIN/availability/price hygiene, disapproval triage, and feed-driven asset-group / listing-group structure. This is the research-phase skill that hardens the product data behind the ROAS O (Offer) dimension; it does not write text-ad copy (that is ad-creative-builder) and does not score the account or compute the RQS (that is ad-account-auditor).
- Expected output: a feed remediation package — (1) a disapproval / diagnostics triage table (item → cause → fix), (2) rewritten titles + descriptions to a front-loaded attribute pattern, (3) an attribute-completeness map (required + recommended, per item, with the missing fields named), (4) identifier/availability/price hygiene fixes (GTIN, availability, price vs landing page), and (5) a feed-driven asset-group / listing-group structure — with notes that inform the ROAS O (Offer) dimension, plus the standard handoff summary.
- Writes: a user-facing feed remediation package and reusable summary to memory/ad/product-feed-optimizer/.

## When to use

- Use as lead for shopping feeds when the studio has an approved brief for this deliverable.
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
Use Product Feed Optimizer to Prepare a bounded recommendation for this approved campaign task. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a feed remediation package — (1) a disapproval / diagnostics triage table (item → cause → fix), (2) rewritten titles + descriptions to a front-loaded attribute pattern, (3) an attribute-completeness map (required + recommended, per item, with the missing fields named), (4) identifier/availability/price hygiene fixes (GTIN, availability, price vs landing page), and (5) a feed-driven asset-group / listing-group structure — with notes that inform the ROAS O (Offer) dimension, plus the standard handoff summary.
- every disapproved item has a named cause and a proposed fix; each rewritten title front-loads the highest-intent attributes within the platform's character limit; required attributes are present or flagged per item; price/availability in the feed match the landing page (or the mismatch is flagged); no title or description carries an unsubstantiated claim or a likely policy violation; and the listing-group / asset-group structure maps to real feed segments.
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
