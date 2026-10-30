---
title: "The level ladder"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# The level ladder

Three levels, each a lab you finish before the next. Every level is a slice of what oryzo.ai (by Lusion) does, rebuilt from our own measurements and written fresh. The ladder is ordered by what depends on what: L2 needs the scroll number from L1, and L3 needs the render targets from L2.

| | Level 1: scroll and type | Level 2: a fixed stage | Level 3: a character and a post chain |
| --- | --- | --- | --- |
| **Lab** | [L1: scroll is a number](lab-l1-scroll-is-a-number.md) | [L2: a fixed stage under the page](lab-l2-fixed-stage.md) | [L3: a skinned character, springs and a post chain](lab-l3-character-and-post.md) |
| **No 3D?** | No 3D | One scene, one baked camera move | Skinned mesh, post passes |
| **You learn** | Scroll engine; section progress `r`; `fit()`; stagger windows; SplitText-style reveals | Fixed WebGL canvas; render to target; one baked animation played by scroll; the masked "blur under the text" pass | GPU skinning; spring-driven hover bands; edge-glow pass; bloom and grade; performance |
| **You build** | A pinned headline that arrives and leaves by scroll alone | A fixed canvas, an orbit camera scrubbed by scroll, a frosted region under the copy | A baked rig played by scroll, a perking finger, a scroll-driven rim glow, a graded frame at 60 fps |
| **Dependencies** | A bundler and TypeScript | + three.js | + three.js |
| **Time** | About 2 hours | About half a day | Two to three days from nothing |
| **Done when** | Scrolling up replays everything backwards; `scrollTo` lands exactly | Glass stays aligned with text at any size; camera is a pure function of scroll | The glow is a function of scroll only; p95 frame time within budget |

## Where each level sits in the case

Numbers are for a 1440×900 viewport, measured on the live site, with `y` in pixels of scroll. They show where each level's technique appears in the real first section.

| Effect on oryzo.ai | y range (px) | Level |
| --- | --- | --- |
| Hero copy exits (letters fade and blur in a stagger) | 0 → 450 | L1 |
| "ISN'T JUST A COASTER." arrives, then leaves | in 450 → 1,125; out 2,475 → 3,150 | L1 |
| "Powered by AI*" letters slide, fade and un-blur | in 3,150 → 4,500 | L1 |
| Caption and "Try to hover hand" arrive | 4,050 → 4,950, then 4,950 → 5,400 | L1 |
| Hero blurs under the copy, with a 5% zoom-out on exit | 0 → 450 | L2 |
| Coaster and camera follow baked paths | 0 → 4,950 | L2 |
| Hand animation plays (baked frames 71 to 115) | 3,056 → 4,950 | L3 |
| Fingers react to the pointer; edge glow on | glow on 4,950 → 5,400, off 6,750 → 7,200 | L3 |
| Hand fades out | 7,200 → 8,100 | L3 |
| Post chain: glow, bloom (5 levels), grade, card blur | throughout | L3 |

For the whole choreography on one chart, see [media/f03-choreography.png](../../media/f03-choreography.png).

## How to climb

- **Do the exercises.** The snippets run, but the exercises make you change them. Skipping them is how people end up with code they cannot adapt.
- **Do the "you're done when" checks.** They are pass or fail, written so that you can check them without anyone else.
- **Keep one shared `math.ts`.** Every later lab imports `fit`, `clamp`, `ease` and `lerp` from L1.
- **Test your own shaders.** The labs were tested by rendering each shader into a small canvas and reading pixels back. Do the same for yours, because a shader that compiles can still draw nothing.

## The deep dives

Four short papers that sit beside the ladder, for when you want to study a real site rather than build one.

| Deep dive | Read it when |
| --- | --- |
| [Reading a minified bundle](deep-dives/reading-a-minified-bundle.md) | You have a site's JavaScript and want its constants and structure |
| [Capturing scenes and shaders](deep-dives/capturing-scenes-and-shaders.md) | You want the scene graph and GLSL from a live three.js page |
| [Custom binary models](deep-dives/custom-binary-models.md) | You see an unfamiliar model format and want the idea, plus a tiny format of your own |
| [The resilient loader](deep-dives/resilient-loader.md) | You are building a preloader, or briefing an agent to build one |

## Beyond L3

Things the case contains that the ladder does not teach yet: MSDF text in 3D, a physics-flavoured prop intro with mouse-velocity wobble, a 2.5D desk built from a photo plus prop sprites with height maps, mobile simplifications, and a production loader with a progress bar. They are the next labs if you need them, and the [BYO-site worksheet](../../worksheets/byo-site.md) will tell you which ones your site needs.
