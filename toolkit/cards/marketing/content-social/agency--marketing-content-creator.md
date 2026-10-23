---
title: Marketing Content Creator Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-content-creator
department: marketing
sub_department: content-social
job: content-writing
role: specialist
trigger: "Use when the studio has approved a long-form or creator-led content assignment with a clear point of view and source material."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-content-creator.md
invoke: "Agent tool: marketing-content-creator"
pairs_with: [skill:content-quality-auditor]
---
# Marketing Content Creator Agent

Marketing Content Creator Agent is a specialist for content-writing at 3RDWRONG, used when this trigger applies: Use when the studio has approved a long-form or creator-led content assignment with a clear point of view and source material.

## What it does

- Organises the work around identity & role definition
- Organises the work around core capabilities
- Organises the work around specialized skills

## When to use

- Use when the studio has approved a long-form or creator-led content assignment with a clear point of view and source material.
- During approved studio content work for LinkedIn, Instagram, the studio journal or portfolio channels (Behance, Dribbble and X).

## When not to use

- Do not use for an unapproved campaign or to publish/schedule directly; the founder must approve every post.
- When the task belongs to another job, use its lead (`skill:content-writer`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use Agent tool: marketing-content-creator for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:content-quality-auditor` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
