---
title: Colour system skill evaluation — Stillsoil Atelier
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---
# Colour system skill evaluation — Stillsoil Atelier

**Fictional example for testing methods and skills. Not a client.**

APCA is not shipped; it may be checked manually with the official tool, subject to its licence. WCAG 2.2 contrast is the pass/fail rule.

## Skill and version

`3w-colour-system` 0.1.0 was run; findings below produced version 0.1.1 of [the skill](../../../skills/3w-colour-system/SKILL.md). The original run was not repeated on 0.1.1; its calculations were recomputed with the reviewed tool on 2026-10-23 after the skill advanced to 0.1.2.

## Test request and inputs

**Request:** "Use 3w-colour-system on route A for Stillsoil Atelier as a formative run. Propose roles and fictional values, compute contrast and colour-vision screening, and state print and cultural limits; do not approve anything."

Inputs: [fictional brief](brief.md), [discovery synthesis](discovery-synthesis.md), [concept route A](concept-route-a.md) and the [formative critique](identity-system-critique.md), plus the [mark test run](mark-exploration-test-run.md). Route A is not chosen and strategy is not signed, so the run was accepted as formative. No category audit, artwork, dimensions, printer or licences exist in the fiction.

Output: [colour system test run](colour-system-test-run.md).

## Procedure followed

All twelve steps were followed. The original calculations were later recomputed on 2026-10-23 with `scripts/colour_check.py` using published WCAG 2.2, Sharma CIEDE2000 and Machado reference values. The palette run declared CIEDE2000 ΔE00 < 5 as its project cutoff before execution. Print conversion and proofing remain unverified (no printer); application tests were text checks only.

## Output review

- Roles came before values and each has a share of use.
- The reviewed tool recomputed the first amber at 3.23:1 for light text and the original descriptor on oat at 3.49:1; both fail normal AA and were revised. The ratios match the earlier report to two decimals.
- With the newly declared CIEDE2000 ΔE00 cutoff of 5, the first clay/moss pair flags under protan (2.72) and greyscale (1.90). Revised clay/amber flags only in greyscale (2.65); the previous OKLab × 100 values are not comparable to ΔE00.
- Cultural notes stayed Unknown; the "clinical colours" idea stayed a Hypothesis.

## What worked

- `scripts/colour_check.py` replaces the ad-hoc calculator and is tested against published WCAG 2.2, CIEDE2000 and Machado reference values.
- Computing instead of eyeballing produced Documented findings and showed that the revised clay/amber pair remains below the declared cutoff in greyscale.
- The rule "colour must not carry the variant alone" from step 1 connects directly to the fictional customer need (R1) and to composition rule I3.
- Print stayed honestly unverified.

## Original gaps and observed failure

- **No declared screening threshold in 0.1.0.** The skill asked for simulation but not for a stated metric and cut-off. Version 0.1.1 fixed this; the tool recomputation uses declared CIEDE2000 ΔE00 < 5.
- **Set check too late.** The variant set's lightness problem appeared only after values were chosen; a greyscale-first check of the set would have saved a revision.
- **Large-text threshold undefined.** The first amber passed only the large-text threshold, but the skill did not define large text.
- **Print proxy.** The skill did not say that WCAG ratios on printed labels are a proxy only.
- **Formative use blocked** as in the other craft skills.

## Skill changes made

- Step 6: large text defined (24 px, or 18.66 px bold); calculator named; print ratios labelled a proxy.
- Step 7: declare metric and threshold before running; check sets in greyscale first; plan a non-colour cue from the start when a set has more than three members or must hold text.
- Output: a screening metric line above the colour-vision table.
- Failure conditions: formative runs allowed when accepted and labelled.
- Example: corrected the contrast figure to the computed 12.7:1.

## Tool recomputation and remaining limits

On 2026-10-23 the fictional palette was recomputed with `scripts/colour_check.py`. WCAG ratios remain the same to two decimal places, including the 3.23:1 first amber and the 3.49:1 original descriptor-on-oat pair. The CIEDE2000 cutoff was declared as ΔE00 < 5; this differs from the original OKLab × 100 metric, so the earlier colour-vision figures and revised flags were replaced in the test run.

- The tool is tested against the published vectors cited in `tests/test_colour_check.py`; palette simulation is still a screening aid and has not been validated with real users with CVD.
- No print proof, dark theme or real audience exists in the fiction.
- Next evaluation: a brief with a dark digital context and a named printer.
