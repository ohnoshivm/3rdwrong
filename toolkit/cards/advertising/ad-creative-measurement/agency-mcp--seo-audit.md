---
title: SEO audit
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency-mcp:seo-audit
department: advertising
sub_department: ad-creative-measurement
job: account-audit
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-agency-mcp-marketplace/skills/seo-audit/SKILL.md
invoke: "Agency MCP server: agency-mcp; skill: seo-audit"
pairs_with: [agency:paid-media-auditor, skill:ad-account-auditor]
---
# SEO audit

SEO audit is a 3RDWRONG specialist for account audit, activated only when its registry trigger applies.

## What it does

- The source describes it as: Audits a client's organic search health using Search Console, Google Analytics and the live WordPress site through the Agency MCP connector. Use when asked how a client's SEO is doing, why traffic dropped, what ranks, what to fix first, or for a monthly SEO review. Also use for "which pages are losing clicks", "what queries are we close to page one on", or "audit this site". Not for paid search (use google-ads-manager) or for writing content (use seo-content).
- Rankings and clicks — gsc_query with dimensions ["query"] for both periods (row_limit 500). Then ["page"] for both periods.
- Position 4–15 opportunities — from the query rows, list terms with impressions ≥ 50 and position between 4 and 15: these move with on-page work.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not use this organic-search audit as a paid-ad account audit or authority to launch, change or fund a campaign.
- Do not use without Search Console/GA4 evidence and a defined studio-demand or approved client-launch site in scope.

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
Use SEO audit to review organic search health for the specifically approved studio-demand site or client launch. Search Console and GA4 property/site: {approved property}. Compare date ranges: {ranges}. Include WordPress access only if the site is WordPress. Report source-backed findings and next actions; do not treat this as a paid-account audit.
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

- `agency:paid-media-auditor` — same job; use when its own role or trigger applies.
- `skill:ad-account-auditor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
