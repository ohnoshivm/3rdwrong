---
title: Colour system
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-colour-system
department: design
sub_department: identity-craft
job: colour
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-colour-system/SKILL.md
invoke: "3w-colour-system skill"
pairs_with: [skill:3w-category-code-audit, skill:3w-typography-system, skill:3w-composition-system, skill:3w-brand-consistency-qa, vectorlab-ux-skills:colour-palette]
---
# Colour system

The studio's lead tool for brand colour: roles, accessible pairings, colour-vision screening, light and dark behaviour, print proofs and tokens, tested across applications.

## What it does

- Assigns roles (primary, secondary, neutral, accent, semantic, variant) before values, with a share of use.
- Checks distinctiveness against category colour codes and records cultural associations only with sources.
- Computes WCAG 2.2 contrast as the pass/fail rule.
- Screens colour-vision deficiencies with a declared metric and threshold; requires non-colour cues where colour collapses.
- Specifies CMYK per the printer's profile and spot references, with proofs on the real substrate; writes primitive and semantic tokens.

## When to use

- Phase 05 Identity, after a route is chosen.
- Phase 06 System, to test colour across the agreed applications.
- Phase 07 Validation, to recheck contrast, colour-vision and print proofs on final files.

## When not to use

- To choose colours before an idea exists, or to claim colour psychology.
- To certify accessibility conformance from ratios alone.
- For accent and elevation distribution inside one interface — use `vectorlab-ux-skills:colour-palette`.

## Inputs it needs

- Chosen route and the founder's colour direction.
- Category audit colour column, sourced cultural research if any.
- Application set, print processes, substrates and printer.

## How to run it

1. Collect the inputs above in one folder or message; state whether the route is chosen or the run is formative.
2. Before a palette check, declare the CIEDE2000 ΔE00 cutoff. Run `uv run python scripts/colour_check.py contrast <fg> <bg>` for a text pair, or `uv run python scripts/colour_check.py palette <hex> <hex> ... --min-delta-e N [--text-pairs fg:bg,...] [--format md|json]` for a palette. The tool requires `--min-delta-e`; WCAG 2.2 contrast determines pass/fail.
   APCA is not shipped; it may be checked manually with the official tool, subject to its licence. See the [official tool](https://apcacontrast.com/) and [licence](https://github.com/Myndex/apca-w3/blob/master/LICENSE.md).
3. Run the skill; a human designer makes every form decision it records.
4. Hand the output to someone other than the maker for review.
5. File the output in the project folder; nothing it produces is an approval.

```text
Use the 3w-colour-system skill for {{project}}. Route: {{link}}. Candidate roles and values: {{…}}. Category audit: {{link or none}}. Applications and printer: {{…}}. Declare a CIEDE2000 ΔE00 cutoff before running `uv run python scripts/colour_check.py palette <hex> <hex> ... --min-delta-e N`; use `uv run python scripts/colour_check.py contrast <fg> <bg>` or `--text-pairs fg:bg,...` for WCAG 2.2 ratios. Use WCAG 2.2 contrast for pass/fail; mark print unverified without a proof. Return the skill's exact output structure.
```

## What good output looks like

- A roles table with OKLCH and hex values and tokens named by role.
- Computed ratios for every pairing in use and a colour-vision table with a declared threshold.
- Non-colour cues wherever colour collapses; cultural notes sourced or Hypothesis; print proof status stated.

## Quality checks

- [ ] Every pairing has a computed ratio using `scripts/colour_check.py`; calculator named.
- [ ] Palette screening names CIEDE2000 ΔE00 and its declared cutoff.
- [ ] No required distinction relies on colour alone.
- [ ] No universal colour-meaning claim.
- [ ] CMYK names the profile; proof status and calibration caveat recorded.
- [ ] Reviewer is not the maker.

## Pairs with

- Upstream: `skill:3w-category-code-audit`.
- Alongside: `skill:3w-typography-system`, `skill:3w-composition-system`.
- Downstream: `vectorlab-ux-skills:colour-palette` for interface distribution; `skill:3w-brand-consistency-qa` once approved.

## Limits and cautions

- Experimental; the fictional run is recomputed with `scripts/colour_check.py`, but has no print proof.
- Simulators and ratios are screening aids, not user tests or conformance.
- India-specific meanings only with sources and a reviewer from the audience context.
