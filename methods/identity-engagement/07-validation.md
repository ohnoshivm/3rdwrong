---
title: 07 Validation
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-22
review_every_days: 180
---
# 07 Validation

## Objective

Check the approved system against real content, accessibility and production conditions before it is packaged for handover.

## Required inputs

- The system-test matrix, approved route and current asset files.
- Representative content, actual dimensions and likely output conditions.
- Accessibility and vendor criteria that apply to the agreed applications.

## Activities

1. Test a matrix of application types against legibility, hierarchy, consistency, contrast, language and production checks.
2. Test strategic fit, recognition, legibility, production feasibility and intended audience interpretation. State the method and limits for each test; do not infer audience response from designer inspection.
3. Check digital text contrast against WCAG 2.2 as the baseline; test colour-blind distinctions and do not depend on colour alone.
4. Inspect print and physical output at intended size and material; where relevant, test emboss, foil, reverse print and embroidery limits with a vendor.
5. Check motion in normal and reduced-motion settings; include a static version where motion is unavailable or unsuitable.
6. Review missing glyphs, substitutions, export errors, links, metadata and asset provenance.
7. Retest each defect fix and record the result; do not mark a failed check as passed because the deadline is near.

## Research methods

- Run manual contrast, keyboard and reduced-motion checks for in-scope digital examples.
- Use print proofs or a production vendor when physical process fidelity matters.
- Use colour-vision simulation as a screening aid, then inspect actual hierarchy and labels.

## Deliverables

- Completed [identity system testing matrix](../../methods/quality/identity-system-testing.md).
- A defect log with severity, owner, fix, retest evidence and accepted exceptions.
- Final validation notes that state untested conditions and scope limits.

## Quality criteria

- Each critical application has a documented pass or unresolved defect.
- Contrast, colour-blindness, type size and language checks match actual use.
- Physical production effects are tested where they materially affect the identity.
- Asset provenance and font permission are reconfirmed.
- No unresolved blocker is hidden in a guideline footnote.

## Common failure modes

- Relying on a simulator as the only accessibility test.
- Testing a print effect only in a screen mock-up.
- Claiming WCAG conformance from a single colour comparison.
- Failing to retest exports after revisions.

## Human approval

The design lead signs the validation record. The client accepts known scope limits and any residual exception in writing. Accessibility or production claims are limited to the checks actually performed.

## Completion conditions

- All high-severity defects are fixed or explicitly accepted with a reason.
- The retest record is complete and files match the approved system.
- Known limitations are ready to transfer into guidelines and handover.

**Supports:** ../../methods/quality/identity-system-testing.md; ../../methods/quality/critique-protocol.md; ../../skills/3w-identity-system-critic/SKILL.md.
