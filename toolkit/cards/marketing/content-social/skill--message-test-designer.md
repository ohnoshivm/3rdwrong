---
title: Message Test Designer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:message-test-designer
department: marketing
sub_department: content-social
job: content-writing
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/message-test-designer
invoke: "/message-test-designer"
pairs_with: [skill:content-quality-auditor]
---
# Message Test Designer

Message Test Designer is a specialist for content-writing at 3RDWRONG, used when this trigger applies: Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.

## What it does

- Designs the pre-scale message validation for a candidate narrative — the hypothesis, the target panel and recruit criteria, the comprehension / 5-second / message-market-fit (Wynter-style) protocols, the stimulus set drawn from the…
- It sits in the **Evaluate** phase of the TALE loop and feeds the `E` sub-item *the message is tested before scale* (comprehension / 5-second / message-market-fit panel) — see tale-benchmark.md (upstream reference `../../../references/tale-benchmark.md`).
- Its output is a **test design spec only**: this skill designs the test, hands execution to the experiment builders, and never runs the panel, analyzes results, or adjudicates a claim.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
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
Use /message-test-designer for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
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
