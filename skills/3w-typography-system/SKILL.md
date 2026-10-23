---
name: 3w-typography-system
description: Select and specify a brand typography system — type chosen against the idea, licensing for desktop, web, app and broadcast, Latin and Indian-script support, pairing, hierarchy and scale, optical sizes, spacing and kerning checks, web-font performance within the D-0023 budget, fallback stacks, specimen and deliverables. Use in identity and system phases after a route is chosen; a human makes the type decisions.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.1
---
# 3w-typography-system

## Purpose

Give the studio one method for choosing and specifying brand typography that is right for the idea, legally usable in every agreed medium, works in every required script and performs on the web. The skill structures shortlisting, checking and specifying; type selection and final judgement stay with the founder or design lead.

## When to use

Use in [phase 05 Identity](../../methods/identity-engagement/05-identity.md) after a route is chosen, to shortlist and check typefaces; in [phase 06 System](../../methods/identity-engagement/06-system.md) to set hierarchy and test across applications; and in [phase 07 Validation](../../methods/identity-engagement/07-validation.md) to reconfirm licences, glyphs and web-font weight on final files.

## When not to use

Do not use before a route exists, to pick a font by mood, or to tune an existing interface's type ramp alone — `agent:visual-designer` converts an approved type system into digital tokens and a ramp, and `vectorlab-ux-skills:typography` fixes a measured scale or line-height defect. Do not use to interpret a licence as legal advice; unclear terms go to the foundry or a lawyer.

## Inputs

- The chosen route, idea statement and strategy status.
- Required languages and scripts for each application (for example English on labels, Hindi or Kannada on retail cards), and who will review them fluently.
- The agreed application set and media: print, web, app, video or broadcast, signage, office documents.
- Real content strings: product names, numerals, prices, legal lines, longest and shortest names.
- Mandatory text the applications must carry (for example ingredients, regulatory and legal lines) with any minimum sizes, confirmed by the client from the applicable rules; the skill does not determine regulatory requirements.
- Budget for licences and any existing fonts the brand owns.
- The digital performance budget ([D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) and [web standards](../../methods/quality/web-standards.md)).

## Dependencies

Read [phase 05 Identity](../../methods/identity-engagement/05-identity.md), [identity system testing](../../methods/quality/identity-system-testing.md), the [final delivery checklist](../../methods/quality/final-delivery-checklist.md), the [creative guardrails](../../methods/creative-guardrails.md) (rule 3 and rule 5) and the typography section of the [identity system specification](../../templates/identity-systems/identity-system-spec.md). Licence documents come from the foundry or distributor. Font-inspection and subsetting can use free tools (for example `fonttools`); no paid tool is required by this skill.

## Procedure

1. **Write the type's job from the idea**, without adjectives: what the type must make visible (a name, a pace of reading, a variant, a voice of instruction) and where it carries the identity versus where it must disappear.
2. **Set hard constraints first:** scripts and languages; smallest real sizes per medium; the media the licence must cover; weights and styles actually needed; budget.
3. **Shortlist two to four candidates per role** (display, text, and only if needed a utility or script companion). For each, record the reason it serves the job, the category audit's type column (is it the category default?), and the never-copy list from the [Taste Graph](../3w-taste-graph/SKILL.md) pack. Reject the D-0006 rejected look (heavy grotesk as a costume) and any default stack chosen by habit.
4. **Check licensing per medium.** For each candidate, read the actual licence and record what is covered: desktop (seats), web (page views or domains, self-hosting allowed), app embedding, video or broadcast, logo or wordmark use, editing or outlining, and client transfer on handover. Open-licence fonts (for example SIL OFL) still need their notice and naming terms recorded. Mark any unclear term **Unknown** and ask the foundry.
5. **Check script support with real text.** Build the specimen string set first: every product name, the longest and shortest names, numerals, currency, units, dates and the mandatory text; for each non-Latin script, strings supplied or checked by a fluent reader, never machine-written and unchecked. Latin: accented characters for the languages in scope, numerals (lining, old-style, tabular), currency (including ₹ where prices appear), punctuation and ligatures. For Devanagari or other Indian scripts: conjuncts, matra placement, reph, nukta, numerals, shaping in the target renderers (browser, InDesign or the print workflow, app), and vertical metrics against the Latin partner. A fluent reader reviews every specimen; a font that "has the glyphs" is not proof it shapes correctly.
6. **Pair by structure, not by mood.** Compare x-height, stroke contrast, proportions, rhythm and colour on the page; for multi-script work, match apparent size and weight between scripts rather than point size. State why the pairing serves the idea; one family with enough range beats a pairing that only adds variety.
7. **Set hierarchy and scale.** Choose levels from the application set (the fewest that work), a scale with stated ratio or steps, line heights, measure limits, case and tracking per level; fluid sizes for the web with clamped minimums; print sizes in points with physical minimums tested at actual size.
8. **Use optical sizes properly.** Where the family has optical sizes or an `opsz` axis, assign text cuts to small sizes and display cuts to large sizes; if it does not, adjust tracking and weight by size and record it.
9. **Check spacing and kerning.** Set real names and numerals at display and text sizes; check problem pairs in the brand's own words, figures in tables and prices, punctuation spacing, all-caps tracking, and any wordmark set in the font. Record fixes as tracking or kerning rules; a wordmark needs hand-kerned artwork, not live type.
10. **Plan web-font performance within the budget.** Web standards set ≤ 2 families, subset, ≤ 100 KB initial font transfer; D-0023 sets mobile p75 LCP ≤ 2.0 s, CLS ≤ 0.1 and ≤ 2 MB before first interaction. Use WOFF2, subset per script and language, prefer a variable font when it is lighter than the static weights needed, preload only the critical file, choose a `font-display` strategy, and record measured file sizes.
11. **Write fallback stacks** per role and script, matched for metrics (`size-adjust`, `ascent-override` and related descriptors) to limit layout shift, including a system fallback for each Indian script in scope.
12. **Test across the agreed applications** with the [identity system testing](../../methods/quality/identity-system-testing.md) matrix, then produce the specimen and deliverables (see Output) and hand them to an independent reviewer.

