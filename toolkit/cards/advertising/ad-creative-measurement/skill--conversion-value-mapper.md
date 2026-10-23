---
title: Conversion Value Mapper
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:conversion-value-mapper
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to \"set up conversion values so tROAS optimizes profit not orders\", \"map margin onto my purchase value\", \"build value rules for lead / phone / signup conversions\", or \"stop bidding to revenue when I care about profit\"; defines and QAs the conversion VALUE model — per-conversion values, margin/net-value adjustment, static-vs-dynamic value rules, proxy values for non-revenue actions, and a value-vs-count sanity check — as a value-model spec plus a pre-launch value QA sheet ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/conversion-value-mapper/SKILL.md
invoke: "Claude Code: `/conversion-value-mapper`; Codex: `conversion-value-mapper` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Conversion Value Mapper

Conversion Value Mapper is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- Defines and QAs the conversion VALUE model behind value-based paid bidding — per-conversion values, margin/net-value adjustment, static-vs-dynamic value rules, proxy values for non-revenue actions, and a value-vs-count sanity check — delivered as a value-model spec plus a pre-launch value QA sheet. **Scope line: this skill BUILDS and QAs the *values* the platform bids toward so tROAS/max-conversion-value chases profit, not raw order count; it does NOT verify that the event fires or that UTMs are clean — conversion-signal-qa owns the plumbing — and it does NOT score the ROAS R1/R2 vetoes — ad-account-auditor judges those. It is a Return-dimension prerequisite, not the verdict. It is also not** the standing cross-platform de-dup / incrementality reconciliation — that is attribution-reconciler; here you only define the value the platform *receives*, not resolve which platform gets credit for it.
- Expected output: a conversion value-model spec (per-conversion value + net-value/margin adjustment + rule logic), a static-vs-dynamic value-rule decision, proxy values for non-revenue actions with a stated derivation, a value-vs-count reconciliation (does the value the platform receives track the profit the business books?), and the standard handoff summary.
- Writes: a user-facing value-model spec + value QA sheet to memory/ad/conversion-value-mapper/.

## When to use

- Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "set up conversion values so tROAS optimizes profit not orders", "map margin onto my purchase value", "build value rules for lead / phone / signup conversions", or "stop bidding to revenue when I care about profit"; defines and QAs the conversion VALUE model — per-conversion values, margin/net-value adjustment, static-vs-dynamic value rules, proxy values for non-revenue actions, and a value-vs-count sanity check — as a value-model spec plus a pre-launch value QA sheet .
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
Use Conversion Value Mapper to Prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a conversion value-model spec (per-conversion value + net-value/margin adjustment + rule logic), a static-vs-dynamic value-rule decision, proxy values for non-revenue actions with a stated derivation, a value-vs-count reconciliation (does the value the platform receives track the profit the business books?), and the standard handoff summary.
- every revenue-bearing conversion has a stated value and a net-value adjustment (or an explicit "revenue = net, margin flat" note); non-revenue conversions have a proxy value with a labeled derivation (never a guessed round number presented as fact); the static-vs-dynamic rule is chosen with a reason; the value-vs-count reconciliation is run and either passes or names the gap; and the spec says the value model is launch-ready for value-based bidding or lists exactly what to fix.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] No spend action occurs without founder approval.

## Pairs with

- `agency:marketing-growth-hacker` — same job; use when its own role or trigger applies.
- `agency:marketing-livestream-commerce-coach` — same job; use when its own role or trigger applies.
- `agency:paid-media-creative-strategist` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
