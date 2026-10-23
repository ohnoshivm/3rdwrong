---
name: 3w-image-qa
description: Check images before release for rights and licence coverage, likeness and property releases, AI disclosure and written client consent (D-0023), brief and art-direction fit, technical quality, accessibility text and web weight. Use as the independent gate after image production and before publishing or handover; do not use to make or select images, or to give legal advice.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-image-qa

## Purpose

Stop images reaching a client, a site or a social channel without the right to use them, without consent from the people in them, without honest AI disclosure, or in a state that harms the work.

## When to use

Use after `skill:3w-image-production` hands over a set, before handover, launch or publication, and whenever an image is replaced. Also use on images received from a client or a third party.

## When not to use

Do not use to make or select images. Do not use as a brand-wide guideline audit; that is `skill:3w-brand-consistency-qa`. This check screens evidence; it is not legal advice.

## Inputs

- The image files at the version to be released.
- The rights register from image production (or equivalent source records).
- The approved art direction and image briefs.
- The client's written AI consent where relevant, and the release scope (channels, territory, term).

## Dependencies

Read [IP and licensing](../../business/legal/ip-and-licensing.md), [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md), [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md), [final-delivery checklist](../../methods/quality/final-delivery-checklist.md) and [web standards](../../methods/quality/web-standards.md#weight-budgets).

## Procedure

1. **Match files to records.** Every file maps to one register row; orphans fail.
2. **Rights.** Licence or contract covers the release scope (media, territory, term, sensitive use). Stock is not used in marks. Unknown fails.
3. **Likeness and property.** Each identifiable person has a release covering the use; minors need guardian consent; recognisable private property, artworks and trademarks are cleared or removed. No identifiable person is AI-generated or altered without consent.
4. **AI.** AI-generated or AI-edited files are marked; client written consent exists for AI material in final deliverables; tool terms permit commercial use; the handover asset register carries the disclosure.
5. **Client data and anonymity.** Public studio uses (case studies, social) carry no confidential client identity unless cleared under D-0021.
6. **Fit.** Each image serves its brief and placement; record misfits as findings, not taste.
7. **Technical.** Resolution for the largest placement, focus, artefacts (AI distortions in hands, text, edges), colour space, cropping at each aspect ratio, print specification where relevant.
8. **Accessibility and weight.** Alt text written for meaning (or empty for decorative); no text baked into images without an equivalent; web exports within budget.
9. Record each check as Pass, Fail or Not testable. The checker is not the image's maker.

## Evidence requirements

Cite the register row, licence or release document, and consent record for each Pass. A file name or a supplier's verbal assurance is not evidence.

## Output

```markdown
# Image QA: {{codename}} — {{set}} v{{version}}

**Checker:** {{not the maker}} · **Release scope:** {{channels, territory, term}}
**Status:** {{ready for release decision | blocked}}

| File | Rights | Likeness / property | AI + consent | Anonymity | Fit | Technical | Alt text / weight | Fix |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Blockers
## Not testable (evidence needed)
```

## Quality checks

- Every file has a register row and evidence for each Pass.
- Releases cover the actual use, not a narrower one.
- AI consent is written, dated and covers the deliverable.
- Unknown rights or consent block release.
- The checker did not make or select the images.

## Failure conditions

Stop and block release when rights, releases or AI consent are missing or unclear, or when the files cannot be opened. Do not pass an image because it is already live.

## Human review

The founder decides release after blockers are cleared; a qualified adviser answers legal questions beyond the evidence.

## Example

**Fictional example.** In a fictional set of seven, six pass. The AI-generated hero texture passes rights and AI consent, but its 2,400 px export is 410 KB as the LCP image. Fail on weight; re-export as AVIF and retest that file only.
