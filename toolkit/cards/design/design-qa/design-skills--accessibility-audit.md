---
title: Accessibility Audit
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-skills:accessibility-audit
department: design
sub_department: design-qa
job: accessibility
role: lead
trigger: ""
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-skills-marketplace/skills/accessibility-audit
invoke: "/accessibility-audit"
pairs_with: [skill:3w-brand-consistency-qa, skill:reviewing-interface-quality, vectorlab-ux-skills:keyboard, vectorlab-ux-skills:reduced-motion]
---
# Accessibility Audit

Accessibility Audit is a 3RDWRONG design QA tool for accessibility: lead for accessibility.

## What it does

- Audits pages, components and flows against WCAG 2.2 and POUR.
- Uses automated scans, keyboard review, screen reader checks, visual/content review and flow testing.
- Prioritises findings by impact and supplies fixes and report templates.
- Treats automated scans as one layer; manual checks are needed for barriers they cannot detect.

## When to use

- Before digital handoff or release when a real page, component or flow can be checked against WCAG 2.2.

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
Use design-skills:accessibility-audit for this accessibility review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
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
- Distribution is `vendor`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
