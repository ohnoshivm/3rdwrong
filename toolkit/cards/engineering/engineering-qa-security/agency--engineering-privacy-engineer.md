---
title: Privacy Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-privacy-engineer
department: engineering
sub_department: engineering-qa-security
job: security-architecture
role: specialist
trigger: "Use for tasks involving Expert privacy engineer who implements privacy in code."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-privacy-engineer.md
invoke: "Agent tool: Privacy Engineer"
pairs_with: [agency:security-architect]
---
# Privacy Engineer

The studio's specialist tool for security architecture: Expert privacy engineer who implements privacy in code — PII discovery and classification, data minimization, consent enforcement at the API layer, automated DSAR and deletion across services, pseudonymization/tokenization, and retention automation.

## What it does

- Locates and classifies personal data across stores and third parties.
- Enforces purpose limitation and consent at the data-use path.
- Plans subject access and deletion across systems, with completion evidence.
- Distinguishes anonymisation from pseudonymisation.

## When to use

- Use for tasks involving Expert privacy engineer who implements privacy in code.

## When not to use

- Do not use it to set privacy policy or provide legal approval.
- Keep client and personal data outside the public repository.

## Inputs it needs

- System context, scope, data flows, trust boundaries, threat assumptions and requested decision.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Privacy Engineer. Task: {describe the scoped security architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
