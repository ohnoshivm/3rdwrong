---
title: security-auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:code-modernization:security-auditor
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "Use for engineering/engineering-qa-security/security-analysis when the brief specifically requires: Adversarial security reviewer — OWASP Top 10, CWE, dependency CVEs, secrets, injection ."
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-code-modernization-marketplace/agents/security-auditor.md
invoke: "Agent tool: security-auditor"
pairs_with: [claude-security:claude-security]
---
# security-auditor

The studio's specialist tool for security analysis: Adversarial security reviewer — OWASP Top 10, CWE, dependency CVEs, secrets, injection.

## What it does

- Reviews code adversarially for OWASP Top 10 and CWE risks.
- Checks dependency CVEs, exposed secrets and injection paths.
- Reports concrete findings against the supplied change or code.

## When to use

- Use for engineering/engineering-qa-security/security-analysis when the brief specifically requires: Adversarial security reviewer — OWASP Top 10, CWE, dependency CVEs, secrets, injection .

## When not to use

- Do not use it to run an authorised penetration test.
- Do not treat source inspection as proof of runtime security.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: security-auditor. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
