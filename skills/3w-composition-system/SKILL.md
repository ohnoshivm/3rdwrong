---
name: 3w-composition-system
description: Define a brand-wide composition system — invariants and variables, grids and modular structures, scale and hierarchy rules, type–image relationships and layout behaviour across digital, print, social, environmental and motion formats — then test it on the agreed application set and package templates. Use in identity and system phases after a route is chosen; a human makes the composition decisions.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.1
---
# 3w-composition-system

## Purpose

Make composition repeatable across a brand's formats so that a colleague can lay out a new application without inventing rules. The skill turns the route's idea into stated invariants, variables and layout behaviours, then tests them on unlike applications. It does not lay out final artwork for the founder or replace interface design for a product.

## When to use

Use in [phase 05 Identity](../../methods/identity-engagement/05-identity.md) once the logo, type and colour directions exist in draft, and in [phase 06 System](../../methods/identity-engagement/06-system.md) to specify and test rules across the agreed applications. Use again when a new format joins the system after launch.

## When not to use

Do not use before a route is chosen, to style a single hero mock-up, or to design a product interface's flows and components (use the experience-design tools). Do not use a preset layout recipe as the system; presets such as `skill:split-layout-technical` are specialists only when the route calls for that exact device. For refining one approved artefact's hierarchy, `design-skills:design-elevation` is the specialist.

## Inputs

- The chosen route, idea statement and strategy status.
- Draft logo family, typography and colour roles (from [3w-mark-exploration](../3w-mark-exploration/SKILL.md), [3w-typography-system](../3w-typography-system/SKILL.md) and [3w-colour-system](../3w-colour-system/SKILL.md) or equivalent).
- The agreed application set with real dimensions, content and output conditions.
- Representative content: real names, long and short, dense and sparse copy, real or stand-in images with rights noted.
- Image direction if it exists, and any motion scope.
- Fixed content blocks each application must carry (mandatory label text, price, size, barcode, die lines), with their minimum sizes where known.

## Dependencies

Read [phase 05 Identity](../../methods/identity-engagement/05-identity.md), [phase 06 System](../../methods/identity-engagement/06-system.md), [identity system testing](../../methods/quality/identity-system-testing.md), the [creative guardrails](../../methods/creative-guardrails.md) and the composition section of the [identity system specification](../../templates/identity-systems/identity-system-spec.md). Digital layout should follow [web standards](../../methods/quality/web-standards.md). Layout software is the designer's choice; no paid tool is required by this skill.

## Procedure

1. **State the compositional idea without adjectives.** What the layout does for the idea: where attention goes first, what is always held back, what relationship repeats. Example form: "the product name always owns the top third and nothing touches its left edge."
2. **Separate invariants from variables.** Invariants: the few rules that make every application recognisable (for example a fixed relationship between mark and edge, a margin ratio, one hierarchy order). Variables: what may change per format (image crop, column count, colour role share). Name exceptions separately with reasons. Keep invariants few; each must survive the smallest format.
3. **Choose the structure.** A grid (columns, gutters, margins, baseline or modular units) or a proportional module derived from the format or the mark. Express margins and gutters as ratios or units of a base, so the structure scales between a 50 mm label and a 1080 px social post. State the base and how it is derived.
4. **Set scale and hierarchy rules.** The order of reading (for example name → variant → descriptor → legal), the scale steps between levels (from the type scale), how many levels any one application may use, and what gives way when space runs out (what drops, shrinks or moves first).
5. **Define type–image relationships.** Whether type sits on, beside or never on images; safe zones for text over image; crop rules (subject position, minimum margin around subject); how the mark relates to images; what to do when no image exists.
6. **Specify layout behaviour per format family:**
   - digital — breakpoints and reflow order, minimum and maximum line lengths, how the structure collapses on mobile, and keeping within the D-0023 performance budget for image use;
   - print — bleed, safe area, trim, fold or die-cut constraints, and fixed physical minimums for text;
   - social — square, portrait and story ratios, platform interface overlays (profile, captions, buttons) as no-go zones, crop survival in feed thumbnails;
   - environmental — viewing distance, eye height, fixing and wayfinding hierarchy, where in scope;
   - motion — what is fixed and what moves, the hold frame that works as a still, timing for reading, and a reduced-motion or static version. Information a person needs to choose or use the product (for example a variant) must be visible without motion; check the route's proposed motion against this.
