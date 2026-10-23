---
title: Reviewing Security
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:reviewing-security
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "Use for engineering/engineering-qa-security/security-analysis when the brief specifically requires: Use when reviewing code for security before merging or shipping, and when a change touches untrusted input, authentication, authorization, secrets, SQL, subprocess execution, file paths, outbound requests, deserialization, uploads, or third-party dep ."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/reviewing-security/SKILL.md
invoke: "reviewing-security skill"
pairs_with: [claude-security:claude-security]
---
# Reviewing Security

The studio's specialist tool for security analysis: Use when reviewing code for security before merging or shipping, and when a change touches untrusted input, authentication, authorization, secrets, SQL, subprocess execution, file paths, outbound requests, deserialization, uploads, or third-party dependencies.

## What it does

- Maps attack surfaces and traces inputs to security-sensitive sinks.
- Checks authorisation, secrets, cryptography and process boundaries.
- Uses evidence-led findings rather than generic checklist advice.

## When to use

- Use for engineering/engineering-qa-security/security-analysis when the brief specifically requires: Use when reviewing code for security before merging or shipping, and when a change touches untrusted input, authentication, authorization, secrets, SQL, subprocess execution, file paths, outbound requests, deserialization, uploads, or third-party dep .

## When not to use

- Do not use as a penetration test or certification.
- Do not infer runtime headers or behaviour from source alone.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use reviewing-security skill. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
