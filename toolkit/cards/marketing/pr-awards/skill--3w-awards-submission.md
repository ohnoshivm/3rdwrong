---
title: Awards submission
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-awards-submission
department: marketing
sub_department: pr-awards
job: awards-submissions
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-awards-submission/SKILL.md
invoke: "3w-awards-submission skill"
pairs_with: [agency:marketing-pr-communications-manager, skill:press-media-relations, skill:3w-care-retention]
---
# Awards submission

The studio's lead tool for awards submissions: fit check, permission, free-only rule (D-0024), checklist, entry text and results log. Registered job lead; the skill remains experimental.

## What it does

- Reads the award's official criteria with an access date.
- Runs the fit check and the client-permission check before any preparation.
- Blocks any fee while D-0024 holds.
- Prepares entry text and logs results in the platform's wording.

## When to use

- After L7 launch for digital work, at L9 for identity work, for strong self-initiated work, and in the monthly growth review.

## When not to use

- Paid awards while the budget is zero.
- Changing client work for a jury.
- Press relations — `skill:press-media-relations`.

## Inputs it needs

- Live work or case study and credits.
- Client permission or self-initiated label.
- Official criteria, deadline and fee.
- Engineering performance and accessibility notes.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-awards-submission skill for {{work}} and {{award}}. Official criteria page: {{URL}} (read {{date}}). Permission: {{record | self-initiated}}. Return the award entry record; do not submit.
```

## What good output looks like

- Fit decision with reason, permission reference and fee status.
- Entry text with no undocumented claims.

## Quality checks

- [ ] Criteria cited with date.
- [ ] No fee committed.
- [ ] No award claim before the official result.

## Pairs with

- Neighbour: `agency:marketing-pr-communications-manager` (earned-media specialist; its business-award template does not fit design juries).
- Upstream: case studies and close-out from `skill:3w-care-retention`.

## Limits and cautions

- Experimental skill; awards reflect a jury's lens, not commercial effect.
- Founder signs off every entry.
