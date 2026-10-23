---
title: Marketing Growth Hacker Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-growth-hacker
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-growth-hacker.md
invoke: "Claude Code Agent tool: Marketing Growth Hacker Agent"
pairs_with: [agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist, skill:ab-testing]
---
# Marketing Growth Hacker Agent

Marketing Growth Hacker Agent is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- Growth Strategy: Funnel optimization, user acquisition, retention analysis, lifetime value maximization.
- Experimentation: A/B testing, multivariate testing, growth experiment design, statistical analysis.
- Analytics & Attribution: Advanced analytics setup, cohort analysis, attribution modeling, growth metrics.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat this tool as authority to launch, change or fund a campaign.
- Do not use without an approved growth question, baseline evidence and named decision owner.

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
Use Marketing Growth Hacker Agent to Prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
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

- `agency:marketing-livestream-commerce-coach` — same job; use when its own role or trigger applies.
- `agency:paid-media-creative-strategist` — same job; use when its own role or trigger applies.
- `skill:ab-testing` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
