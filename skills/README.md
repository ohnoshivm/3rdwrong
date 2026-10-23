# Skills

These eighteen Agent Skills are **experimental**. Their outputs are drafts for human review; none can approve strategy, design, rights or release.

| Skill | Purpose | Phase | Inputs | Output |
| --- | --- | --- | --- | --- |
| [3w-brand-discovery](3w-brand-discovery/SKILL.md) | Source-grounded synthesis | 01 Discovery | Brief, notes and source inventory | Evidence-led discovery synthesis |
| [3w-category-code-audit](3w-category-code-audit/SKILL.md) | Count visible category conventions | 02 Diagnosis | Bounded category and at least eight linked examples | Code table, tallies and hypotheses |
| [3w-creative-direction](3w-creative-direction/SKILL.md) | Develop distinct ideas from approved strategy | 04 Concept | Signed strategy and criteria | At least three routes and trade-offs |
| [3w-identity-system-critic](3w-identity-system-critic/SKILL.md) | Critique idea, system and craft | 04 or 07 | Strategy, route, artefacts and scope | Evidence-labelled findings |
| [3w-brand-consistency-qa](3w-brand-consistency-qa/SKILL.md) | Check assets against approved rules | 06 System / 08 Delivery | Approved guideline and asset set | Pass, fail and not-testable checks |
| [3w-taste-graph](3w-taste-graph/SKILL.md) | Reference pack before creative output; capture references | Any creative output | Brief, or a link/screenshot to save | Do/don't pack with exemplars, or a captured node |
| [3w-behavioural-lens](3w-behavioural-lens/SKILL.md) | Cited behavioural mechanisms as testable hypotheses | 02–03 Strategy | Decision, behaviour, sourced evidence | Mechanism table, hypotheses, rejected levers |
| [3w-narrative-analysis](3w-narrative-analysis/SKILL.md) | Sourced brand, founder and cultural stories | 01–03 Strategy | Source material with provenance | Story inventory and anchor recommendation |
| [3w-image-production](3w-image-production/SKILL.md) | Brief, route, rights and AI consent, export | After art direction | Approved art direction, placements, consents | Image production register |
| [3w-image-qa](3w-image-qa/SKILL.md) | Independent image release gate | Before handover or publication | Files, rights register, release scope | Pass, fail and not-testable checks |
| [3w-care-retention](3w-care-retention/SKILL.md) | Warranty closure, care plans, check-ins, once-only asks | L7–L9 | Handover record, care log | Care and retention record |
| [3w-awards-submission](3w-awards-submission/SKILL.md) | Free award entries with fit and permission | After L7 / L9 | Live work, permission, official criteria | Award entry record and results log |
| [3w-prospect-qualification](3w-prospect-qualification/SKILL.md) | Contact, watch or exclude before outbound | L0 outbound | Sourced account research | Qualification record |
| [3w-reply-triage](3w-reply-triage/SKILL.md) | Classify and answer outbound replies | L0 outbound | Replies, suppression list | Triage table and suppression updates |
| [3w-effect-study](3w-effect-study/SKILL.md) | Re-author an effect as an original technique card | Labs | Study question, source recipe | Technique card with budget fit |
| [3w-labs-benchmark](3w-labs-benchmark/SKILL.md) | Reproducible comparison for a decision | Labs | Options, fixture, threshold | Benchmark record |
| [3w-engine-validation](3w-engine-validation/SKILL.md) | Gate a house-engine kit before project use | Labs | Kit, README, demo, licences | Validation record with one verdict |
| [3w-demo-publishing](3w-demo-publishing/SKILL.md) | Pre-release gate for public Labs demos | Labs | Demo, third-party list, AI use | Publication record for founder approval |

## Discovery and use

The repository links the skills through relative symlinks in `.claude/skills/`. Claude Code discovers the `SKILL.md` files from those paths. Read each skill's dependencies before use; no external paid tool is required.

## Evaluation process

For each evaluation, save the request, exact input set, skill version, actual output, observed strengths, gaps and resulting changes using the [skill evaluation template](../templates/learning/skill-evaluation.md). Keep fictional tests visibly fictional. One run is not evidence of reliability; test varied briefs and failure cases, then have a human review the outputs.

## Proposing changes

Use a focused skill-improvement record or change proposal. Cite the observed failure or correction, name the procedure or check that changes, and include a counterexample if the change could overconstrain another case. Do not promote `experimental` status automatically. The founder reviews status changes and versions after evaluating the effect.
