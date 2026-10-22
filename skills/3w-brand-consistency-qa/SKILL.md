---
name: 3w-brand-consistency-qa
description: Check supplied brand assets against an approved identity specification and documented use rules. Use before publishing or handover when files can be compared; do not claim conformance when no approved baseline exists.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-22
  version: 0.1.0
---
# 3w-brand-consistency-qa

## Purpose

Run a traceable quality check across brand assets and identify deviations from approved rules. Report conformance, defects and untestable items so a person can correct the work before use.

## When to use

Use when current assets, guidelines and their versions are available. It can review public-facing materials, a handover folder or an agreed set of exports.

## When not to use

Do not claim conformance without an approved baseline. Do not rewrite strategy, approve design, infer asset rights or certify legal, accessibility or print compliance from filenames alone.

## Inputs

- Approved identity system specification or guideline with approver, date and version.
- Assets to inspect, with file paths, formats, dimensions and intended use.
- Agreed scope: channels, languages, output sizes and production processes.
- Rights, font and image provenance notes where relevant.
- Prior exceptions or approved variants.

## Dependencies

Read [identity system specification template](../../templates/identity-systems/identity-system-spec.md), [phase 06 System](../../methods/identity-engagement/06-system.md), [identity testing matrix](../../methods/quality/identity-system-testing.md) and [final delivery checklist](../../methods/quality/final-delivery-checklist.md). No external paid tools are required; if measurement software is unavailable, mark that check not run.

## Procedure

1. Verify baseline status and version. If it is not approved, stop conformance scoring and report a missing or provisional baseline.
2. Inventory every asset: name, format, dimensions, channel, intended use and version. Flag broken, duplicate or ambiguous files.
3. Extract applicable written rules: logo variant, clear space, minimum size, type, colour, composition, image, motion, language and naming.
4. Map each asset only to rules that apply. Do not invent a rule because the asset looks unusual.
5. Inspect logo and layout variants for fit, cropping, clear space, hierarchy and consistency against the specified version, not memory.
   Compare minimum-size and one-colour use to written rules; mark either check Not testable when no rule or file exists.
6. Inspect typography and scripts using representative text. Check specified fonts, glyphs, sizes, substitutions and licence notes; a preview does not prove embedding rights.
   Include real names, numerals, punctuation and every required script in specimen text.
7. Check colour values and digital contrast for in-scope combinations. Note whether WCAG 2.2 contrast screening and colour-blind checks were run.
   Confirm that meaning is also conveyed by labels, shape or hierarchy when colour varies.
8. Check imagery, motion, file quality, dimensions, colour space and production notes against scope. Missing proof or vendor information is Not testable.
   Check linked assets, transparent exports and raster dimensions; do not judge print texture from a screen mock-up.
9. Record each check as **Pass**, **Fail** or **Not testable**, with rule ID, evidence, severity, fix and retest requirement.
10. Summarise readiness and blockers. Human review decides whether exceptions are accepted or assets can be released.

## Evidence requirements

Cite the exact guideline section and inspected asset. Use **Documented**, **Interpretation**, **Hypothesis** and **Unknown** for claims; do not confuse those labels with QA result labels. Record tool and version for automated checks. Do not claim WCAG conformance, licence permission or production tolerance without evidence.

## Output

Return this exact Markdown structure.

```markdown
# Brand consistency QA: {{project}}

**Baseline:** {{approved file, version, approver, date | missing}}
**Assets checked:** {{scope and date}}
**Overall status:** {{ready for human review | blocked | not testable}}

## Asset inventory
| Asset | Intended use | Format / size | Version | Review status |
| --- | --- | --- | --- | --- |

## Checks
| Asset | Rule ID and requirement | Result | Evidence | Severity | Fix / retest |
| --- | --- | --- | --- | --- | --- |

## Not tested
- {{check}} — why it could not be run; evidence needed.

## Rights and accessibility notes
{{font/image provenance, contrast and checks actually run}}

## Human release decision
- Approver: {{name or role}}
- Decision and date: {{pending | recorded decision}}
```

## Quality checks

- Baseline version and approval are verified before scoring.
- Every asset has intended use and a traceable file identity.
- Results refer to written rules rather than taste or memory.
- Pass, Fail and Not testable are used consistently.
- Missing script, contrast, permission or vendor checks stay visible.
- Fixes have owners and retest criteria.
- Human release decision is separate from automated checks.
- Report deviations from written rules only; do not flag personal taste as a QA failure.
- Retest a corrected export, not merely the source design file.
- Include the tested file version so a later replacement cannot inherit a pass.
- Keep legal, licence and accessibility conclusions within the evidence actually inspected.

- An approved exception names its approver, date and affected assets.
- A file that cannot be opened is not scored from its name or thumbnail.
- The report distinguishes an asset defect from a missing guideline rule.
- The test set covers requested channels or states omissions.
- A contrast ratio names foreground, background and text size.
- Retest evidence points to the corrected version.
- Unknown asset rights block release pending human review.
- A pass is not a claim of preference or business effect.

## Failure conditions

Stop and ask for an approved baseline when a conformance verdict is requested but none is supplied. Ask for assets, dimensions or intended uses when missing information affects checks. Stop if files are corrupted, inaccessible or scope exceeds evidence. Never infer permission from possession or claim certification from a limited review.

## Human review

A human designer reviews failures and records accepted exceptions. The authorised owner decides release. A qualified rights reviewer, language reviewer or vendor confirms issues beyond supplied evidence. This skill never marks an asset approved or released.

## Example

**Fictional example.** A synthetic guideline specifies horizontal and compact marks; a fictional line sheet uses the compact mark but substitutes a font. Record logo **Pass**, font rule **Fail**, and print proof **Not testable** because no vendor output was supplied. Request a licensed font correction and retest; do not approve release.
