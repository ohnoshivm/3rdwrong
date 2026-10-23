---
title: Next.js Cache Components Adoption
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:next-cache-components-adoption
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for tasks involving >."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/next-cache-components-adoption/SKILL.md
invoke: "next-cache-components-adoption skill"
pairs_with: [vercel:next-cache-components, vercel:nextjs]
---
# Next.js Cache Components Adoption

Next.js Cache Components Adoption is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides adoption of Next.js Cache Components
- Supports assessing current code and planning feature adoption
- Provides framework-specific migration guidance

## When to use

- Use for tasks involving >.
- Only when approved Next.js task specifically concerns Cache Components
- registry trigger `Use for tasks involving >` is malformed

## When not to use

- For Next.js 16 cache APIs use `vercel:next-cache-components`
- For broader App Router use `vercel:nextjs`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Next version and cache/rendering patterns
- Adoption scope and routes/data
- Build/runtime checks

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `next-cache-components-adoption skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:next-cache-components-adoption` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Scoped adoption plan and compatibility concerns
- Observed validation rather than assumed cache behaviour

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `vercel:next-cache-components` — coordinate the artefacts and handoff at the relevant stage.
- `vercel:nextjs` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Registry trigger malformed
- verify framework version and source guidance
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
