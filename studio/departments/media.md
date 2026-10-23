---
title: Media department
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Media department

Produce film, motion graphics, images and sound assets from approved creative direction. Image and motion intent remain Design decisions.

Status: proposed registry routing. Source review does not establish live tool performance, licence clearance, runtime connectivity or founder approval.

68 tools; 14 lead, 33 specialist, 6 bench, 15 parked, 0 excluded; 47 active / 21 library.

## Sub-departments → jobs → leads

### film-motion-graphics

| Job | Lead(s) |
| --- | --- |
| `brand-film` | `anthropic-skills:motionmaxxing` |
| `programmatic-video` | `remotion:remotion-best-practices` |
| `video-editing` | `chatcut-desktop:chatcut-plugin-basics` |
| `video-effects` | `chatcut-desktop:shader-gen` |
| `media-quality-check` | `chatcut-desktop:verification` |
| `media-tool-access` | `chatcut-desktop:widget-forms` |
| `short-form-editing` | `agency:marketing-short-video-editing-coach` |
| `asset-research` | `juicylucy-ads:media-use` |

### image-photo-direction

| Job | Lead(s) |
| --- | --- |
| `brand-image-assets` | `skill:imagegen` |
| `image-production-workflow` | `skill:3w-image-production` |
| `image-quality-check` | `skill:3w-image-qa` |

### sound-voice

| Job | Lead(s) |
| --- | --- |
| `voice-and-sound` | `chatcut-desktop:voice` |
| `transcription-captions` | `chatcut-desktop:transcription` |
| `music-composition` | `agency:specialized-focus-music-architect` |

## Specialists with activation triggers

| Tool | Job | Trigger |
| --- | --- | --- |
| `chatcut-desktop:asset-import` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:create-motion-graphics` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:digital-human` | `film-motion-graphics/brand-film` | Use when an approved deliverable requires a synthetic presenter or avatar. |
| `chatcut-desktop:export` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:known-errors` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:multicam-sync` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:music` | `sound-voice/voice-and-sound` | Use for an approved voiceover, audio cleanup, music, or speech workflow. |
| `chatcut-desktop:talking-head-guide` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:video-gen` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `chatcut-desktop:video-translation` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `heygen:heygen-workflows` | `film-motion-graphics/brand-film` | Use when an approved deliverable requires a synthetic presenter or avatar. |
| `hyperframes:gsap` | `film-motion-graphics/video-effects` | Use when the video needs custom effects or transitions. |
| `hyperframes:hyperframes` | `film-motion-graphics/programmatic-video` | Use for the specific Remotion or HyperFrames production task. |
| `hyperframes:hyperframes-cli` | `film-motion-graphics/programmatic-video` | Use for the specific Remotion or HyperFrames production task. |
| `hyperframes:hyperframes-registry` | `film-motion-graphics/programmatic-video` | Use for the specific Remotion or HyperFrames production task. |
| `hyperframes:website-to-hyperframes` | `film-motion-graphics/programmatic-video` | Use for the specific Remotion or HyperFrames production task. |
| `mcp:chatcut_desktop` | `film-motion-graphics/media-tool-access` | Use when the connected production server is required. |
| `mcp:creative_production_mcp` | `film-motion-graphics/media-tool-access` | Use when the connected production server is required. |
| `mcp:heygen` | `film-motion-graphics/media-tool-access` | Use when the approved work needs this capability: Configured MCP server: heygen. Transport details and credentials are not inventoried |
| `mcp:hyperframes` | `film-motion-graphics/media-tool-access` | Use when the connected production server is required. |
| `skill:chatcut-app-promo-guide` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `skill:chatcut-create-motion-graphics` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `skill:chatcut-image-gen` | `image-photo-direction/brand-image-assets` | Use when the task explicitly calls for this image generation workflow or host. |
| `skill:chatcut-multicam-sync` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `skill:chatcut-transcription` | `sound-voice/transcription-captions` | Use for transcript-driven captions or speech cleanup. |
| `skill:chatcut-visual-analysis` | `film-motion-graphics/media-quality-check` | Use when validating an edit with timeline structure or rendered-frame evidence. |
| `skill:chatcut-voice-isolation` | `sound-voice/voice-and-sound` | Use for an approved voiceover, audio cleanup, music, or speech workflow. |
| `skill:chatcut-web-browser` | `film-motion-graphics/asset-research` | Use to collect source media or brand assets from a URL for production. |
| `skill:chatcut-widget-forms` | `film-motion-graphics/media-tool-access` | Use for the matching ChatCut support or input task. |
| `skill:image` | `image-photo-direction/brand-image-assets` | Use when the task explicitly calls for this image generation workflow or host. |
| `skill:video` | `film-motion-graphics/video-editing` | Use for the named production workflow when its format or host matches the brief. |
| `skill:viral-clip-extractor` | `film-motion-graphics/short-form-editing` | Use when extracting short-form clip candidates from source video. |
| `stitch-build:remotion` | `film-motion-graphics/programmatic-video` | Use for the specific Remotion or HyperFrames production task. |

## Bench and parked summary

- **bench: 6.** `chatcut-desktop:product-help`, `juicylucy-ads:hyperframes-animation`, `juicylucy-ads:hyperframes-audio`, `juicylucy-ads:hyperframes-cli`, `juicylucy-ads:hyperframes-core`, `juicylucy-ads:hyperframes-keyframes`
- **parked: 15.** `remotion:remotion-captions`, `remotion:remotion-create`, `remotion:remotion-docs`, `remotion:remotion-interactivity`, `remotion:remotion-maps`, `remotion:remotion-markup`, `remotion:remotion-multimedia`, `remotion:remotion-render`, `remotion:remotion-saas`, `remotion:remotion-studio`, `remotion:remotion-upgrade`, `skill:browser-video-recording`, `skill:codex-gpt-image-2-5-flare`, `skill:elevenlabs-tts`, `skill:nextphase-persa-shorts`
- **excluded: 0.** None.

Individual reasons and activation requirements are in the [canonical registry](../../toolkit/sources/registry.json). Library means callable by explicit name after review; it is not loaded by default.

## Gaps

The previous lead gaps now have experimental studio methods:

- `image-photo-direction/image-production-workflow` — [`skill:3w-image-production`](../../skills/3w-image-production/SKILL.md).
- `image-photo-direction/image-quality-check` — [`skill:3w-image-qa`](../../skills/3w-image-qa/SKILL.md).

Routing closes the ownership gap; it does not prove output quality, human
approval, installed prerequisites or completed delivery. Independent evidence
and the charter gates remain required.

## Counts by sub-department and role

| Sub-department | Lead | Specialist | Bench | Parked | Excluded | Active | Library | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| film-motion-graphics | 8 | 28 | 5 | 12 | 0 | 36 | 17 | 53 |
| image-photo-direction | 3 | 2 | 0 | 1 | 0 | 5 | 1 | 6 |
| sound-voice | 3 | 3 | 1 | 2 | 0 | 6 | 3 | 9 |

## Operating contract

Use the job lead first and a specialist only on its trigger. Maker and checker must be separate people/agent instances; a reviewer never approves its own department alone. Proposed `load: active` is the desired loading policy, while the source inventory records installation presence. No physical activation was performed.

Design and Engineering prototype together early; the handoff names artefacts, constraints, budgets and evidence rather than creating a wall. Human judgement and founder approval remain separate from tool routing.
