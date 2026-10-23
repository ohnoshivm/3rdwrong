---
title: Web quality audit
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:web-quality-audit
department: engineering
sub_department: engineering-qa-security
job: release-verification
role: specialist
trigger: "a broad live website audit spanning performance, accessibility, SEO, best practices, and agentic browsing."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/web-quality-audit/SKILL.md
invoke: "web-quality-audit skill"
pairs_with: [skill:web-accessibility, skill:playwright-cli]
---
# Web quality audit

The studio's specialist tool for release verification: Run an evidence-led web quality audit covering performance, accessibility, SEO, best practices, and agentic browsing.

## What it does

- Combines live browser evidence with source inspection for web quality.
- Routes checks across performance, accessibility, SEO and best practices.
- Uses observed behaviour and metrics rather than an aggregate score alone.

## When to use

- a broad live website audit spanning performance, accessibility, SEO, best practices, and agentic browsing.

## When not to use

- Do not infer deployed behaviour from source configuration alone.
- Do not use an aggregate score instead of category findings.

## Inputs it needs

- Brief, implementation, running build or artefacts, target devices and acceptance criteria.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use web-quality-audit skill. Task: {describe the scoped release verification need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Concrete issues cite observed evidence and remaining release risks.
- Unverified areas are named.

## Quality checks

- [ ] Reviewer is independent.
- [ ] Relevant interactions and contexts are inspected.
- [ ] Open issues and evidence are explicit.

## Pairs with

- `skill:web-accessibility`, `skill:playwright-cli`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Respect accessibility and reduced-motion requirements when inspecting digital experiences.
