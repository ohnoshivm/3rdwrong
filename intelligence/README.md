# Creative intelligence

This library turns research into explicit design questions, reusable principles and original exercises. It is not a collection of images to imitate. Creator intent, our interpretation, untested applications and missing evidence stay separate. A reference study does not approve a method or select 3RDWRONGS's own visual direction.

## Folder map

- `projects/` — four substantial identity-system studies, with source limits and proposed exercises.
- `agencies/` — a cross-project study of DIA's kinetic and programmable practice.
- `psychology/` — evidence-graded perception and memory notes with prohibited overclaims.
- `principles/` — three proposed cross-study principles with conditions and rejection tests.
- [Research queue](research-queue.md) — verified leads awaiting deep study and an unstudied watchlist.
- [Resources](resources.md) — weighted source library; each input names a proposed output.
- [Research templates](../templates/README.md) — the wider template catalogue; research-specific forms are indexed below.

## Entry index

Evidence strength describes the scope of support, not a ranking of design quality. “Primary” means creator or client material, not an independent effectiveness test. Review dates record this library's review, not the reference project's date.

| Entry | Type | Evidence strength | Last reviewed |
| --- | --- | --- | --- |
| [Experimental Jetset — Whitney](projects/experimental-jetset-whitney.md) | reference-study | Client + studio primary; strong attribution and process account; no isolated outcome evidence | 2026-10-22 |
| [PORTO ROCHA — MASP](projects/porto-rocha-masp.md) | reference-study | Studio primary + visible secondary heading; full review paywalled; no independent effectiveness study | 2026-10-22 |
| [COLLINS — Spotify](projects/collins-spotify.md) | reference-study | Studio primary + contemporary design reporting; no causal commercial inference | 2026-10-22 |
| [Studio Dumbar — DEMO](projects/studio-dumbar-demo.md) | reference-study | Three edition pages; documented mechanisms and evolution; creator-reported outcomes | 2026-10-22 |
| [DIA — kinetic identity](agencies/dia-studio.md) | research | Three primary project pages; collaboration credits; incomplete technical specifications | 2026-10-22 |
| [Distinctive assets and memory](psychology/distinctive-assets-and-memory.md) | research | Journal abstract/appendix preview + institutional communication + practitioner sources | 2026-10-22 |
| [Processing fluency and distinctiveness](psychology/processing-fluency-and-distinctiveness.md) | research | Peer-reviewed theoretical review + NN/g practitioner account; no modern replication audit | 2026-10-22 |
| [Define rules before variants](principles/rules-before-variants.md) | principle, proposed | Synthesis of Whitney + DEMO; local test unrun | 2026-10-22 |
| [Let content shape identity](principles/content-is-a-design-input.md) | principle, proposed | Synthesis of Whitney + Spotify; local test unrun | 2026-10-22 |
| [Design for the next operator](principles/handover-is-part-of-the-concept.md) | principle, proposed | Synthesis of Whitney + DIA; local test unrun | 2026-10-22 |
| [Research queue](research-queue.md) | research | Four primary pages verify queued leads; deep studies pending | 2026-10-22 |
| [Resources](resources.md) | research | 27 weighted entries; includes clearly limited book listings and video metadata | 2026-10-22 |

## Template index

All seven templates are proposed question sets. They contain placeholders deliberately; completed studies must not retain them. Their own `type: template` metadata is distinct from the resulting document type.

| Template | Result type | Evidence requirement | Last reviewed |
| --- | --- | --- | --- |
| [Agency study](../templates/research/agency-study.md) | research | Compare two or three attributable projects; separate house-method inference | 2026-10-22 |
| [Project study](../templates/research/project-study.md) | reference-study | Opened sources, intelligence card, decision rules and original exercise | 2026-10-22 |
| [Psychology research](../templates/research/psychology-research.md) | research | Source design, sample, uncertainty, replication limits and myth check | 2026-10-22 |
| [Visual system analysis](../templates/research/visual-system-analysis.md) | research | Documented grammar versus inferred patterns and exceptions | 2026-10-22 |
| [Typography analysis](../templates/research/typography-analysis.md) | research | Foundry provenance, licence scope, scripts and hierarchy | 2026-10-22 |
| [Motion system analysis](../templates/research/motion-system-analysis.md) | research | Purpose, behaviour, timing evidence and static alternatives | 2026-10-22 |
| [Design principle](../templates/research/design-principle.md) | principle | At least two studies, conditional application and falsification | 2026-10-22 |

