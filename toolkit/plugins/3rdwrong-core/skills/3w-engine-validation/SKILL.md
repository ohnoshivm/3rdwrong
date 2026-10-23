---
name: 3w-engine-validation
description: Validate a 3RDWRONG house-engine kit (a reusable component, shader, motion or 3D module) before it may be offered to projects, by testing it against the D-0023 performance budget, reduced-motion and accessibility rules, the browser and device matrix, licences and documentation. Use as the Labs gate between a technique study and project reuse; do not use as a client launch gate.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-engine-validation

## Purpose

Decide, with evidence, whether a house-engine kit is safe to offer to a project: it stays inside budget, degrades well, is accessible, is licensed and is documented well enough that a different engineer can use it.

## When to use

Use when a kit built from an adopted effect study or extracted by `skill:web-technique-to-skill` is proposed for the house engine, and again when its dependencies or API change.

## When not to use

Do not use to approve a client site; that is the [launch-readiness checklist](../../methods/quality/launch-readiness-checklist.md). Do not use to compare options; that is `skill:3w-labs-benchmark`. Validation is not approval of creative fit: each project still chooses the kit for its concept.

## Inputs

- The kit: repository path, version, public API and README.
- The technique card or benchmark it came from, if any.
- A demo page that uses the kit with neutral content.
- Dependency list with versions and licences.

## Dependencies

Read [web standards](../../methods/quality/web-standards.md) (Core Web Vitals, weight, WebGL and 3D budgets, accessibility, devices and browsers, motion standards), [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md), [web QA checklist](../../methods/quality/web-qa-checklist.md) and [IP and licensing](../../business/legal/ip-and-licensing.md). Performance runs use the tools available locally; record what ran.

## Procedure

1. Confirm scope: what the kit promises, its inputs and its stated limits. A kit without a written API or README fails here.
2. Licence check: list every dependency and asset with licence. Copyleft or unknown licences block validation for client use.
3. Budget run on the reference mid-range phone and desktop: frame rate (60 fps target), long tasks, transferred bytes added (the kit must leave the page inside ≤ 2 MB before first interaction), CLS added, draw calls and texture memory for 3D. At least five runs; report medians.
4. Degradation: force low pixel ratio, throttled CPU, WebGL off and `prefers-reduced-motion: reduce`. Each must give meaningful content, never a blank or broken state.
5. Accessibility: keyboard reach, visible focus, no trapped scroll, text alternatives for meaningful visuals, no flashing above WCAG 2.2 thresholds.
6. Browser matrix from the web standards: record pass, fail or not tested per browser and device.
7. Integration: install the kit into a clean fixture from its README only. Note every undocumented step.
8. Write the validation record (Output) with one verdict. A second engineer reviews the evidence; the maker does not validate their own kit.

## Evidence requirements

Each result cites tool, version, device, browser and date, or is marked not tested. Budget numbers are lab measurements and are labelled as such; field data does not exist for a kit.

## Output

```markdown
# Engine validation: {{kit}} v{{version}}

**Validator:** {{name, not the maker}} · **Date:** {{date}}
**Verdict:** {{validated | validated with conditions | not validated}}

| Check | Result | Evidence | Condition or fix |
| --- | --- | --- | --- |
| API and README | | | |
| Licences | | | |
| Performance budget (D-0023) | | | |
| Degradation and reduced motion | | | |
| Accessibility | | | |
| Browser and device matrix | | | |
| Clean install from README | | | |

## Conditions of use
## Re-validation trigger
```

## Quality checks

- Every budget figure has run count, device and tool.
- Reduced-motion and no-WebGL states were observed, not assumed.
- Licences are listed for all dependencies and assets.
- The validator is not the kit's maker.
- Conditions of use are specific enough to enforce in a project.

## Failure conditions

Stop and return "not validated" when the kit cannot be installed from its README, when a licence is unknown, or when it breaks the budget with no documented degradation. Do not soften a failed check into a condition.

## Human review

The Engineering lead accepts the verdict; the founder approves adding a kit to the house-engine index. Projects still record kit use and any budget exception in their `decisions.md`.

## Example

**Fictional example.** A fictional scroll-linked text reveal kit passes budget on desktop and phone, but its reduced-motion state hides the last line of text. Verdict: not validated. Fix: render the final text state when motion is reduced; re-run step 4 only.
