---
title: Accessibility Review
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design:accessibility-review
department: design
sub_department: design-qa
job: accessibility
role: specialist
trigger: "A supplied design artefact needs a WCAG 2.1 AA review before implementation."
kind: plugin-skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/afe29730-8d0c-470c-801a-a52a510c0510/skills/accessibility-review/SKILL.md
invoke: "/accessibility-review"
pairs_with: [skill:3w-brand-consistency-qa, skill:reviewing-interface-quality, vectorlab-ux-skills:keyboard, vectorlab-ux-skills:reduced-motion]
---
# Accessibility-review

Accessibility-review is a 3RDWRONG design QA specialist for accessibility, activated when a supplied design artefact needs a WCAG 2.1 AA review before implementation.

## What it does

- Reviews screenshots, mockups, designs and flows using WCAG 2.1 A/AA as the baseline.
- Checks perceptibility, operability, understandability and robustness.
- Separates visible risks from checks requiring code or interaction testing.
- Returns a short verdict, likely issues, design fixes, implementation checks and priorities.

## When to use

- A supplied design artefact needs a WCAG 2.1 AA review before implementation. In practice: before implementation sign-off or release, for the supplied design or implemented flow.

## When not to use

- Do not claim compliance from a static artefact or automated scan alone; use `agency:engineering-section-508-specialist` for a deeper engineering/document audit.

## Inputs it needs

- The supplied artefact, component or flow, target WCAG level and intended users/context.
- For implementation claims: a running build, keyboard/screen reader access and test environment; note any missing access.

## How to run it

1. Name the target level and inspect the supplied artefact with the tool’s documented visual/manual methods.
2. Separate visible risks from code, keyboard, assistive-technology and responsive checks.
3. Prioritise by access impact, cite the affected control/state, and recommend a concrete correction.
4. Record what was tested and what remains unverified; do not claim conformance without evidence.

```text
Use design:accessibility-review for this accessibility review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- Findings point to the supplied artefact or state and distinguish observation from interpretation.
- Each recommendation names a concrete next action, owner or retest condition.
- Unknowns and unrun checks remain visible; no result is inferred from a filename, mock-up or claim.

## Quality checks

- [ ] Keyboard, focus, semantic and screen reader claims are not inferred from screenshots alone.
- [ ] Findings identify the affected component, user impact and applicable criterion/level when documented.
- [ ] Reduced motion, contrast and non-colour cues are checked where relevant.

## Pairs with

- Work with `skill:3w-brand-consistency-qa`, `skill:reviewing-interface-quality`, `vectorlab-ux-skills:keyboard`, `vectorlab-ux-skills:reduced-motion` at the accessibility handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Static designs cannot prove keyboard access, semantics, screen reader behaviour or WCAG conformance. Honour reduced motion and accessible interaction states where relevant.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `manual`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
