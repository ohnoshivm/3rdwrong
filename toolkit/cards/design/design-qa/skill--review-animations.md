---
title: Review Animations
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:review-animations
department: design
sub_department: design-qa
job: consistency-qa
role: specialist
trigger: "When the approved scope specifically requires use when the task specifically needs reviews animation and motion code against a high craft bar derived from emil kowalski's design engineering philosophy."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/review-animations
invoke: "/review-animations"
pairs_with: [skill:3w-brand-consistency-qa, skill:reviewing-interface-quality, skill:accessibility]
---
# Review Animations

Review Animations is a 3RDWRONG design QA specialist for consistency-qa, activated when the approved scope specifically requires use when the task specifically needs reviews animation and motion code against a high craft bar derived from emil kowalski's design engineering philosophy.

## What it does

- Reviews only animation and motion code against ten craft standards.
- Checks purpose, frequency, easing, duration, origin, interruptibility, GPU properties and accessibility.
- Returns a before/after/why findings table and an explicit Block or Approve decision.
- Loads STANDARDS.md when exact curves, durations or spring values are needed.

## When to use

- When the approved scope specifically requires use when the task specifically needs reviews animation and motion code against a high craft bar derived from emil kowalski's design engineering philosophy. In practice: after motion code is authored and before the animation is accepted.

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
Use skill:review-animations for this consistency-qa review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- One row per motion issue in the required Before/After/Why table, followed by tiered commentary.
- Motion findings cite file and line and use source standards for exact values.
- The final decision is Block or Approve with stated criteria.

## Quality checks

- [ ] Baseline approval/version and asset version are verified.
- [ ] Each status maps to a written rule and evidence; missing proof is Not testable.
- [ ] Checker is independent and human release decision remains separate.

## Pairs with

- Work with `skill:3w-brand-consistency-qa`, `skill:reviewing-interface-quality`, `skill:accessibility` at the consistency-qa handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Do not claim conformance without an approved baseline. Rights, licence, production and accessibility checks remain Not testable without their evidence.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `vendor`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
