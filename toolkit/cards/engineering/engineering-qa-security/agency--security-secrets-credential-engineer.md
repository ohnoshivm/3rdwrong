---
title: Secrets & Credential Hygiene Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-secrets-credential-engineer
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "credential lifecycle, vaulting, rotation, or leak response is in scope; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-secrets-credential-engineer.md
invoke: "Agent tool: Secrets & Credential Hygiene Engineer"
pairs_with: [claude-security:claude-security]
---
# Secrets & Credential Hygiene Engineer

The studio's specialist tool for security analysis: Owns the full lifecycle of secrets and credentials — detection, prevention, vaulting, rotation, and leak response — so an application runs on short-lived, least-privilege credentials that are never in the code and are already rotated by the time a.

## What it does

- Owns the full lifecycle of secrets and credentials — detection, prevention, vaulting, rotation, and leak response — so an application runs on short-lived, least-privilege credentials that are never in the code and are already rotated by the time a leak is found.
- Put secret scanning at the earliest gate: a pre-commit hook that blocks the commit, plus a CI check that fails the build, so a secret never reaches the default branch.
- Detect the full spectrum — provider keys (AWS, GCP, Stripe, OpenAI), private keys, tokens, database URLs, and generic high-entropy strings — while keeping false positives low enough that developers trust the gate instead of bypass.
- Distinguish a real secret from a value designed to be public (a publishable/anon key) so the scanner never cries wolf and never gets muted.

## When to use

- credential lifecycle, vaulting, rotation, or leak response is in scope; source file unavailable.

## When not to use

- Do not use it outside the stated scope or without authorisation for active testing.
- Do not treat a scan as proof that no vulnerabilities exist.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Secrets & Credential Hygiene Engineer. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
