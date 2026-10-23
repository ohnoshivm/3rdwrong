---
title: Ad Test Designer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ad-test-designer
department: advertising
sub_department: ad-creative-measurement
job: creative-testing
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/ad-test-designer/SKILL.md
invoke: "Claude Code: `/ad-test-designer`; Codex: `ad-test-designer` skill"
pairs_with: [skill:ad-creative-builder, skill:paid-measurement-loop]
---
# Ad Test Designer

Ad Test Designer is 3RDWRONG’s lead for creative testing in ad creative measurement.

## What it does

- Designs paid-ad creative/landing A/B/n and incrementality tests and reads them out: hypothesis, variant matrix, sample-size/duration/power plan, effect size, uncertainty, practical-effect status, and guardrail state. This skill owns experiment design + statistical interpretation. It may apply an owner-approved, precommitted action rule, but it never treats a p-value or helper output as an automatic business decision. It does not produce variants (ad-creative-builder), read back one already-shipped change (paid-measurement-loop), or do cross-channel reporting (performance-analyzer).
- Expected output: a test design (hypothesis, variant matrix, immutable test/variant/measurement binding, primary/secondary/guardrail metrics, sample-size + duration + power plan) and/or a read-out bound to that exact design (effect estimate, interval, statistical flag, practical-effect flag, guardrails, and either an owner-governed recommendation or decision: UNDECIDED).
- Writes: a user-facing test-design or read-out doc plus a ### Handoff Summary.

## When to use

- Use as lead for creative testing when the studio has an approved brief for this deliverable.
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat statistical flags as automatic business decisions or as authority to launch, change or fund a campaign.
- Do not use to generate variants — use `skill:ad-creative-builder`; do not read back one already-shipped change — use `skill:paid-measurement-loop`.
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
Use Ad Test Designer to design or read out a paid-ad/landing A/B/n or incrementality test. Test mode and hypothesis: {brief}. Baseline, target lift, variants and measurement binding: {details}. Results CSV for read-out: {path}. Do not ask this tool to generate variants; no spend without founder approval.
```

## What good output looks like

- a test design (hypothesis, variant matrix, immutable test/variant/measurement binding, primary/secondary/guardrail metrics, sample-size + duration + power plan) and/or a read-out bound to that exact design (effect estimate, interval, statistical flag, practical-effect flag, guardrails, and either an owner-governed recommendation or decision: UNDECIDED).
- a falsifiable hypothesis is stated; the matrix isolates one variable per variant; the control, candidate, variant hash, signal spec, and measurement contract are bound; baseline, MDE, alpha, power, multiplicity/sequential policy, duration, and guardrails are declared; and a read-out reports effect/interval/statistical/practical flags with Calculated provenance against the same binding. A mismatch returns NEEDS_INPUT/UNDECIDED; without a precommitted action rule and owner, return decision: UNDECIDED.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns ar
- No same-job peer appears in this scoped registry slice.
- `skill:ad-creative-builder` — produce the variants before designing their test.
- `skill:paid-measurement-loop` — read back an approved change after it ships.e result before use.
- [ ] No spend action occurs without founder approval.

## Pairs with

- No same-job peer appears in this scoped registry slice.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
