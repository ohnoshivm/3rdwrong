---
title: Narrative Resonance Monitor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:narrative-resonance-monitor
department: marketing
sub_department: studio-brand-voice
job: message-architecture
role: specialist
trigger: "Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/narrative-resonance-monitor/SKILL.md
invoke: "Claude Code: `/narrative-resonance-monitor`; Codex: `narrative-resonance-monitor` skill"
pairs_with: [skill:message-house-builder, skill:message-system-architect, skill:narrative-baseline-mapper]
---
# Narrative Resonance Monitor

Narrative Resonance Monitor is a 3RDWRONG specialist for message architecture, activated only when its registry trigger applies.

## What it does

- Measures whether the durable brand narrative is actually landing in the market — an echo rate (how much of the market's own language overlaps the narrative-registry canon lexicon, with the matching method declared), an AI-answer perception read (how answer engines describe the brand versus the canon, via scripts/connectors/tavily.py --answer, proxy-labeled), share-of-voice on a locked competitor panel, and public resonance signals from Bluesky / GDELT / Wikipedia-attention. It sits in the Evaluate phase of the TALE loop and is the resonance-evidence feed for the E dimension — specifically the upstream of the E1 evidence-integrity veto: the *proxy-not-Measured* discipline, echo-rate-with-declared-method, and AI-answer-perception sub-items (see tale-benchmark.md). It reads the canon lexicon but never edits it, and it never adjudicates a claim.
- Expected output: a resonance report — an echo rate with its matching method and corpus declared, an AI-answer perception read (proxy-labeled) comparing answer-engine descriptions against the canon, a share-of-voice figure on a named locked panel, and resonance signals from the keyless connectors — every number labeled Measured / proxy / User-provided with its as-of date, plus the standard handoff summary.
- Writes: the resonance report to memory/narrative/narrative-resonance-monitor/; any resonance/effectiveness statement it cannot back with Measured or User-provided evidence stays [needs source] and goes to memory/events/claims.ndjson via an authorized operation: propose request to registry-events.py — this skill never adjudicates it and never asserts a proxy number as Measured.

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
Use Narrative Resonance Monitor for message architecture at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a resonance report — an echo rate with its matching method and corpus declared, an AI-answer perception read (proxy-labeled) comparing answer-engine descriptions against the canon, a share-of-voice figure on a named locked panel, and resonance signals from the keyless connectors — every number labeled Measured / proxy / User-provided with its as-of date, plus the standard handoff summary.
- the report binds the exact canon and, when applicable, stimulus/result evidence-observation it measures; the echo rate states method and corpus; every proxy remains proxy and every own-export number carries an as-of date; the SOV figure names the locked panel; and any canon, panel, method, or stimulus switch restarts the trend rather than silently merging histories.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.

## Pairs with

- `skill:message-house-builder` — same job; use when its own role or trigger applies.
- `skill:message-system-architect` — same job; use when its own role or trigger applies.
- `skill:narrative-baseline-mapper` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- The studio’s visual identity is unapproved. Avoid the rejected black backgrounds, heavy grotesk and neon; use motion only when the concept needs it and respect reduced motion and accessibility.
