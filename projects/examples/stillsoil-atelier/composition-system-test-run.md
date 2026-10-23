---
title: Stillsoil Atelier composition system test run
type: project
status: experimental
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---
# Composition system: Stillsoil Atelier / Pause with purpose

**Fictional example for testing methods and skills. Not a client.**

> Fictional skill test run of `3w-composition-system` 0.1.0. Dimensions marked
> "stand-in" are invented for the test because the brief does not supply them.
> No layout was drawn; results are text specifications. Nothing here is
> approved.

**Status:** draft (formative) — not approved
**Route and strategy:** [concept route A](concept-route-a.md), not chosen; strategy not signed ([fictional brief](brief.md)). Inputs: [mark](mark-exploration-test-run.md), [typography](typography-system-test-run.md) and [colour](colour-system-test-run.md) test runs.

## Compositional idea without adjectives

Every application holds an empty field above the product name, the name is always read first, and the variant sits directly beneath it with its number; nothing else enters the field.

## Invariants

| Invariant | Measure | Smallest format it survives | Label |
| --- | --- | --- | --- |
| I1 Held field | An empty field of at least 2u above the name, where u = format width ÷ 12 | Stand-in 70 × 45 mm label (u ≈ 5.8 mm) | Hypothesis — not drawn |
| I2 Name first | The product name is the largest text and is never truncated; it wraps to a second line before its size drops | Stand-in 375 px mobile product card | Hypothesis |
| I3 Variant under name | Variant word and number directly under the name, within 1u; never conveyed by colour alone | Shelf card | Hypothesis |

## Variables and exceptions

| Variable or exception | Range or reason | Formats |
| --- | --- | --- |
| Variant band position | Top or bottom edge, chosen per pack shape | Label, oil bottle |
| Column count | 1 on label, 2–4 on line sheet, 1–2 on mobile | All |
| Mandatory text block | Size and position set by the label regulation once known | Label — exception pending, Unknown |

## Structure

- Base unit and derivation: u = format width ÷ 12; margins 1u, gutters 0.5u.
- Grid or module per format family: label 12 × u; line sheet A4 12 columns; mobile 4 columns at 375 px.

## Hierarchy and scale

- Reading order: name → variant and number → descriptor → size and price → instructions and mandatory text.
- Levels allowed: four on the label, five on the line sheet; what gives way first: descriptor drops, then the held field shrinks to its 2u minimum; the name never shrinks below its tested minimum.

## Type and image

- Type never sits on product photography; names sit on a paper panel — measure: panel at least 1u past the text on every side.
- Without an image (line sheet text-only entry), the held field and name carry the entry alone.
- Route A's fade that reveals the variant after the name is removed from the static rule: the variant is visible without motion (R1, I3).

## Format behaviour

| Format family | Rules | No-go zones | Static / reduced-motion fallback |
| --- | --- | --- | --- |
| Digital (shop) | 4-column mobile, name wraps, never truncates; images lazy-loaded within the D-0023 budget | — | Variant visible with no animation |
| Print (label, shelf card, line sheet) | Bleed and safe area from the printer; 2u held field | Die line and mandatory block — Unknown | Not applicable |
| Social, environmental, motion | Out of scope in the brief; market signage noted as a possible later format | — | — |

## Application tests

| Application | Dimensions | Content case | Result | Defect | Rule change | Label |
| --- | --- | --- | --- | --- | --- | --- |
| Label | Stand-in 70 × 45 mm | Longest stand-in name: "Unscented cleansing bar" plus "fragrance-free" | Text check: the name needs two lines at the minimum size | Mandatory text space unknown | Name wraps; held field may shrink to 2u | Hypothesis |
| Shelf card | Stand-in 90 × 55 mm | Four products side by side | Text check: I3 places the variant under each name | Size at shelf distance untested | — | Unknown |
| Line sheet | A4 portrait | Dense (four products, prices, sizes) and sparse (one product) | Text check: dense entry drops the descriptor | — | Descriptor is optional on the line sheet | Hypothesis |
| Mobile product page | 375 px | Longest name | Rule I2 removes the current crop defect (F1) | Not built | — | Hypothesis |

## Unfamiliar-colleague test

- Not run: a single-agent fictional run has no unfamiliar colleague. Listed as a required check before any system claim.

## Template deliverables

| Template | Format | Locked | Editable | Status |
| --- | --- | --- | --- | --- |
| Label master | Layout file per pack | Held field, name position, variant line | Name, variant, mandatory text | Not produced |
| Line sheet | A4 layout file | Grid, entry structure | Products, prices | Not produced |
| Shop product card | Component spec | Order and wrap rule | Content | Not produced |

## Human decisions needed

- Founder: accept I1–I3 as invariants or revise.
- Founder: decide whether route A's centred field stays centred on the shelf card, where left-aligned names may scan faster (Interpretation — needs a comprehension test).
- Client: supply real label and shelf-card dimensions, printer and mandatory label text.
