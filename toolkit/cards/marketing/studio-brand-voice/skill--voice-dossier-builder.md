---
title: Voice Dossier Builder
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:voice-dossier-builder
department: marketing
sub_department: studio-brand-voice
job: brand-voice
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/voice-dossier-builder/SKILL.md
invoke: "Claude Code: `/voice-dossier-builder`; Codex: `voice-dossier-builder` skill"
pairs_with: []
---
# Voice Dossier Builder

Voice Dossier Builder is 3RDWRONG’s lead for brand voice in studio brand voice.

## What it does

- Codifies how the brand AND the founder/exec actually sound — extracted from the user's own posts, emails, and decks, never invented and never borrowed from competitors — into the versioned voice record that channel-registry stores as voice-dossier.md and every Craft-phase skill (starting with social-creative-builder) reads first. It feeds two ECHO C sub-items directly — *voice-card adherence* (C6: per-platform register, banned phrases respected, few-shots from own posts only) and *pillar-allocation adherence* (C7) — and writes the per-context disclosure lines the ECHO C2 disclosure veto is later judged against (see echo-benchmark.md); social-quality-auditor does that judging, not this skill.
- Expected output: a versioned voice dossier — brand + founder per-platform register map, banned phrases, per-context disclosure lines, a few-shot bank citing own posts only, and 3-5 content pillars with Estimated %-allocations — plus the candidates submission and the standard handoff summary.
- Writes: the working dossier to memory/social/voice-dossier-builder/; the registry-grade voice record to memory/events/channels.ndjson via an authorized operation: propose request to registry-events.py for promotion (channel-registry is the sole writer of memory/channels/); disclosure or boilerplate wording that makes a product/offer claim to memory/events/claims.ndjson via an authorized operation: propose request to registry-events.py.

## When to use

- Use as lead for brand voice when the studio has an approved brief for this deliverable.
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
Use Voice Dossier Builder for brand voice at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a versioned voice dossier — brand + founder per-platform register map, banned phrases, per-context disclosure lines, a few-shot bank citing own posts only, and 3-5 content pillars with Estimated %-allocations — plus the candidates submission and the standard handoff summary.
- every register row and every few-shot cites an own post (ID/URL/date); disclosure lines cover founder/employee/advocate and AI-media contexts; pillars sum to 100% with every % labeled Estimated; and the versioned record sits in memory/events/channels.ndjson via an authorized operation: propose request to registry-events.py.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.

## Pairs with

- No same-job peer appears in this scoped registry slice.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
