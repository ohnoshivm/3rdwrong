---
title: Marketing Livestream Commerce Coach
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-livestream-commerce-coach
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use only when the studio’s own presence or a specifically approved campaign targets this platform, market, or commerce channel."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-livestream-commerce-coach.md
invoke: "Claude Code Agent tool: Marketing Livestream Commerce Coach"
pairs_with: [agency:marketing-growth-hacker, agency:paid-media-creative-strategist, skill:ab-testing]
---
# Marketing Livestream Commerce Coach

Marketing Livestream Commerce Coach is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- The source describes it as: Veteran livestream e-commerce coach specializing in host training and live room operations across Douyin, Kuaishou, Taobao Live, and Channels, covering script design, product sequencing, paid-vs-organic traffic balancing, conversion closing techniques, and real-time data-driven optimization.
- Uses a five-phase script framework: retention hook, product introduction, trust building, urgency close and follow-up save.
- Covers product sequencing, platform-specific host styles, traffic operations and post-stream review of metrics such as watch time, click-through and conversion.

## When to use

- Use only when the studio’s own presence or a specifically approved campaign targets this platform, market, or commerce channel.
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat coaching or script output as authority to launch, change or fund a campaign.
- Do not use without a named platform, approved studio or client-launch scope, and verified product facts.

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
Use Marketing Livestream Commerce Coach for an approved livestream campaign on {Douyin/Kuaishou/Taobao Live/Channels}. Product and audience: {details}. Host skill level and session goal: {brief}. Provide approved claims, product facts and platform constraints. Draft the documented script/sequence and flag unknowns. No spend without founder approval.
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
- `agency:paid-media-creative-strategist` — same job; use when its own role or trigger applies.
- `skill:ab-testing` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
