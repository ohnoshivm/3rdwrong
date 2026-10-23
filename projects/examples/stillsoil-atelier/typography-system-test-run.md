---
title: Stillsoil Atelier typography system test run
type: project
status: experimental
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---
# Typography system: Stillsoil Atelier / Pause with purpose

**Fictional example for testing methods and skills. Not a client.**

> Fictional skill test run of `3w-typography-system` 0.1.0. Candidate
> typefaces are described by role and specification only (T1–T3); no real
> font, licence or foundry is named or assessed. Nothing here is approved.

**Status:** shortlist (formative) — not approved
**Route and strategy:** [concept route A](concept-route-a.md), not chosen; strategy not signed ([fictional brief](brief.md)).

## The type's job

The type makes each product name the first thing read on a label, shelf card and mobile product page, and sets the variant directly under it at a size that still reads on a compact shelf card (R2). Instructions must stay readable on tactile paper (R4). Today three unrelated typefaces are in use (F1); the system should use one family where possible.

## Constraints

| Constraint | Value | Source / label |
| --- | --- | --- |
| Scripts and languages | English on all current touchpoints; any Indian script is an open question | Documented — B1 open questions; Unknown — script need |
| Mandatory label text | Ingredients, legal and regulatory lines not supplied | Unknown — the client must confirm approved claims and the applicable labelling rules |
| Smallest print size | Label size unknown; ingredient text likely the smallest | Unknown |
| Media for licence | Print labels and line sheet, web shop, possibly market signage | Documented — B1 scope (signage Interpretation) |
| Wordmark | Mark exploration recommends a drawn wordmark, not live type | Documented — [mark test run](mark-exploration-test-run.md) |
| Web budget | ≤ 2 families, subset, ≤ 100 KB initial fonts; mobile p75 LCP ≤ 2.0 s, CLS ≤ 0.1 | Documented — web standards and D-0023 |

## Shortlist

| Role | Candidate | Why it serves the job | Category default? | Risk | Status |
| --- | --- | --- | --- | --- | --- |
| Single family, names and text | T1 — a serif with separate text and display optical sizes, large x-height text cut | One family covers names and instructions; text cut holds at small label sizes | Unknown — no audit | Route A's "tall serif" may push towards a narrow display cut that hurts small-size reading | Lead candidate |
| Names only | T2 — a narrow display serif | Matches the route's "tall serif" wording | Unknown | Two families for a four-product brand; narrow forms lose the variant line on the shelf card | Held |
| Utility (numbers, batch, price) | T3 — a sans with tabular figures | Only if T1 lacks tabular figures and ₹ | Unknown | Adds a second family to the web budget | Only if needed |

## Licensing

| Font | Desktop | Web | App | Video / broadcast | Logo use | Client transfer | Source and label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1–T3 | Not checked | Not checked | Out of scope | Out of scope | Not needed if the wordmark is drawn | Not checked | Unknown — fictional candidates; licences must be read before selection |

## Script support

| Script / language | Font | Checks run | Renderer | Fluent reviewer | Result |
| --- | --- | --- | --- | --- | --- |
| Latin (English) | T1 | Specimen strings defined: the four product names, "fragrance-free", numerals 0–9, ₹ and price formats, batch and date formats | Not run | Not needed | Unverified |
| Kannada, Hindi or other | — | Not run — need not confirmed | — | None assigned | Unknown — delivered as unverified, not passed |

## Pairing rationale

One family is the starting decision: the brief's problem is three unrelated typefaces (F1), and hierarchy can come from optical size, size and position. A second family is added only if a measured need appears (tabular figures, ₹ or a required script).

## Hierarchy and scale

| Level | Font and cut | Size (print / web) | Line height | Measure | Tracking / case |
| --- | --- | --- | --- | --- | --- |
| Product name | T1 display | Label: largest that fits the field; web: clamp, minimum 28 px | 1.1 | One to two lines, never truncated | Sentence case |
| Variant | T1 text, medium | Label: at least the size that reads at shelf distance (to test); web 18 px | 1.3 | One line | Sentence case, with number |
| Descriptor | T1 text | Web 16 px | 1.5 | 45–70 characters | — |
| Instructions, ingredients | T1 text | Physical minimum to test at actual size on the real stock | 1.4 | Column of label | — |

## Spacing and kerning

- Check "ll" in "Stillsoil" and the pairs in each product name at display and text sizes.
- Check ₹ with numerals and the space before units.
- Wordmark is drawn artwork; live T1 never sets the brand name as a logo.

## Web performance and fallbacks

| File | Subset | Format | Size | Loading | Fallback stack |
| --- | --- | --- | --- | --- | --- |
| T1 text (roman) | Latin, ₹ | WOFF2 | Not measured | Preload, `font-display: swap` | Metric-matched system serif |
| T1 display | Latin | WOFF2 | Not measured | Not preloaded | Same |

## Application tests

| Application | Result | Defect | Rule change |
| --- | --- | --- | --- |
| Mobile shop product name | Not built; rule set: wrap, never truncate | F1's crop problem addressed in rule only | Name wraps to two lines before size drops |
| Shelf card variant line | Not built | Size unknown | Test at real shelf distance |
| Label ingredients | Not built | Mandatory text unknown | Blocked on client |

## Deliverables

- Shortlist and hierarchy (this file) — draft.
- Specimen, licence register and web font kit — not produced.

## Human decisions needed

- Founder: confirm the one-family direction.
- Client: confirm required scripts and languages, approved claims and mandatory label text.
- Founder: name a fluent reviewer for any Indian script brought into scope.
