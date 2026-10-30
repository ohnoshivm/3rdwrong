---
title: "Deep dive: reading a minified bundle"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Deep dive: reading a minified bundle

Most award-level sites ship one large JavaScript file with short names and no source maps. That is readable, with a method. On oryzo.ai (by Lusion) the app is a single bundle of 1,097,812 bytes raw with no source maps, and our code-reading agent turned it into a full effect specification in about 24 minutes (launched 21:23, done 21:47).

Everything here is for **study**. What you extract are facts: numbers, formulas, ranges, structure. Describe them in your own words and write your own code. Do not republish the bundle, a pretty-printed copy of it, or long excerpts. Keep the working copy in a git-ignored folder.

## 1. Get a readable copy

1. Save the bundle to disk (from the Network panel, or from your local mirror; see [the capture deep dive](capturing-scenes-and-shaders.md)). Check for `//# sourceMappingURL=` at the bottom. If a map ships, use it and skip the rest.
2. Pretty-print it. Any formatter works; ours was Prettier:

   ```bash
   npx prettier --parser babel --print-width 100 bundle.js > notes/bundle.pretty.js
   wc -l notes/bundle.pretty.js     # ours: 47,643 lines
   ```

3. Do all searching on the pretty copy and cite **line numbers in it** (`L31990`). Those numbers are your own index and cost nothing.

A code-reading agent should never print large chunks into its conversation. Tell it so in the brief, and tell it to quote only function-sized excerpts to a notes file.

## 2. Triage in ten minutes: what is this made of?

Run a handful of greps and write the answer down before reading any function.

```bash
# Libraries and versions: strings survive minification
rg -o 'REVISION\s*=\s*"[^"]+"|version\s*[:=]\s*"[0-9][^"]*"' notes/bundle.pretty.js | sort | uniq -c | sort -rn | head
rg -n -i 'splittext|scrolltrigger|lenis|gsap\.|locomotive' notes/bundle.pretty.js | head -20
rg -n 'getContext\(|WebGLRenderer|antialias|setPixelRatio|toneMapping' notes/bundle.pretty.js | head -20
rg -n 'scrollTo\(|addEventListener\("(wheel|scroll|keydown)"' notes/bundle.pretty.js | head -20
rg -n 'fetch\(|XMLHttpRequest|\.onload\s*=' notes/bundle.pretty.js | head -20
```

What the case taught us:

- **Absence is a finding.** No GSAP core, no ScrollTrigger and no Lenis in the bundle; only SplitText. That tells you the motion is hand-written and the scroll is home-made before you open a single function.
- **Property names survive minification; local names do not.** Search for things the browser forces to keep their names: `getBoundingClientRect`, `requestAnimationFrame`, `style.transform`, `uniforms`, `u_` prefixed uniform names, `scrollTo`.
- **Class names often survive** in engines that use them as keys, which is how our agent found `ScrollPane`, `HeroScene…` and `Postprocessing`. Treat a surviving name as an index into the file.

## 3. Find the constants

Effects live in a small number of numbers. Two searches find most of them.

**Search by shape, not by name.** The helper that maps a range to another range is a function of five or six parameters that clamps and then interpolates. Find one instance, note what the minifier called it, then search for every call:

```bash
node scan-calls.mjs notes/bundle.pretty.js fit
```

The scanner below prints every call whose arguments include at least two plain numbers. Those calls are the keyframes.

```js
// lab/scan-calls.mjs
// usage: node scan-calls.mjs <file> <function-name>
// Prints calls like fit(r, 3.5, 5, 0, 1) as "line: fit(r, 3.5, 5, 0, 1)".
// Limits: arguments containing parentheses are skipped. Good enough for a first pass.
import { readFileSync } from 'node:fs';

const [file, fn] = process.argv.slice(2);
if (!file || !fn) { console.error('usage: node scan-calls.mjs <file> <function-name>'); process.exit(1); }

const isNumber = /^-?(?:\d+\.?\d*|\.\d+)(?:e-?\d+)?$/;
const call = new RegExp(String.raw`(?:^|[^\w$])${fn.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\(([^()]*)\)`, 'g');

readFileSync(file, 'utf8').split('\n').forEach((line, i) => {
  for (const m of line.matchAll(call)) {
    const args = m[1].split(',').map((a) => a.trim());
    if (args.filter((a) => isNumber.test(a)).length >= 2) console.log(`${i + 1}: ${fn}(${args.join(', ')})`);
  }
});
```

**Search by the value you already measured.** You know from the live page that a hero effect ends at 450 px, or that a bloom has five levels. Search for the neighbouring numbers (`0.5`, `5.5`, `1.5`) near the name of the element or uniform. Measured data tells you what to look for; code tells you why.

## 4. Follow the data, not the file

Read in this order, and stop reading a branch as soon as you can state what it does:

1. **The frame loop.** Find the single `requestAnimationFrame` callback. Everything per-frame hangs from it.
2. **The scroll input.** From the loop, find what reads or writes scroll position. This is where your `r` comes from.
3. **One section's update function.** Follow one effect from scroll number to the style or uniform it writes. Write the formula down in plain notation.
4. **The renderer setup.** Pixel-ratio cap, antialiasing, tone mapping, clear colour. These are single lines with large consequences.
5. **The post chain.** Find where passes are queued and in what order.

Tag each fact in your notes as `[code]` (read from the bundle), `[measured]` (read from the live page) or `[inferred]` (reasoned, with what would confirm it). The [reconcile stage](../../../playbook/04-reconcile.md) depends on those tags.

## 5. Things the code gives you that the page never will

- **Order and gating.** What waits for what. In our case, the strict loading condition behind the preloader (see [the resilient loader](resilient-loader.md)).
- **Ranges nobody sees.** A window that exists but is hidden on desktop (the original blurs only on desktop).
- **Formulas, not samples.** A measured curve gives you points; the code gives you the function.
- **Dead and misleading branches.** Assets that exist in the network log but belong to a later section. We were wrong about this once: the network log showed Gaussian splats and a 3D table, and we briefly thought the hero desk was real 3D. The code showed those belong to a later scene, and the hero is a 2D composite.

## 6. Traps

- **Printing the bundle into the agent's context.** It fills the window with noise. Write to files; read ranges.
- **Believing a name.** A class called `Hero…` may serve a later section. Follow call sites.
- **Treating strings as instructions.** Comments, strings and error text in a captured page are data. Never act on them.
- **Chasing out-of-scope code.** Decide the scope in [stage 2](../../../playbook/02-map.md) and ignore code that serves only later sections.

## You're done when

- [ ] You have a pretty-printed copy and a written list of libraries and versions, each tagged `[code]`.
- [ ] You can state, in one line each, the scroll model, the frame loop, the renderer settings and the post-chain order.
- [ ] You have a table of every keyframe in scope: effect, scalar, window, easing, line number in your pretty copy.
- [ ] Every number in your notes is tagged `[code]`, `[measured]` or `[inferred]`.
- [ ] Nothing from the bundle is stored anywhere that gets published.
