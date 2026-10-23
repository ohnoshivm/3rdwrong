---
title: Visual QA Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:visual-qa-engineer
department: design
sub_department: design-qa
job: visual-qa-browser
role: lead
trigger: ""
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/visual-qa-engineer.md
invoke: "Agent tool: visual-qa-engineer"
pairs_with: [skill:ceos-visual-audit, skill:reviewing-interface-quality, design-steward:verify]
---
# Visual QA engineer

Visual QA engineer is a 3RDWRONG design QA tool for visual-qa-browser: lead for visual-qa-browser.

## What it does

- Inspects the rendered page at real viewport widths using screenshots or measured DOM evidence.
- Reports location, observed and expected behaviour, severity, evidence and the owner of each fix.
- Checks contrast with measurements and regressions against the previous state or approved reference.
- Returns a pass at inspected widths or lists remaining failures and unverified checks.

## When to use

- After a meaningful UI change, during Phase 07 Visual Inspection and Refinement, with a running page and stated art direction.

## When not to use

- Do not use it for unrendered concept critique or to make fixes unless its source explicitly allows edits; use `skill:3w-identity-system-critic` for identity concepts.

## Inputs it needs

- A running URL or local server, intended art direction/reference, changed scope and target widths.
- Relevant states and interactions; browser access and screenshot capture for visual claims.

## How to run it

1. Confirm the page loads and capture the stated widths/states before reporting.
2. Exercise the named flow; inspect screenshots and measurements that support each finding.
3. Report location, observed/expected behaviour, impact, evidence and fix owner.
4. Mark inaccessible or untested widths and behaviours unverified, then re-check fixes against the same evidence.

```text
Use agent:visual-qa-engineer for this visual-qa-browser review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- Findings point to the supplied artefact or state and distinguish observation from interpretation.
- Each recommendation names a concrete next action, owner or retest condition.
- Unknowns and unrun checks remain visible; no result is inferred from a filename, mock-up or claim.

## Quality checks

- [ ] Screenshots or measured evidence exist for each visual claim and inspected viewport is named.
- [ ] Primary interactions and key responsive states were exercised where in scope.
- [ ] Unavailable browser checks are marked unverified; no completion claim exceeds evidence.

## Pairs with

- Work with `skill:ceos-visual-audit`, `skill:reviewing-interface-quality`, `design-steward:verify` at the visual-qa-browser handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- A source or code inspection alone does not prove rendered appearance; without browser evidence mark visual QA unverified.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `vendor`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
