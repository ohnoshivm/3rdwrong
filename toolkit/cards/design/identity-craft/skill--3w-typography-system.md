---
title: Typography system
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-typography-system
department: design
sub_department: identity-craft
job: typography
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-typography-system/SKILL.md
invoke: "3w-typography-system skill"
pairs_with: [skill:3w-mark-exploration, skill:3w-colour-system, skill:3w-composition-system, agent:visual-designer, vectorlab-ux-skills:typography]
---
# Typography system

The studio's lead tool for brand typography: type chosen against the idea, licensed for every medium, shaped correctly in every required script and fast on the web.

## What it does

- Writes the type's job from the idea and sets hard constraints first.
- Records licence coverage per medium: desktop, web, app, video or broadcast, logo use, client transfer.
- Builds a specimen string set and checks Latin and Indian-script shaping in real renderers with a fluent reader.
- Sets pairing, hierarchy, optical sizes, spacing and kerning rules.
- Plans web fonts within web standards (≤ 2 families, ≤ 100 KB initial) and D-0023, with metric-matched fallbacks.

## When to use

- Phase 05 Identity, to shortlist and check typefaces after a route is chosen.
- Phase 06 System, to set hierarchy and test across applications.
- Phase 07 Validation, to reconfirm licences, glyphs and file sizes.

## When not to use

- To pick a font by mood or before a route exists.
- To convert an approved system into web tokens — use `agent:visual-designer`; to fix a measured ramp defect — use `vectorlab-ux-skills:typography`.
- As legal advice on licences.

## Inputs it needs

- Chosen route; required scripts and fluent reviewers.
- Media, real content strings and mandatory text confirmed by the client.
- Licence budget and the performance budget.

## How to run it

1. Collect the inputs above in one folder or message; state whether the route is chosen or the run is formative.
2. Run the skill; a human designer makes every form decision it records.
3. Hand the output to someone other than the maker for review.
4. File the output in the project folder; nothing it produces is an approval.

```text
Use the 3w-typography-system skill for {{project}}. Route: {{link}}. Scripts and reviewers: {{…}}. Media: {{…}}. Content strings and mandatory text: {{…}}. Read each candidate's licence; mark unverified scripts Unknown. Return the skill's exact output structure.
```

## What good output looks like

- A shortlist tied to the type's job, with licence rows read from the documents.
- Script rows with renderer and fluent reviewer, or Unknown.
- Measured web-font sizes inside the budget and metric-matched fallbacks.

## Quality checks

- [ ] Licences were read per medium; unclear terms sent to the foundry.
- [ ] Every required script was shaped and checked by a fluent reader, or is unverified.
- [ ] Numerals, currency and brand names were kerned.
- [ ] Initial web fonts measured within budget.
- [ ] Reviewer is not the maker.

## Pairs with

- Alongside: `skill:3w-mark-exploration` (wordmark), `skill:3w-colour-system`, `skill:3w-composition-system`.
- Downstream: `agent:visual-designer` for digital tokens and ramp; `vectorlab-ux-skills:typography` for measured defects.

## Limits and cautions

- Experimental; one fictional run so far with fictional fonts, so licensing and shaping are untested.
- Never use unlicensed fonts or outline a font in a logo against its licence.
- The founder chooses type; AI shortlists and checks.
