---
title: Social Measurement Loop
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:social-measurement-loop
department: marketing
sub_department: content-social
job: social-measurement
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/social-measurement-loop
invoke: "/social-measurement-loop"
pairs_with: [skill:performance-analyzer]
---
# Social Measurement Loop

Social Measurement Loop is the lead tool for social-measurement at 3RDWRONG.

## What it does

- The weekly organic-social readback loop — the sibling of paid-measurement-loop (upstream reference `../../../ad/scale/paid-measurement-loop/SKILL.md`) for unpaid channels.
- It owns the measurement-integrity core of the ECHO **O** lever and feeds five O sub-items in echo-benchmark.md (upstream reference `../../../references/echo-benchmark.md`): declared period-stable denominators (the upstream of the **ECHO-O1** veto),…
- It owns the O lever's dictionary and loop but **never computes the ECHO profile result** — only social-quality-auditor (upstream reference `../../host/social-quality-auditor/SKILL.md`) scores ECHO and runs vetoes.

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
Use /social-measurement-loop for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:performance-analyzer` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
