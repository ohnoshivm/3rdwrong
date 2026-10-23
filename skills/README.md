# Skills

These ten Agent Skills are **experimental**. Their outputs are drafts for human review; none can approve strategy, design, rights or release.

| Skill | Purpose | Phase | Inputs | Output |
| --- | --- | --- | --- | --- |
| [3w-brand-discovery](3w-brand-discovery/SKILL.md) | Source-grounded synthesis | 01 Discovery | Brief, notes and source inventory | Evidence-led discovery synthesis |
| [3w-category-code-audit](3w-category-code-audit/SKILL.md) | Count visible category conventions | 02 Diagnosis | Bounded category and at least eight linked examples | Code table, tallies and hypotheses |
| [3w-creative-direction](3w-creative-direction/SKILL.md) | Develop distinct ideas from approved strategy | 04 Concept | Signed strategy and criteria | At least three routes and trade-offs |
| [3w-identity-system-critic](3w-identity-system-critic/SKILL.md) | Critique idea, system and craft | 04 or 07 | Strategy, route, artefacts and scope | Evidence-labelled findings |
| [3w-brand-consistency-qa](3w-brand-consistency-qa/SKILL.md) | Check assets against approved rules | 06 System / 08 Delivery | Approved guideline and asset set | Pass, fail and not-testable checks |
| [3w-taste-graph](3w-taste-graph/SKILL.md) | Reference pack before creative output; capture references | Any creative output | Brief, or a link/screenshot to save | Do/don't pack with exemplars, or a captured node |
| [3w-mark-exploration](3w-mark-exploration/SKILL.md) | Mark from idea to tested production vector | 05 Identity / 07 Validation | Chosen route, name, scripts, category audit, media | Routes, optical-correction and size/medium test record, deliverable list |
| [3w-typography-system](3w-typography-system/SKILL.md) | Brand type selection, licensing, scripts and web fonts | 05 Identity / 06 System | Chosen route, scripts, media, content strings | Shortlist, licence and script tables, hierarchy, font budget |
| [3w-colour-system](3w-colour-system/SKILL.md) | Perception-aware colour roles, contrast, print and tokens | 05 Identity / 06 System / 07 Validation | Chosen route, colour direction, applications, printer | Roles, computed contrast and colour-vision tables, print and token spec |
| [3w-composition-system](3w-composition-system/SKILL.md) | Brand-wide composition across formats | 05 Identity / 06 System | Draft mark, type and colour; applications with dimensions | Invariants, grids, format rules, test record, templates |

## Identity-craft order

The four identity-craft skills feed each other: run mark exploration and typography first (the wordmark and type share stroke contrast and spacing), then colour, then composition, which uses all three. Iterate when a later skill exposes a defect in an earlier one. The [Stillsoil Atelier test runs](../projects/examples/README.md) show the hand-offs. Each records craft decisions for a human; the founder or design lead decides type, mark, colour and composition.

## Discovery and use

The repository links the skills through relative symlinks in `.claude/skills/`. Claude Code discovers the `SKILL.md` files from those paths. Read each skill's dependencies before use; no external paid tool is required.

## Evaluation process

For each evaluation, save the request, exact input set, skill version, actual output, observed strengths, gaps and resulting changes using the [skill evaluation template](../templates/learning/skill-evaluation.md). Keep fictional tests visibly fictional. One run is not evidence of reliability; test varied briefs and failure cases, then have a human review the outputs.

## Proposing changes

Use a focused skill-improvement record or change proposal. Cite the observed failure or correction, name the procedure or check that changes, and include a counterexample if the change could overconstrain another case. Do not promote `experimental` status automatically. The founder reviews status changes and versions after evaluating the effect.
