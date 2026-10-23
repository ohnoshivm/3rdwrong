---
title: Message System Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:message-system-architect
department: marketing
sub_department: studio-brand-voice
job: message-architecture
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/message-system-architect/SKILL.md
invoke: "Claude Code: `/message-system-architect`; Codex: `message-system-architect` skill"
pairs_with: [skill:message-house-builder, skill:narrative-baseline-mapper, skill:narrative-resonance-monitor]
---
# Message System Architect

Message System Architect is 3RDWRONG’s lead for message architecture in studio brand voice.

## What it does

- Authors the durable brand message hierarchy — the main narrative, three value pillars, per-persona proof points, and the tagline/one-liner — that outlives any single launch and seeds the narrative-registry canon. It is the anchor of the TALE Architect phase and the upstream of the A1 canon-integrity veto: the auditor judges *canon exists and its hierarchy does not contradict itself* against the record this skill proposes. It feeds several TALE-A sub-items directly — *message house complete (tagline, one-liner, three value pillars, per-persona proof points)*, *each pillar traces to a positioning value theme (no orphan pillar)*, and *per-persona proof points each labeled Measured / User-provided / [needs source]*. The per-launch message-house-builder is reused, not replaced — it derives its launch PR-FAQ *from* this durable house, and its output must not contradict the canon this skill seeds.
- Expected output: a durable brand message house — main narrative, three value pillars, per-persona proof points, and tagline/one-liner — with an internal-consistency pass, an immutable canon-grade candidate binding (canon_id, version, hash, current head, supersedes), a [needs source] claims list, and the standard handoff summary.
- Writes: the durable message house to memory/narrative/message-system-architect/; the canon-grade block (main narrative, pillars + claim IDs, tagline) to memory/events/narrative.ndjson via an authorized operation: propose request to registry-events.py only — narrative-registry is the sole writer of memory/narrative-registry/canon.md; every unsubstantiated claim to memory/events/claims.ndjson via an authorized operation: propose request to registry-events.py tagged [needs source], never memory/claims/claims-ledger.md directly.

## When to use

- Use as lead for message architecture when the studio has an approved brief for this deliverable.
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
Use Message System Architect for message architecture at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a durable brand message house — main narrative, three value pillars, per-persona proof points, and tagline/one-liner — with an internal-consistency pass, an immutable canon-grade candidate binding (canon_id, version, hash, current head, supersedes), a [needs source] claims list, and the standard handoff summary.
- the house names a main narrative, three traceable value pillars, a tagline/one-liner, and evidence-labeled proof points; the internal-consistency pass finds no contradiction; the canon candidate has an exact ID/version/hash/current-head/supersedes binding without a fork; and every [needs source] claim and canon candidate is queued through its authorized proposal path.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.

## Pairs with

- `skill:message-house-builder` — same job; use when its own role or trigger applies.
- `skill:narrative-baseline-mapper` — same job; use when its own role or trigger applies.
- `skill:narrative-resonance-monitor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
