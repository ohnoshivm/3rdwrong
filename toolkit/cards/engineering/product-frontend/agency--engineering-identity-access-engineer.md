---
title: Identity & Access Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-identity-access-engineer
department: engineering
sub_department: product-frontend
job: application-integrations
role: lead
trigger: ""
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-identity-access-engineer.md
invoke: "Claude Code agent: Identity & Access Engineer Agent"
pairs_with: [agency:engineering-feishu-integration-developer, agent:frontend-architect]
---
# Identity & Access Engineer

Identity & Access Engineer is the studio's lead for `application-integrations`.

## What it does

- Designs OAuth/OIDC, enterprise SSO, SCIM, passkeys and session architecture
- Models tenant-scoped RBAC/ABAC with server-side checks
- Requires threat notes, auth audit events and failure-path tests

## When to use

- Phase 02 Architecture before choosing login, SSO, session or tenant-authorisation patterns
- For security-sensitive identity changes

## When not to use

- Not the sole security reviewer or penetration tester
- For Feishu-specific auth use `agency:engineering-feishu-integration-developer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Identity providers, clients and tenant model
- Session/token constraints and recovery flows
- Threat model and failure cases, no public secrets

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Identity & Access Engineer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-identity-access-engineer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Explicit auth/session/authorisation design
- Server-side checks, recovery, audit and failure tests

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-feishu-integration-developer` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Reject custom auth primitives
- high-risk changes need a separate checker
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
