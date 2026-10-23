---
name: 3w-demo-publishing
description: Prepare and gate the public release of a 3RDWRONG Labs demo or open-source showcase, checking licences, third-party assets, AI disclosure, client-data exclusion, performance budget, reduced motion and accessibility before founder approval. Use when a Labs study or kit is to be published as a live demo or public repository; do not use for client launches or case studies.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-demo-publishing

## Purpose

Publish Labs work so it is lawful to share, honest about how it was made, fast and accessible, and safe to show — without exposing client material or overstating what it proves.

## When to use

Use when an effect study, benchmark or validated kit is proposed for a public demo page, a public repository or a showcase submission. Run it before `skill:publish-project-to-github` packages and pushes anything.

## When not to use

Do not use for client launches or client case studies; use the [launch-readiness checklist](../../methods/quality/launch-readiness-checklist.md) and the case-study bundle. Do not use to decide whether Labs work is good enough; that is a founder decision after review.

## Inputs

- The demo or repository, its version and the intended public location.
- The study, benchmark or validation record it comes from.
- A list of every third-party library, font, image, model and dataset used.
- Any AI tools used to make code, images or text.

## Dependencies

[Tool card](../../toolkit/cards/labs/open-source-showcase/skill--3w-demo-publishing.md) records routing, invocation and independent checks.

Read [IP and licensing](../../business/legal/ip-and-licensing.md) (open source, stock, AI-generated assets), [licensing model D-0009](../../studio/decisions/0009-licensing-model.md) and [LICENSING.md](../../LICENSING.md), [public-private boundary](../../docs/public-private-boundary.md), [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md), [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) and [web standards](../../methods/quality/web-standards.md).

## Procedure

1. **Provenance.** Confirm the work is Labs-originated. Search code, assets, commit history and screenshots for client names, codenames, client files or personal data. Any hit blocks publication.
2. **Licence.** Apply approved D-0009: MIT for original code and CC BY 4.0 for original documentation, methods and skills; reserve trademarks and brand assets, and retain third-party rights and notices. Check every dependency and asset licence is compatible; list notices to keep.
3. **Third-party assets.** Fonts must allow web embedding and redistribution in the repository, or be loaded from a permitted source. Images, models and datasets need a licence that permits public redistribution. Unknown means remove.
4. **AI disclosure.** State which parts used AI tools and how they were edited. Do not publish AI-generated material as the studio's own craft without saying so.
5. **Performance and access.** Run the demo against the D-0023 budget and the reduced-motion and no-WebGL paths; check keyboard access and text alternatives. Record numbers with tool, device and date.
6. **Description.** Write a plain README or page text: the question, the technique, the measured cost, limits, licence, credits and how to run it. No claims of audience effect or award status.
7. **Gate.** Fill the publication record (Output). A reviewer who did not build the demo checks it; the founder approves publication.
8. Hand over to `skill:publish-project-to-github` for packaging and to `agency:specialized-developer-advocate` for community follow-up.

## Evidence requirements

Licence findings cite the licence file or terms page with access date. Performance figures cite run conditions. Unknown provenance or licence is recorded as Unknown and blocks release.

## Output

```markdown
# Demo publication record: {{demo}}

**Public location:** {{URL or repository}} · **Version:** {{tag}}
**Outbound licence:** {{licence}} · **D-0009:** approved studio licensing model; record any proposed exception for founder review

| Check | Result | Evidence |
| --- | --- | --- |
| No client material or personal data | | |
| Dependency licences compatible | | |
| Fonts, images, models, datasets cleared | | |
| AI use disclosed | | |
| D-0023 budget and reduced motion | | |
| Accessibility basics | | |
| README: question, cost, limits, credits | | |

**Reviewer:** {{non-maker}} · **Founder approval:** {{pending | date}}
```

## Quality checks

- No client identifier survives in code, history, assets or captures.
- Every third-party item has a licence that allows public redistribution.
- AI use is disclosed where it occurred.
- Budget figures and the reduced-motion path are verified.
- The README states limits as plainly as results.

## Failure conditions

Stop when provenance or a licence is Unknown, when client material is found, or when the founder has not approved. Publishing cannot be undone reliably; when in doubt, do not publish.

## Human review

The reviewer checks the record; the founder approves every publication. Legal questions about licence compatibility go to a qualified adviser.

## Example

**Fictional example.** A clip-path reveal study is prepared for a public repository. The check finds a commercial font in the demo folder; it is replaced with an open-licence font and its licence file is added. Budget and reduced-motion checks pass. The record waits for founder approval before packaging.
