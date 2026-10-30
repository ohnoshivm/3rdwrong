---
title: "Verify without reading code"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Verify without reading code

You can direct an agent that writes thousands of lines you will never read, so long as you can check the result in ways that do not need the code. This page is how: the same scripted positions on both pages, pictures side by side, a score per step, the console, and frame times. In the oryzo.ai (by [Lusion](https://oryzo.ai)) rebuild, the founder asked to see the rebuild running on localhost and approved it there at 01:20.

The rule behind all of it: **an agent's "done" is a claim. A file on disk is evidence.** Ask for files.

## 1. Same positions, same script, both pages

Pick scroll positions up front (ours, at 1440×900: 0, 270, 900, 1530, 2250, 3060, 3600, 4320, 5130, 6000, 7200, 8100 px) and drive both pages with the same `window.scrollTo(0, y)`, followed by two animation frames, then a screenshot. Same viewport, same device pixel ratio. A given `y` then means a given picture. Repeat at the mobile viewport.

## 2. Side by side, then look

Original on the left, rebuild on the right, one image per position. Look for: position, size, line breaks, blur amount, object pose, glow on or off. This takes about a minute per ten pairs and finds most real defects. Our rebuild-only grid is in [media/f07-rebuild-grid.jpg](../../media/f07-rebuild-grid.jpg), with the rebuild hero at [media/f01-rebuild-hero.png](../../media/f01-rebuild-hero.png). Side-by-side comparisons with the original appear in the Substack edition; see the live site at [https://oryzo.ai](https://oryzo.ai). The hand and coaster geometry come from oryzo.ai by Lusion, recoloured.

## 3. Step captures through the whole range

Positions every 90 px (101 steps for 8,100 px) catch what twelve positions miss: a fade that ends late, a pop between two steps. Use them for the score below and as a flip-book when something looks wrong. The original's captures were made once, in [stage 3](../../playbook/03-teardown.md), and reused as the reference every time.

## 4. A fidelity score per step

A number does not replace looking, but it tells you where to look. Compare **luminance structure**, because your palette is meant to differ: convert both pictures to greyscale, scale them the same, and compute structural similarity (SSIM) with ffmpeg. Chart it by step ([media/f08-fidelity.png](../../media/f08-fidelity.png)). Read the lowest steps first.

Two cautions. Low scores are pointers, and a sudden dip between two good steps means an effect that is out of step with scroll. And a recolour, a different font or new prop art will always cost some score: separate **intentional differences** from defects in the report.

## 5. The console, and the frame times

- **Console:** zero errors and zero warnings during a full scroll of the page. Warnings count.
- **Frame times:** sweep the whole range and report the 95th percentile. Ours averaged 60 fps on an Apple M3 with a 95th percentile of 17.2 to 17.4 ms.
- **Layout shift:** CLS 0.
- **Failure paths:** a missing file (does the page still start within its deadline?), reduced motion, and the mobile viewport.

## A script that does all of it

This is a short version of the capture-and-compare script. The generalised versions live in [agent-system/scripts](../../agent-system/scripts/README.md) (`capture-steps.mjs`, `compare.mjs`). This one is tested against two local pages.

```js
// lab/compare-steps.mjs
// usage: node compare-steps.mjs <urlA> <urlB> [outDir]
// Needs: playwright-core, Chrome, ffmpeg. Writes a-<y>.png, b-<y>.png, pair-<y>.png, report.json.
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const [urlA, urlB, out = 'qa/compare'] = process.argv.slice(2);
const ys = [0, 270, 900, 1530, 2250, 3060, 3600, 4320, 5130, 6000, 7200, 8100];
mkdirSync(out, { recursive: true });

const twoFrames = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));

const browser = await chromium.launch({ channel: 'chrome' });
const report = { a: {}, b: {}, ssim: {} };

for (const [tag, url] of [['a', urlA], ['b', urlB]]) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const problems = [];
  page.on('console', (m) => { if (['error', 'warning'].includes(m.type())) problems.push(m.text()); });
  page.on('pageerror', (e) => problems.push(String(e)));
  await page.goto(url, { waitUntil: 'load' });

  for (const y of ys) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await page.evaluate(twoFrames);
    await page.screenshot({ path: `${out}/${tag}-${y}.png` });
  }

  // frame times over one sweep of the whole page
  const frames = await page.evaluate(async () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const dts = [];
    let last = performance.now();
    for (let i = 0; i <= 300; i++) {
      scrollTo(0, (max * i) / 300);
      await new Promise((r) => requestAnimationFrame(r));
      const now = performance.now();
      dts.push(now - last);
      last = now;
    }
    dts.shift();
    dts.sort((x, y) => x - y);
    return { p50: dts[Math.floor(dts.length * 0.5)], p95: dts[Math.floor(dts.length * 0.95)] };
  });
  report[tag] = { ...frames, consoleProblems: problems };
  await page.close();
}
await browser.close();

for (const y of ys) {
  const a = `${out}/a-${y}.png`, b = `${out}/b-${y}.png`;
  spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', a, '-i', b, '-filter_complex', 'hstack', `${out}/pair-${y}.png`]);
  const r = spawnSync('ffmpeg', ['-i', a, '-i', b, '-lavfi',
    '[0:v]scale=720:-2,format=gray[a];[1:v]scale=720:-2,format=gray[b];[a][b]ssim', '-f', 'null', '-'], { encoding: 'utf8' });
  report.ssim[y] = Number(/All:([0-9.]+)/.exec(r.stderr)?.[1] ?? NaN);
}
writeFileSync(`${out}/report.json`, JSON.stringify(report, null, 2));
console.log(JSON.stringify({ a: report.a, b: report.b, ssim: report.ssim }));
```

Use it with a rebuild running locally and the original either live (if you are allowed to load it in automation) or, better, served from your own private mirror. Remember that headless or contended runs give pessimistic frame times; note the machine.

## What to ask an agent for

A completion report you can trust has files in it:

| Ask for | Why |
| --- | --- |
| Screenshots at the agreed positions, saved at known paths | You can open them |
| The build output and the test count | A pass or a fail, with numbers (ours: 20 of 20 functional tests) |
| The console output from a full scroll | Warnings are findings |
| Frame times as p50 and p95 | The average hides hitches |
| A list of the original modules or formulas ported, with where from | You can audit fidelity without reading the code |
| A mismatch list against the references | The agent finds its own gaps |
| "Not verified" for anything it did not run | An honest gap beats a confident one |

## Red flags in a report

- "Done" with no screenshots or counts.
- Screenshots at positions you did not ask for.
- A frame-rate average and no p95.
- "Matches the original" with no mismatch list. Something always differs.
- A check that is described and not run.

## You're done when

- [ ] Both pages were driven by the same script and the images are side by side.
- [ ] Every low-scoring step has been looked at, and each difference is labelled as intentional or a defect.
- [ ] The console is clean over a full scroll.
- [ ] p95 frame time and CLS are on record, with the machine.
- [ ] Missing-asset, reduced-motion and mobile checks passed or are marked "not verified".
- [ ] The person who asked has seen it running and said yes.

Related: [stage 8 of the playbook](../../playbook/08-compare.md), [qa-brief.md](../../agent-system/templates/qa-brief.md).
