---
title: Paid Measurement Loop
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:paid-measurement-loop
department: advertising
sub_department: ad-creative-measurement
job: attribution-reporting
role: specialist
trigger: "Use for advertising/ad-creative-measurement/attribution-reporting when the brief specifically requires: Use when the user asks to \"read back\" a paid campaign change, \"did this ad change work\", or \"compare ROAS/CPA before and after\"; reads ROAS/CPA against a control over a fixed readback window and returns a Promote / Keep-testing / Rollback / Unproven readback decision with the math delegated to roi-calculator ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/paid-measurement-loop/SKILL.md
invoke: "Claude Code: `/paid-measurement-loop`; Codex: `paid-measurement-loop` skill"
pairs_with: [skill:attribution-reconciler]
---
# Paid Measurement Loop

Paid Measurement Loop is a 3RDWRONG specialist for attribution reporting, activated only when its registry trigger applies.

## What it does

- Reads a paid-ads change back against a control over a fixed readback window and returns Promote / Keep-testing / Rollback / Unproven. This is the paid readback loop — distinct from roi-calculator (the ROI/CPA math, which this delegates to), ad-account-auditor (RQS score/veto adjudication), and performance-analyzer (cross-channel rollup); it owns only the readback decision, window, and control.
- Expected output: a per-change readback_decision (Promote / Keep-testing / Rollback / Unproven) and Cycle Retro bound to the exact change/test head, artifact and measurement-contract hashes, with delta-vs-control on a primary metric (ROAS or CPA), the readback window used, normalization notes (attribution window + currency), evidence refs, and a handoff summary ready for memory/ad/paid-measurement-loop/. readback_decision is not an RQS auditor verdict.
- Writes: a user-facing readback table plus a reusable readback summary storable under memory/ad/paid-measurement-loop/.

## When to use

- Use for advertising/ad-creative-measurement/attribution-reporting when the brief specifically requires: Use when the user asks to "read back" a paid campaign change, "did this ad change work", or "compare ROAS/CPA before and after"; reads ROAS/CPA against a control over a fixed readback window and returns a Promote / Keep-testing / Rollback / Unproven readback decision with the math delegated to roi-calculator .
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
Use Paid Measurement Loop to Review the supplied campaign evidence and report findings, unknowns and next steps. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a per-change readback_decision (Promote / Keep-testing / Rollback / Unproven) and Cycle Retro bound to the exact change/test head, artifact and measurement-contract hashes, with delta-vs-control on a primary metric (ROAS or CPA), the readback window used, normalization notes (attribution window + currency), evidence refs, and a handoff summary ready for memory/ad/paid-measurement-loop/. readback_decision is not an RQS auditor verdict.
- the selected change binding is current and non-forked; the change exited learning phase before the window opened; primary metric is read delta-vs-control over the precommitted window; attribution window, currency, and timezone are normalized; the result references the matching measurement contract and evidence; and readback_decision is one of the four. Without a verified platform receipt, execution remains user-reported or recommended rather than being fabricated.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] No spend action occurs without founder approval.

## Pairs with

- `skill:attribution-reconciler` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
