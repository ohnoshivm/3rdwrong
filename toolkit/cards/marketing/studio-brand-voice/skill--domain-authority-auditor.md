---
title: Domain Authority Auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:domain-authority-auditor
department: marketing
sub_department: studio-brand-voice
job: editorial-quality
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/domain-authority-auditor/SKILL.md
invoke: "Claude Code: `/domain-authority-auditor`; Codex: `domain-authority-auditor` skill"
pairs_with: [skill:content-quality-auditor]
---
# Domain Authority Auditor

Domain Authority Auditor is a 3RDWRONG specialist for editorial quality, activated only when its registry trigger applies.

## What it does

- The source describes it as: Use when auditing domain authority, trust, or citation credibility; runs a peer-relative 40-item CITE profile with evidence coverage and verified manipulation/penalty veto checks. Not for page-level content quality — use content-quality-auditor; not for backlink profiling alone — use offsite-signal-analyzer. 域名权威/网站可信度.
- The user asks whether a domain is trustworthy, authoritative, or citation-ready.
- A campaign needs a peer-relative CITE baseline or rerun.

## When to use

- Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available.
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
Use Domain Authority Auditor for editorial quality at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
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

- `skill:content-quality-auditor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
