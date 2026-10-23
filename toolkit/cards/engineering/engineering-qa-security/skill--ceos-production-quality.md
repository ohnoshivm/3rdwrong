---
title: Production quality
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-production-quality
department: engineering
sub_department: engineering-qa-security
job: release-verification
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-production-quality
invoke: "ceos-production-quality skill"
pairs_with: [skill:web-quality-audit, skill:web-accessibility]
---
# Production quality

The studio's lead tool for release verification: Production verification for creative websites — Playwright smoke and interaction tests, visual regression snapshots, automated accessibility (axe-core) plus keyboard checks, responsive and cross-browser runs, console/error budgets, build.

## What it does

- Production verification for creative websites — Playwright smoke and interaction tests, visual regression snapshots, automated accessibility (axe-core) plus keyboard checks, responsive and cross-browser runs, console/error budgets, build verification, basic security review and deployment/release validation with rollback. Use before merging or deploying, when adding tests to a creative site, when setting up CI for a template, or when verifying a release actually works.
- Returns work within the documented scope.
- States evidence and scope limits where relevant.

## When to use

- Phase 07 Validation, before client hand-over.

## When not to use

- Do not let the maker approve their own work.
- Do not infer audience or business outcomes from inspection.

## Inputs it needs

- Brief, implementation, running build or artefacts, target devices and acceptance criteria.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use ceos-production-quality skill. Task: {describe the scoped release verification need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Concrete issues cite observed evidence and remaining release risks.
- Unverified areas are named.

## Quality checks

- [ ] Reviewer is independent.
- [ ] Relevant interactions and contexts are inspected.
- [ ] Open issues and evidence are explicit.

## Pairs with

- `skill:web-quality-audit`, `skill:web-accessibility`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Respect accessibility and reduced-motion requirements when inspecting digital experiences.
