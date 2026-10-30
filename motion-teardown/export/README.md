---
title: Publishing Motion Teardown
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Publishing Motion Teardown

Edit [ARTICLE.md](../ARTICLE.md), then rebuild the lightweight Markdown exports from the repository root:

```sh
python3 motion-teardown/export/build_exports.py
```

[substack.md](substack.md) and [medium.md](medium.md) turn tables into lists, expand publication links to the studio repository and mark each included image with its filename and caption. Upload the images directly from [media](../media/README.md). HTML previews and duplicate upload kits are excluded to keep GitHub small.

Original-site screenshots and side-by-side comparisons are not included. Side-by-side comparisons with the original appear in the Substack edition; see the live site at [https://oryzo.ai](https://oryzo.ai). Rebuild renders retain their geometry credit. The optional comparison video is not included.

Review rights, captions, sources and links before publishing elsewhere. Follow the root [licensing guide](../../LICENSING.md) and [publication rules](../../docs/public-private-boundary.md). The director reviews the branch before anything goes public.
