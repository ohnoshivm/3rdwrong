---
name: 3w-mark-exploration
description: Take a mark or logo from a written idea to a production-ready vector family through at least three conceptually distinct routes, construction and optical correction, small-size and medium tests, one-colour and reverse versions, and a distinctiveness check. Use after a concept route is chosen; a human designer makes every final form decision.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.1
---
# 3w-mark-exploration

## Purpose

Give the studio one repeatable path from a mark's idea to a vector family that survives real sizes and media. The skill structures exploration, construction and testing; it does not draw the final mark, judge taste for the founder or clear a trademark.

## When to use

Use in [phase 05 Identity](../../methods/identity-engagement/05-identity.md) after a concept route has been chosen in [phase 04 Concept](../../methods/identity-engagement/04-concept.md), when the logo family needs exploring, refining, testing or specifying. Use it again in [phase 07 Validation](../../methods/identity-engagement/07-validation.md) to re-run the size and medium tests on the final artwork.

## When not to use

Do not use before a route is chosen, to restyle an existing approved mark without a brief, or to generate a finished logo with an image model and call it original. Do not use it to decide registrability; a trademark search and opinion are legal steps. Do not use for icon sets or illustration systems, which need their own brief.

## Inputs

- The chosen concept route, its idea statement and the strategy status (approved, or draft marked formative).
- The brand name as it must appear, including any required scripts, and the mark type in scope (wordmark, symbol, monogram, combination or an open question).
- Brand architecture: whether the mark signs one product, a product line or sub-brands, and any evidence about name recognition or recall.
- The [category code audit](../3w-category-code-audit/SKILL.md) for the same category, or a note that none exists.
- A [Taste Graph](../3w-taste-graph/SKILL.md) reference pack with its never-copy list, if one has been built.
- The agreed application set and media: screen sizes, favicon and app icon, labels, print, and any embroidery, emboss, deboss, foil or signage.
- Production constraints known so far: vendors, minimum stroke, substrate, colour count.

## Dependencies

Read [phase 05 Identity](../../methods/identity-engagement/05-identity.md), [identity system testing](../../methods/quality/identity-system-testing.md), the [final delivery checklist](../../methods/quality/final-delivery-checklist.md), the [creative guardrails](../../methods/creative-guardrails.md) and the logo section of the [identity system specification](../../templates/identity-systems/identity-system-spec.md). Hand finished routes to [3w-identity-system-critic](../3w-identity-system-critic/SKILL.md). Vector work needs a drawing application chosen by the designer; no paid tool is required by this skill.

## Procedure

1. **State the idea first.** Write what the mark must do in one or two sentences without visual adjectives (no "bold", "clean", "organic", "minimal"). Name the job: recognise the brand, carry a product line, sign off a page, sit beside a partner logo. If the idea cannot be written without adjectives, return to the route; do not start drawing.
2. **List constraints that shape form.** Name length and letters, scripts, smallest real size on screen (px) and in print (mm), colour count, media, brand architecture and any category entry code the audit says is worth keeping. Record unknowns. Decide, with labelled evidence, whether the name or a symbol must carry recognition; this sets the mark type, not taste.
3. **Write at least three conceptually distinct routes.** Each route needs a different organising idea — for example a letterform idea, a symbol from the product or ritual, a structural device — not three styles of one idea. For each give: idea, mechanism, what it borrows from the category and why, first risk. Reject any route that is the studio's rejected own-identity look ([D-0006](../../studio/decisions/0006-rejected-own-identity-direction.md)) or a reference on the never-copy list.
4. **Sketch rough, then pick for test, not polish.** Rough sketches (paper or quick vector) for each route at thumbnail size first. Shortlist by idea strength and small-size survival; keep rejected routes and reasons.
5. **Move to vector deliberately.** Build on a construction grid only where it helps; draw with the fewest points that hold the curve; keep handles horizontal or vertical at extremes; close and join paths; outline strokes only at the end and keep a live master.
6. **Run the construction and optical-correction checklist** (see Quality checks) and record each correction made: overshoot of rounds and points beyond the baseline and cap height; optical centre placed slightly above the geometric centre; horizontal strokes thinner than verticals so they read equal; stroke contrast consistent with the type it sits beside; counters opened so they do not fill at small sizes; apertures wide enough to stay open; letter and component spacing set by eye, not by numeric equal gaps; ink traps or notches only where the smallest size or medium demands.
7. **Test sizes on screen.** Render at 16, 24, 32 and 48 px, as a favicon (including the browser tab on light and dark chrome) and as an app icon inside its platform mask. Decide explicitly what represents the brand below the master's minimum size (a cut from the wordmark, a monogram or a symbol); a long wordmark rarely survives 16 px. Draw it as a designed variant, not a scaled-down master.
8. **Test media in scope.** Label at actual size, recording the physical minimum in millimetres for the smallest print application; line sheet; mobile header; embroidery (minimum stitch width and fill direction from the vendor), emboss or deboss (relief depth, closed counters fill), foil (fine lines and small counters break). Mark each medium tested, unverified or out of scope; a screen mock-up of foil or emboss is not a test.
9. **Make the colour and reverse versions.** Full colour, one-colour positive, one-colour reverse (on dark and on image), and check that reverse versions are optically corrected: light shapes on a dark ground read heavier, so a reverse may need slight thinning, while in print ink spread can close fine reversed lines and counters, so those may need opening.
10. **Set clear space and minimum size.** Define clear space by a unit taken from the mark itself; set minimum sizes per medium from the tests in steps 7–8, not by assumption.
11. **Check distinctiveness.** Compare silhouettes and devices against the category audit and the Taste Graph pack: list any audited example sharing the same device, silhouette or letter treatment. If no audit exists, distinctiveness is **Unknown**. A reverse-image search may screen for close matches; record it as a screening step, never as clearance.
12. **Flag registrability cautions.** Note generic devices (leaf, drop, swoosh, initial in a circle), descriptive words and close audited matches as risks for a legal search. State plainly that trademark clearance is a legal step done by a qualified professional in the relevant classes and jurisdictions; this skill gives no verdict.
13. **Specify deliverables** (see Output) and hand the family to an independent critic. Record decisions for the founder; do not mark anything approved.

