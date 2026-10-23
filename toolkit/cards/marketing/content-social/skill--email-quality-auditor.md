---
title: Email Quality Auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:email-quality-auditor
department: marketing
sub_department: content-social
job: lifecycle-copy
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/email-quality-auditor
invoke: "/email-quality-auditor"
pairs_with: [skill:email-sequence-designer]
---
# Email Quality Auditor

Email Quality Auditor is a specialist for lifecycle-copy at 3RDWRONG, used when this trigger applies: Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.

## What it does

- Audit one email program/profile and observation window with SEND.
- Open rate is MPP-sensitive proxy evidence; direct action and the program's declared outcome truth set carry the outcome read.
- Organises the work around when this must trigger

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
- During approved studio content work for LinkedIn, Instagram, the studio journal or portfolio channels (Behance, Dribbble and X).

## When not to use

- Do not use for an unapproved campaign or to publish/schedule directly; the founder must approve every post.
- When the task belongs to another job, use its lead (`skill:email-sequence-designer`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use /email-quality-auditor for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- Pairs with `skill:email-sequence-designer` to return quality findings to lifecycle copy planning.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
