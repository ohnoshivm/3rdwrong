---
title: Email Sequence Designer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:email-sequence-designer
department: marketing
sub_department: content-social
job: lifecycle-copy
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/email-sequence-designer
invoke: "/email-sequence-designer"
pairs_with: [skill:email-quality-auditor]
---
# Email Sequence Designer

Email Sequence Designer is the lead tool for lifecycle-copy at 3RDWRONG.

## What it does

- Designs email lifecycle and automation flows plus the program's frequency governance, and scores the SEND **N (Nurture / Lifecycle)** dimension.
- It maps each flow's trigger, step timing, branch/exit conditions, and goal, layers a global cadence policy (send caps, quiet hours, fatigue guardrail) and a re-engagement/sunset path over the top, then hands the flow map to the skill…
- It covers general lifecycle flows and owns the engagement-decay/sunset sub-item; the closed-loop win-back / re-consent (re-permission) program on a defined lapsed cohort is…

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
Use /email-sequence-designer for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:email-quality-auditor` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
