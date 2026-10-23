---
title: Compliance Auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-compliance-auditor
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "SOC 2, ISO 27001, HIPAA, or PCI-DSS readiness/evidence work is explicitly in scope; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-compliance-auditor.md
invoke: "Agent tool: Compliance Auditor"
pairs_with: [claude-security:claude-security]
---
# Compliance Auditor

The studio's specialist tool for security analysis: Expert technical compliance auditor specializing in SOC 2, ISO 27001, HIPAA, and PCI-DSS audits — from readiness assessment through evidence collection to certification.

## What it does

- Expert technical compliance auditor specializing in SOC 2, ISO 27001, HIPAA, and PCI-DSS audits — from readiness assessment through evidence collection to certification.
- Assess current security posture against target framework requirements.
- Identify control gaps with prioritized remediation plans based on risk and audit timeline.
- Map existing controls across multiple frameworks to eliminate duplicate effort.

## When to use

- SOC 2, ISO 27001, HIPAA, or PCI-DSS readiness/evidence work is explicitly in scope; source file unavailable.

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
Use Agent tool: Compliance Auditor. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
