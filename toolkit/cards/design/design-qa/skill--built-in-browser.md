---
title: Built In Browser
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:built-in-browser
department: design
sub_department: design-qa
job: visual-qa-browser
role: specialist
trigger: "When the studio needs the documented visual qa browser task."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/built-in-browser/SKILL.md
invoke: "/built-in-browser"
pairs_with: [skill:ceos-visual-audit, skill:reviewing-interface-quality, design-steward:verify]
---
# Built-in-browser

Built-in-browser is a 3RDWRONG design QA specialist for visual-qa-browser, activated when the studio needs the documented visual qa browser task.

## What it does

- Provides the Claude desktop built-in browser pane and its browser tools for tabs, navigation, reading page content and interactions.
- Loads the browser tools in bulk when they are deferred; `preview_start` can open a known URL in a new tab.
- Uses screenshots when visual layout is the point; prefers page text/structure for reading.
- Keeps the browser profile and persistent sign-ins separate from Chrome.

## When to use

- When the studio needs the documented visual qa browser task. In practice: read this before the first action in Claude desktop’s browser pane, then pair it with the actual audit method.

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
Use skill:built-in-browser for this visual-qa-browser review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
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
- Distribution is `manual`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
