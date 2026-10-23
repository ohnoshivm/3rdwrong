---
title: Facebook Page Optimizer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: facebook-skills:fb-page-optimizer
department: marketing
sub_department: content-social
job: social-copy
role: specialist
trigger: "Use when producing, adapting, reviewing, or engaging on the named social platform; follow its current channel norms."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-local-desktop-app-uploads-facebook-skills-marketplace/skills/facebook-skills/.codex-marketplace/facebook-skills/skills/fb-page-optimizer
invoke: "/fb-page-optimizer"
pairs_with: [skill:social-quality-auditor]
---
# Facebook Page Optimizer

Facebook Page Optimizer is a specialist for social-copy at 3RDWRONG, used when this trigger applies: Use when producing, adapting, reviewing, or engaging on the named social platform; follow its current channel norms.

## What it does

- Audit the parts of a Facebook Page that decide whether a first-time visitor follows the Page or takes the action you want, then rewrite each part that needs it.
- On a Page the decision happens fast on the top card: Page name, profile picture, cover photo, and the CTA button.
- The button is the whole point of a Page.

## When to use

- Use when producing, adapting, reviewing, or engaging on the named social platform; follow its current channel norms.
- During approved studio content work for LinkedIn, Instagram, the studio journal or portfolio channels (Behance, Dribbble and X).

## When not to use

- Do not use for an unapproved campaign or to publish/schedule directly; the founder must approve every post.
- When the task belongs to another job, use its lead (`skill:social-creative-builder`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use /fb-page-optimizer for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
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
