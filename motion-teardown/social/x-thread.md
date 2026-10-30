---
title: "X thread"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# X thread

13 posts. Each post is under 280 characters. No hashtags or emojis. Replace `<ARTICLE_URL>` and `<REPO_URL>` before posting.

---

**1/13** [attach: media/v01-side-by-side.mp4]

We screen-recorded 12 seconds of oryzo.ai, a site by Lusion, and rebuilt its hero and first scroll section in crimson and white in about six hours, with AI agents.

Left: theirs. Right: ours.

The method, one lesson per post:

---

## 2/13

Video tells you what happens. Code tells you how.

Our plan from the video said the edge glow was triggered by hovering the hand. The site's code turns it on between 4,950 and 5,400 px of scroll. Hover only moves the fingers.

---

**3/13** [attach: media/f03-choreography.png]

Each section reduces scroll to one number:

r = 1 + (scrollY − sectionTop) / viewportHeight

Every effect is fit(r, a, b, from, to). No timeline, no tweens. Everything reverses on scroll-up because state is a function of scroll.

---

## 4/13

Stagger is a formula. Each letter gets its own slice of the block's window, starting at about 0.3 × its position and lasting 0.4–0.6 of it.

The slices overlap, so "Powered by AI*" sharpens as one movement, not a row of separate ones.

---

## 5/13

Smoothing lives in one place: the scroll engine.

Each wheel event is clamped to 200 px, eased with a coefficient of 12 and rounded to whole pixels. Every effect reads that one value, so every effect shares the same physics.

---

**6/13** [attach: media/f01-rebuild-hero.png]

The photoreal desk is a flat photo plus 7 cut-out props, each with its own shadow and a wobble driven by mouse speed. Only the coaster is 3D.

The blur sits only under the copy, growing with the cube of a rounded mask.

---

**7/13** [attach: media/f10-hand-sequence.jpg]

The hand has 36 bones, skinned on the GPU, with baked frames 71→115 played by scroll between 3,056 and 4,950 px.

The hover never checks whether your cursor is on the hand. Four mouse-height bands and a spring move the fingers.

---

## 8/13

Read the code first.

One agent spent about 50 minutes stuck behind the site's preloader. Another, reading the bundle, found why in about 25: the loader waits for loaded weight to exactly equal total weight, and has no error handler.

---

**9/13** [attach: media/f04-orchestration.png]

Split agents by evidence type, not by page section.

A read the code, with no browser. B captured the page at every 90 px of scroll. C took fonts, colours, network and performance. Each brief named the files it owned.

---

## 10/13

Two build agents worked on one page at once because of one file: a contract defining the state the HTML layer hands to WebGL every frame.

We wrote it into the spec before either agent started. Neither could change it.

---

## 11/13

Four agent runs died early: a quota, a DNS error, a lost stream, a usage limit.

None cost more than a few minutes, because every brief said "append progress to disk after every step", and every relaunch began with a resume note.

---

## 12/13

Match effort to the task. Low for file operations, high for research and building.

The one agent we ran at maximum effort read for about 40 minutes before writing its first file. High would have done.

---

## 13/13

The human made four decisions, in one prompt: colours, props, font, copy. The agents did the rest, on subscriptions and free tiers we already had.

The full guide and all 11 briefs: <ARTICLE_URL>
The repo: <REPO_URL>

Try it on one site you admire.
