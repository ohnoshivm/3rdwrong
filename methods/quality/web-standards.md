---
title: Web craft standards
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Web craft standards

The measurable bar for every Digital Experience build. External thresholds are
cited; studio budgets are **Hypothesis** starting values, confirmed or
replaced with explicit numbers at the stage 04 prototype and recorded in the
project's `qa/README.md`. Award-level craft never waives these standards.

## Purpose

Give Design, Engineering and the client one shared definition of "good
enough to launch": performance, accessibility, compatibility, motion, search,
privacy, security and content handover.

## When it applies

Every website, campaign site and interactive experience the studio delivers,
from the stage 04 prototype onwards. A project may tighten a standard; loosening
one needs a founder-approved exception in the project's `decisions.md`.

## Roles

- **Engineering** (platform-performance, engineering-qa-security): owns
  measurement and the technical standards.
- **Design** (design-qa, experience-design): owns visual, motion and
  accessibility design standards.
- **Founder:** approves exceptions. **Client `C1`:** accepts the budgets at
  DX-04 and the results at DX-08.

## Core Web Vitals

Targets for the "good" threshold, measured at the 75th percentile of page
loads, segmented by mobile and desktop
([web.dev: Web Vitals](https://web.dev/articles/vitals)).

| Metric | Target | Source |
| --- | --- | --- |
| Largest Contentful Paint (LCP) | ≤ 2.5 s | [web.dev: LCP](https://web.dev/articles/lcp) |
| Interaction to Next Paint (INP) | ≤ 200 ms | [web.dev: INP](https://web.dev/articles/inp) |
| Cumulative Layout Shift (CLS) | ≤ 0.1 | [web.dev: CLS](https://web.dev/articles/cls) |

- **Field first.** p75 field data from real users is the acceptance measure
  once it exists. Before launch, field values are **not verified**; say so.
- **Lab as proxy.** Before launch, measure on the reference mid-range mobile
  profile (below) with Lighthouse's default mobile throttling or equivalent,
  and record tool, version, device, network profile and date. Lab tools cannot
  measure INP; use Total Blocking Time and manual interaction tests as proxies
  and say so.

## Weight budgets

Studio starting budgets (**Hypothesis**), per page on first load,
compressed transfer:

| Budget | Content page | Experience page with 3D |
| --- | --- | --- |
| JavaScript on the critical path | ≤ 150 KB | ≤ 300 KB including the 3D runtime |
| Total transfer before first interaction | ≤ 1 MB | ≤ 3 MB, streamed progressively |
| LCP image | ≤ 200 KB, AVIF or WebP, responsive sizes | same |
| Web fonts | ≤ 2 families, subset, ≤ 100 KB initial | same |

Lazy-load everything below the fold. Video never autoplays with sound, always
has a poster frame and a muted, user-controllable player.

## WebGL and 3D budgets

Studio starting budgets (**Hypothesis**), confirmed on the reference devices at
the prototype:

| Budget | Reference mid-range mobile | Desktop |
| --- | --- | --- |
| Frame rate target | 60 fps (≈ 16.7 ms per frame) | 60 fps |
| Degrade when sustained below | 45 fps | 50 fps |
| Draw calls per frame | ≤ 100 | ≤ 300 |
| GPU texture memory | ≤ 64 MB | ≤ 256 MB |
| Device pixel ratio cap | 1.5 | 2 |

**Graceful degradation, in order:** lower the pixel ratio, reduce
post-processing, reduce geometry and texture resolution, pause off-screen
scenes, then switch to the static fallback. With WebGL unavailable or
`prefers-reduced-motion: reduce`, show meaningful static content; never a
blank canvas. Compress geometry and textures (for example Draco or meshopt,
KTX2/Basis) and stream assets after first paint.

## Accessibility

Target [WCAG 2.2](https://www.w3.org/TR/WCAG22/) level AA for the agreed
experience, with automated checks plus manual testing. Criteria that most
often fail on expressive sites:

| Area | Requirement | WCAG 2.2 |
| --- | --- | --- |
| Text contrast | 4.5:1, or 3:1 for large text | 1.4.3 (AA) |
| Non-text contrast | 3:1 for interface components and focus indicators | 1.4.11 (AA) |
| Keyboard | All functionality operable by keyboard; no traps | 2.1.1, 2.1.2 (A) |
| Focus | Visible, logical order, not hidden by sticky elements | 2.4.3 (A), 2.4.7 (AA), 2.4.11 (AA) |
| Target size | At least 24 × 24 CSS px, or adequately spaced | 2.5.8 (AA) |
| Reflow and zoom | No loss at 320 CSS px wide or 200 % text | 1.4.10, 1.4.4 (AA) |
| Moving content | Pause, stop or hide anything moving over 5 s | 2.2.2 (A) |
| Flashing | Nothing flashes more than three times per second | 2.3.1 (A) |
| Dragging | A single-pointer alternative to every drag | 2.5.7 (AA) |
| Media | Captions for prerecorded video; audio description where needed | 1.2.2 (A), 1.2.5 (AA) |
| Names and roles | Custom controls expose name, role and state | 4.1.2 (A) |

**Reduced motion is a house standard.** WCAG places motion triggered by
interaction at AAA (2.3.3); the studio adopts it for every project by honouring
the [`prefers-reduced-motion`](https://www.w3.org/TR/mediaqueries-5/#prefers-reduced-motion)
media feature with equivalent, static or cross-faded alternatives. Never claim
compliance from an automated score alone.

## Devices and browsers

Proposed default matrix; confirm against the client's analytics at DX-01.

- **Browsers:** the latest two stable versions of Chrome, Edge, Firefox and
  Safari on desktop; Safari on the latest two iOS versions; Chrome on Android;
  Samsung Internet latest.
- **Features:** use features that are Baseline widely available
  ([web.dev: Baseline](https://web.dev/baseline)) without fallback; anything
  newer needs progressive enhancement.
- **Reference devices:** one mid-range Android phone (record the model in the
  project), one iPhone at least two generations old, one tablet and one
  13–14 inch laptop.
- **Widths inspected:** 390, 834 and 1440 CSS px as standard, plus 320 for
  reflow and 1920 for large screens.

## Motion standards

- Every motion states its purpose: hierarchy, narrative, feedback or
  continuity. No purpose, no motion.
- Durations and easings come from motion tokens; no unexplained one-off values.
- Animate `transform` and `opacity`; avoid animating layout properties.
- One smooth-scroll engine at most; native scrolling, keyboard scrolling,
  anchor links and browser find keep working.
- Scroll-driven sequences never trap the user; content is reachable without
  completing the sequence.
- Reduced-motion and no-WebGL alternatives carry the same information.

## Search, metadata and social cards

Follow [Google Search Central](https://developers.google.com/search/docs/fundamentals/seo-starter-guide):

- Unique, descriptive `<title>` and meta description per page; one `<h1>`;
  `lang` set; canonical URLs; real links, not script-only navigation.
- Content in server-rendered HTML where it matters for search; no
  text-in-canvas only.
- `sitemap.xml`, `robots.txt`, 301 redirects from every retired URL, a helpful
  404 page.
- Structured data only where it truthfully applies ([Schema.org](https://schema.org/)).
- [Open Graph](https://ogp.me/) and social card tags with a designed image per
  key page; check previews in each platform's validator.

## Privacy, consent and analytics

- Collect the minimum. Prefer privacy-friendly analytics without cross-site
  tracking.
- Account for India's Digital Personal Data Protection Act, 2023 and, for
  visitors in other jurisdictions, their law (for example the GDPR); take legal
  advice. The studio does not give legal advice.
- No non-essential tracking before consent where the applicable law requires
  consent; consent is as easy to refuse as to give.
- Publish a privacy notice the client has approved; list processors and
  embedded third parties.
- Forms send only the fields needed, over HTTPS, with spam protection that
  does not exclude assistive-technology users.

## Security headers

Set and verify on production, following the
[OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/):

- `Strict-Transport-Security` with an appropriate `max-age`.
- `Content-Security-Policy`, including `frame-ancestors`; no `unsafe-inline`
  scripts without a documented reason.
- `X-Content-Type-Options: nosniff`.
- `Referrer-Policy: strict-origin-when-cross-origin` or stricter.
- `Permissions-Policy` disabling unused features.

Also: dependency audit before launch, secrets only in the host's secret store,
least-privilege accounts, and a documented recovery procedure.

## CMS and content handover

- Structured content models named in the client's language, with field help
  text and validation.
- Editor roles with least privilege; a preview that matches production.
- Image guidance: sizes, crops, alt text rules.
- Content cannot break layout: tested with the longest real titles and
  missing optional fields.
- Training on the client's own content and a written editor guide; see
  [handover and care](../handover-and-care.md#digital-handover-pack).

## Quality gate

- [ ] Budgets recorded as numbers at DX-04, with approved exceptions.
- [ ] Measurements cite tool, device, network profile and date.
- [ ] Accessibility tested manually and automatically against WCAG 2.2 AA,
      plus reduced motion.
- [ ] Matrix covered; gaps recorded.
- [ ] Security headers, consent and metadata verified on production.

## Metrics

Proposed: p75 LCP, INP and CLS 28 days after launch; budget exceptions per
project; accessibility defects found after launch.

## Failure modes

- Quoting a lab score as a field result.
- Setting budgets after the build.
- Accessibility as an end-of-project audit instead of a design input.
- A WebGL hero with no fallback content.

## Related

[Digital experience method](../digital-experience/README.md) ·
[Web QA checklist](web-qa-checklist.md) ·
[Launch-readiness checklist](launch-readiness-checklist.md) ·
[Critique protocol](critique-protocol.md)
