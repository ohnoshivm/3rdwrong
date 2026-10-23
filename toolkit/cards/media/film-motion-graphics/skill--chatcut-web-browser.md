---
title: Chatcut Web Browser
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-web-browser
department: media
sub_department: film-motion-graphics
job: asset-research
role: specialist
trigger: "Use to collect source media or brand assets from a URL for production."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-web-browser/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-web-browser`"
pairs_with: [juicylucy-ads:media-use]
---
# Chatcut Web Browser

The studio's specialist for asset-research; activate when Use to collect source media or brand assets from a URL for production

## What it does

- No setup: Firecrawl key lives in the backend proxy, not in the agent.
- country` is auto-applied for known geo-blocked sites (Amazon, Walmart, eBay, etc.). Pass `country` explicitly to override.
- execJs` runs JavaScript BEFORE content extraction. Return value at `data.actions.javascriptReturns`.
- actions` takes raw Firecrawl actions JSON. See [Firecrawl docs](https://docs.firecrawl.dev/features/scrape#actions) for all action types.

## When to use

- Use to collect source media or brand assets from a URL for production.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-web-browser/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-web-browser` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-web-browser` for the asset-research task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `juicylucy-ads:media-use`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-web-browser/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
