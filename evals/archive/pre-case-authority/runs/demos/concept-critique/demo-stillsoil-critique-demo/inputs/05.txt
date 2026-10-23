---
title: Identity system testing matrix
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-22
review_every_days: 180
---
# Identity system testing matrix

Select application rows that are in the agreed scope. Add real dimensions,
content, output conditions and owner. A mock-up alone does not validate
production performance.

| Application | Legibility and hierarchy | Identity consistency | Accessibility and language | Production and asset checks |
| --- | --- | --- | --- | --- |
| Small logo or avatar | Read at intended pixel and print sizes; test silhouette | Correct approved variant and clear space | Do not rely on colour difference alone | SVG/raster export, one-colour output, minimum-size note |
| Product label or pack mock-up | Product and variant scan at actual size | Logo, type, colour, image and information hierarchy | Required scripts, glyphs, contrast and legibility | Stock, ink, bleed and finish; test emboss/foil only if relevant |
| Line sheet or sales document | Dense and sparse entries remain distinct | Repeated grid and asset rules hold | Text size, contrast, selectable text and scripts | Print and PDF output, links, embedded or licensed fonts |
| Digital product or landing page | Mobile crop, headings and content order | Type, colour, logo and image use follow rules | WCAG 2.2 contrast baseline; keyboard and colour-blind checks | Responsive export, alt text and asset weight where in scope |
| Social post or small banner | Message remains readable in crop and feed size | Flexible template still looks like the brand | Meaning is not carried by colour alone; captions where needed | Correct dimensions, profile and source asset rights |
| Motion or interaction | Key information remains readable in time | Motion expresses the same identity idea | Reduced-motion alternative, keyboard and sound-off use | File size, loop, codec or fallback as agreed |
| Embroidery, emboss or signage | Form survives distance and minimum stroke | Approved mark remains recognisable | Contrast and readable content remain adequate | Vendor tolerances, material, stitch or relief depth |

For each selected application, record version; dimension; content; viewing
condition; expected process; checks run; evidence; result; defects; retest;
owner; and accepted exceptions. Use **Documented** for a cited specification
or observed test, **Interpretation** for the team's reading, **Hypothesis** for
an untested expectation and **Unknown** when information is missing.

Check digital text contrast against WCAG 2.2 as a baseline for in-scope digital
examples. Check colour-blind distinctions and provide labels, shapes or
hierarchy that do not depend on colour alone. An automated ratio or simulator
is a screening aid; it does not establish overall accessibility conformance.

Test print, emboss, foil, embroidery, small-size and other production
constraints when relevant to scope. If no proof or vendor data is available,
record the limitation as unverified and state what evidence is needed before
production.
