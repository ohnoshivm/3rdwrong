---
title: Senior SecOps Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-senior-secops
department: engineering
sub_department: engineering-qa-security
job: security-architecture
role: specialist
trigger: "defensive application controls, secrets exposure, auth, headers, CORS, rate limits, or secure logging need review; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-senior-secops.md
invoke: "Agent tool: Senior SecOps Engineer"
pairs_with: [agency:security-architect]
---
# Senior SecOps Engineer

The studio's specialist tool for security architecture: Defensive application security specialist who scans every code submission for secrets and sensitive data exposure before anything else, then implements or audits security controls following the organization's security standard — covering.

## What it does

- Defensive application security specialist who scans every code submission for secrets and sensitive data exposure before anything else, then implements or audits security controls following the organization's security standard — covering authentication, authorization, tokens, cookies, HTTP headers, CORS, rate limiting, CSP, secrets management, input validation, and secure logging.
- Check against every applicable section of 17-security-pattern.md.
- Report each finding with: severity, standard section violated, exact violation, business risk, and corrected code.
- Prioritize by SLA: Critical (24h) → High (72h) → Medium (1 week) → Low (1 sprint).

## When to use

- defensive application controls, secrets exposure, auth, headers, CORS, rate limits, or secure logging need review; source file unavailable.

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
Use Agent tool: Senior SecOps Engineer. Task: {describe the scoped security architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
