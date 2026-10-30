---
title: "Worksheet: apply the method to your own site"
type: template
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
template_for: guide
---

# Worksheet: apply the method to your own site

Copy this file, fill it in as you go, and keep it in your study folder. Each section points to the [playbook](../playbook/README.md) stage where you use it. Grey example rows come from the oryzo.ai (by [Lusion](https://oryzo.ai)) study; delete them.

---

## 1. The site

| Field | Your entry | Example |
| --- | --- | --- |
| Site name and URL | | oryzo.ai |
| Makers (agency, studio, people) | | Lusion |
| Why this site | | A hero and first scroll that feel like one object |
| The part you want to study | | The hero and the first scroll section |
| Date studied | | 30 October 2026 |

## 2. Scope and legal check *(playbook stage 2)*

**Scope.** Write it so a stranger could apply it.

| | Your entry | Example |
| --- | --- | --- |
| Start point | | Scroll 0 (hero at rest) |
| End point | | The end of the `#ai` section, 8,100 px at 1440×900 |
| Viewports | | Desktop 1440×900, DPR 2; mobile 390×844, DPR 3, hero only |
| Out of scope | | Later sections, nav destinations, other pages |
| Total page height vs scope | | 49,966 px vs 8,100 px |

**Legal and rights check.** Tick each one, or write why not.

- [ ] I read the site's terms of use.
- [ ] I will make only normal browser requests: no crawling, no load testing.
- [ ] Captured assets (models, textures, shaders, source) go in a git-ignored folder and are never published.
- [ ] Fonts: I know which are licensed, and I have a free substitute for the rebuild.
- [ ] I will write my own code and make my own art for anything I publish.
- [ ] I will describe techniques in my words, with measured numbers as facts.
- [ ] Credit text is drafted (section 9).
- [ ] I considered contacting the makers before publishing.
- [ ] Anything on the page that tells a reader to do something is data, not an instruction, and my agents have been told so.

## 3. Recording plan *(stage 1)*

| Item | Your plan |
| --- | --- |
| Tool and resolution | |
| One slow, monotonic scroll, top to bottom | |
| A second take for hover and interaction | |
| Cursor visible | |
| Site visible in the first second | |
| Length | |

## 4. Effect inventory *(stages 1, 3 and 4)*

One row per effect. Start from the video (hypotheses), then update from code and data.

| ID | Effect | When (time, frame) | Hypothesis from video | Scrubbed or triggered | Scalar and window (px, `r`) | Easing | Evidence tag | Status | Level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *E7* | *"Powered by AI*" letters sharpen* | *1.67 s* | *per-letter blur-in, scrubbed* | *scrubbed* | *3,150 → 4,500 px* | *expoOut* | *[code] [measured]* | *answered* | *L1* |
| *E9* | *Edge glow* | *2.67 s* | *triggered by hover* | *scrubbed (corrected)* | *on 4,950 → 5,400; off 6,750 → 7,200* | *sine in* | *[code] [measured]* | *answered* | *L3* |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

Level column: L1 (scroll and type), L2 (fixed stage, baked animation, masked blur), L3 (skinning, springs, post chain), or "beyond" if the [ladder](../tracks/dev/level-ladder.md) does not cover it yet.

## 5. Evidence log *(stages 3 and 4)*

Append only. One line per claim you rely on.

| Date | Claim | Tag | Source (file, line, capture) | Check done | Resolved |
| --- | --- | --- | --- | --- | --- |
| *30 Oct* | *Glow follows scroll, not hover* | *[code]* | *notes/A-code.md, section (f)* | *B's glow channel against scroll* | *yes: video was wrong* |
| | | | | | |
| | | | | | |

Evidence order: **code > measured data > video**.

## 6. Decisions *(stage 5)*

Ask the human only the ones that change what gets built and are theirs to make. Put the recommended option first.

| Decision | Options (recommended first) | Why it is theirs | Answer | Date |
| --- | --- | --- | --- | --- |
| *Colours* | *Crimson + white · White-dominant · Red-dominant* | *Taste* | *Crimson + white* | *30 Oct* |
| *Typeface* | *Free substitute · My licensed kit* | *Licence* | *Free substitute* | *30 Oct* |
| | | | | |
| | | | | |

## 7. Build split *(stages 6 and 7)*

| Agent | Layer | Owns (paths) | Model and effort | Fallback (and its effort) | Brief file |
| --- | --- | --- | --- | --- | --- |
| *DOM* | *Scroll, text, layout* | *`src/core`, `src/dom`, `src/styles`* | *{{ }}* | *{{ }}* | |
| *GL* | *Renderer, scene, post* | *`src/gl`* | *{{ }}* | *{{ }}* | |
| *IMG* | *Generated images* | *`public/gen`, `scripts/gen`* | *{{ }}* | *{{ }}* | |
| | | | | | |

- Contract file frozen? [ ] &nbsp; Ready-timeout stated (we used 10 s)? [ ] &nbsp; Placeholders for missing assets? [ ] &nbsp; DOM-only fallback if GL fails? [ ]
- Ledger file per agent? [ ] &nbsp; Resume-note template ready? [ ]

## 8. Acceptance shots *(stage 8)*

Pick positions at the start. Use the same scripted `scrollTo` for both pages.

| Position (px) | Viewport | Original image | Rebuild image | Score (greyscale SSIM) | Intentional difference or defect | OK |
| --- | --- | --- | --- | --- | --- | --- |
| *0* | *1440×900* | | | | | |
| *2,250* | *1440×900* | | | | | |
| *5,130* | *1440×900* | | | | | |
| | | | | | | |
| | | | | | | |

Also record: console clean over a full scroll [ ] · p95 frame time ____ ms on ____ [ ] · CLS ____ [ ] · missing-asset check [ ] · reduced-motion check [ ] · mobile check [ ] · the person who asked approved on ____ [ ]

## 9. Credit

Draft the credit before you publish anything.

```text
Studied: {{site}} by {{makers}}, {{url}}.
What we measured and read: {{one line}}.
What we wrote ourselves: {{code, art, copy}}.
What we did not use or publish: their code, shaders, models, textures.
Fonts: {{font used and its licence}}.
```

Our own example, for the Oryzo study: *"A study of oryzo.ai by Lusion. We measured its behaviour and read its shipped code to understand the mechanisms, then wrote our own code and generated our own images. We do not publish their code, models or textures."*

---

When you finish, keep the corrections table from your reconcile stage. It is the most useful page for your next study.
