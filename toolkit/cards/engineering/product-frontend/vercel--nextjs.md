---
title: Vercel Next.js
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vercel:nextjs
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Next.js App Router expert guidance ."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-vercel-0.50.0/skills/nextjs
invoke: "nextjs skill"
pairs_with: [skill:next-upgrade, vercel:next-cache-components]
---
# Vercel Next.js

Vercel Next.js is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides App Router routing, RSC, Server Actions, caching, middleware/proxy and fetching
- Includes framework path and command signals
- Supports architecture and implementation decisions

## When to use

- Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Next.js App Router expert guidance .
- For App Router work
- Phase 02/05

## When not to use

- For non-Next React use `agent:frontend-architect`
- For version migration use `skill:next-upgrade`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Next version and App Router structure
- Route/data/rendering needs
- Runtime and performance constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `nextjs skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `vercel:nextjs` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Version-aligned implementation
- Data, server/client, cache and error boundaries explicit

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:next-upgrade` — coordinate the artefacts and handoff at the relevant stage.
- `vercel:next-cache-components` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Check official versioned guidance
- avoid unnecessary caching and client complexity
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
