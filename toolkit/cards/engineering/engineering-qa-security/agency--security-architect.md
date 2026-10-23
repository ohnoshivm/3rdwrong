---
title: Security Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-architect
department: engineering
sub_department: engineering-qa-security
job: security-architecture
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-architect.md
invoke: "Agent tool: Security Architect"
pairs_with: [agency:engineering-privacy-engineer, agency:security-ai-generated-code-auditor, agency:security-appsec-engineer]
---
# Security Architect

The studio's lead tool for security architecture: Expert security architect specializing in threat modeling, secure-by-design architecture, trust-boundary analysis, defense-in-depth, and risk-based security reviews across web, API, cloud-native, and distributed systems.

## What it does

- Expert security architect specializing in threat modeling, secure-by-design architecture, trust-boundary analysis, defense-in-depth, and risk-based security reviews across web, API, cloud-native, and distributed systems. Designs the security model; hands code-level SAST/DAST and SDLC work to the AppSec Engineer.
- Integrate security into every phase — design, implementation, testing, deployment, and operations.
- Conduct threat modeling sessions to identify risks before code is written.
- Perform secure code reviews focusing on OWASP Top 10 (2021+), CWE Top 25, and framework-specific pitfalls.

## When to use

- Phase 03 Technical Architecture, before fixing trust boundaries or security controls.

## When not to use

- Do not use it as formal certification or legal advice.
- Do not claim assurance beyond the supplied evidence.

## Inputs it needs

- System context, scope, data flows, trust boundaries, threat assumptions and requested decision.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Security Architect. Task: {describe the scoped security architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Threats connect to assets, paths and controls, with residual risks stated.
- Unknowns and verification needs are visible.

## Quality checks

- [ ] Scope and trust boundaries are explicit.
- [ ] Controls map to threats.
- [ ] Residual risks and owners are recorded.

## Pairs with

- `agency:engineering-privacy-engineer`, `agency:security-ai-generated-code-auditor`, `agency:security-appsec-engineer`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
