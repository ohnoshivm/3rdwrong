---
title: Stillsoil Atelier colour system test run
type: project
status: experimental
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---
# Colour system: Stillsoil Atelier / Pause with purpose

**Fictional example for testing methods and skills. Not a client.**

APCA is not shipped; it may be checked manually with the official tool, subject to its licence. WCAG 2.2 contrast is the pass/fail rule.

> Fictional skill test run. Colour values are invented for the test. The
> contrast and palette figures were recomputed on 2026-10-23 with
> `scripts/colour_check.py`, using WCAG 2.2 relative luminance,
> CIEDE2000 ΔE00, and Machado (2009) CVD
> matrices. For this recomputation the declared screening cutoff was ΔE00 < 5;
> it is a project choice, not a standard. Nothing here is approved.

**Status:** draft (formative) — not approved
**Route and strategy:** [concept route A](concept-route-a.md), not chosen; strategy not signed ([fictional brief](brief.md)).

## What colour must do

Colour separates the four products at shelf and thumbnail distance, and keeps the routine's surfaces quiet so the name reads first. Colour must not carry the variant alone (R1 wants the fragrance-free variant obvious before purchase; R2 needs name and variant to scan on a shelf card). The fragrance-free bar must not read as a medical product (F1).

## Roles and values

| Role | Token (semantic → primitive) | OKLCH | sRGB hex | Share of use | Rationale |
| --- | --- | --- | --- | --- | --- |
| Neutral surface | `surface-paper` → `oat-50` | 95.3% 0.013 87 | `#F3EFE6` | Most of every surface | Quiet field for the name |
| Text primary | `text-primary` → `soil-900` | 28.7% 0.012 78 | `#2E2A24` | All names and body text | Brand ink |
| Text secondary | `text-secondary` → `soil-600` | 50.4% 0.020 76 | `#6B6358` | Descriptors on paper only | — |
| Variant: clay bar | `variant-clay` → `clay-600` | 53.9% 0.112 39 | `#A4553A` | One band per label | — |
| Variant: moss bar | `variant-moss` → `moss-800` (revised) | 39.0% 0.058 123 | `#3F4A26` | One band per label | Darkened from `#5E6B3A` after the colour-vision check |
| Variant: fragrance-free bar | `variant-unscented` → `oat-300` | 82.9% 0.027 85 | `#CFC6B4` | One band per label | Near-neutral; avoids an invented "clinical" code |
| Variant: body oil | `variant-amber` → `amber-700` (revised) | 50.9% 0.101 70 | `#8A5A16` | One band per label | Darkened from `#B07A2A` for text contrast |
| Text on oat band | `text-on-unscented` → `soil-700` | 40.6% 0.017 74 | `#4F483F` | Descriptors on the oat band | Replaces `soil-600`, which failed |

## Category colour codes

| Code | Count / N | Kept or avoided | Reason | Label |
| --- | --- | --- | --- | --- |
| Any category colour pattern | — | — | No category audit exists | Unknown |
| "Clinical" colours for fragrance-free products | — | Avoided by decision | F1 asked to avoid a medical look; which colours read as clinical is not sourced | Hypothesis — needs an audit and a comprehension test |

## Cultural notes

| Association | Source and scope | Label | Check needed |
| --- | --- | --- | --- |
| None recorded | No cultural research supplied for the fictional Bengaluru audience | Unknown | Sourced research and a reviewer from the audience context before any meaning is used |

## Contrast pairings

| Foreground / background | Use | WCAG 2.2 ratio | Threshold | Pass |
| --- | --- | --- | --- | --- |
| `#2E2A24` / `#F3EFE6` | Names, body | 12.43:1 | 4.5:1 | Yes |
| `#6B6358` / `#F3EFE6` | Descriptors | 5.15:1 | 4.5:1 | Yes |
| `#F3EFE6` / `#A4553A` | Variant name on clay band | 4.65:1 | 4.5:1 | Yes, narrowly |
| `#F3EFE6` / `#5E6B3A` | Variant name on first moss | 5.03:1 | 4.5:1 | Yes |
| `#F3EFE6` / `#3F4A26` | Variant name on revised moss | 8.25:1 | 4.5:1 | Yes |
| `#F3EFE6` / `#B07A2A` | Variant name on first amber | 3.23:1 | 4.5:1 (3:1 large) | No — large text only |
| `#F3EFE6` / `#8A5A16` | Variant name on revised amber | 5.15:1 | 4.5:1 | Yes |
| `#2E2A24` / `#CFC6B4` | Variant name on oat band | 8.41:1 | 4.5:1 | Yes |
| `#6B6358` / `#CFC6B4` | Descriptor on oat band | 3.49:1 | 4.5:1 | No |
| `#4F483F` / `#CFC6B4` | Revised descriptor on oat band | 5.31:1 | 4.5:1 | Yes |

