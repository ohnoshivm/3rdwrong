---
title: "Stage 6: Assets"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Stage 6: Assets

**Purpose.** Produce the new material the build needs (images, maps, textures) without copying the original's, in exact sizes, ready to drop in, while the code agents work.

**Case.** The founder wanted the rebuild of oryzo.ai (by [Lusion](https://oryzo.ai)) in red and white with GPT-made images. The IMG agent, GPT-6 Luna at medium effort with built-in image generation, was briefed at 23:41 on 30 October and finished at 23:51: 27 files.

## Inputs → outputs

| In | Out |
| --- | --- |
| The spec's asset table, palette and art direction | `public/gen/`: the desk, 7 props, 2 leaf-shadow gobos, a red cork coaster texture, a video thumbnail |
| | Derived maps: an alpha map and a height map for each prop, a height map for the cork |
| | A re-runnable script in `scripts/gen/` and the prompts actually used |

The 27 files are: the desk; seven props (pen, pencil, eraser, cutter, three paperclips) each with an alpha and a height map; two gobos; the cork texture and its height map; and the video thumbnail.

## Steps

1. **Check the tool first.** The brief's first line: check you have an image-generation tool. If not, stop and report `NO_IMAGE_TOOL`. No code-drawn fakes, no paid API. A silent substitution would spoil the art direction and hide the failure.
2. **Write one shared art direction** and apply it to every image: strictly top-down orthographic, soft daylight from the upper left, a palette of crimson, warm white and neutral greys only, no text unless specified, no real brand logos.
3. **Specify each file exactly**: name, pixel size, background (fully transparent for props), orientation (long axis vertical, tip at the top), and what must not appear (no cast shadow in the image, since the renderer draws shadows).
4. **Decide the shading model with the human.** The original's props are strips of several renders under different light angles plus a height map, so they can be relit live. We chose new art lit from one angle and derived the height map from the alpha channel, which is simpler and sufficient.
5. **Script the derivations.** Alpha map from the alpha channel. Height map: the alpha blurred at about 6% of the image width and normalised to 0 to 1. Both deterministic and re-runnable (ffmpeg, or Python with Pillow).
6. **Make the pipeline tolerate absence.** The spec tells GL to use correctly sized flat placeholders until these files exist, so nothing waits on the image agent.
7. **Verify against the brief**, then look at each image once. Regenerate any that are clearly off: wrong colours, object not vertical, visible text, background not transparent.
8. **Record the prompts** actually used. They belong in the repo with the images.

## Evidence to collect

- A table of every file: name, size in pixels, bytes.
- A check that props have real transparency (corner alpha 0, object opaque) and gobos are single-channel.
- Which images were regenerated and why.
- The prompts used.

A contact sheet of the 27 files is in the article's figures ([media/f11-generated-assets.jpg](../media/f11-generated-assets.jpg)), and the idea of the original's prop atlas against ours in [media/f06-props.png](../media/f06-props.png).

## Common traps

- **Substituting a fake when the tool is missing.** The brief says to stop. Obey it, and the director chooses what to do.
- **Cast shadows baked in.** The renderer draws its own shadows from the alpha. A shadow in the image would be doubled.
- **Wrong aspect ratios.** Each prop has a specific aspect; a prop at the wrong ratio looks fine alone and wrong on the desk. State sizes in pixels.
- **Textures with visible seams.** Cork must tile; ask for a tileable texture and check the seams.
- **Copying the original.** *The trap we set ourselves:* the original's desk photo and prop renders are Lusion's. Generating new art and recolouring in shaders keeps ours clean. The five geometry and animation files and six textures we reused from the original (hand albedo, environment maps, LUTs) stayed in the private study folder and were recoloured in shaders; we do not redistribute them.
- **Over-prompting every file.** Share art direction; keep per-file lines short.

## Done when

- [ ] Every file exists at the exact size listed.
- [ ] Prop PNGs have real alpha; gobos are single-channel; the cork tiles without a visible seam.
- [ ] The derivation script runs from scratch and reproduces the maps.
- [ ] You looked at each output and regenerated the off-brief ones.
- [ ] The prompts used are saved beside the images.
- [ ] Nothing in `public/gen/` is a copy of the original's art.

## Tools

| Tool | Use |
| --- | --- |
| Image generation (GPT-6 Luna's built-in tool in our case) | The 27 files, on the ChatGPT subscription, with no paid API |
| ffmpeg or Python with Pillow | Resizing, trimming, alpha and height maps |
| The director | Art direction, review of outputs |

Template: [build-agent-images.md](../agent-system/templates/build-agent-images.md). Prompt: [prompt-pack, stage 6](../tracks/ai-builder/prompt-pack.md#stage-6-assets). Next: [stage 7, Parallel build](07-parallel-build.md).
