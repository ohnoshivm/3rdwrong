---
name: 3w-colour-system
description: Build a perception-aware brand colour system — roles, distinctiveness against category colour codes, sourced cultural notes, WCAG 2.2 contrast with APCA as reference, colour-vision-deficiency checks, light and dark contexts, print conversion and proofing, design tokens and application tests. Use in identity and system phases after a route is chosen; a human sets the colour direction.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.2
---
# 3w-colour-system

## Purpose

Turn a chosen route's colour intent into a tested, documented system: named roles with values, accessible pairings, behaviour in light and dark, print equivalents with proof requirements, and tokens a builder can use without guessing. The skill makes colour decisions inspectable; it does not choose the palette for the founder or claim what a colour makes people feel.

## When to use

Use in [phase 05 Identity](../../methods/identity-engagement/05-identity.md) once a concept route is chosen, in [phase 06 System](../../methods/identity-engagement/06-system.md) to test colour across applications, and in [phase 07 Validation](../../methods/identity-engagement/07-validation.md) to recheck contrast, colour-vision and print proofs on final files.

## When not to use

Do not use to pick colours before an idea exists, to assert colour psychology ("blue builds trust"), or to certify accessibility conformance from a ratio table. Do not use for a single interface's elevation and accent distribution after the system is set; `vectorlab-ux-skills:colour-palette` handles that as a specialist.

## Inputs

- The chosen route, its idea statement and strategy status (approved, or draft marked formative).
- The founder's or design lead's colour direction: intended roles and candidate values, even if rough.
- The [category code audit](../3w-category-code-audit/SKILL.md) colour column, or a note that none exists.
- Audience geography and any sourced cultural research; otherwise a note that none exists.
- The agreed application set (screen, label, line sheet, social, signage) and known print processes, substrates and vendors.
- Any existing brand colours that must be kept.

## Dependencies

Read [phase 05 Identity](../../methods/identity-engagement/05-identity.md), [phase 06 System](../../methods/identity-engagement/06-system.md), [identity system testing](../../methods/quality/identity-system-testing.md), the [perception-to-identity map](../../methods/perception-to-identity-map.md), [web standards](../../methods/quality/web-standards.md) and the colour section of the [identity system specification](../../templates/identity-systems/identity-system-spec.md). Use the reviewed, standard-library tool `scripts/colour_check.py`: `uv run python scripts/colour_check.py contrast <fg> <bg>` computes WCAG 2.x contrast and signed APCA Lc (reference only); `uv run python scripts/colour_check.py palette <hex> <hex> ... --min-delta-e N [--text-pairs fg:bg,...] [--format md|json]` reports CIEDE2000 ΔE00 matrices under normal vision, Machado protanopia, deuteranopia and tritanopia simulations, and luminance greyscale. Choose and state the CIEDE2000 cutoff before each palette run; `--min-delta-e` has no default. `--cvd-severity` accepts 0–1 and defaults to full severity. Print proofing still needs the named vendor.