Ratios on printed labels are a proxy only; WCAG applies to digital content.

## Colour-vision checks

Screening metric: CIEDE2000 ΔE00; declared cutoff **below 5.0** before running `uv run python scripts/colour_check.py palette ... --min-delta-e 5`. This project cutoff is not a standard. The earlier OKLab × 100 values are replaced; they are not directly comparable to ΔE00.

| Where colour distinguishes | Protan | Deutan | Tritan | Greyscale | Non-colour cue |
| --- | ---: | ---: | ---: | ---: | --- |
| Clay vs first moss (`#A4553A` / `#5E6B3A`) | 2.72 | 5.85 | 30.95 | 1.90 | Below cutoff in protan and greyscale; moss darkened in revised palette |
| Clay vs revised moss (`#A4553A` / `#3F4A26`) | 9.19 | 17.04 | 33.34 | 13.17 | Variant name and number |
| Clay vs revised amber (`#A4553A` / `#8A5A16`) | 7.79 | 5.45 | 6.13 | 2.65 | Below cutoff in greyscale; variant name and number; oil also has a distinct pack format |
| Revised moss vs revised amber (`#3F4A26` / `#8A5A16`) | 11.96 | 16.08 | 30.45 | 10.55 | Variant name and number |
| Oat vs any variant (minimum across tested pairings) | ≥ 35.10 | ≥ 29.37 | ≥ 35.68 | ≥ 29.67 | Variant name and number |

The recomputation confirms the contrast figures to their displayed precision. The first amber is 3.23:1, passing AA large text only; the revised amber is 5.15:1. Under the declared CIEDE2000 cutoff, revised clay and amber no longer flag in protan or deutan, but still flag in greyscale at 2.65. The initial clay and moss pair flags under protan (2.72) and greyscale (1.90). Values differ from the earlier OKLab × 100 screen because the metric changed; a screening tool is not a user test.

Result: four variants still cannot rely on colour alone. Variant names and a printed number carry identification; colour supports it (**Documented** for these fictional values; real users are **Unknown**).

## Light and dark behaviour

- `surface-paper` and `text-primary` invert for a dark shop theme only if one is in scope; the brief does not ask for it — Unknown, not designed.
- Variant bands keep their values on light surfaces; on product photography they sit on a paper panel, never directly on the image.

## Print

| Role | Process and profile | CMYK | Spot | Substrate | Proof status |
| --- | --- | --- | --- | --- | --- |
| All roles | Unknown — no printer named | Not converted; CMYK depends on the printer's profile | Not specified | Uncoated tactile stock is likely (R4, Hypothesis) | Not proofed — print unverified |

Uncoated stock usually prints darker and less saturated than screen; the revised values need a hard proof on the real stock before sign-off. A calibrated screen preview does not stand in for that proof.

## Application tests

| Application | Result | Defect | Rule change |
| --- | --- | --- | --- |
| Label (text specification) | Variant band plus name and number specified | Label size unknown | — |
| Shelf card | Four variants side by side screened | Clay and revised amber remain below the declared greyscale cutoff (ΔE00 2.65) | Number and name required on every variant use |
| Mobile shop thumbnail | Not built | Unknown | — |

## Deliverables

- Colour specification (this file) — draft.
- Token file — not produced; names above are ready for CSS custom properties.
- Print sheet — blocked on printer and proof.

## Human decisions needed

- Founder: approve or replace the variant colours, and accept that colour supports, not carries, variant identity.
- Founder: decide whether the fragrance-free variant should be near-neutral (current) or have its own hue.
- Client: name the printer and substrate for proofing.
