---
title: Next.js Partial Prefetching Adoption
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:next-partial-prefetching-adoption
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for tasks involving >."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/next-partial-prefetching-adoption/SKILL.md
invoke: "next-partial-prefetching-adoption skill"
pairs_with: [vercel:nextjs, skill:next-best-practices]
---
# Next.js Partial Prefetching Adoption

Next.js Partial Prefetching Adoption is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides adoption of Next.js partial prefetching
- Frames work as framework feature adoption
- Requires validating resulting route/loading behaviour

## When to use

- Use for tasks involving >.
- Only when approved Next task needs partial prefetching
- registry trigger `Use for tasks involving >` is malformed

## When not to use

- For general App Router use `vercel:nextjs`
- For Cache Components use `vercel:next-cache-components`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Next version and routes
- Current/desired navigation behaviour
- Test environment

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `next-partial-prefetching-adoption skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:next-partial-prefetching-adoption` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Scoped adoption and observed navigation behaviour
- Compatibility and build validation recorded

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `vercel:nextjs` — coordinate the artefacts and handoff at the relevant stage.
- `skill:next-best-practices` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Registry trigger malformed
- do not promise speed without measurement
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
