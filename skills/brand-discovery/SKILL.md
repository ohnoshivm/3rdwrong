---
name: brand-discovery
description: Synthesise supplied brand discovery material into traceable evidence, tensions, unknowns and strategy questions before strategy approval. Use when a project needs a source-grounded discovery summary; do not invent research or claim a representative market view.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-22
  version: 0.2.0
---
# brand-discovery

## Purpose

Turn supplied briefs, research notes and brand materials into a useful discovery synthesis. Preserve the source boundary so a designer can see which facts support a decision and which questions remain open. This skill does not approve strategy or replace primary research.

## When to use

Use before diagnosis or strategy when a project has source material to organise. It can work with a brief alone, but must label unsupported audience or market claims as hypotheses or unknowns. Use it to prepare focused research questions when evidence is incomplete.

## When not to use

Do not fabricate interviews, quantify market demand, infer consumer behaviour from aesthetics, or write a finished positioning without approval. Do not use this skill as a substitute for consent, research design, source verification or legal review.

## Inputs

- A client or project brief with the decision to support.
- Research notes, interviews, source links, existing assets or a clear statement that these are absent.
- Participant role, method, date and consent limits where research is supplied.
- Known business constraints, deliverables and decision roles.
- Optional category audit and existing positioning, with their status stated.

## Dependencies

Read [phase 01 Discovery](../../methods/identity-engagement/01-discovery.md), [perception-to-identity map](../../methods/perception-to-identity-map.md), the [critique protocol](../../methods/quality/critique-protocol.md), [client brief template](../../templates/briefs/client-brief.md) and [research intake template](../../templates/learning/research-intake.md). Read [studio positioning](../../studio/positioning.md) and [ICP hypothesis](../../studio/initial-icp.md) only when those claims affect the assignment. No external paid tools are required.

## Procedure

1. Restate the decision, project stage, scope and intended audience from the supplied brief. Flag conflicts between documents.
2. Inventory every source: identifier, source type, date, author or role, consent or use limit, and location. An unattributed claim is not a source.
3. Extract material statements into a claim ledger. Keep quotes short and traceable; preserve the speaker's role and context.
4. Assign each statement one exact evidence label: **Documented**, **Interpretation**, **Hypothesis** or **Unknown**. A fictional note is Documented only inside that fiction.
5. When the source boundary is fictional, write “within the fictional scenario” in the scope or limit for every Documented observation, so it cannot be mistaken for real participant or market evidence.
6. Separate founder intent, observed audience behaviour, secondary research, existing asset evidence and your own interpretation. Do not merge them into “customer truth”.
7. Compare sources for agreement, contradiction and missing voices. State sample and method limits next to any synthesis.
   Distinguish independent sources from repeated notes about the same participant.
   Treat silence as evidence only when the prompt or observation covered that topic.
8. Identify the business trigger, audience task or tension, current identity problem and practical constraints only where inputs support them.
9. Use the perception-to-identity map to connect the commercial problem, audience understanding, intended strategic meaning, creative question, recognition/experience checks and later measurement. Mark untested links Unknown or Hypothesis; do not imply that identity work causes a commercial result.
10. Treat five to eight interviews as hypothesis-generating only. State sample, recruitment and method limits; do not describe a small convenience sample as representative.
11. Write strategy questions that could change a decision. Label proposed answers as hypotheses; do not resolve unknowns silently.
12. Check unsupported market, cultural, efficacy, behavioural or commercial claims. Remove them, source them, or relabel them.
13. Deliver the schema below. If sources are absent, return an intake gap report, not a fabricated synthesis.

## Evidence requirements

Every material observation points to a supplied source ID or a working HTTPS source link. For web sources, record title and access date. Use the four evidence labels exactly. Cite factual claims near the claim, preserve sample and date, and separate interpretation from its documented input. Never present fictional inputs as real interviews or findings.

The map is an organising aid, not validated causal science. An observed brand
problem does not establish that a particular identity treatment will improve
recognition, desirability or sales.

## Output

Return this exact Markdown structure. Mark an unavailable section “Not supplied” and explain why.

```markdown
# Discovery synthesis: {{project}}

**Status:** {{draft | proposed | formative}}
**Decision supported:** {{decision}}
**Source boundary:** {{real sources | fictional scenario | brief only}}

## Inputs and limits
| ID | Source and date | Role or source type | Method or scope | Limits |
| --- | --- | --- | --- | --- |

## Evidence and observations
| ID | Observation | Evidence label | Source ID | Scope and limit |
| --- | --- | --- | --- | --- |

## Tensions and interpretations
| Tension | Interpretation | Sources | Confidence or limit |
| --- | --- | --- | --- |

## Perception-to-identity map
| Commercial problem | Audience understanding | Intended strategic meaning | Creative question | Recognition / experience test | Measurement and limits |
| --- | --- | --- | --- | --- | --- |
| {{supported input or Unknown}} | {{evidence and sample limit}} | {{intent, not response}} | {{question, not solution}} | {{proposed test or Unknown}} | {{what is measurable later; no outcome promise}} |

## Working audience and trigger
{{supported statement; label each hypothesis}}

## Unknowns and risks
- {{unknown}} — why it matters; next check.

## Questions for diagnosis and strategy
1. {{question that could change a decision}}

## Claims not to make
- {{unsupported audience, market, efficacy or outcome claim}}

## Human review needed
- {{fact check, access check or strategy decision}}
```

## Quality checks

- A second reader can trace each material statement to a source or label.
- Founder intent is not described as observed consumer behaviour.
- No sample is called representative without a suitable research design.
- Five to eight interviews, if supplied, are described as a way to generate hypotheses, not representative evidence.
- The commercial problem, audience, intended meaning and validation question are linked without promising an outcome.
- Contradictions and missing voices are visible, not averaged away.
- Unknowns include a next question rather than an invented answer.
- Fiction and real-world evidence are clearly separated.
- Personal details are minimised; short quotes cannot identify a participant.
- A repeated statement is not counted as independent corroboration.
- The output helps a specific next decision and does not claim approval.

- The summary does not exceed the scope of materials reviewed.
- A real-world claim is never justified by a fictional source.

## Failure conditions

Stop and ask for missing source attribution, scope or participant permission when the requested conclusion depends on it. If a brief is all that exists, provide only a brief-based intake and state that research synthesis is not possible. Stop if asked to invent quotes, hide a source limitation, claim market validation or turn a hypothesis into an approved position.

## Human review

A human checks factual extraction, source permissions, confidentiality and fair representation. The authorised decision-maker approves strategy separately in phase 03. This skill never marks a fact, strategy or interpretation approved.

## Example

**Fictional example.** A synthetic brief says a founder wants a fragrance-free bar to feel “considered, not clinical”; a fictional participant says the variant should be easy to identify. Label each observation **Documented** and state the limit “within the fictional scenario”. A possible tension is **Interpretation**; broader category preference is **Unknown** until tested. Ask how the label reads at shelf distance; do not claim consumers prefer minimal packaging.
