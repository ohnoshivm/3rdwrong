---
title: DX Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:product-dx-engineer
department: engineering
sub_department: product-frontend
job: application-integrations
role: specialist
trigger: "Use for engineering/product-frontend/application-integrations when the brief specifically requires: Removes every unnecessary step between a developer and their first success — SDK samples, onboarding flows, error messages, and the feedback loops that make products feel like they were built by someone who's used them ."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/product-dx-engineer.md
invoke: "Claude Code agent: DX Engineer Agent"
pairs_with: [agency:engineering-frontend-developer, agency:engineering-identity-access-engineer]
---
# DX Engineer

DX Engineer is the studio's specialist for `application-integrations`; use it when the registry trigger below applies.

## What it does

- Audits developer onboarding and first-run journeys
- Improves SDK samples and actionable errors
- Routes feedback and requires validation with new developers

## When to use

- Use for engineering/product-frontend/application-integrations when the brief specifically requires: Removes every unnecessary step between a developer and their first success — SDK samples, onboarding flows, error messages, and the feedback loops that make products feel like they were built by someone who's used them .
- When developer first-success, SDK, onboarding or error-message experience is in scope
- Use during product integration work

## When not to use

- For end-user onboarding use product design/research
- For auth implementation use `agency:engineering-identity-access-engineer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Developer product and first-success action
- Docs, SDK examples, errors and user feedback
- Access to new-developer testing or explicit evidence limits

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: DX Engineer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:product-dx-engineer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Prioritised friction report with concrete fixes
- Observed behaviour separated from assumptions

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-identity-access-engineer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not invent research or A/B outcomes
- source scope is broader developer experience than registry application-integrations label
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
