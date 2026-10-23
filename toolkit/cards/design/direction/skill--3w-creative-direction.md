---
title: 3W Creative Direction
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-creative-direction
department: design
sub_department: direction
job: concept-direction
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: vendor
source: skills/3w-creative-direction
invoke: "3w-creative-direction skill"
pairs_with: [skill:3w-category-code-audit, agent:creative-director, skill:3w-identity-system-critic]
---

# 3W Creative Direction

The identity concept lead that turns signed strategy into distinct idea routes before visual polish. For 3RDWRONG, this is the lead tool for concept direction.

## What it does

- Verifies strategy sign-off, version, date and approver before route work.
- Develops at least three ideas with different organising logic, not palette or type variations.
- Writes each idea without visual adjectives, links rationale to strategy and records risks and a disconfirming test.
- Separates recommendation from approval and provides a route comparison.

## When to use

- After the phase 03 strategy gate, when the signed version, criteria and constraints are available.
- For early identity exploration, not final production artwork.

## When not to use

- When strategy is missing, provisional or disputed; resolve the strategy gate first.
- Final visual QA or production artwork; hand off to craft and independent QA.

## Inputs it needs

- Signed strategy with approver, date and version.
- Audience, positioning, proof boundaries, creative criteria, category audit and constraints.

## How to run it

1. Invoke the `3w-creative-direction` skill from the repository.
2. Supply verified strategy and constraints; request at least three materially different routes.
3. Review the route comparison with an independent creative lead; record founder selection separately.

```text
Use 3w-creative-direction skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Three distinct ideas pass the no-visual-adjectives test and include risks and tests.
- No claims of audience response, originality, rights clearance or approval without evidence/review.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-category-code-audit` — upstream context or hand-off.
- `agent:creative-director` — downstream review or delivery.
- `skill:3w-identity-system-critic` — downstream review or delivery.

## Limits and cautions

- Stop if strategy sign-off or consequential constraints are missing.
- Route selection for development is not visual sign-off.
- AI assistance needs human originality and rights review; evidence labels are required.
