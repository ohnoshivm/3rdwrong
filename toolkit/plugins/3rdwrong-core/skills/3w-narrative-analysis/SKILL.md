---
name: 3w-narrative-analysis
description: Analyse the stories a brand, its founders and its audience already tell — origin, heritage, cultural and customer narratives — from sourced material, and test whether the identity's intended narrative is coherent, honest and culturally sound. Use in Strategy before positioning and concept work; do not use for competitor messaging maps or for writing brand copy.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-narrative-analysis

## Purpose

Find the load-bearing stories behind a brand from evidence, separate them from wishful framing, and give Strategy and Design a narrative the identity can carry truthfully.

## When to use

Use in identity phases 01 Discovery to 03 Strategy when founder interviews, heritage material, customer reviews or cultural sources contain stories that could shape the idea: an origin, a craft lineage, a place, a turning point, a promise to customers.

## When not to use

Do not use to map competitors' messaging or category clichés; use `skill:category-narrative-mapper`. Do not use to write taglines or copy; that is verbal identity. Do not use on fiction; for plot and character structure use `agency:academic-narratologist`.

## Inputs

- Source material with provenance: interview notes, founder writing, archives, reviews, press, cultural references.
- The discovery synthesis from `skill:3w-brand-discovery`, if it exists.
- The market, languages and cultures the identity must work in.

## Dependencies

[Tool card](../../toolkit/cards/strategy/culture-behaviour/skill--3w-narrative-analysis.md) records routing, invocation and independent checks.

Read [01 Discovery](../../methods/identity-engagement/01-discovery.md), [03 Strategy](../../methods/identity-engagement/03-strategy.md), the [perception-to-identity map](../../methods/perception-to-identity-map.md) and [creative guardrails](../../methods/creative-guardrails.md). Use `agency:academic-historian` to verify heritage or period claims and `agency:academic-anthropologist` or `agency:specialized-cultural-intelligence-strategist` for cultural meaning.

## Procedure

1. **Inventory stories.** List each story found, who tells it, where (source and date) and to whom.
2. **Structure each story.** Record the actors, the starting situation, the tension or change, the turning point, the resolution and the value it implies. Note the teller's point of view.
3. **Check truth.** Mark each element Documented (supported by source), Interpretation, Hypothesis or Unknown. Heritage, provenance and "first/only" claims need independent verification.
4. **Compare tellers.** Where founder, customer and press versions differ, record the difference; it is often the most useful finding.
5. **Cultural reading.** Note symbols, references or framings whose meaning changes across the target cultures and languages; route doubts to the cultural specialists.
6. **Test candidate narratives.** For each story that could anchor the identity, ask: is it true, is it the client's own, does it serve the audience's job, can a visual and verbal system carry it, and would it still hold in five years?
7. **Recommend.** Name one primary narrative and supporting stories, or report that no story is strong enough yet and what evidence would change that.
8. A reviewer other than the analyst checks sources and claims before the strategy owner uses the result.

## Evidence requirements

Quote sources briefly with location and date. Customer stories come from real material, never invented personas. Claims about heritage, firsts or awards need documentary support.

## Output

```markdown
# Narrative analysis: {{project codename}}

## Story inventory
| Story | Teller | Source, date | Structure (tension → turn → value) | Label |
| --- | --- | --- | --- | --- |

## Differences between tellers
## Cultural notes
## Candidate anchor narratives
| Narrative | True? | Owned? | Serves audience? | Carriable? | Durable? |
| --- | --- | --- | --- | --- | --- |

## Recommendation and unknowns
```

## Quality checks

- Every story has a source and teller.
- Truth labels are applied element by element, not to the whole story.
- Heritage and "first/only" claims are verified or marked Unknown.
- Cultural readings flagged for specialist review where uncertain.
- The recommendation states what would change it.

## Failure conditions

Stop when there is no source material beyond the brief, or when a central claim cannot be verified and the client asks to publish it as fact. Report the gap rather than polishing an unsupported story.

## Human review

The strategy owner decides what enters the strategy; the founder approves strategy; the client confirms facts about their own history.

## Example

**Fictional example.** Stillsoil Atelier's founder tells an origin in a grandparent's pottery; reviews instead praise the quiet ritual of use. The analysis marks the lineage Unknown (no documents yet), finds the ritual story consistent across customers, and recommends "objects for slow daily ritual" as the anchor while the lineage is verified.
