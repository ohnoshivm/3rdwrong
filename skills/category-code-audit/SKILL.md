---
name: category-code-audit
description: Audit visible conventions in linked category and competitor identities before positioning or concept work. Use when a team needs a traceable comparison across logo form, type, colour, imagery, language and layout; do not use without source links.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-22
  version: 0.1.0
---
# category-code-audit

## Purpose

Make category conventions inspectable. The audit helps a team decide which codes aid recognition, which are repeated without a reason, and which candidate spaces deserve testing. It does not prove consumer response or market opportunity.

## When to use

Use during diagnosis or concept development when category distinction matters and a source-linked sample can be assembled. Use it before mood-board selection so references are coded systematically rather than selected only for taste.

## When not to use

Do not use without verifiable source links or to claim a category-wide pattern from a few famous brands. Do not copy competitor assets, infer sales performance from visual style, or label a visual difference as consumer preference.

## Inputs

- A bounded category, geography, channel and observation date.
- At least **8 distinct examples**, each with a working source link.
- A strategy question the audit should inform.
- Coding dimensions: logo form, typography, colour, imagery, language and layout.
- Inclusion and exclusion rules; disclose convenience or search bias.

## Dependencies

Use [inspiration discovery sources](../../taste/discovery-sources.md) as the first-stop reference source for visual and interactive inspiration.

Read [phase 02 Diagnosis](../../methods/identity-engagement/02-diagnosis.md), the [critique protocol](../../methods/quality/critique-protocol.md) and [concept route template](../../templates/identity-systems/concept-route.md). If the audit informs the initial audience, read the [ICP hypothesis](../../studio/initial-icp.md). No paid market database, crawler or image library is required.

## Procedure

1. Restate the strategy question and define category boundaries, geography, channels and observation date. Narrow a boundary that is too broad.
2. Collect at least eight distinct examples. Prefer primary brand sites or owned channels; record URL, page title and access date for every example.
   Check that a parent brand and a product line are not counted as two independent brands.
   Save the relevant page or screenshot reference when the live source may change.
3. Note selection method and bias, such as search query, directory or supplied list. If fewer than eight verifiable examples remain, stop the pattern tally and report a preliminary sample only.
4. Code each example across logo form, typography, colour, imagery, language and layout. Describe what is visible before interpreting its role.
5. Tally recurring conventions by dimension. State counts and denominator; do not replace counts with “many”.
6. Separate **category entry codes** that may aid recognition or comprehension from **clichés** repeated without a clear reason for this brand. A convention is not automatically a cliché.
7. Identify candidate white space only as **Hypothesis**. Explain which sample pattern suggests it and what test could disconfirm it.
8. Link every interpretation to examples. Exclude brand, performance and audience-response claims unless independently sourced.
9. Produce the schema, limitations and next test. Never copy a logo, wording or distinctive composition into a proposed route.

## Evidence requirements

Each example needs brand name, URL, source title or page and access date. Mark directly visible details **Documented**. Meanings are **Interpretation** unless the brand documents them. Pattern generalisations and candidate white space are **Hypothesis** with a named test. Use **Unknown** when intent or performance is not documented.

## Output

Return this exact Markdown structure.

```markdown
# Category code audit: {{category and scope}}

**Status:** {{preliminary | complete for stated sample}}
**Strategy question:** {{question}}
**Sample:** {{N; geography; channel; date range}}
**Selection method and bias:** {{method and omissions}}

## Source register
| ID | Brand | Page | URL | Accessed | Use limits |
| --- | --- | --- | --- | --- | --- |

## Coding table
| ID | Logo form | Type | Colour | Imagery | Language | Layout |
| --- | --- | --- | --- | --- | --- | --- |

## Conventions and counts
| Dimension | Convention | Count / N | Evidence IDs | Label |
| --- | --- | --- | --- | --- |

## Entry codes worth testing
- {{code}} — role; evidence IDs.

## Clichés to challenge
- {{code without a strategic reason}} — evidence IDs; limits.

## Candidate white space
- {{hypothesis}} — sample pattern; disconfirming test.

## Unknowns and next checks
- {{unknown}} — source or participant needed.

## Claims not supported by this audit
- {{performance or audience claim}}
```

## Quality checks

- At least eight linked examples are coded before a tally is called complete.
- Every sample has an access date and selection method.
- All six dimensions are considered; unavailable evidence is Unknown.
- Tallies include denominator and source IDs.
- Entry codes and clichés are explained separately.
- White space remains a hypothesis with a disconfirming test.
- Each counted convention has a coding definition another reviewer can apply.
- Excluded or inaccessible examples are listed so the denominator can be checked.
- Visual inspection is not described as proof of preference or sales.

- Visual details and interpretations are not merged in one uncited sentence.
- Candidate white space is not presented as an ownable position.
- Another reviewer can code a new example from the stated definitions.

## Failure conditions

Stop and ask for links or permission to inspect sources when they are missing, inaccessible or unattributed. With fewer than eight verifiable examples, provide a preliminary audit only, without category-wide tallies or white-space conclusions. Stop if asked to invent a source, hide sample bias, copy work or claim performance from visual evidence.

## Human review

A human checks category boundaries, sample relevance, coding and interpretation before concepts use the audit. A strategist decides which codes matter to the approved positioning. This skill does not approve a strategy or route.

## Example

**Fictional example.** In eight linked pages supplied for a fictional soap category, seven show wordmarks and six use high-contrast product names. These counts are **Documented for this sample**. “Numbered variants may be less common” remains a **Hypothesis** until the sample supports it and a comprehension test checks usefulness.