## Evidence legend

- **Documented** — stated in a cited primary or credible secondary source. A studio's claim remains attributed; the label does not make it independent proof.
- **Interpretation** — our reasoned reading of documented material. Give the reasoning and a plausible alternative.
- **Hypothesis** — plausible but untested. Name a comparison and a result that would reject it.
- **Unknown** — absent from reviewed material or inaccessible. Specify which; do not fill the gap with plausible production lore.

The psychology notes add [practice triage tiers](psychology/distinctive-assets-and-memory.md#evidence-tiers-for-practice): research-supported, context-dependent and reject-without-evidence. Those tiers complement the four labels and never substitute for checking a particular source.

## Add a study

1. Open a [research-study issue](../.github/ISSUE_TEMPLATE/research-study.yml) or a [design-reference issue](../.github/ISSUE_TEMPLATE/design-reference.yml). State the question and the decision research could change.
2. Open the original creator/client material before writing. Record failed access and attribution conflicts. Use the matching template; for a project, run the command below from the repository root.
3. Set the new record's `type: reference-study`, `status: reference`, `review_every_days: 365` and real frontmatter `sources`. Each source needs title, HTTPS URL and access date; add author/publication date when known. Do not claim a full book was read from a publisher listing.
4. Replace all placeholders, complete the intelligence card and preserve evidence labels. The card's reviewed flag concerns actual review; applied_to_original_work stays false until linked work exists. Neither changes approval status.
5. Propose an original exercise or application. Link any later work and critique instead of silently implying that study has produced demonstrated capability.
6. Run the checks below and submit a PR using the [contribution process](../CONTRIBUTING.md). A reviewer should assess source support, transfer limits and originality; merge does not make a principle approved.

```bash
uv run python scripts/new_doc.py templates/research/project-study.md intelligence/projects/<slug>.md
```

```bash
npx --yes markdownlint-cli2 "intelligence/**/*.md" "templates/research/*.md"
uv run python scripts/validate.py
```

## Quality bar

A study is acceptable when the question, attribution and evidence can be reconstructed without trust in the author. Specific requirements:

- Every factual claim has an opened supporting source, with frontmatter metadata and an inline or Sources link. Dates and attribution conflicts remain visible.
- Documented facts occupy clearly named sections; interpretations, proposed mechanisms and hypotheses are labelled. Portfolio outcomes never become proof of design causality.
- The account explains rules, invariants, variables and exceptions to the extent sources permit. Missing numerical specifications, tools, fees and team details remain Unknown.
- Transfer identifies what a small studio and the real client could use, what does not transfer and how to test it. Consult [initial ICP](../studio/initial-icp.md) for the current market hypothesis; do not treat the blueprint's examples as an approved market.
- Each substantial study includes an Exercise. Proposed exercises are not completed work, client evidence or approved methods. The reference studies are 120–250 lines to encourage depth without becoming archives.
- No protected imagery or assets are committed. Link originals; describe visuals in original language. Limit quotations to two short attributed excerpts per study, each at most 25 words, and no more than 25 quoted words from any one source.
- Psychological notes distinguish empirical studies, theoretical reviews, institutional communication and practitioner material. Effect sizes and replication claims require reviewed evidence; include Claims we must not make.
- Principles remain proposed and link at least two studies plus opened external sources. They state when they fail and a project test that could reject them.

## Review cadence

Studies and library records explicitly use `review_every_days: 365`; all current reviews are dated 2026-10-22, next due 2027-10-22. Recheck earlier when a source moves, an attribution is challenged, a study is used in a consequential decision or new research materially changes its interpretation.

At review, reopen sources, revise the access limit, inspect any claimed application and update the date only after doing the work. Preserve the review log. An annual date is a maintenance trigger, not evidence that the underlying claim remains true.
