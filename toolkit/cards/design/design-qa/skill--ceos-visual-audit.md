---
title: Ceos Visual Audit
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-visual-audit
department: design
sub_department: design-qa
job: visual-qa-browser
role: specialist
trigger: "An independent Codex reviewer has real rendered screenshots and needs a prioritised visual defect report."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-visual-audit
invoke: "/ceos-visual-audit"
pairs_with: [agent:creative-auditor, agent:visual-qa-engineer, skill:reviewing-interface-quality]
---
# Ceos Visual Audit

Ceos Visual Audit is a 3RDWRONG design QA specialist for visual-qa-browser, activated when an independent Codex reviewer has real rendered screenshots and needs a prioritised visual defect report.

## What it does

- Runs a rendered visual audit against a concept, art direction and Creative Engineering OS standards.
- Uses captured viewports and reduced-motion evidence.
- Produces a scored verdict and defect table with evidence, rule and exact fix.
- States visual QA as unverified and stops when browser evidence is unavailable.

## When to use

- An independent Codex reviewer has real rendered screenshots and needs a prioritised visual defect report. In practice: Phase 07 Visual Inspection after real screenshots exist.

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
Use skill:ceos-visual-audit for this visual-qa-browser review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
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

- Work with `agent:creative-auditor`, `agent:visual-qa-engineer`, `skill:reviewing-interface-quality` at the visual-qa-browser handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- A source or code inspection alone does not prove rendered appearance; without browser evidence mark visual QA unverified.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `vendor`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
