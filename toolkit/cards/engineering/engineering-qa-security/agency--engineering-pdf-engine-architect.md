---
title: PDF Engine Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-pdf-engine-architect
department: engineering
sub_department: engineering-qa-security
job: codebase-analysis
role: specialist
trigger: "Use for engineering/engineering-qa-security/codebase-analysis when the brief specifically requires: Architect and specialist in deterministic HTML-to-PDF document compilation, Playwright browser context pools, dynamic Euclidean page sizing, LayoutNG subpixel budgeting, tagged PDF (PDF/UA-1 & PDF/A-2b), and 1:1 sheet canvas editors ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-pdf-engine-architect.md
invoke: "Agent tool: PDF Engine Architect"
pairs_with: [agency:engineering-codebase-onboarding-engineer]
---
# PDF Engine Architect

The studio's specialist tool for codebase analysis when the brief concerns deterministic HTML-to-PDF output: designs browser rendering, page geometry and tagged document pipelines.

## What it does

- Designs deterministic HTML-to-PDF rendering and print geometry.
- Addresses browser context pools, page sizing, subpixel layout and tagged PDF output.
- Considers vector preservation, semantic structure and input sanitisation.

## When to use

- Use for engineering/engineering-qa-security/codebase-analysis when the brief specifically requires: Architect and specialist in deterministic HTML-to-PDF document compilation, Playwright browser context pools, dynamic Euclidean page sizing, LayoutNG subpixel budgeting, tagged PDF (PDF/UA-1 & PDF/A-2b), and 1:1 sheet canvas editors .

## When not to use

- Do not use for general repository orientation; use `agency:engineering-codebase-onboarding-engineer`.
- Do not claim PDF/UA or PDF/A compliance without verification.

## Inputs it needs

- Document types, target PDF standards, page sizes and representative input documents.
- Rendering environment, fonts, browser concurrency and editor geometry requirements.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: PDF Engine Architect. Task: {describe the deterministic HTML-to-PDF requirement}. Inputs: {document types, page geometry, fonts and output standards}. Runtime: {browser and concurrency constraints}. Return a rendering architecture with assumptions, failure cases and verification steps; do not claim standards compliance without evidence.
```

## What good output looks like

- Rendering assumptions, geometry calculations and failure cases are explicit.
- Accessibility and output-format claims include verification steps.

## Quality checks

- [ ] Representative page sizes, fonts and edge cases are accounted for.
- [ ] PDF tags and vector output are verified in the actual output.
- [ ] Any unsupported browser or format behaviour is stated.

## Pairs with

- Upstream: `agency:engineering-codebase-onboarding-engineer` can map the current document pipeline; this specialist designs deterministic PDF rendering for the scoped requirement. The registry places it under codebase analysis, while its source is an HTML-to-PDF architect.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.

- Registry placement may be too broad: the source describes a specialist PDF rendering architect, not general codebase analysis.
