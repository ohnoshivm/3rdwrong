---
title: "Stage 8: Compare"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Stage 8: Compare

**Purpose.** Prove the rebuild matches the original, without anyone having to read the code. Same positions, same viewport, side by side; a score per step; frame times, layout shift and console output; and a human who approves what they have seen.

**Case.** The red-and-white rebuild of oryzo.ai (by [Lusion](https://oryzo.ai)) was checked against the original's captures at every 90 px of scroll. The founder approved it on localhost at 01:20 on 31 October, and a verified share zip (4.6 MB, 92 files) followed at 01:29.

## Inputs → outputs

| In | Out |
| --- | --- |
| The original's step captures (`captures/desktop/step-000…100.jpg`, one per 90 px) | Side-by-side images at the spec's positions |
| The running rebuild | A per-step fidelity score and chart |
| The acceptance list from the spec | A report: frame times, CLS, console output, reduced motion, mobile |
| | The human's approval, with its time |

## Steps

1. **Start when the first screenshots exist.** Do not wait for the final report. Our QA of the GL screenshots ran in parallel at 00:29, while the agents were still working.
2. **Drive both pages with the same script.** Same viewport (1440×900, then 390×844), same scripted `window.scrollTo(0, y)`, two animation frames, then a screenshot. For us: y = 0, 270, 900, 1530, 2250, 3060, 3600, 4320, 5130, 6000, 7200 and 8100, where step number = y ÷ 90.
3. **Place the pairs side by side**, original left, rebuild right. Compare composition: positions, sizes, line breaks, blur amount, coaster and hand pose, glow on or off. Our rebuild-only figures: [f01](../media/f01-rebuild-hero.png), [f07](../media/f07-rebuild-grid.jpg), [f10](../media/f10-hand-sequence.jpg). Side-by-side comparisons with the original appear in the Substack edition; see the live site at [https://oryzo.ai](https://oryzo.ai). The hand and coaster geometry come from oryzo.ai by Lusion, recoloured.
4. **Score structure, not colour.** The two palettes differ on purpose, so convert both images to greyscale before comparing, then compute a structural similarity score. ffmpeg can do it:

   ```bash
   ffmpeg -i original.jpg -i rebuild.jpg \
     -lavfi "[0:v]scale=720:-2,format=gray[a];[1:v]scale=720:-2,format=gray[b];[a][b]ssim" \
     -f null - 2>&1 | grep -o 'All:[0-9.]*'
   ```

   Run it for every step and chart the result ([f08-fidelity.png](../media/f08-fidelity.png)). A low score is a pointer to a screenshot to look at, not a verdict. (We checked this command on two generated test images. The score values for the Oryzo rebuild are in the media folder, not here.)
5. **Read the console.** Zero errors and warnings during a full scroll.
6. **Measure frame times** across the whole scroll, 0 to 8,100 px, and report the 95th percentile as well as the average (ours: 60 fps average on the M3; p95 17.2 to 17.4 ms). Record layout shift (ours: CLS 0).
7. **Test failure paths.** A missing asset: does `stage.ready` settle within 10 seconds? Reduced motion: do blurs go away and positions snap? Mobile: is the hero blur off and the scrim on?
8. **Settle the unknowns from stage 4.** For instance, the wheel follower measured at about 7 per second against a coefficient of 12 in the code: compare the feel side by side and decide.
9. **Show the human, and write down the deviations they accept.** Ours: the strong red glow. The founder accepted it as it was.
10. **Package and verify.** We built a shareable zip and confirmed it builds before zipping (4.6 MB, 92 files).

## Evidence to collect

- Side-by-side images at every acceptance position, desktop and mobile.
- The fidelity table: step, score, and a note on every low one.
- The console log from a full scroll (it should be empty).
- Frame-time data (p50, p95), CLS, and the machine and GPU.
- The failure-path results: missing asset, reduced motion, mobile.
- The approval: who, what they saw, when. And the deviations accepted.

## Common traps

- **Comparing colour.** A recolour will never score well on raw pixel difference. Compare luminance structure.
- **Trusting one number.** A good average hides a bad step. Look at the images behind the lowest scores.
- **Different scroll positions.** If the two pages scroll by different mechanisms, the pictures will not line up. Use the same `scrollTo` on both, after the same two frames.
- **Sandboxed server.** *Ours: the sandbox blocked local port binding when the founder asked to see it.* The server ran outside the sandbox at 127.0.0.1:5180. If you cannot serve it, you cannot show it.
- **Never asking the human.** A pass by script is not an approval by the person who asked.
- **Waiting for "done".** We did not: QA of the GL screenshots started at 00:29, in parallel with the build, so defects surfaced while the agents were still working.

## Done when

- [ ] Side-by-sides exist for every acceptance position at both viewports.
- [ ] A fidelity score exists per step, and every low score has been looked at.
- [ ] The console is clean across a full scroll.
- [ ] p95 frame time and CLS are recorded, with the machine.
- [ ] Missing-asset, reduced-motion and mobile checks passed.
- [ ] The human approved what they saw on localhost, and accepted deviations are noted.
- [ ] The package builds from scratch.

## Tools

| Tool | Use |
| --- | --- |
| Playwright | The same scripted scroll on both pages; screenshots; console capture; frame-time sampling ([compare.mjs](../agent-system/scripts/compare.mjs)) |
| ffmpeg | Greyscale conversion and the SSIM score |
| `qa-brief.md` template | The QA agent's brief |
| The director | Reads the images, decides what is a defect |

Template: [qa-brief.md](../agent-system/templates/qa-brief.md). Prompt: [prompt-pack, stage 8](../tracks/ai-builder/prompt-pack.md#stage-8-compare). See also [verifying without reading code](../tracks/ai-builder/verify-without-reading-code.md).
