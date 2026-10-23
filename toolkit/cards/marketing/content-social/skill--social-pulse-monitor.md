---
title: Social Pulse Monitor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:social-pulse-monitor
department: marketing
sub_department: content-social
job: social-listening
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/social-pulse-monitor
invoke: "/social-pulse-monitor"
pairs_with: [skill:offsite-signal-analyzer]
---
# Social Pulse Monitor

Social Pulse Monitor is the lead tool for social-listening at 3RDWRONG.

## What it does

- Always-on brand and community listening — the ears of the ECHO **Observe** phase.
- It maintains the listening-query architecture, sweeps the keyless public surfaces for mentions, triages each one to an owner with an SLA, and keeps the 7-day rolling baseline whose spike flag is the trigger input for…
- It feeds three ECHO `O` sub-items directly: *7-day listening baseline maintained with spike thresholds set*, *listening-query architecture current (brand variants incl. 中文 names and misspellings, exclusion terms, per-source syntax)*,…

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
Use /social-pulse-monitor for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
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
