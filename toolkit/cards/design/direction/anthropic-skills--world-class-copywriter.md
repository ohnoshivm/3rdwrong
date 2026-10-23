---
title: World-Class Copywriter
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: anthropic-skills:world-class-copywriter
department: design
sub_department: direction
job: verbal-identity
role: lead
trigger: ""
kind: plugin-skill
availability: claude-managed
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/world-class-copywriter/SKILL.md
invoke: "/world-class-copywriter skill (Claude-managed)"
pairs_with: [skill:brand-language-codifier, agent:creative-writer, skill:3w-creative-direction]
---

# World-Class Copywriter

A copywriting lead for brand copy and persuasive writing across channels. For 3RDWRONG, this is the lead tool for verbal identity.

## What it does

- Defines an activation sequence: consult the skill’s brain, audience, tension, idea, emotion and format resources before drafting.
- Rejects the first idea, scores candidates, and filters copy through ten quality gates.
- Supports headlines, brand ads, landing pages, social, video, email and other listed formats.
- Returns a concept, headline, optional subhead, body, tagline, CTA and an explanation of the mechanism.

## When to use

- Phase 05 Identity Craft, when brand copy or a verbal expression needs a developed persuasive concept.
- When the requested output is brand copy or a listed persuasive format, and the source materials can be supplied.

## When not to use

- A durable voice and naming canon; use `skill:brand-language-codifier`.
- Strategy or claims adjudication; use the appropriate strategy/claims tool and keep evidence separate.

## Inputs it needs

- Brand, audience, actual product/service facts and copy brief.
- Brand-owned voice samples and supporting source material; the skill requires audience research and supporting brain files.

## How to run it

1. Invoke `/world-class-copywriter` in Claude Code.
2. Follow the mandatory activation sequence in its skill file and provide verified inputs.
3. Review claims and fit against 3RDWRONG voice; have a human approve the final copy.

```text
Use /world-class-copywriter skill (Claude-managed). Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- The skill’s stated output format, with a specific concept and CTA.
- Distinct concepts rather than tone-only variants; unsupported claims remain out.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:brand-language-codifier` — upstream context or hand-off.
- `agent:creative-writer` — downstream review or delivery.
- `skill:3w-creative-direction` — downstream review or delivery.

## Limits and cautions

- Claude-managed; confirm it is enabled in the account before relying on it.
- The skill references a large companion library; capability details beyond SKILL.md are Not documented here.
- Do not import unsupported audience effects or results; keep the maker separate from final review.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
