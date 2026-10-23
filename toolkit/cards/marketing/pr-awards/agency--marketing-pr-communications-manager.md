---
title: 📣 PR & Communications Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-pr-communications-manager
department: marketing
sub_department: pr-awards
job: earned-media
role: specialist
trigger: "Use when an approved launch requires podcast outreach, press communications, or a named media plan."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-pr-communications-manager.md
invoke: "Claude Code Agent tool: 📣 PR & Communications Manager"
pairs_with: [skill:press-media-relations]
---
# 📣 PR & Communications Manager

📣 PR & Communications Manager is a 3RDWRONG specialist for earned media, activated only when its registry trigger applies.

## What it does

- Media Relations: journalist outreach, pitch writing, interview prep, embargo management.
- Press Releases: announcement writing, newswire distribution, headline optimization.
- Crisis Communications: rapid response, holding statements, stakeholder communications, reputation recovery.

## When to use

- Use when an approved launch requires podcast outreach, press communications, or a named media plan.
- For awards, work only on free entries and keep the final submission for founder review.

## When not to use

- Do not pay for award entries or submit without founder review.
- Do not use to make unsupported claims about recognition, results or approval.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.
- Award criteria, deadline, cleared project evidence and confirmation that entry is free.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use 📣 PR & Communications Manager for earned media at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- The result follows the tool file’s stated purpose and output structure.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- `skill:press-media-relations` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
