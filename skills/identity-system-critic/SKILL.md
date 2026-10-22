---
name: identity-system-critic
description: Critique an identity concept or system against strategy, underlying idea, distinctiveness, repeatability and craft. Use before route selection or visual sign-off; formative review of a clearly labelled draft strategy is allowed, but this skill never approves work.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-22
  version: 0.2.0
---
# identity-system-critic

## Purpose

Find consequential strengths, gaps and risks in an identity route or system. Review the idea separately from style, then inspect whether the rules survive the agreed applications.

## When to use

Use during concept, identity or validation when a route description, design artefact or application examples can be inspected. A formative critique may use a provisional strategy if its status and limits are explicit.

## When not to use

Do not use to invent strategy, choose a route for a human, certify accessibility or production, or claim audience response from a design file. Do not deliver a final verdict when required material is missing.

## Inputs

- Approved strategy and criteria, or a draft strategy explicitly marked formative.
- Concept route and the decision requested.
- Current artefacts and representative applications at stated sizes and contexts.
- Category audit and source links if distinctiveness is assessed.
- Type, colour, motion, language, licence and production constraints where relevant.

## Dependencies

Read [critique protocol](../../methods/quality/critique-protocol.md), [phase 04 Concept](../../methods/identity-engagement/04-concept.md), [phase 07 Validation](../../methods/identity-engagement/07-validation.md), and [design critique template](../../templates/critique/design-critique.md). Read [identity system testing](../../methods/quality/identity-system-testing.md) when application evidence is supplied. No external paid tools are required.

## Procedure

1. State the decision, phase, artefact version and strategy status. If strategy is a draft, mark the review formative.
2. Inventory what was inspected: route words, sketches, files, applications, dimensions and sources. Mark missing items Unknown.
3. Review the work in four modes: **concept** (idea and strategy fit), **formal** (hierarchy, type, composition and craft), **audience** (intended interpretation versus observed response), and **implementation** (system behaviour, accessibility, rights and production). Mark each unavailable mode Not testable; if no audience test exists, response remains Unknown.
4. Review the idea by explaining it without visual adjectives. If only style remains, say the concept is not yet inspectable.
5. Review distinctiveness against linked category examples. Separate entry codes from repeated conventions. If no category sample is supplied, mark distinctiveness **Unknown / Not testable**; do not infer white space or audience uniqueness from visual inspection.
6. Review system repeatability across supplied applications, sizes, content and scripts. If one mock-up exists, list unrun system checks.
7. Review craft: hierarchy, legibility, spacing, contrast, type support, asset quality and relevant production constraints.
8. Record findings with severity, exact evidence label, source, consequence, next check and owner. Distinguish defects from optional suggestions. Do not average judgements into a taste score.
   A severity describes consequence, not how strongly the reviewer feels about a choice.
   If the same issue affects several applications, list each affected use or cite the test set.
9. Identify blockers, major and minor findings, observations and unknowns. Recommend a next step with trade-offs, not an approval.
10. Choose exactly one written verdict: “Strong enough to advance”, “Promising but structurally unresolved”, “Technically sound but conceptually weak”, “Distinctive but commercially inappropriate”, or “Rejected, with explicit reasons”. Then state the next design action, owner and evidence needed.
11. State the human decision needed and which checks require a specialist, user or vendor.

## Evidence requirements

Use **Documented**, **Interpretation**, **Hypothesis** and **Unknown** exactly. Cite the strategy, asset, test or source. Visual inspection documents what is present; it cannot document memorability, preference, cultural meaning or sales. A fictional critique stays inside the fiction. Do not claim contrast, script, licence or production checks unless actually run.

## Output

Return this exact Markdown structure.

```markdown
# Identity system critique: {{project and route}}

**Status:** {{formative | review}}
**Decision requested:** {{decision}}
**Strategy:** {{approved source and version | draft source and limit}}
**Inspected:** {{assets, applications, dimensions, sources}}

## Summary
{{short recommendation; no approval claim}}

**Verdict:** {{one exact verdict from the protocol}}

## Findings
| Mode / lens | Finding | Evidence label and source | Severity | Consequence | Next check / owner |
| --- | --- | --- | --- | --- | --- |

## Idea without style adjectives
{{one sentence; or why it cannot be described}}

## Distinctiveness and category evidence
{{sample and link, or Unknown / Not testable}}

## System evidence and gaps
{{tested applications and untested items}}

## Unknowns and unsupported claims
- {{unknown or unsupported response claim}}

## Human decision needed
- {{approver, decision, artefact version}}

## Next design action
- {{specific action, owner, evidence required}}
```

## Quality checks

- Strategy status and critique scope are stated.
- Concept, formal, audience and implementation modes are each covered or marked Not testable.
- Strategy, idea, distinctiveness, system and craft each get a finding or Not testable note; the output has a dedicated distinctiveness field.
- Idea and visual style are distinguished.
- Severity matches consequence, not taste.
- Findings have source, next check and owner.
- Unrun access and production checks remain unverified.
- Recommendation cannot be mistaken for approval.
- A missing artefact is described as untested, not as a failed design.
- A critique suggestion is not silently added to the acceptance criteria.

- The review states which parts of the artefact could not be inspected.
- No single mock-up is treated as proof of a complete identity system.
- Category statements cite a sample or are marked Unknown.
- Proposed fixes become next checks when evidence is incomplete.
- Strategy fit is distinguished from aesthetic preference.
- Human approval remains a separate recorded action.
- The critique does not imply legal, accessibility or production certification.
- Exactly one permitted written verdict appears; no averaged taste score is used.
- The critique ends with a concrete next design action or a named missing input.

## Failure conditions

Stop and ask when no strategy or decision question is supplied, unless the user accepts a formative critique of a draft strategy. Stop if the artefact is inaccessible or too incomplete. Ask for links before category claims. If asked to approve, certify or report user response without evidence, return only a bounded critique and explain the missing decision or test.

## Human review

A human designer checks findings against the artefact and may reject a recommendation with rationale. The authorised client or founder makes route and visual approval decisions. Accessibility specialists, fluent language reviewers or vendors confirm checks outside supplied evidence. This skill never approves work.

## Example

**Fictional example.** A synthetic route says “returning the jar completes the story” and shows a loop on one label. Strategy fit is **Interpretation** from the fictional strategy; system behaviour beyond that label is **Unknown**; visible hierarchy is **Documented** within the fictional artefact. Request a line-sheet and small-size test before recommending development.
