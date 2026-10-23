---
title: Stitched Full Page Capture
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:stitched-full-page-capture
department: design
sub_department: design-qa
job: visual-qa-browser
role: specialist
trigger: "When the approved scope specifically requires verifying rendered web touchpoints, interactions, responsive states, or screenshots."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/stitched-full-page-capture/SKILL.md
invoke: "/stitched-full-page-capture"
pairs_with: [skill:ceos-visual-audit, skill:reviewing-interface-quality, design-steward:verify]
---
# Stitched Full Page Capture

Stitched Full Page Capture is a 3RDWRONG design QA specialist for visual-qa-browser, activated when the approved scope specifically requires verifying rendered web touchpoints, interactions, responsive states, or screenshots.

## What it does

- Repairs unreliable full-page captures on lazy-loaded, scroll-animated, Framer, WebGL/canvas or reveal-heavy pages.
- Warms the real page with one top-to-bottom scroll, captures settled viewport slices with overlap, and stitches them vertically.
- Derives section crops from the stitched image and validates it against representative stills, video and motion frames.
- Rejects blank or incomplete native full-page captures as the source of truth.

## When to use

- When the approved scope specifically requires verifying rendered web touchpoints, interactions, responsive states, or screenshots. In practice: during Phase 07 Visual Inspection when the named rendered states can be captured.

## When not to use

- Do not treat a one-shot native fullPage screenshot or scroll video as the source of truth; use the stitched viewport image for section evidence.

## Inputs it needs

- The actual page URL, representative still/video evidence and target viewport.
- Browser and image-stitch tooling available to capture settled viewport slices.

## How to run it

1. Open the real page URL and warm lazy/reveal content by scrolling top to bottom once.
2. Return to the top; capture settled viewport slices with overlap, waiting about two seconds after each stop.
3. Stitch the slices and derive section crops from that image, not from a native fullPage capture.
4. Inspect dimensions and lower-page coverage, then compare with still/video evidence; reject any blank or mismatched candidate.

```text
Use /stitched-full-page-capture on {{actual page URL}}. Warm the page, then capture settled viewport slices with overlap and stitch them into a full-page image. Create section crops from the stitched image. Inspect the saved image and validate it against {{representative still/video}}; report missing sections or capture limits.
```

## What good output looks like

- The stitched image includes lower-page lazy content and has expected wide/tall dimensions.
- Section crops are generated from the accepted stitched source and align with the full image.
- The capture agrees with representative still/video evidence; failures remain rejected or unverified.

## Quality checks

- [ ] Settled viewport slices cover the whole page, including lazy-loaded lower content.
- [ ] Stitched dimensions and section-crop boundaries are checked.
- [ ] Accepted capture agrees with representative still/video evidence; mismatches remain rejected.

## Pairs with

- Work with `skill:ceos-visual-audit`, `skill:reviewing-interface-quality`, `design-steward:verify` at the visual-qa-browser handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- A source or code inspection alone does not prove rendered appearance; without browser evidence mark visual QA unverified.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `fetch`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
