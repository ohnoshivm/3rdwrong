---
title: Message House Builder
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:message-house-builder
department: marketing
sub_department: studio-brand-voice
job: message-architecture
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/message-house-builder/SKILL.md
invoke: "Claude Code: `/message-house-builder`; Codex: `message-house-builder` skill"
pairs_with: [skill:message-system-architect, skill:narrative-baseline-mapper, skill:narrative-resonance-monitor]
---
# Message House Builder

Message House Builder is a 3RDWRONG specialist for message architecture, activated only when its registry trigger applies.

## What it does

- Derives launch-specific messaging from accepted L1 Narrative canon and positioning evidence: a message house, PR-FAQ spine, and per-channel angle packs. It never turns launch copy into a competing brand canon and never adjudicates claims.
- Expected output: a message house (tagline + one-liner + three value pillars + per-persona proof points, each labeled Measured / User-provided / [needs source]), a PR-FAQ narrative spine (launch-day tense, empty-chair test, numbers over adjectives, five external + five internal FAQs), per-channel message angle packs (angles, not finished copy), a [needs source] claims list for the ledger, and the standard handoff summary.
- Writes: the launch house/PR-FAQ/angle packs to memory/launch/message-house-builder/ with permission; unresolved claims and durable canon changes become separate authorized proposal events.

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
Use Message House Builder for message architecture at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a message house (tagline + one-liner + three value pillars + per-persona proof points, each labeled Measured / User-provided / [needs source]), a PR-FAQ narrative spine (launch-day tense, empty-chair test, numbers over adjectives, five external + five internal FAQs), per-channel message angle packs (angles, not finished copy), a [needs source] claims list for the ledger, and the standard handoff summary.
- the house is internally coherent and traceable to accepted canon, proof points are evidence-labeled, PR-FAQ checks pass, unresolved claims are blocked/proposed, and the dependency tuple is present.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.

## Pairs with

- `skill:message-system-architect` — same job; use when its own role or trigger applies.
- `skill:narrative-baseline-mapper` — same job; use when its own role or trigger applies.
- `skill:narrative-resonance-monitor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
