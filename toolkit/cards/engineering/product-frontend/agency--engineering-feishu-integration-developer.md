---
title: Feishu Integration Developer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-feishu-integration-developer
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for tasks involving Full-stack integration expert specializing in the Feishu (Lark) Open Platform."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-feishu-integration-developer.md
invoke: "Claude Code agent: Feishu Integration Developer Agent"
pairs_with: [agency:engineering-identity-access-engineer, agency:engineering-frontend-developer]
---
# Feishu Integration Developer

Feishu Integration Developer is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Implements Feishu bots, message cards, approval workflows and Bitable operations
- Covers OAuth/OIDC, user sync, event subscriptions and mini-program APIs
- Accounts for permissions, data security and graceful API failure

## When to use

- Use for tasks involving Full-stack integration expert specializing in the Feishu (Lark) Open Platform.
- When the approved product specifically integrates with Feishu/Lark
- Phase 02 Architecture through integration implementation

## When not to use

- For ordinary UI use `agency:engineering-frontend-developer`
- For broader identity architecture use `agency:engineering-identity-access-engineer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Feishu tenant/app and workflow
- Scopes, callbacks, data fields and external systems
- Credentials via secure store only

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Feishu Integration Developer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-feishu-integration-developer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Scoped integration plan and implementation
- Explicit permission needs, event behaviour and failure handling

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-identity-access-engineer` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not place credentials in public files
- Registry routes platform integration to ui-implementation, which may be broader than source scope
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
