---
title: UI Finish Gate Reviewer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:design-ui-finish-gate-reviewer
department: design
sub_department: design-qa
job: consistency-qa
role: specialist
trigger: "When the approved scope specifically requires consistency qa expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/design-ui-finish-gate-reviewer.md
invoke: "Agent tool: design-ui-finish-gate-reviewer"
pairs_with: [skill:3w-brand-consistency-qa, skill:reviewing-interface-quality, skill:accessibility]
---
# UI finish-gate reviewer

UI finish-gate reviewer is a 3RDWRONG design QA specialist for consistency-qa, activated when the approved scope specifically requires consistency qa expertise.

## What it does

- Establish a product lens and written design contract before visual recommendations.
- Compare three to five relevant product patterns and explain the transferable lesson.
- Review the implemented screen at desktop and mobile, including accessibility and product states.
- Return PASS or HOLD with observable fixes and evidence requirements.

## When to use

- When the approved scope specifically requires consistency qa expertise. In practice: phase 07 validation or the relevant handoff, against the current approved system.

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
Use agency:design-ui-finish-gate-reviewer for this consistency-qa review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- Findings point to the supplied artefact or state and distinguish observation from interpretation.
- Each recommendation names a concrete next action, owner or retest condition.
- Unknowns and unrun checks remain visible; no result is inferred from a filename, mock-up or claim.

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
