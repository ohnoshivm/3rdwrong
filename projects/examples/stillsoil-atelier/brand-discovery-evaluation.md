---
title: Brand discovery skill evaluation — Stillsoil Atelier
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-22
review_every_days: 180
---
# Brand discovery skill evaluation — Stillsoil Atelier

**Fictional example for testing methods and skills. Not a client.**

## Skill and version

The first pass used `brand-discovery` 0.1.0 and prompted version 0.1.1. The
blueprint integration added the perception-to-identity map and small-sample
rule in version 0.2.0; the output below was rerun against that version.

## Test request and inputs

**Request:** “Run brand-discovery on this fictional brief. Produce an evidence-led synthesis for the next strategy conversation. Do not invent research or make real-market claims.”

Inputs were the [fictional client brief](brief.md), including B1 (business and
scope), F1 (founder statements) and R1–R4 (synthetic participant notes). No
external category sources, actual assets or real participants were supplied.

## Procedure followed

1. Restated the decision as preparing evidence and questions for strategy, before strategy approval.
2. Inventoried B1, F1 and R1–R4 with role, source file, date, method and fictional limits.
3. Extracted eight claims into a source-linked ledger without inventing quotations.
4. Applied the exact evidence labels and repeated the fictional scope beside every Documented observation.
5. Kept founder intent, synthetic participant notes, brief facts and interpretations separate; did not count repeated notes as independent corroboration.
6. Compared tensions around tone, variant clarity, name prominence and instruction legibility.
7. Mapped the commercial trigger, audience understanding, intended meaning, creative question, proposed test and measurement limits.
8. Treated the four synthetic notes as within-fiction inputs only, not a real or representative sample. The five-to-eight interview rule was not triggered because no real interviews were supplied.
9. Asked strategy questions rather than resolving them as recommendations; kept real audience segments Unknown.
10. Listed market preference, product efficacy, demand and sales claims as unsupported.
11. Returned the required schema with the perception map and marked the deliverable draft and fictional.

## Output review

The resulting [discovery synthesis](discovery-synthesis.md) traces every
observation to a source ID and includes the six-step perception-to-identity
map. The fictional boundary is clear and no real Indian market facts are
asserted. The synthesis helps frame a strategy question but is not a research
report or positioning approval.

## What worked

- The source ledger made founder preference distinct from fictional participant evidence.
- Tensions were interpreted without turning four invented notes into a market pattern.
- Unknowns led to concrete questions about size, language, retailer intent and evidence.
- The output blocked efficacy, sales and representativeness claims.

## Gaps and observed failure

The first pass placed “fictional scenario only” in the overall source boundary
and table limits, but the skill did not require it beside every Documented
row. A copied row could look like real research. The blueprint revision then
required the map, but the old output schema did not provide a place to show
where evidence ended and measurement remained unknown.

## Skill changes made

After the first pass, updated `skills/brand-discovery/SKILL.md` from 0.1.0 to
0.1.1: procedure and quality checks now require the fictional boundary beside
each Documented row and prevent duplicate notes from counting as independent
corroboration. For version 0.2.0, integrated the perception map, stated that
five to eight interviews generate hypotheses only, and added the six-field map
to the output schema. The rerun confirmed that the map can be completed while
keeping real audience response and outcomes Unknown.

## Remaining limits and next evaluation

This run used synthetic notes in one file and did not test external-source
citations, contradictory real interviews or a brief with no research. Evaluate
those failure cases before treating the skill as dependable. No human approval
or client outcome is represented here.
