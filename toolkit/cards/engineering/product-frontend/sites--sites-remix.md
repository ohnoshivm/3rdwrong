---
title: Sites Remix
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: sites:sites-remix
department: engineering
sub_department: product-frontend
job: site-and-cms-build
role: specialist
trigger: "Use for engineering/product-frontend/site-and-cms-build when the brief specifically requires: Remix a Site built with the Sites plugin into a new Site ."
kind: plugin-skill
availability: both
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/sites/1.1.1/skills/sites-remix/SKILL.md
invoke: "sites-remix skill"
pairs_with: [sites:sites, agent:frontend-architect]
---
# Sites Remix

Sites Remix is the studio's specialist for `site-and-cms-build`; use it when the registry trigger below applies.

## What it does

- Creates a new unpublished Site adapted from a published source
- Copies bundled content but not runtime settings, database records or stored files
- Requires source inspection, content decisions, adaptation and handoff

## When to use

- Use for engineering/product-frontend/site-and-cms-build when the brief specifically requires: Remix a Site built with the Sites plugin into a new Site .
- Only when an identified Sites source is to be remixed

## When not to use

- For editing same site use `sites:sites`
- Do not assume runtime data transfers
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Source URL/slug or project ID
- Keep/clear content and feature decisions
- Required integrations and config

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `sites-remix skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `sites:sites-remix` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- New adapted unpublished Site matching agreed choices
- Confirmed publish state and data limitations

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `sites:sites` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Runtime settings/data/files do not copy
- source access may not provide complete schema
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
