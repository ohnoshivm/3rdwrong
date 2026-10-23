---
title: AI Identifiers
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ai-identifiers
department: design
sub_department: direction
job: verbal-identity
role: specialist
trigger: "When the approved scope specifically requires defining the brand-level visual, verbal, and behavioral identity of an AI."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/ai-identifiers/SKILL.md
invoke: "/ai-identifiers skill"
pairs_with: [skill:brand-language-codifier, skill:3w-creative-direction, skill:3w-identity-system-critic]
---

# AI Identifiers

A specialist for the brand-level visual, verbal and behavioural identity of an AI feature or product. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires defining the brand-level visual, verbal, and behavioral identity of an AI.”

## What it does

- Defines five identifier types: name, avatar, colour, iconography and personality.
- Explains trade-offs such as names implying human competence, avatar realism and colour conventions.
- Covers disclosure, cross-surface consistency, accessible labels and state changes.
- Warns against deceptive realism and overloading familiar AI symbols.

## When to use

- When the approved scope specifically requires defining the brand-level visual, verbal, and behavioral identity of an AI.
- Phase 03 Strategy or Phase 04 Concept, when an AI product needs coherent identity decisions across surfaces.

## When not to use

- A general brand identity without an AI-specific identity question; use `skill:3w-creative-direction`.
- For claiming usability or audience preference without research.

## Inputs it needs

- AI product purpose, actual capability and interaction contexts.
- Existing brand positioning, surfaces, constraints and disclosure requirements.

## How to run it

1. Invoke `/ai-identifiers` in Codex.
2. Ask for decisions across name, avatar, colour, iconography and personality, with trade-offs and unknowns.
3. Have a human validate capability claims, cultural fit and disclosure.

```text
Use /ai-identifiers skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Each proposed identifier fits actual product capability and the wider brand.
- State, action and AI nature remain clear without relying on colour alone.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:brand-language-codifier` — upstream context or hand-off.
- `skill:3w-creative-direction` — downstream review or delivery.
- `skill:3w-identity-system-critic` — downstream review or delivery.

## Limits and cautions

- Skill is available in Codex; the installation does not prove all providers have it.
- The skill describes patterns, not validated audience preferences.
- Avoid defaulting to purple/green gradients or deceptive human likeness; 3RDWRONG’s rejected own-identity direction still applies.
