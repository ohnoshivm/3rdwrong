---
title: Content Quality Auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:content-quality-auditor
department: marketing
sub_department: studio-brand-voice
job: editorial-quality
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/content-quality-auditor/SKILL.md
invoke: "Claude Code: `/content-quality-auditor`; Codex: `content-quality-auditor` skill"
pairs_with: [skill:domain-authority-auditor]
---
# Content Quality Auditor

Content Quality Auditor is 3RDWRONG’s lead for editorial quality in studio brand voice.

## What it does

- The source describes it as: Use when auditing content quality, E-E-A-T, or publish readiness; runs a typed 80-item CORE-EEAT profile with evidence coverage, veto checks, and a fix plan. Not for structural tags/headers alone — use on-page-seo-checker; not for domain/citation trust — use domain-authority-auditor. 内容质量/EEAT评分.
- The user asks for content quality, E-E-A-T, publish-readiness, or CORE-EEAT review.
- A new/refreshed artifact needs the content gate before publication.

## When to use

- Use as lead for editorial quality when the studio has an approved brief for this deliverable.
- Use for the studio’s own brand voice or a specifically approved client brief with cleared evidence.

## When not to use

- Do not use to invent brand strategy, claims, audience evidence or approval.
- Do not use as the sole reviewer of its own output; assign an independent checker.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use Content Quality Auditor for editorial quality at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- The result follows the tool file’s stated purpose and output structure.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.

## Pairs with

- `skill:domain-authority-auditor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
