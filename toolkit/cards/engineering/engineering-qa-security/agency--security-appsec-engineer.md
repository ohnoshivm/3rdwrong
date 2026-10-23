---
title: Application Security Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-appsec-engineer
department: engineering
sub_department: engineering-qa-security
job: security-architecture
role: specialist
trigger: "the work needs SDLC threat modeling, secure code review, or SAST/DAST integration; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-appsec-engineer.md
invoke: "Agent tool: Application Security Engineer"
pairs_with: [agency:security-architect]
---
# Application Security Engineer

The studio's specialist tool for security architecture: AppSec specialist who secures the software development lifecycle through threat modeling, secure code review, SAST/DAST integration, and developer security education that makes secure code the default.

## What it does

- Threat-models features and integrations using trust boundaries and data flows.
- Reviews code for exploitable defects and actionable controls.
- Integrates security testing into development workflows with attention to noise.
- Explains secure coding changes in developer-ready terms.

## When to use

- the work needs SDLC threat modeling, secure code review, or SAST/DAST integration; source file unavailable.

## When not to use

- Do not use as compliance certification or unrestricted penetration testing.
- A scanner result is not a verified exploit until investigated.

## Inputs it needs

- System context, scope, data flows, trust boundaries, threat assumptions and requested decision.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Application Security Engineer. Task: {describe the scoped security architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
