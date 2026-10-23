---
title: Marketing Baidu SEO Specialist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-baidu-seo-specialist
department: marketing
sub_department: search-aeo
job: keyword-research
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-baidu-seo-specialist.md
invoke: "Agent tool: marketing-baidu-seo-specialist"
pairs_with: [skill:seo-content-brief]
---
# Marketing Baidu SEO Specialist

Marketing Baidu SEO Specialist is a specialist for keyword-research at 3RDWRONG, used when this trigger applies: Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.

## What it does

- Organises the work around 🧠 your identity & memory
- Organises the work around 🎯 your core mission
- Organises the work around master baidu's unique search algorithm

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
- During approved work on the studio journal or studio presence when organic or AI search visibility is in scope.

## When not to use

- Do not use to claim rankings, traffic, citations or search performance without source data and a defined measurement window.
- When the task belongs to another job, use its lead (`skill:keyword-research`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use Agent tool: marketing-baidu-seo-specialist for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:seo-content-brief` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
