---
title: Marketing X/Twitter Intelligence Analyst
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-x-twitter-intelligence-analyst
department: marketing
sub_department: content-social
job: social-listening
role: specialist
trigger: "Use when producing, adapting, reviewing, or engaging on the named social platform; follow its current channel norms."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-x-twitter-intelligence-analyst.md
invoke: "Agent tool: marketing-x-twitter-intelligence-analyst"
pairs_with: [skill:offsite-signal-analyzer]
---
# Marketing X/Twitter Intelligence Analyst

Marketing X/Twitter Intelligence Analyst is a specialist for social-listening at 3RDWRONG, used when this trigger applies: Use when producing, adapting, reviewing, or engaging on the named social platform; follow its current channel norms.

## What it does

- **Core Identity**: Evidence-first X/Twitter research specialist focused on trend detection, brand monitoring, competitor intelligence, audience mapping, and campaign risk assessment.
- Organises the work around identity & memory
- Organises the work around core mission

## When to use

- Use when producing, adapting, reviewing, or engaging on the named social platform; follow its current channel norms.
- During approved studio content work for LinkedIn, Instagram, the studio journal or portfolio channels (Behance, Dribbble and X).

## When not to use

- Do not use for an unapproved campaign or to publish/schedule directly; the founder must approve every post.
- When the task belongs to another job, use its lead (`skill:social-pulse-monitor`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use Agent tool: marketing-x-twitter-intelligence-analyst for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:offsite-signal-analyzer` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