APCA Lc is licensed by the [APCA-W3 repository terms](https://github.com/Myndex/apca-w3/blob/master/LICENSE.md) for web-content contrast assessment; commercial use outside the W3 cooperative web-content agreement requires a written license. Do not use APCA results to evaluate print. WCAG remains the baseline for web accessibility checks.

## Procedure

1. **State what colour must do for the idea**, without adjectives: carry recognition, separate variants, mark a state, recede behind product. Name what colour must not carry alone (for example the only cue for a product variant).
2. **Assign roles before values.** Primary (recognition), secondary (support), neutrals (surfaces and text, warm, cool or true by decision), accent (rare signal), semantic (success, warning, error, information — only where applications need them) and any product or variant colours. Give each role a share of use, not just a swatch.
3. **Check distinctiveness against category colour codes.** From the audit, tally the category's dominant hues and value ranges with denominator. Mark which code the system keeps as an entry cue and which it avoids, with reasons. Without an audit, distinctiveness is **Unknown**.
4. **Record cultural associations only with evidence.** For each association, cite a source and its scope (community, region, period, context) and label it; otherwise mark it **Hypothesis** with the research or participant test needed. Make no universal colour-psychology claim. For India-specific meanings, use sourced, context-bound notes only — meanings differ by region, community, religion and occasion — and have a reviewer from the audience context check them.
5. **Define values in a perceptual model.** Set master values in OKLCH (or another stated perceptual space) and derive tonal steps there so lightness steps are even; record sRGB hex for the web and note any Display P3 value with its sRGB fallback.
6. **Test contrast with WCAG 2.2 as the baseline.** For every text and interface pairing in use, record the WCAG 2.x ratio against 4.5:1 for normal text, 3:1 for large text (at least 18 pt, or at least 14 pt bold) and 3:1 for non-text interface components and meaningful graphics. Calculate text pairings with `uv run python scripts/colour_check.py contrast <fg> <bg>` or `--text-pairs fg:bg,...` in a palette report. The tool uses the WCAG 2.2 sRGB transfer breakpoint (0.04045) and reports AA/AAA outcomes for normal and large text. On printed applications the ratio is a proxy for legibility, not a conformance result. Record the signed APCA Lc value as a reference only; never replace a WCAG result with it or present APCA as a conformance standard.
7. **Simulate colour-vision deficiencies.** Before running, declare the metric as CIEDE2000 ΔE00 and choose a project cutoff; state both in the record before running `uv run python scripts/colour_check.py palette ... --min-delta-e N`. The cutoff is a project choice, not a standard. The tool checks every pair under normal vision, full-severity protanopia, deuteranopia and tritanopia (Machado et al. matrices applied in linear RGB), plus a greyscale view made from relative luminance. `--cvd-severity 0–1` selects an anomalous-trichromacy severity; 1.0 is dichromacy. Check every set colour distinguishes (variants, charts, states) in greyscale first: when a set has more than three members, or each member must also hold readable text, expect lightness alone not to separate every pair and plan the non-colour cue from the start. Then check the simulated views on the real applications. Where pairs fall below the declared cutoff, add a non-colour cue (label, shape, position, pattern) rather than only shifting hue. A simulator is a screening aid, not a user test.
8. **Specify light and dark contexts.** Define how each role behaves on light and dark surfaces and on photography: which roles invert, which stay, adjusted values for dark backgrounds (saturated colours glare on dark; desaturate or lighten by decision), and re-run steps 6–7 for each context.
9. **Convert for print and plan proofs.** For each process, give CMYK built for the ICC profile the printer names (not a generic default) and spot references where specified, noting coated and uncoated differences. Require a hard proof or press check on the real substrate and lighting before sign-off; record that a screen preview, even on a calibrated display, does not predict the printed result, and an uncalibrated display cannot be used for colour approval.
10. **Write tokens and names.** Two layers: primitives named by hue family and step (for example `clay-600`) and semantic roles that point to them (`text-primary`, `surface-raised`, `variant-fragrance-free`). Name by role, not by appearance in semantic tokens. Provide a machine-readable file (CSS custom properties and/or a W3C Design Tokens Community Group format JSON) and a human table.
11. **Test across the agreed applications** using the [identity system testing](../../methods/quality/identity-system-testing.md) matrix: small logo, label at actual size, line sheet, mobile page, social crop, plus any physical medium. Fix the rule, not each mock-up, when several fail together.
12. **Package deliverables** (see Output) and hand the system to an independent reviewer.

## Evidence requirements

A contrast ratio, APCA value or simulation is **Documented** only when actually computed or run on named files; name `scripts/colour_check.py` and record the declared CIEDE2000 cutoff for palette checks. Print colour is Documented only from a proof on the named substrate. Category colour patterns need the linked audit; without it they are **Unknown**. Cultural meanings need a cited source and scope or stay **Hypothesis**. Emotional or behavioural effects of colour are never Documented from studio work. Fictional runs stay inside the fiction.

## Output

Return this exact Markdown structure.

```markdown
# Colour system: {{project and route}}

**Status:** {{draft | tested | validation record}} — not approved
**Route and strategy:** {{route link; strategy status}}

## What colour must do
{{sentences without adjectives; what colour must not carry alone}}

## Roles and values
| Role | Token (semantic → primitive) | OKLCH | sRGB hex | Share of use | Rationale |
| --- | --- | --- | --- | --- | --- |

## Category colour codes
| Code | Count / N | Kept or avoided | Reason | Label |
| --- | --- | --- | --- | --- |

## Cultural notes
| Association | Source and scope | Label | Check needed |
| --- | --- | --- | --- |

## Contrast pairings
| Foreground / background | Use | WCAG 2.x ratio | Threshold | Pass | APCA Lc (reference) |
| --- | --- | --- | --- | --- | --- |

## Colour-vision checks
Screening metric and threshold: {{metric, cut-off, tool}}

| Where colour distinguishes | Protan | Deutan | Tritan | Greyscale | Non-colour cue |
| --- | --- | --- | --- | --- | --- |

## Light and dark behaviour
- {{role}} — {{light value / dark value / on image}}

## Print
| Role | Process and profile | CMYK | Spot | Substrate | Proof status |
| --- | --- | --- | --- | --- | --- |

## Application tests
| Application | Result | Defect | Rule change |
| --- | --- | --- | --- |

## Deliverables
- {{file — format — status}}

## Human decisions needed
- {{decision, owner}}
```

Deliverables when final: the colour specification page; token files (CSS custom properties and DTCG-format JSON); a contrast and colour-vision table; print sheet with CMYK per named profile, spot references and proof records; light and dark examples; swatch files in the designer's tools (for example ASE) if agreed.

## Quality checks

- Roles are defined before values and each has a share of use.
- No role relies on colour alone to carry a required distinction.
- Category colour codes cite the audit with denominator, or are Unknown.
- Every cultural association has a source and scope, or is a Hypothesis; no universal colour-psychology claim appears.
- Every text and interface pairing in use has a computed WCAG 2.x ratio with `scripts/colour_check.py`; APCA is labelled reference.
- Every palette screen names CIEDE2000 ΔE00 and states the user-chosen cutoff before the command runs.
- Colour-vision simulation covered every colour-coded distinction; collapses have a non-colour cue.
- Light and dark contexts were each tested, not assumed.
- CMYK values name the profile; proof status is recorded; the calibration caveat is stated.
- Semantic tokens are named by role; primitives by family and step.
- The reviewer is not the maker.

## Failure conditions

Stop and ask when no route or colour direction exists, when the application set is undefined, or when asked to state what a colour means to an audience without sources. A formative run on an unchosen route is allowed only when the user accepts it; label every output formative. Do not sign off print colour without a proof; return the specification as "print unverified". Do not report accessibility conformance from contrast ratios alone.

## Human review

The founder or design lead chooses the palette and approves value changes. An independent reviewer checks the tables against files; an accessibility specialist confirms conformance claims; a reviewer from the audience context checks cultural notes; the printer confirms proofs. The client gives visual sign-off in phase 06. This skill records no approval.

## Example

**Fictional example.** For a fictional tea brand, "Kettlereed", the variant colours green and amber collapse under deuteranopia simulation (**Documented** in the fictional test file), so each variant gains a printed leaf count. Body text `#2B2A27` on paper `#F4F1EA` computes at about 12.7:1 (**Documented** by `scripts/colour_check.py`). "Amber signals warmth to this audience" is recorded as a **Hypothesis**; no source was supplied.