7. **Write the rules as decisions a colleague can repeat.** Each rule: statement, measure, example, failure example. Avoid "balanced", "breathing" or "dynamic" without a measure.
8. **Test on the agreed application set.** Use the [identity system testing](../../methods/quality/identity-system-testing.md) matrix with at least three unlike applications where scope permits, long and short names, dense and sparse content, and the smallest real size. Then ask someone unfamiliar with the route, and not its maker, to build one new application from the rules alone; record each place they had to guess. An AI rebuild from the rule sheet alone may screen for gaps first, labelled as a proxy; it never replaces the human test.
9. **Revise the rule, not the mock-up.** When several applications fail on one rule, change the rule and retest all affected applications.
10. **Package templates** (see Output) and hand to an independent reviewer.

## Evidence requirements

A layout behaviour is **Documented** only when an application was built at real dimensions with representative content; name the file and size. The unfamiliar-colleague test is Documented when run and recorded. Statements about how a composition is perceived (calm, premium, clear) are **Interpretation**; claims about audience response are **Hypothesis** until tested. Untested formats are **Unknown**, not passed.

## Output

Return this exact Markdown structure.

```markdown
# Composition system: {{project and route}}

**Status:** {{draft | tested | validation record}} — not approved
**Route and strategy:** {{route link; strategy status}}

## Compositional idea without adjectives
{{one or two sentences}}

## Invariants
| Invariant | Measure | Smallest format it survives | Label |
| --- | --- | --- | --- |

## Variables and exceptions
| Variable or exception | Range or reason | Formats |
| --- | --- | --- |

## Structure
- Base unit and derivation: {{unit}}
- Grid or module per format family: {{columns, gutters, margins}}

## Hierarchy and scale
- Reading order: {{order}}
- Levels allowed: {{n}}; what gives way first: {{rule}}

## Type and image
- {{rule — measure — failure example}}

## Format behaviour
| Format family | Rules | No-go zones | Static / reduced-motion fallback |
| --- | --- | --- | --- |

## Application tests
| Application | Dimensions | Content case | Result | Defect | Rule change | Label |
| --- | --- | --- | --- | --- | --- | --- |

## Unfamiliar-colleague test
- {{who, what they built, where they guessed}}

## Template deliverables
| Template | Format | Locked | Editable | Status |
| --- | --- | --- | --- | --- |

## Human decisions needed
- {{decision, owner}}
```

Template deliverables when final: master grids per format family; editable templates for the agreed applications (layout files, slide master, social frames) with locked invariants and editable variables; a one-page composition rule sheet with correct and incorrect examples; image crop guides; motion hold-frame and reduced-motion examples where motion is in scope.

## Quality checks

- The compositional idea is written without adjectives.
- Invariants are few, measurable and survive the smallest real format.
- Margins and gutters are derived from a stated base, not fixed numbers per mock-up.
- Reading order and what gives way first are stated.
- Type–image rules include a no-image case.
- Every in-scope format family has rules or is marked out of scope; social no-go zones and print safe areas are explicit.
- Motion rules include a hold frame and a reduced-motion or static version.
- At least three unlike applications were built with real content, or the limit is stated.
- The unfamiliar-colleague test ran, or is listed as not run.
- Templates lock invariants and leave variables editable.
- The checker is not the maker.

## Failure conditions

Stop and ask when no route exists, the application set has no real dimensions, or only one application can be tested and the user expects a system claim. A formative run with stand-in dimensions is allowed only when the user accepts it; label every stand-in and every output formative. Do not call the system flexible if every application needed bespoke art direction; record those as unresolved rules. Do not use mock-up lighting or texture to hide a failing layout.

## Human review

The founder or design lead decides invariants, structure and hierarchy. An independent reviewer runs [3w-identity-system-critic](../3w-identity-system-critic/SKILL.md) on the tested set and [3w-brand-consistency-qa](../3w-brand-consistency-qa/SKILL.md) once rules are approved. The client gives visual sign-off in phase 06. This skill records no approval.

## Example

**Fictional example.** For a fictional ceramics studio, "Lowkiln", the invariant "the maker's mark sits one base unit from the bottom-left edge on every format" holds on a 40 mm price tag and a 1080 × 1350 px post (**Documented** in the fictional test files). On a 9:16 story the bottom-left is covered by the platform's reply bar, so the rule gains a named exception: the mark moves to the top-left safe zone. Whether customers notice the repeated corner is a **Hypothesis**.
