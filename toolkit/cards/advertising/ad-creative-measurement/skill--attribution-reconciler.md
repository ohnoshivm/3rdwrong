---
title: Attribution Reconciler
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:attribution-reconciler
department: advertising
sub_department: ad-creative-measurement
job: attribution-reporting
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/attribution-reconciler/SKILL.md
invoke: "Claude Code: `/attribution-reconciler`; Codex: `attribution-reconciler` skill"
pairs_with: [skill:paid-measurement-loop]
---
# Attribution Reconciler

Attribution Reconciler is 3RDWRONG’s lead for attribution reporting in ad creative measurement.

## What it does

- The single rule: the truth set is the order IDs from GA4/ecommerce, never any platform's reported-conversion count. This workbook reconciles paid channels only — decomposing GA4 direct traffic and estimating organic dark-social share attribution belongs to dark-social-attributor.
- Expected output: a reconciliation workbook that maps every platform-reported conversion to (or away from) an order in the truth set, a de-duped conversion count per platform, a normalized-window/currency view, an attribution-model comparison table, and an incrementality read if a holdout exists.
- Writes: a reconciliation workbook at memory/ad/attribution-reconciler/YYYY-MM-DD-<topic>.md — match table, de-duped counts, normalized view, model-comparison table, incrementality read, and a handoff summary.

## When to use

- Use as lead for attribution reporting when the studio has an approved brief for this deliverable.
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
Use Attribution Reconciler to Review the supplied campaign evidence and report findings, unknowns and next steps. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a reconciliation workbook that maps every platform-reported conversion to (or away from) an order in the truth set, a de-duped conversion count per platform, a normalized-window/currency view, an attribution-model comparison table, and an incrementality read if a holdout exists.
- every platform conversion is reconciled to the order-ID truth set (matched / double-counted / unmatched), windows and currency are normalized to a common basis, at least one attribution-model comparison is shown, incrementality is read where a holdout exists (or marked N/A), and the ratio/ROAS math is handed to roi-calculator rather than computed here.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] No spend action occurs without founder approval.

## Pairs with

- `skill:paid-measurement-loop` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
