---
title: Tool card standard
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
---

# Tool card standard

A tool card tells a designer or AI agent, in under two minutes, when, where and how to use one tool at 3RDWRONG — and when to choose something else. Cards document use; they do not approve a tool or prove its quality, connectivity or licence.

Only tools whose [registry](../toolkit/sources/registry.json) role is `lead` or `specialist` get a card. Bench and parked tools appear in the generated handbook with their registry reason. Follow [D-0019](../studio/decisions/0019-organisation-and-loading-policy.md): start with the job lead, call specialists only on their triggers, and keep bench/parked tools for explicit requests after review.

## Sources and scope

Read the tool's own `SKILL.md`, agent file or plugin README before writing: the full file for a lead, at least the first 120 lines for a specialist. Consult [materials.json](../toolkit/sources/materials.json) for distribution, package and source location; use the department charter for studio context. A local path is not a portable installation instruction. FETCH and MANUAL tools may require installation, an account or rights review.

Every stated capability must come from the source. Write “Not documented” where the source is silent. Never invent commands, flags, results or provider support. Keep the [evidence labels and status rules](knowledge-governance.md): **Documented**, **Interpretation**, **Hypothesis**, **Unknown**. Agents may write proposed cards; only a named human can approve them.

## Location and metadata

Write `toolkit/cards/<department>/<sub_department>/<slug>.md`. Form the slug from the card's `tool_id`: lowercase it, replace each `:` with `--`, then replace every character outside `[a-z0-9-]` with `-`. For example, `skill:3w-identity-system-critic` becomes `skill--3w-identity-system-critic.md`.

The registry owns `department`, `sub_department`, `job` and `role`; copy these exactly. Canonical IDs are preferred; aliases resolve to the same tool for validation and coverage, and still use the card's written ID for the slug. There must be only one card per canonical tool.

All fields below are required. `trigger` is an empty string for a lead and a concrete description of the registry trigger's intent for a specialist. `pairs_with` is a list of registry IDs or aliases; an empty list is allowed. `kind` follows the source tool's kind. `availability` is `claude`, `codex`, `both`, `mcp`, `repo` or `claude-managed`. `distribution` is `vendor`, `fetch`, `manual` or `repo`.

```yaml
title: Human name of the tool
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-identity-system-critic
department: design
sub_department: design-qa
job: concept-critique
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-identity-system-critic/SKILL.md
invoke: "3w-identity-system-critic skill"
pairs_with: [skill:3w-creative-direction, skill:3w-brand-consistency-qa]
```

Enclose metadata in YAML `---` delimiters at the top of the file, then leave a blank line before the single H1. Use British English, plain language and no hype or emoji. Keep the entire card, including frontmatter, at or below 90 lines; exceeding the limit produces a warning.

## Body structure

Use exactly one H1 with the human tool name. Follow it with a one-sentence introduction saying what the tool does for the studio and whether it leads a job or supports a specific trigger. The handbook and routing index use the first sentence of this introductory paragraph as the summary.

Include these H2 sections once each, in this order:

1. **What it does** — three to six source-supported capabilities.
2. **When to use** — concrete studio moments tied to the job; specialists retain the registry trigger's intent.
3. **When not to use** — boundaries and the better tool's ID where one exists.
4. **Inputs it needs** — artefacts, evidence, constraints and decisions needed before starting.
5. **How to run it** — numbered steps, the exact skill or `/command`, agent name for the Agent tool, or MCP server; include a copy-paste prompt in a fenced `text` block. State host or installation limitations when applicable.
6. **What good output looks like** — observable passing results, without invented claims.
7. **Quality checks** — reviewer checkboxes against the actual output.
8. **Pairs with** — upstream/downstream tool IDs and the handoff between them.
9. **Limits and cautions** — documented limits, distribution/licence requirements and relevant studio guardrails.

Keep maker ≠ checker, source/evidence labels, [D-0006's rejected own-identity direction](../studio/decisions/0006-rejected-own-identity-direction.md), purposeful motion, accessibility/reduced motion and [D-0021's publication boundary](../studio/decisions/0021-client-work-public-anonymised.md) visible where relevant. Client identities, files, credentials and money stay outside the public repo. A card never substitutes for a founder decision.

## Add or update a card

1. Find the canonical registry tool and confirm its role is lead or specialist. Confirm department, sub-department and job against the charter.
2. Read the source and check distribution/installation requirements. Record missing or contradictory evidence; do not silently change routing to fit the card.
3. Create or revise the correctly named file, metadata and ordered sections. Update `last_reviewed` when the source and card have actually been reviewed. Include only documented invocation instructions and a usable example prompt.
4. Ask a separate person or agent instance to check the card against the source and registry. Maker ≠ checker applies to both the card and the output it describes. Record unresolved contradictions in the review; only a human grants approval.
5. Rebuild the handbook, then the knowledge index, and run the checks below. Review the generated diff with the source card.

```bash
uv run python scripts/build_handbook.py
uv run python scripts/build_index.py
uv run python scripts/validate.py
uv run python -m unittest discover -s tests -q
npx --yes markdownlint-cli2 "**/*.md" "#.venv" "#node_modules"
```

## Validation and rollout

The `cards` check validates all card metadata, registry IDs and aliases, routing matches, slug/path, the single H1, ordered H2 sections, paired tool IDs and eligible roles. Routing mismatches show the registry value. Code-fenced example headings do not count as document headings. Missing fields, unknown IDs, duplicate cards and bench/parked cards are errors; cards above 90 lines warn.

Missing lead/specialist cards produce one warning per department during rollout. Use `uv run python scripts/validate.py --strict-cards` to require coverage everywhere, or set `cards.strict_departments` in [schemas/metadata.json](../schemas/metadata.json) to department slugs such as `design` and `engineering`. An empty list keeps every department in warning mode. `--check cards` runs only card validation; combine it with `--strict-cards` for a focused coverage gate.

The `handbook` check compares generated files with their sources and fails for missing, stale or obsolete outputs. Run `uv run python scripts/build_handbook.py --check` for the same generation check without writing. Fix card errors before generating. Neither check can prove that a capability, trigger interpretation or invocation matches its upstream documentation: independent source review remains required.

## Generated views

- [handbook/README.md](../handbook/README.md) explains use and shows per-department card coverage.
- `handbook/<department>.md` groups leads and specialists by sub-department and job, followed by a bench/parked table. Missing cards are marked “card pending”.
- [toolkit/cards/index.json](../toolkit/cards/index.json) lists every lead/specialist with canonical ID, routing, trigger, invocation, availability, distribution, card path and summary. Paths are relative to the repository root. Pending cards have a null path; invocation and availability remain null until documented by a card. Distribution falls back to materials.json. A pending summary says “Card pending.”
- [toolkit/cards/README.md](../toolkit/cards/README.md) explains the source-card folder. The README and index are generated; edit cards, registry or materials instead.

Agents filter the routing index by department and job, open only the chosen card and follow “How to run it”. Humans can browse the handbook. Generated output is deterministic and retains proposed status; regeneration never implies fresh human approval.
