---
title: Paid Media Search Query Analyst Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:paid-media-search-query-analyst
department: advertising
sub_department: search-programmatic
job: query-optimization
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/paid-media-search-query-analyst.md
invoke: "Claude Code Agent tool: Paid Media Search Query Analyst Agent"
pairs_with: []
---
# Paid Media Search Query Analyst Agent

Paid Media Search Query Analyst Agent is 3RDWRONG’s lead for query optimization in search programmatic.

## What it does

- Search Term Analysis: Large-scale search term report mining, pattern identification, n-gram analysis, query clustering by intent.
- Negative Keyword Architecture: Tiered negative keyword lists (account-level, campaign-level, ad group-level), shared negative lists, negative keyword conflicts detection.
- Intent Classification: Mapping queries to buyer intent stages (informational, navigational, commercial, transactional), identifying intent mismatches between queries and landing pages.

## When to use

- Use as lead for query optimization when the studio has an approved brief for this deliverable.
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
Use Paid Media Search Query Analyst Agent to Review the supplied campaign evidence and report findings, unknowns and next steps. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
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
