---
title: Vercel Next.js Cache Components
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vercel:next-cache-components
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Next.js 16 Cache Components guidance — PPR, use cache directive, cacheLife, cacheTag, updateTag, and migration from unstable_cache ."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-vercel-0.50.0/skills/next-cache-components
invoke: "next-cache-components skill"
pairs_with: [vercel:nextjs, skill:next-cache-components-adoption]
---
# Vercel Next.js Cache Components

Vercel Next.js Cache Components is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides Next.js 16 Cache Components, PPR and cache APIs
- Covers `use cache`, `cacheLife`, `cacheTag`, `updateTag` and unstable_cache migration
- Supports scoped caching strategy

## When to use

- Use for engineering/product-frontend/frontend-architecture when the brief specifically requires: Next.js 16 Cache Components guidance — PPR, use cache directive, cacheLife, cacheTag, updateTag, and migration from unstable_cache .
- For measured Next.js 16 cache requirement
- Phase 02/05

## When not to use

- For general App Router use `vercel:nextjs`
- Do not add caching without invalidation need
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Next version and cache implementation
- Freshness/invalidation and request requirements
- Build/runtime measurements

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `next-cache-components skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `vercel:next-cache-components` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Explicit cache boundaries and invalidation
- Correct fresh/stale/revalidated behaviour observed

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `vercel:nextjs` — coordinate the artefacts and handoff at the relevant stage.
- `skill:next-cache-components-adoption` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Confirm exact version
- do not promise performance without measurement
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
