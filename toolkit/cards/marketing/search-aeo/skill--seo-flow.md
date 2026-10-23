---
title: "FLOW Framework: Find \u00b7 Leverage \u00b7 Optimize \u00b7 Win"
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:seo-flow
department: marketing
sub_department: search-aeo
job: seo-strategy
role: specialist
trigger: "Use when organic or AI search visibility is in scope for the studio presence or a specifically approved campaign."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-agricidaniel-claude-seo-mit/skills/seo-flow
invoke: "/seo-flow"
pairs_with: [skill:technical-seo-checker]
---
# FLOW Framework: Find · Leverage · Optimize · Win

FLOW Framework: Find · Leverage · Optimize · Win is a specialist for seo-strategy at 3RDWRONG, used when this trigger applies: Use when organic or AI search visibility is in scope for the studio presence or a specifically approved campaign.

## What it does

- FLOW is an evidence-led SEO operating model built for the AI-search era.
- Claude SEO integrates the FLOW prompt library (41 prompts across 5 stages) so every analysis can be driven by structured, evidence-backed AI prompts rather than improvised queries.
- Organises the work around commands

## When to use

- Use when organic or AI search visibility is in scope for the studio presence or a specifically approved campaign.
- During approved work on the studio journal or studio presence when organic or AI search visibility is in scope.

## When not to use

- Do not use to claim rankings, traffic, citations or search performance without source data and a defined measurement window.
- When the task belongs to another job, use its lead (`skill:seo-plan`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use /seo-flow for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:technical-seo-checker` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
