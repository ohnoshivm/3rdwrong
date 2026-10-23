---
title: Engagement Inbox Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:engagement-inbox-manager
department: marketing
sub_department: content-social
job: community-engagement
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/engagement-inbox-manager
invoke: "/engagement-inbox-manager"
pairs_with: [skill:social-quality-auditor]
---
# Engagement Inbox Manager

Engagement Inbox Manager is the lead tool for community-engagement at 3RDWRONG.

## What it does

- Runs the always-on inbox — comments, DMs, mentions — as a hosting discipline: read the register before the sentiment, classify the commenter before the reply, and turn everything answerable into ranked drafts a human posts.
- It is the Host-phase workhorse of the ECHO loop and feeds four ECHO H sub-items directly: the UGC-permission fact base the **H2** veto is judged against, inbox SLA attainment (**H3**), the live escalation matrix with named owners…
- The per-channel SLA tiers, cadence commitments, and `ugc-permissions.md` status it works from live in channel-registry (upstream reference `../../../protocol/channel-registry/SKILL.md`), and [social-quality-auditor](../../../vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/social-quality-auditor/SKILL.md)…

## When to use

- During approved studio content work for LinkedIn, Instagram, the studio journal or portfolio channels (Behance, Dribbble and X).

## When not to use

- Do not use for an unapproved campaign or to publish/schedule directly; the founder must approve every post.
- When the task belongs to another job, use its appropriate lead, such as `skill:social-calendar-builder` for adjacent work.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use /engagement-inbox-manager for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:social-quality-auditor` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
