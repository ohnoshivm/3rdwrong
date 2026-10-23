---
title: Cloud Security Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-cloud-security-architect
department: engineering
sub_department: engineering-qa-security
job: security-architecture
role: specialist
trigger: "AWS, Azure, GCP, or infrastructure-as-code security architecture is in scope; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-cloud-security-architect.md
invoke: "Agent tool: Cloud Security Architect"
pairs_with: [agency:security-architect]
---
# Cloud Security Architect

The studio's specialist tool for security architecture: Cloud-native security specialist designing zero trust architectures, implementing defense-in-depth across AWS, Azure, and GCP, and securing infrastructure-as-code pipelines from day one.

## What it does

- Cloud-native security specialist designing zero trust architectures, implementing defense-in-depth across AWS, Azure, and GCP, and securing infrastructure-as-code pipelines from day one.
- Design network architectures where no traffic is trusted by default — every request is authenticated, authorized, and encrypted regardless of source.
- Implement identity-based access control: service mesh mTLS, workload identity federation, just-in-time access, and continuous authorization.
- Segment environments using cloud-native constructs: VPCs, security groups, network policies, private endpoints, and service perimeters.

## When to use

- AWS, Azure, GCP, or infrastructure-as-code security architecture is in scope; source file unavailable.

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
Use Agent tool: Cloud Security Architect. Task: {describe the scoped security architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
