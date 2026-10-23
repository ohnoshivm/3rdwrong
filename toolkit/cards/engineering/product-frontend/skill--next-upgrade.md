---
title: Next.js Upgrade
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:next-upgrade
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Upgrade Next.js to the latest version following official migration guides and codemods ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-vercel-vercel-plugin-apache-2.0/skills/next-upgrade
invoke: "next-upgrade skill"
pairs_with: [skill:next-best-practices, vercel:nextjs]
---
# Next.js Upgrade

Next.js Upgrade is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides upgrading Next.js using official migration guidance and codemods
- Scopes steps to current project versions
- Supports version-specific migration planning

## When to use

- Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Upgrade Next.js to the latest version following official migration guides and codemods .
- When an explicit Next.js upgrade is approved
- Phase 02/05

## When not to use

- For feature adoption without version upgrade use `skill:next-best-practices`
- Do not upgrade as incidental cleanup
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Current Next/React versions and package manager
- Target version and app router
- Tests and deployment constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `next-upgrade skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:next-upgrade` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Staged upgrade with official guidance
- Build/type/test results and gaps

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:next-best-practices` — coordinate the artefacts and handoff at the relevant stage.
- `vercel:nextjs` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Keep package changes approved
- codemod alone does not prove compatibility
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
