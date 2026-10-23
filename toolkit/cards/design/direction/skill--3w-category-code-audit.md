---
title: 3W Category Code Audit
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-category-code-audit
department: design
sub_department: direction
job: category-audit
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: vendor
source: skills/3w-category-code-audit
invoke: "3w-category-code-audit skill"
pairs_with: [skill:3w-creative-direction, skill:taste-skill]
---

# 3W Category Code Audit

The category-audit lead for making visible identity conventions inspectable before positioning or concept work. For 3RDWRONG, this is the lead tool for category audit.

## What it does

- Codes linked examples across logo form, typography, colour, imagery, language and layout.
- Tallies conventions with counts and denominators, separating entry codes from clichés.
- Labels visible details Documented, interpretations Interpretation and candidate white space Hypothesis.
- Produces a source register, coding table, conventions, candidate tests, unknowns and unsupported claims.

## When to use

- Phase 02 Diagnosis or concept development when category distinction matters and a linked sample is available.
- Before mood-board selection, so references are coded systematically rather than selected only for taste.

## When not to use

- Without verifiable source links or to claim a category-wide pattern from a few famous brands.
- To claim consumer response, sales or market opportunity from visual inspection; use research with suitable evidence.

## Inputs it needs

- Bounded category, geography, channel and observation date.
- At least eight distinct examples with working source links, plus the strategy question and coding rules.

## How to run it

1. Invoke the `3w-category-code-audit` skill in the repository.
2. Provide eight or more linked examples, scope, selection method and bias.
3. Review the exact audit schema and keep a human check before concept use.

```text
Use 3w-category-code-audit skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Eight or more examples, six dimensions, source register and denominators.
- White space remains a Hypothesis with a disconfirming test.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `skill:taste-skill` — downstream review or delivery.

## Limits and cautions

- No category-wide tally or white-space conclusion below eight verifiable examples.
- Never copy competitor assets or infer performance/preference from visual style.
- Human review is required before concept work.
