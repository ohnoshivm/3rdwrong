---
name: 3w-effect-study
description: Run a bounded Labs effect study that re-authors a parked effect recipe or a captured reference technique as an original 3RDWRONG technique card, measured against the D-0023 performance budget with a complete reduced-motion path. Use for non-client effect research; do not use to ship an effect into a client build or to copy a reference.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-effect-study

## Purpose

Turn a visual or interaction effect into studio knowledge: what the technique is, what it costs, when it serves a concept and how it degrades. The output is an original technique card and a small study build, not a reusable preset.

## When to use

Use in Labs when a parked effect recipe (registry job `effect-studies`), a Taste Graph capture or a design question names a technique worth understanding before a project needs it. Use before a technique is proposed for the house engine.

## When not to use

Do not use inside a client build; client motion follows [06 Motion, 3D and interaction](../../methods/digital-experience/06-motion-3d-and-interaction.md). Do not reproduce a reference's assets, code, sequence or composition. Do not use to justify motion the concept does not need.

## Inputs

- The study question: which technique, and which design problem it might serve.
- The source: parked recipe id (read its own file through `toolkit/sources/materials.json`) or a reference with link and access date.
- Target devices from the [web standards](../../methods/quality/web-standards.md#devices-and-browsers).
- An empty study folder under `experiments/<study-name>/` started from the [experiment template](../../templates/learning/experiment.md).

## Dependencies

Read the [Labs department](../../studio/departments/labs.md) operating contract, [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) budget, [web standards](../../methods/quality/web-standards.md) (WebGL budgets, motion standards), [creative guardrails](../../methods/creative-guardrails.md) and the [experiments guide](../../experiments/README.md). Measurement uses browser performance tools available on the machine; if none run, mark measurements Unknown.

## Procedure

1. Write the question and the hypothesis in one sentence each. State the concept roles the technique could serve (hierarchy, narrative, feedback or continuity); no role, stop.
2. Read the source recipe or reference. Record what is technique (the underlying method: a shader idea, a masking approach, an easing structure) and what is expression (assets, palette, sequence, layout). Only technique may carry forward.
3. Re-author from first principles in the study folder: new code, neutral placeholder geometry and type, no copied assets. Note any third-party library and its licence.
4. Build the reduced-motion and no-WebGL path first; it must carry the same information as a static or minimal-motion state.
5. Measure on the reference mid-range mobile profile and on desktop: frame time, dropped frames, draw calls, texture memory, transferred bytes, main-thread blocking. Record tool, version, device and date.
6. Compare with the D-0023 budget: 60 fps target, ≤ 2 MB before first interaction, CLS ≤ 0.1, no INP regression. List each degradation step that keeps it inside budget.
7. Write the technique card (Output). Mark every claim Documented, Interpretation, Hypothesis or Unknown.
8. Ask a second person or agent instance to review originality (`skill:audit-reference-originality`) and the measurements. The maker does not review.
9. Record the decision: adopt for house-engine validation, iterate, or drop.

## Evidence requirements

Measurements cite tool, version, device, network profile and date. Claims about audience effect are Hypothesis unless a study supports them. A screen recording or numbers are evidence; "feels smooth" is not.

## Output

```markdown
# Technique card: {{technique name}}

**Study:** experiments/{{study}} · **Source:** {{recipe id or reference, accessed date}} · **Status:** experimental
**Concept roles it can serve:** {{hierarchy | narrative | feedback | continuity}}

## Technique (original re-authoring)
{{method in plain words; what was deliberately not carried over}}

## Cost on reference devices
| Device | fps (median / p5) | Draw calls | Texture MB | Transfer KB | Notes |
| --- | --- | --- | --- | --- | --- |

## Budget fit (D-0023)
{{inside | inside with degradations listed | outside}}

## Degradation ladder and reduced-motion path
1. {{step}} …

## Risks and licence notes
## Decision: {{adopt for validation | iterate | drop}} — reviewer: {{name}}
```

## Quality checks

- The question names a design problem, not "make something cool".
- No asset, palette, layout or sequence from the source survives.
- The reduced-motion path exists and conveys the same information.
- Measurements are on named devices with tool versions.
- The rejected own-identity look (D-0006) is not the default study styling.
- Review is by someone other than the maker.

## Failure conditions

Stop when the source cannot be read, when the technique cannot be separated from a reference's expression, or when the effect cannot meet the budget even with degradation. Report the result as drop; a dropped study is a valid outcome.

## Human review

The founder or the Engineering lead decides whether a technique enters house-engine validation. Use in client work needs a concept-specific choice, independent originality review and project performance evidence.

## Example

**Fictional example.** A study re-authors the parked `skill:masked-reveal` idea as a clip-path reveal driven by scroll position, built with system type and grey blocks. On the reference phone it holds 60 fps with no WebGL; reduced motion shows the final state immediately. Decision: adopt for validation; the reviewer notes the timing must come from project motion tokens.
