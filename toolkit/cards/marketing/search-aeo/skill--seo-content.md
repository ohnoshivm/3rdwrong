---
title: Content Quality & E-E-A-T Analysis
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:seo-content
department: marketing
sub_department: search-aeo
job: seo-content
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-agricidaniel-claude-seo-mit/skills/seo-content
invoke: "/seo-content"
pairs_with: [skill:seo-content-brief]
---
# Content Quality & E-E-A-T Analysis

Content Quality & E-E-A-T Analysis is the lead tool for seo-content at 3RDWRONG.

## What it does

- Before scoring E-E-A-T sub-factors, every page audit should pass Google's own three-question heuristic from the helpful-content guide:
- Organises the work around google's "who / how / why" test (canonical heuristic)
- Organises the work around e-e-a-t framework (updated sept 2025 qrg)

## When to use

- During approved work on the studio journal or studio presence when organic or AI search visibility is in scope.

## When not to use

- Do not use to claim rankings, traffic, citations or search performance without source data and a defined measurement window.
- When the task belongs to another job, use its appropriate lead, such as `skill:seo-plan` for adjacent work.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use /seo-content for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- Pairs with `skill:seo-content-brief` to turn search intent and queries into a content brief.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