## Evidence requirements

Licence coverage is **Documented** only from the licence text (name the document and date); otherwise **Unknown**. Script support is Documented only after shaping is tested in the named renderer and reviewed by a fluent reader. Web-font weight is Documented only from measured files. Statements about how type is perceived are **Interpretation**; audience response is **Hypothesis** until tested. Category type conventions need the linked audit or are **Unknown**.

## Output

Return this exact Markdown structure.

```markdown
# Typography system: {{project and route}}

**Status:** {{shortlist | specified | validation record}} — not approved
**Route and strategy:** {{route link; strategy status}}

## The type's job
{{sentences without adjectives}}

## Constraints
| Constraint | Value | Source / label |
| --- | --- | --- |

## Shortlist
| Role | Candidate | Why it serves the job | Category default? | Risk | Status |
| --- | --- | --- | --- | --- | --- |

## Licensing
| Font | Desktop | Web | App | Video / broadcast | Logo use | Client transfer | Source and label |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Script support
| Script / language | Font | Checks run | Renderer | Fluent reviewer | Result |
| --- | --- | --- | --- | --- | --- |

## Pairing rationale
{{structural reasons}}

## Hierarchy and scale
| Level | Font and cut | Size (print / web) | Line height | Measure | Tracking / case |
| --- | --- | --- | --- | --- | --- |

## Spacing and kerning
- {{issue — rule}}

## Web performance and fallbacks
| File | Subset | Format | Size | Loading | Fallback stack |
| --- | --- | --- | --- | --- | --- |

## Application tests
| Application | Result | Defect | Rule change |
| --- | --- | --- | --- |

## Deliverables
- {{file — status}}

## Human decisions needed
- {{decision, owner}}
```

Deliverables when final: a type specimen (every role, size and script with real strings); hierarchy table and tokens; licence register with documents; font files only where the licence permits transfer (otherwise purchase instructions); web font kit (subset WOFF2, CSS with fallbacks); application examples.

## Quality checks

- The type's job is written without adjectives and every shortlisted face is tied to it.
- Licences were read per medium; unclear terms are Unknown and sent to the foundry.
- Every required script was shaped in its real renderer and checked by a fluent reader.
- Numerals, currency and the brand's own names were set and kerned.
- Hierarchy uses the fewest levels the applications need; print minimums were checked at actual size.
- Optical sizes are used, or size-specific adjustments recorded.
- Initial web fonts fit ≤ 2 families and ≤ 100 KB, measured; fallbacks are metric-matched.
- No wordmark relies on live type.
- The checker is not the maker.

## Failure conditions

Stop and ask when the media are unknown or a licence cannot be read. When a script need is unconfirmed or no fluent reviewer is available, continue for the confirmed scripts and deliver the others as unverified, not as passed. A formative run on an unchosen route is allowed only when the user accepts it; label every output formative. Stop if asked to use an unlicensed or pirated font, to outline a font in a logo against its licence, or to choose type before the route exists.

## Human review

The founder or design lead shortlists and chooses type. A fluent reader signs each script specimen. The foundry or a lawyer answers licence questions. An engineer confirms web-font sizes and layout shift in the build. The client gives visual sign-off in phase 06. This skill records no approval.

## Example

**Fictional example.** For a fictional spice importer, "Ashgrove Pantry", labels need English and Hindi. A shortlisted serif covers Latin well but its Devanagari companion places one matra wrongly in a fictional InDesign test (**Documented** in that test), so it is held until the foundry confirms a fix. The web licence for a second candidate allows self-hosting but not app embedding (**Documented** from the fictional licence); the app is out of scope, so it stays on the list with the limit recorded.
