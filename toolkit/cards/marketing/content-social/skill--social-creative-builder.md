---
title: Social Creative Builder
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:social-creative-builder
department: marketing
sub_department: content-social
job: social-copy
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/social-creative-builder
invoke: "/social-creative-builder"
pairs_with: [skill:social-quality-auditor]
---
# Social Creative Builder

Social Creative Builder is the lead tool for social-copy at 3RDWRONG.

## What it does

- Turns one approved idea into N platform-native, ready-to-paste packages — post/thread, caption, Threads text, 小红书 note, link post with first-comment placement — plus a carousel slide-spec mode.
- It is the per-post build skill of the ECHO **Craft** phase and feeds the C sub-items directly: claim-ledger match and required disclosures (the upstream of the ECHO C1/C2 vetoes), dated-norm-card adaptation (never verbatim…
- Claims handling mirrors email-creative-builder (upstream reference `../../../email/engage/email-creative-builder/SKILL.md`): product claims ship only in approved ledger wording; anything unverified is flagged, never invented.

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
Use /social-creative-builder for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
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
