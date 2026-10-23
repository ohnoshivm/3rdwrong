---
title: Next.js Best Practices
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:next-best-practices
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Next.js best practices - file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image/font optimization, bundling ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-vercel-vercel-plugin-apache-2.0/skills/next-best-practices
invoke: "next-best-practices skill"
pairs_with: [skill:next-upgrade, vercel:nextjs]
---
# Next.js Best Practices

Next.js Best Practices is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides file conventions, RSC boundaries and data patterns
- Covers async APIs, metadata, errors, route handlers, assets and bundling
- Provides framework-specific implementation guidance

## When to use

- Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Next.js best practices - file conventions, RSC boundaries, data patterns, async APIs, metadata, error handling, route handlers, image/font optimization, bundling .
- When Next.js architecture conventions or APIs are in scope
- Phase 02/05

## When not to use

- For React without Next use `agent:frontend-architect`
- For version migration use `skill:next-upgrade`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Next.js version/router and relevant files
- Route/data behaviour
- Cache/deployment constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `next-best-practices skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:next-best-practices` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Version-aware recommendation aligned to selected router
- Server/client and error behaviour explicit

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:next-upgrade` — coordinate the artefacts and handoff at the relevant stage.
- `vercel:nextjs` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Verify installed version
- avoid unnecessary client components and caching
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
