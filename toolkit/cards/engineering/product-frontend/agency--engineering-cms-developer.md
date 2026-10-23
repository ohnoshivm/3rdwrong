---
title: CMS Developer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-cms-developer
department: engineering
sub_department: product-frontend
job: site-and-cms-build
role: lead
trigger: ""
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-cms-developer.md
invoke: "Claude Code agent: CMS Developer Agent"
pairs_with: [agency:engineering-frontend-developer, agent:frontend-architect, skill:building-accessible-interfaces]
---
# CMS Developer

CMS Developer is the studio's lead for `site-and-cms-build`.

## What it does

- Models content and editorial workflows before implementation
- Builds Drupal/WordPress themes, plugins, modules and editorial blocks
- Uses extension points and audits accessibility, security and performance

## When to use

- Phase 02 Architecture when selecting or extending Drupal/WordPress
- Before theme implementation, lock the content model and editorial workflow

## When not to use

- For framework-agnostic UI use `agency:engineering-frontend-developer`
- For decoupled frontend architecture use `agent:frontend-architect`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Target CMS/version and new vs existing site
- Approved content model, editorial roles, tokens and integrations
- Accessibility and deployment constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: CMS Developer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-cms-developer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Code-based content model and scoped CMS implementation
- Documented extension choices and editorial/accessibility checks

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not modify parent or contributed themes
- Keep configuration in code and vet extensions
- Source states WCAG 2.1 AA baseline
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
