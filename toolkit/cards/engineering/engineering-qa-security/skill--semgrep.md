---
title: Semgrep Security Scan
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:semgrep
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/semgrep/SKILL.md
invoke: "semgrep skill"
pairs_with: [skill:codeql, skill:sarif-parsing]
---
# Semgrep Security Scan

The studio's lead tool for security analysis: Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and.

## What it does

- Detects languages and proposes scan rulesets for approval.
- Runs approved Semgrep scans and reports skipped or failed rulesets.
- Preserves raw results for review and disables telemetry per workflow.

## When to use

- For first-pass static security scanning when Semgrep fits the repository.
- Before code review when scope and rulesets can be explicitly approved.

## When not to use

- Do not duplicate an existing Semgrep CI pipeline.
- Do not use to parse SARIF; use `skill:sarif-parsing`.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use semgrep skill. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Findings identify evidence, impact, remediation direction and unknowns.
- The report distinguishes observation from assessment.

## Quality checks

- [ ] Scope matches the request and any authorisation.
- [ ] Findings cite evidence.
- [ ] Limitations and untested areas are stated.

## Pairs with

- `skill:codeql`, `skill:sarif-parsing`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
