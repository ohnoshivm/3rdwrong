---
title: Launch Strategy
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch
department: marketing
sub_department: pr-awards
job: launch-planning
role: specialist
trigger: "Use for an approved studio or client launch with the specific launch phase, audience, and assets in scope."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/skills/launch/SKILL.md
invoke: "Claude Code: `/launch`; Codex: `launch` skill"
pairs_with: [skill:launch-tier-planner, skill:launch-window-planner]
---
# Launch Strategy

Launch Strategy is a 3RDWRONG specialist for launch planning, activated only when its registry trigger applies.

## What it does

- The source describes it as: When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user mentions 'launch,' 'Product Hunt,' 'feature release,' 'announcement,' 'go-to-market,' 'beta launch,' 'early access,' 'waitlist,' 'product update,' 'how do I launch this,' 'site launch,' 'go live,' 'pre-launch QA,' 'launch checklist,' 'GTM plan,' 'we're about to ship,' 'changelog,' 'release notes,' or 'what did we ship this week.' Use this whenever someone is preparing to release something publicly. For ongoing marketing after launch, see marketing-ideas. For the offer being launched (bonuses, guarantees, scarcity, naming), see offers.
- Getting your product into users' hands early.
- Learning from real feedback.

## When to use

- Use for an approved studio or client launch with the specific launch phase, audience, and assets in scope.
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
Use Launch Strategy for launch planning at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
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

- `skill:launch-tier-planner` — same job; use when its own role or trigger applies.
- `skill:launch-window-planner` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
