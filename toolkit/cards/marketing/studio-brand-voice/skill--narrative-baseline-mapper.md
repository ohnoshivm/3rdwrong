---
title: Narrative Baseline Mapper
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:narrative-baseline-mapper
department: marketing
sub_department: studio-brand-voice
job: message-architecture
role: specialist
trigger: "Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/narrative-baseline-mapper/SKILL.md
invoke: "Claude Code: `/narrative-baseline-mapper`; Codex: `narrative-baseline-mapper` skill"
pairs_with: [skill:message-house-builder, skill:message-system-architect, skill:narrative-resonance-monitor]
---
# Narrative Baseline Mapper

Narrative Baseline Mapper is a 3RDWRONG specialist for message architecture, activated only when its registry trigger applies.

## What it does

- Inventories what every owned surface says today — the homepage headline, the pricing page value line, the docs intro, the pitch-deck one-liner, the social bios, the email footer — and reads each against the intended message to expose the gap. It is the first move of the TALE Trace phase and the "before" snapshot the rest of the narrative work is measured against. It feeds the TALE T (Truth) dimension — specifically the *positioning matches shippable reality* and *surface-truth* reads — and freezes the drift baseline that the Evaluate phase (narrative-drift-monitor) measures future surface drift against. It never scores and never authors: it records the current state so the gap is visible.
- Expected output: a narrative baseline document — a surface-by-surface inventory (surface · current headline/value line/claim · as-of date · label Measured / User-provided / Estimated), a per-surface gap read vs the intended message (aligned / drifted / contradictory / silent), a [needs source] list of any unverifiable claim found on a live surface, the frozen drift-baseline snapshot, and the standard handoff summary.
- Writes: the baseline map to memory/narrative/narrative-baseline-mapper/; any unverifiable claim seen on a surface marked [needs source] to memory/events/claims.ndjson via an authorized operation: propose request to registry-events.py (this skill never adjudicates it); no canonical memory/narrative-registry/canon.md write — only narrative-registry writes canon.

## When to use

- Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.
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
Use Narrative Baseline Mapper for message architecture at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a narrative baseline document — a surface-by-surface inventory (surface · current headline/value line/claim · as-of date · label Measured / User-provided / Estimated), a per-surface gap read vs the intended message (aligned / drifted / contradictory / silent), a [needs source] list of any unverifiable claim found on a live surface, the frozen drift-baseline snapshot, and the standard handoff summary.
- every named surface has a current-state line with an as-of date and a Measured / User-provided / Estimated label; each surface carries a gap read (aligned / drifted / contradictory / silent) vs the intended message or existing canon; and the drift-baseline snapshot is frozen with its source and as-of date.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.

## Pairs with

- `skill:message-house-builder` — same job; use when its own role or trigger applies.
- `skill:message-system-architect` — same job; use when its own role or trigger applies.
- `skill:narrative-resonance-monitor` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
