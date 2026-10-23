---
name: 3w-behavioural-lens
description: Apply behavioural theory to a 3RDWRONG strategy, identity or experience decision by naming the behaviour in question, mapping candidate mechanisms from cited research with their limits and replication status, and turning them into testable hypotheses with ethical guardrails. Use when a perception or behaviour claim would change a decision; do not use to profile real individuals, diagnose anyone or design manipulative patterns.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-behavioural-lens

## Purpose

Keep behavioural claims honest. The [perception-to-identity map](../../methods/perception-to-identity-map.md) requires psychology claims to carry their own cited research and context; this skill does that work and turns theory into hypotheses the studio can test, not rules it asserts.

## When to use

Use in Strategy (identity phases 02 Diagnosis and 03 Strategy; digital stage 02 Experience strategy) when a decision rests on how people notice, interpret, choose or act: for example, whether a distinctive asset aids recognition, whether a sign-up flow reduces effort, or why an audience trusts one category cue over another.

## When not to use

Do not use to analyse a named real person, to make clinical or diagnostic statements, or to build dark patterns, false urgency, hidden costs or pressure tactics. Do not use when sourced audience evidence already answers the question; use `agency:research-synthesist` for synthesis. Fictional character psychology belongs to `agency:academic-psychologist`.

## Inputs

- The decision and the behaviour that matters (who, in what context, doing what).
- Existing evidence: discovery synthesis, research notes, analytics, with sources.
- The audience and market context, including culture and language.

## Dependencies

Read the [perception-to-identity map](../../methods/perception-to-identity-map.md), [03 Strategy](../../methods/identity-engagement/03-strategy.md) and [creative guardrails](../../methods/creative-guardrails.md). Use `agency:academic-psychologist` as a specialist for deeper theory review and `agency:academic-statistician` before any quantitative test.

## Procedure

1. **State the behaviour.** One sentence: actor, context, observable action. Feelings and attitudes are recorded separately from behaviour.
2. **Collect what is known.** Separate observed behaviour (research, analytics) from stated preference and from founder belief.
3. **Map mechanisms.** For each plausible mechanism, record the named theory or finding, the primary source, the population and context it was studied in, and its known replication status or debate. If you cannot cite a source, the mechanism is Unknown, not common sense.
4. **Check fit.** Ask whether the original context transfers to this audience, culture, category and channel. Note where it does not.
5. **Write hypotheses.** Each: "If we {{change}}, {{audience}} will {{observable behaviour}} because {{mechanism}}; we would see {{signal}}." Mark each Hypothesis.
6. **Design the cheapest honest test.** A small qualitative check, a prototype task, an A/B test with adequate sample, or desk evidence. Route sample-size questions to the statistician.
7. **Ethics screen.** Reject any lever that works by deception, pressure, exploiting vulnerability or hiding information. Record what was rejected and why.
8. Hand the hypotheses to the strategy owner; a reviewer other than the author checks citations and fit.

## Evidence requirements

Every mechanism names a primary source with year; popular summaries are marked secondary. Use Documented only for what the cited study found in its context; transfer to this project is Interpretation or Hypothesis.

## Output

```markdown
# Behavioural lens: {{decision}}

**Behaviour:** {{actor, context, action}} · **Evidence held:** {{sources}}

| Mechanism | Source (primary, year) | Studied in | Replication / debate | Fit here | Label |
| --- | --- | --- | --- | --- | --- |

## Hypotheses and tests
1. If … then … because … — test: … — signal: …

## Rejected levers (ethics)
## Unknowns
```

## Quality checks

- Behaviour is observable and separate from attitudes.
- Every mechanism has a primary source and a context note.
- Contested or poorly replicated findings are flagged as such.
- No lever relies on deception, pressure or exploiting vulnerability.
- No real individual is profiled.

## Failure conditions

Stop when the decision is not stated, when no source can be found for a load-bearing mechanism, or when the request asks for manipulation. Report Unknown rather than filling the gap with folk psychology.

## Human review

The strategy owner decides which hypotheses enter the brief; the founder approves strategy. Research with people follows the studio's research and consent practice.

## Example

**Fictional example.** For Stillsoil Atelier, the question is whether a consistent glaze-colour band on labels helps returning buyers find the range on a crowded shelf. The lens maps distinctive-asset and visual-search research, notes that the cited studies used Western supermarket settings, and proposes a five-person shelf-finding task with printed mock-ups as the test. Status: Hypothesis.
