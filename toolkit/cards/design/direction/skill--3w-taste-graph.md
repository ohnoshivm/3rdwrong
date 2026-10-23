---
title: Taste Graph reference pack
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-taste-graph
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: Before any creative-output task, load a Taste Graph reference pack for the brief (AGENTS.md; D-0020).
kind: repo-skill
availability: repo
distribution: vendor
source: skills/3w-taste-graph
invoke: "3w-taste-graph skill"
pairs_with: [skill:taste-skill, skill:3w-creative-direction, skill:audit-reference-originality]
---

# Taste Graph reference pack

The studio's prerequisite for creative output: retrieve curated principles,
exemplars and anti-patterns for the actual brief before making work. It remains
an experimental specialist; the inspiration-taste lead stays `skill:taste-skill`.

## What it does

- Retrieves a bounded reference pack from the local PostgreSQL Taste Graph.
- Records principles to apply and mistakes to avoid; references never license copying.
- Captures public references with provenance and analysis into the inbox when requested.

## When to use

- Before any creative-output task under D-0020 and AGENTS.md.
- When the founder supplies a public reference to save or explicitly requests a capture run.

## When not to use

- Non-creative backend, data or operational work.
- As evidence of audience response, originality, rights or effectiveness.
- For authenticated, paywalled or otherwise restricted captures.

## Inputs it needs

- The actual brief, output kind and project slug when applicable.
- A running local PostgreSQL database configured through `TASTE_GRAPH_DSN`.
- For capture, a public URL or rights-cleared file and an analysis of its transferable principles.

## How to run it

1. Read the [skill](../../../../skills/3w-taste-graph/SKILL.md) and
   [setup guide](../../../../taste/graph/README.md).
2. Run the pack command with the actual brief and read only its listed references.
3. State the principles to apply and anti-patterns to avoid before creative work.
4. If the database is unreachable, stop and report the missing pack; never invent one.

```text
uv run scripts/taste_graph.py pack "<actual brief>" --kind <kind> --project <slug>
```

## What good output looks like

- A pack tied to the actual brief and a short applying/avoiding statement.
- Captures identify provenance and transferable principles, and remain inbox entries until founder curation.

## Quality checks

- [ ] The command actually ran and the reference count is recorded.
- [ ] Taste judgements are Interpretation, not claimed performance evidence.
- [ ] No recognisable layout, asset, copy or identity is copied.
- [ ] An independent reviewer checks the resulting creative work.

## Pairs with

- `skill:taste-skill` — inspiration-taste lead; the pack is a prerequisite, not a replacement.
- `skill:3w-creative-direction` — applies principles to distinct concept routes.
- `skill:audit-reference-originality` — independently checks reference distance.

## Limits and cautions

- Database availability and a registry entry do not prove that a pack was loaded.
- Media and third-party text stay outside Git in the private data home.
- Only the founder curates references or approves creative work.
- The skill's Inputs and Failure conditions differ on unavailable-database handling;
  AGENTS.md requires stopping, so use that stricter rule.
