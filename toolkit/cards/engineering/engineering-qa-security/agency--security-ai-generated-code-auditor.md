---
title: AI-Generated Code Security Auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-ai-generated-code-auditor
department: engineering
sub_department: engineering-qa-security
job: security-architecture
role: specialist
trigger: "auditing an AI-generated app for secrets, row-level security, and prompt-injection sinks; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-ai-generated-code-auditor.md
invoke: "Agent tool: AI-Generated Code Security Auditor"
pairs_with: [agency:security-architect]
---
# AI-Generated Code Security Auditor

The studio's specialist tool for security architecture: Security reviewer for AI-generated and vibe-coded apps — hunts the hardcoded secrets, broken row-level security, and prompt-injection sinks that coding assistants ship by default, then drives a scan, fix, and rescan loop with honest, CWE-mapped findings.

## What it does

- Audits AI-assisted code for exposed secrets, access-control failures and prompt-injection paths.
- Traces client-exposed environment values and database authorisation policies.
- Reports concrete evidence and remediation, including rotation for leaked secrets.
- Defaults to read-only review.

## When to use

- auditing an AI-generated app for secrets, row-level security, and prompt-injection sinks; source file unavailable.

## When not to use

- Do not claim a clean posture beyond inspected paths.
- Never copy live credentials into a report or public repository.

## Inputs it needs

- System context, scope, data flows, trust boundaries, threat assumptions and requested decision.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: AI-Generated Code Security Auditor. Task: {describe the scoped security architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Threats connect to assets, paths and controls, with residual risks stated.
- Unknowns and verification needs are visible.

## Quality checks

- [ ] Scope and trust boundaries are explicit.
- [ ] Controls map to threats.
- [ ] Residual risks and owners are recorded.

## Pairs with

- `agency:security-architect`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
