---
title: Sites
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: sites:sites
department: engineering
sub_department: product-frontend
job: site-and-cms-build
role: specialist
trigger: "Use for engineering/product-frontend/site-and-cms-build when the brief specifically requires: Use Sites when the user wants a website built for them (including a landing page, portfolio, dashboard, portal, tracker, hub, game, event registration, or tool), requests changes to a website already built with Sites, wants to publish a website with Sites, or wants to manage Sites hosting ."
kind: plugin-skill
availability: both
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/sites/1.1.1/skills/sites/SKILL.md
invoke: "sites skill"
pairs_with: [sites:sites-remix, agent:frontend-architect]
---
# Sites

Sites is the studio's specialist for `site-and-cms-build`; use it when the registry trigger below applies.

## What it does

- Runs supported Sites work through source prep, implementation and validation
- Supports new/existing hosted sites and hosting configuration
- Separates local-only work from hosted publication

## When to use

- Use for engineering/product-frontend/site-and-cms-build when the brief specifically requires: Use Sites when the user wants a website built for them (including a landing page, portfolio, dashboard, portal, tracker, hub, game, event registration, or tool), requests changes to a website already built with Sites, wants to publish a website with Sites, or wants to manage Sites hosting .
- Only when user requests Sites build, edit, publish or hosting
- follow requested hosted/local mode

## When not to use

- For ordinary local repo use `agent:frontend-architect`
- For a remix use `sites:sites-remix`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Clear request and new/existing Site
- Project ID/URL and source
- Assets, integrations and constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `sites skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `sites:sites` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Prepared and validated source plus confirmed hosting state
- Actual preview/build outcomes and blockers

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `sites:sites-remix` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- New hosted Sites start private
- publishing is default unless local-only requested
- protect credentials
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
