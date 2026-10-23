---
name: 3w-image-production
description: Run the 3RDWRONG image production workflow from approved art direction to delivered files — image brief, sourcing route (commission, shoot, stock, AI, own), rights and AI-consent check before production, selection, retouch, export and rights register. Use for brand and project imagery; do not use to set art direction or to approve images for release.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-image-production

## Purpose

Produce the images an approved art direction calls for, with every file traceable to a brief, a source and a right to use it.

## When to use

Use after art direction is approved (identity phases 05–06; digital stage 03 onwards) when photographs, illustrations, renders or AI-generated images are needed for a deliverable or the studio's own channels.

## When not to use

Do not use to invent the image direction; that is art direction (`skill:ceos-art-direction`) and image-generation direction (`anthropic-skills:gpt-image-2-director`). Do not use to pass images for release; that is `skill:3w-image-qa`. Never use AI-generated material in a mark, logo or any element the client must own exclusively.

## Inputs

- Approved art direction and the list of placements (page, channel, format, size).
- Budget and schedule notes from Production (money stays in the vault).
- The client's written AI consent where AI-generated material might reach a final deliverable (D-0023).
- People, places or products to appear, with consent status.

## Dependencies

Read [IP and licensing](../../business/legal/ip-and-licensing.md) (stock and third-party content; AI-generated assets), [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) AI use, [03 Art direction and design system](../../methods/digital-experience/03-art-direction-and-design-system.md), [web standards](../../methods/quality/web-standards.md#weight-budgets) image budgets and [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md). Generation tools: `skill:imagegen` (lead for brand image assets).

## Procedure

1. **Image brief.** For each placement: purpose in the concept, subject, composition, light and material notes from the art direction, aspect ratios, sizes and the alt-text intent.
2. **Choose the route** per image: commission or shoot, licensed stock, AI generation, or studio-made. Record why.
3. **Clear before making.** Commission and shoots: contract with usage and assignment terms, model and property releases. Stock: licence scope (media, territory, term, sensitive use). AI: written client consent for finals, tool terms on output ownership and training, no client confidential data or personal data in prompts. No route proceeds with an open rights question.
4. **Produce.** Shoot, generate or source against the brief. For AI, keep prompts, settings, tool, version and date; real people are never generated or altered to look like an identifiable person without their consent.
5. **Select** with the art director against the brief, not against novelty.
6. **Retouch and edit**, logging material changes (composites, removals, AI edits).
7. **Export** per placement: format (AVIF or WebP for web), responsive sizes, colour space, the LCP image ≤ 200 KB, print files at the vendor's specification.
8. **Register.** Add every file to the rights register (Output) and hand the set to `skill:3w-image-qa`.

## Evidence requirements

Every image has a source record: creator or tool, licence or contract, releases, AI disclosure and edit log. Missing items are recorded as Unknown and block release.

## Output

```markdown
# Image production: {{codename}} — {{set}}

| File | Placement | Route | Creator / tool, version | Licence or contract | Releases | AI used (consent ref) | Edits | Export spec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Open rights questions
## Handed to image QA: {{date}}
```

## Quality checks

- Every placement has a brief that cites the art direction.
- Rights and consent were cleared before production, not after.
- AI use is recorded per file and backed by written client consent for finals.
- No AI material in marks or exclusive elements.
- Exports meet the web image budget and vendor specifications.

## Failure conditions

Stop when art direction is not approved, when a rights or consent question is open, or when the client has not consented to AI material in finals. Choose another route rather than proceeding.

## Human review

The art director approves selection; the founder approves the rights section; release is decided after image QA.

## Example

**Fictional example.** Stillsoil Atelier needs six product images and one hero. The products are shot by a commissioned photographer under an assignment contract; the hero background texture is AI-generated after the client's written consent, with the prompt log stored. All seven files enter the register and go to image QA.
