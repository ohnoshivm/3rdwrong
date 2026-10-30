---
title: "Stage 1: Watch"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Stage 1: Watch

**Purpose.** Turn a screen recording into a list of effects you can name, each written down as a *hypothesis*. Video tells you what happens. It cannot tell you how, and as we found, it can mislead you about why.

**Case.** The founder recorded oryzo.ai (by [Lusion](https://oryzo.ai)) on 30 October at 19:29: 12 seconds, 2508×1306, 60 fps.

## Inputs → outputs

| In | Out |
| --- | --- |
| A screen recording (`.mov` or `.mp4`) of the effect you want | `research/<site>/video-frames/` with about a dozen named key frames |
| | `research/<site>/MOTION-PLAN.md`: numbered effects (E1, E2…), each a hypothesis with "what to measure" |
| | The site's identity (URL, makers), if the recording does not say |

## Steps

1. **Record it properly** (see the recording plan below). A better recording saves an hour later.
2. **Extract frames locally.** Three frames a second is enough to follow scroll effects:

   ```bash
   mkdir -p frames
   ffmpeg -i recording.mov -vf "fps=3,scale=1280:-2" -q:v 3 frames/f_%03d.jpg
   ```

   A 12-second clip gives 36 frames (we checked the command on a synthetic 12 s, 60 fps clip). Local frames never leave your machine and never fail on a quota.
3. **Try the `watch` skill for the full picture.** It can download a video, extract frames and a transcript, and, with a Gemini key configured, let Google's video model watch the whole clip. Be aware that local and downloaded videos are uploaded to Google for that engine; do not use it on a recording you must keep private. On our night the Gemini engine returned HTTP 503 (high demand) at about 19:40, so we fell back to the ffmpeg frames and read them directly. Plan for that.
4. **Identify the site.** Our site was named by the hero card in frame 1 ("Designed by Lusion"). If the recording does not name it, look at the address bar or the credits in the footer.
5. **Pick and name the key frames.** One frame per distinct effect or state, named by time and effect, so that a later agent can match them without opening each one: `00.67s-isnt-just-a-coaster-line-highlight.jpg`, `03.00s-hand-holds-coaster.jpg`. We kept 12.
6. **Write the effect list.** One row per effect: what you see, the likely technique, and what you would have to measure to be sure. Label every row as a hypothesis. We wrote ten (E1 to E10), among them smooth scroll, a persistent 3D object, hero defocus, a per-line text exit, a hand rig and an edge glow.
7. **Delegate the housekeeping.** Linking the skill into the project and saving the key frames is a two-line job for a cheap agent. We gave it to a DeepSeek agent in one short brief (the full brief is in `case-study/oryzo/prompts/`).

## Evidence to collect

- The key frames, with timestamps in the file names.
- The recording's properties (resolution, frame rate, length). `ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 recording.mov` prints them.
- The effect list with **hypotheses clearly marked** and a "what would settle it" column.
- A note on how the recording was made: did the person scroll steadily, or down and back up?

### The recording plan (before you press record)

- Scroll **slowly and monotonically**, top to bottom, once. Then, in a second take, hover over anything interactive.
- Keep the cursor visible so hover effects can be seen.
- Record at the resolution you will build at; note the window size.
- Say the site's URL aloud, or show it, in the first second.

## Common traps

- **Believing the video is linear.** *Ours was not.* The 12-second clip looked like one smooth pass, but the founder scrolled down, up and down again, so frames do not map in order to scroll positions. Only a few early frames matched cleanly to our later step captures.
- **Mistaking cause for coincidence.** From the video we wrote "the glow is triggered by hovering the hand". The cursor was over the hand at the time. The code later showed the glow follows scroll. Write what you *see* ("a glow appears while the pointer is over the hand") separately from why.
- **Over-trusting the AI's reading of frames.** Treat each frame-based claim as a hypothesis until code or measurement agrees.
- **Losing the plot to one failed tool.** If the video model errors, fall back to local frames immediately.

## Done when

- [ ] Frames are extracted and about a dozen are saved with time-and-effect names.
- [ ] The site is identified and the URL recorded.
- [ ] `MOTION-PLAN.md` lists each effect as a hypothesis with a "what to measure" column.
- [ ] You know whether the recording is linear in scroll, and you have written it down either way.
- [ ] Nothing in the notes is stated as fact that only the video supports.

## Tools

| Tool | Use |
| --- | --- |
| `watch` skill | Frames and transcript, optionally Gemini-assisted |
| ffmpeg / ffprobe | Frame extraction and recording properties, locally |
| Image viewing by the director | Reading frames directly, a few at a time |
| A cheap executor | Saving, renaming and linking, not judging |

Template: [motion-plan-template.md](../agent-system/templates/motion-plan-template.md). Prompt: [prompt-pack, stage 1](../tracks/ai-builder/prompt-pack.md#stage-1-watch). Next: [stage 2, Map](02-map.md).
