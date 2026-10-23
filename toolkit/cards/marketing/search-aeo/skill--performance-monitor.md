---
title: Performance Monitor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:performance-monitor
department: marketing
sub_department: search-aeo
job: search-measurement
role: specialist
trigger: "SEO performance reporting or alerts are requested; registry summary identifies marketing/search analytics, so route to Marketing."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/performance-monitor
invoke: "/performance-monitor"
pairs_with: [skill:rank-tracker]
---
# Performance Monitor

Performance Monitor is a specialist for search-measurement at 3RDWRONG, used when this trigger applies: SEO performance reporting or alerts are requested; registry summary identifies marketing/search analytics, so route to Marketing.

## What it does

- One monitor skill, two modes. **`report`** builds a stakeholder-facing multi-metric snapshot of what already happened (traffic, rankings, GEO/AI, authority, backlinks, content) and turns period-over-period deltas into prioritized…
- Pick the mode from intent: past-tense reporting → `report`; future-tense "tell me when" → `alert`.
- Organises the work around handoff summary

## When to use

- SEO performance reporting or alerts are requested; registry summary identifies marketing/search analytics, so route to Marketing.
- During approved work on the studio journal or studio presence when organic or AI search visibility is in scope.

## When not to use

- Do not use to claim rankings, traffic, citations or search performance without source data and a defined measurement window.
- When the task belongs to another job, use its lead (`skill:rank-tracker`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use /performance-monitor for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- Pairs with `skill:rank-tracker` to combine ongoing search monitoring with rank tracking.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
