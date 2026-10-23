---
title: CodeQL Analysis
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:codeql
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "language support and interprocedural analysis needs suit CodeQL; read the installed skill workflow before use."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/codeql/SKILL.md
invoke: "codeql skill"
pairs_with: [claude-security:claude-security]
---
# CodeQL Analysis

The studio's specialist tool for security analysis: Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis.

## What it does

- Uses CodeQL databases and queries for interprocedural data-flow and taint analysis.
- Guides database discovery or build and records scan outputs.
- Requires available CodeQL tooling and the installed workflow.

## When to use

- language support and interprocedural analysis needs suit CodeQL; read the installed skill workflow before use.

## When not to use

- Do not use to parse SARIF; use `skill:sarif-parsing`.
- A scan cannot prove the absence of vulnerabilities.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use codeql skill. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Findings identify evidence, impact, remediation direction and unknowns.
- The report distinguishes observation from assessment.

## Quality checks

- [ ] Scope matches the request and any authorisation.
- [ ] Findings cite evidence.
- [ ] Limitations and untested areas are stated.

## Pairs with

- `claude-security:claude-security`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