## Evidence requirements

Label every claim **Documented** (seen in the artwork, test render or a cited source), **Interpretation** (the team's reading), **Hypothesis** (untested expectation, with the test that would check it) or **Unknown**. A size or medium test is Documented only when it was actually rendered, printed or proofed; name the size, device or vendor. Distinctiveness without a linked category sample is Unknown. Memorability, recognition and preference are never Documented from studio inspection. AI-generated sketches are labelled as such and need the client's written consent before any AI-derived form reaches a final deliverable (D-0023).

## Output

Return this exact Markdown structure.

```markdown
# Mark exploration: {{project and route}}

**Status:** {{exploration | refinement | test record}} — not approved
**Route and strategy:** {{route link; strategy status}}
**Mark type in scope:** {{wordmark | symbol | monogram | combination | open}}

## Idea without visual adjectives
{{one or two sentences}}

## Form constraints
| Constraint | Value | Source / label |
| --- | --- | --- |

## Routes
| Route | Organising idea | Mechanism | Category borrowing and reason | First risk | Status |
| --- | --- | --- | --- | --- | --- |

## Construction and optical corrections
| Check | Finding | Correction made | Label |
| --- | --- | --- | --- |

## Size and medium tests
| Size / medium | Variant used | Result | Evidence | Label |
| --- | --- | --- | --- | --- |

## Colour and reverse versions
- {{version}} — {{correction or note}}

## Clear space and minimum size
- Clear space: {{unit from the mark}}
- Minimum size: {{per medium, with test reference}}

## Distinctiveness and registrability cautions
- {{closest audited match or Unknown}} — {{difference}}
- Legal step required: trademark search by a qualified professional; no AI verdict.

## Deliverables
| File | Variant | Format | Colour space | Status |
| --- | --- | --- | --- | --- |

## Human decisions needed
- {{decision, owner}}

## Handoff
- Critic: {{who runs 3w-identity-system-critic; not the maker}}
```

Deliverable set, when the family is final: master and variants as SVG (screen, outlined, no embedded raster), PDF (vector, print) and EPS only if a named vendor requires it; colour-space variants — RGB/sRGB for screen, CMYK for the named print process, spot (for example a Pantone reference) where specified, one-colour black and one-colour white; favicon ICO/SVG and app-icon PNG set at platform sizes; a construction sheet showing grid, clear space and minimum sizes.

## Quality checks

- The idea is written without visual adjectives before any form is described.
- At least three routes differ in organising idea, not style; rejected routes keep their reasons.
- No route uses the D-0006 rejected look or a never-copy reference.
- Overshoot, optical centre, stroke contrast, counters, apertures and spacing each have a recorded finding.
- 16, 24, 32 and 48 px, favicon and app-icon renders exist or are marked unverified; a small-size variant is drawn, not merely scaled.
- Every in-scope medium is tested, unverified or out of scope; no screen simulation is counted as a physical test.
- One-colour positive and reverse exist and the reverse is optically checked.
- Clear space uses a unit from the mark; minimum sizes come from tests.
- Distinctiveness cites the audit or is Unknown; registrability is a caution list plus a legal step, never a verdict.
- Vector files are clean: closed paths, no stray points, no hidden layers, outlined text, correct colour space per file.
- The checker is not the maker.

## Failure conditions

Stop and ask when there is no chosen route, the brand name or script is unsettled, or the idea cannot be stated without visual adjectives. A formative run on an unchosen route is allowed only when the user accepts it; label every output formative and set no minimum sizes or deliverables as final. Stop if asked to copy, trace or closely adapt an existing mark, to present an AI image as finished artwork, or to say a mark is registrable or "safe". Return a preliminary record, without minimum sizes, when the size and medium tests could not be run.

## Human review

The founder or the design lead makes every form decision: route shortlist, final drawing, optical corrections and variants. An independent reviewer runs [3w-identity-system-critic](../3w-identity-system-critic/SKILL.md) before the founder chooses. Vendors confirm physical tolerances; a fluent reader checks every non-Latin script; a qualified trademark professional runs clearance. The client gives visual sign-off in phase 06; this skill records no approval.

## Example

**Fictional example.** For a fictional bakery, "Northfold", the idea reads: "the mark shows the one fold every loaf gets by hand." Three routes follow — a folded letter N, a symbol built from the dough-fold diagram, and a wordmark whose spacing tightens where the fold sits. At 16 px the dough-fold symbol closes into a blob (**Documented** from a test render), so a two-stroke small-size variant is drawn. The category sample of eight fictional bakeries shows five wheat-ear symbols (**Documented for that sample**); none uses a fold. Whether customers notice the fold remains a **Hypothesis**, and trademark clearance is left to a legal search.
