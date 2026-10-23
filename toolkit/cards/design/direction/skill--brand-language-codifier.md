---
title: Brand Language Codifier
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:brand-language-codifier
department: design
sub_department: direction
job: verbal-identity
role: specialist
trigger: "When defining verbal identity, voice, naming rules, or brand language."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/brand-language-codifier
invoke: "/brand-language-codifier skill"
pairs_with: [skill:3w-creative-direction, agent:creative-writer, skill:message-system-architect]
---

# Brand Language Codifier

A verbal-identity specialist that codifies a brand’s voice and naming rules from its own material. For 3RDWRONG, use this specialist when the registry trigger applies: “When defining verbal identity, voice, naming rules, or brand language.”

## What it does

- Produces two blocks: voice rules and naming rules for product, feature and tier names.
- Defines register, tone spectrum, banned phrases and few-shots drawn only from the brand’s own published material.
- Labels naming terms Measured, User-provided or Estimated and marks implied claims [needs source].
- Requires an upstream durable message house and stages proposals for the narrative registry.

## When to use

- When defining verbal identity, voice, naming rules, or brand language.
- Before channel copy scales, when the durable message house and the brand’s own published samples exist.

## When not to use

- Finished copy or platform-specific adaptation; use `agent:creative-writer` or the channel voice tool.
- When no durable message house exists; the skill directs to `message-system-architect` first.

## Inputs it needs

- Durable message house and any current narrative canon.
- Brand-owned published copy, existing names/tiers and the intended surfaces.

## How to run it

1. Invoke `/brand-language-codifier` in Claude Code or Codex.
2. Supply the message house and own published samples; request voice, naming and source-needed claims.
3. Review proposed canon with the authorised narrative registry and human owner.

```text
Use /brand-language-codifier skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Voice rules and naming tax are both present, with provenance labels and source gaps.
- Few-shots come only from the brand’s own material; no competitor copy or unsupported claims.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `agent:creative-writer` — downstream review or delivery.
- `skill:message-system-architect` — downstream review or delivery.

## Limits and cautions

- Apache-2.0; vendored skill.
- Stop if the durable message house is missing; do not guess a voice.
- Does not author channel adaptation, finished copy, message hierarchy or claim truth.
