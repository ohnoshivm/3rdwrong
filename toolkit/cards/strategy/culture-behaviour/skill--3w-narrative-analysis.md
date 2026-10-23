---
title: Narrative analysis
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-narrative-analysis
department: strategy
sub_department: culture-behaviour
job: narrative-analysis
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-narrative-analysis/SKILL.md
invoke: "3w-narrative-analysis skill"
pairs_with: [skill:3w-brand-discovery, agency:academic-historian, skill:category-narrative-mapper]
---
# Narrative analysis

The studio's lead tool for narrative analysis: sourced brand, founder, customer and cultural stories, tested before the identity carries them. Registered job lead; the skill remains experimental.

## What it does

- Inventories stories with teller, source and date.
- Structures each story (tension, turn, value) and labels each element's truth.
- Compares founder, customer and press versions.
- Tests candidate anchor narratives for truth, ownership, audience fit, carriability and durability.

## When to use

- Identity 01 Discovery to 03 Strategy when source material contains origin, heritage, place or customer stories.
- Before positioning and concept work.

## When not to use

- Competitor messaging maps — use `skill:category-narrative-mapper`.
- Writing copy — verbal identity.
- Fiction — `agency:academic-narratologist`.

## Inputs it needs

- Source material with provenance.
- Discovery synthesis if available.
- Markets, languages and cultures in scope.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-narrative-analysis skill for {{codename}}. Sources: {{list with dates}}. Discovery synthesis: {{link}}. Markets: {{…}}. Return the story inventory, differences between tellers, cultural notes, candidate anchors and a recommendation with unknowns.
```

## What good output looks like

- Element-level truth labels.
- Heritage and first/only claims verified or Unknown.
- A recommendation that states what would change it.

## Quality checks

- [ ] Every story has a source and teller.
- [ ] No invented customer stories.
- [ ] Cultural doubts routed to specialists.

## Pairs with

- Upstream: `skill:3w-brand-discovery`.
- Verification: `agency:academic-historian`, `agency:specialized-cultural-intelligence-strategist`.
- Neighbour: `skill:category-narrative-mapper` for competitor narratives.

## Limits and cautions

- Experimental skill; the client confirms facts about their own history.
- Client material stays codenamed (D-0021).
