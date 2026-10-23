---
title: 3w Brand Consistency QA
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-brand-consistency-qa
department: design
sub_department: design-qa
job: consistency-qa
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: vendor
source: skills/3w-brand-consistency-qa
invoke: "3w-brand-consistency-qa skill"
pairs_with: [skill:3w-identity-system-critic, skill:accessibility, agency:design-ui-finish-gate-reviewer]
---
# 3w Brand Consistency Qa

3w Brand Consistency Qa is a 3RDWRONG design QA tool for consistency-qa: lead for consistency-qa.

## What it does

- Checks supplied brand assets against an approved identity specification and its use rules.
- Inventories assets and maps them only to applicable written requirements.
- Records each check as Pass, Fail or Not testable with evidence, severity, fix and retest.
- Keeps human release approval separate from the QA report.

## When to use

- Phase 06 System or Phase 07 Validation, before publishing or handover, when current assets can be compared to an approved identity specification.

## When not to use

- Do not use it to choose the strategy or approve its own work; use `skill:3w-brand-consistency-qa` for identity assets against an approved baseline.

## Inputs it needs

- The approved design/identity baseline with version and scope, plus the exact assets, screens or code to check.
- Applicable states, sizes, scripts, formats and acceptance criteria; rights/provenance notes where relevant.

## How to run it

1. Confirm the baseline is approved and current; if not, stop conformance scoring.
2. Inventory the supplied scope and compare each item only to applicable written requirements.
3. Record evidence and status for every check; mark missing measurement, production or rights proof Not testable.
4. Hand failures and retest criteria to a separate maker; leave release approval to the authorised human.

```text
Use skill:3w-brand-consistency-qa for this consistency-qa review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- Every asset is identified by version and intended use; results use Pass, Fail or Not testable consistently.
- Checks cite written rules and inspected assets; missing rights, script, contrast or production evidence stays visible.
- Human release decision is recorded separately; no approval or compliance claim is inferred.

## Quality checks

- [ ] Baseline approval/version and asset version are verified.
- [ ] Each status maps to a written rule and evidence; missing proof is Not testable.
- [ ] Checker is independent and human release decision remains separate.

## Pairs with

- Work with `skill:3w-identity-system-critic`, `skill:accessibility`, `agency:design-ui-finish-gate-reviewer` at the consistency-qa handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Do not claim conformance without an approved baseline. Rights, licence, production and accessibility checks remain Not testable without their evidence.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `vendor`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
