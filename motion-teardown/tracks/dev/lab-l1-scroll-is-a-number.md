---
title: "Lab L1: scroll is a number"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Lab L1: scroll is a number

*Level 1 of the [level ladder](level-ladder.md). No 3D, no dependencies beyond a bundler. About two hours.*

**Goal.** Build a pinned section whose headline arrives letter by letter and leaves in reverse, where the whole state is a pure function of the scroll position. Scroll up and everything un-plays itself, with no reverse code.

**Case.** oryzo.ai by Lusion works this way. Our reading of its shipped code: a home-made virtual scroller moves the real page, every section reduces scroll to one number, and every effect is a `fit()` of that number. There is no timeline object and no tweening. The numbers we quote below were measured on that site; the code on this page is ours.

## Concepts

**Virtual scroll over native scroll.** The page really scrolls (so scrollbars, anchors and `scrollTo` still work), but the wheel is cancelled and a small model chases a target. The model's output is written back with `window.scrollTo`. Smoothing happens here, once. Nothing downstream smooths again.

**Section progress `r`.** For each section you compute one number from the scroll position: `r = 1 + (scrollY − sectionTop) / viewportHeight`. It is 0 when the section's top edge touches the bottom of the viewport, 1 when it reaches the top, and rises by 1 for every further viewport scrolled. A section that is pinned for eight viewports has an `r` that runs through eight units, and every keyframe is authored in those units.

**`fit()`.** `fit(x, a, b, c, d, ease)` maps `x` from the range `[a, b]` onto `[c, d]`, clamps outside it and applies an easing. Everything else is built from it.

**Stagger windows.** A group of letters shares one progress value `g` from 0 to 1. Letter `i` of `n` starts a little later than letter `i−1` and takes a fixed slice of the group. On the live site each item starts at about 0.3 × its normalised index, in a window 0.4 to 0.6 wide.

**Reveals.** Split the text into spans and write `opacity`, `transform` and `filter` inline on every frame. No CSS transitions: a transition would fight the scroll.

## The code

Six small files. Create a folder, run `npm i -D vite typescript`, put these in it and run `npx vite`.

### `math.ts`: `fit` and the easings

```ts
// lab/math.ts
export type Ease = (t: number) => number;

export const clamp = (x: number, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, x));
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

export const ease = {
  linear: (t) => t,
  cubicIn: (t) => t * t * t,
  cubicOut: (t) => 1 - (1 - t) ** 3,
  sineIn: (t) => 1 - Math.cos((t * Math.PI) / 2),
  expoOut: (t) => (t >= 1 ? 1 : 1 - 2 ** (-10 * t)),
  backOut: (t) => {
    const c = 1.70158;
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2;
  },
} satisfies Record<string, Ease>;

/** Map x from [a, b] to [c, d], clamped, eased. a > b is allowed and runs the range backwards. */
export function fit(x: number, a: number, b: number, c = 0, d = 1, e: Ease = ease.linear): number {
  const t = a === b ? (x >= b ? 1 : 0) : clamp((x - a) / (b - a));
  return lerp(c, d, e(t));
}
```

### `section.ts`: one number per section

```ts
// lab/section.ts
/** 0: top edge at the bottom of the viewport. 1: top edge at the top. +1 per further viewport. */
export const sectionR = (scrollY: number, sectionTop: number, vh: number) =>
  1 + (scrollY - sectionTop) / vh;

/** The same measure for the bottom edge. -1 while the section fills the screen, 0 once it has left. */
export const exitR = (scrollY: number, sectionTop: number, sectionH: number, vh: number) =>
  (scrollY - sectionTop - sectionH) / vh;
```

A check against the live site's numbers: with `#hero` at 0 px and 900 px tall in a 900 px viewport, `exitR` runs from −1 at `scrollY = 0` to −0.5 at `scrollY = 450`. That is the hero's exit window (0 to 450 px) that we measured.

### `scroll-engine.ts`: the virtual scroller

```ts
// lab/scroll-engine.ts
import { clamp } from './math';

export const WHEEL_CLAMP = 200; // px a single wheel event may add
export const EASE_RATE = 12; // 1/s: how fast `current` chases `target`
export const KEY_STEP = 100;

export interface ScrollModel {
  target: number;
  current: number;
  max: number;
}

export const createScroll = (max: number): ScrollModel => ({ target: 0, current: 0, max });

export function pushWheel(m: ScrollModel, deltaY: number) {
  m.target = clamp(m.target + clamp(deltaY, -WHEEL_CLAMP, WHEEL_CLAMP), 0, m.max);
}

export function pushKey(m: ScrollModel, key: string, viewportH: number) {
  const d =
    key === 'ArrowDown' ? KEY_STEP
    : key === 'ArrowUp' ? -KEY_STEP
    : key === 'PageDown' || key === ' ' ? viewportH
    : key === 'PageUp' ? -viewportH
    : 0;
  m.target = clamp(m.target + d, 0, m.max);
}

/** Advance by dt seconds. Exponential chase, so the result does not depend on the frame rate. */
export function step(m: ScrollModel, dt: number): number {
  m.current += (m.target - m.current) * (1 - Math.exp(-EASE_RATE * dt));
  if (Math.abs(m.target - m.current) < 0.1) m.current = m.target;
  return Math.round(m.current); // whole pixels: a screenshot at y is reproducible
}

/** Wire the model to the page. onFrame receives the smoothed integer scroll position. */
export function attach(m: ScrollModel, onFrame: (y: number, dt: number) => void) {
  let written = -1; // the last value we pushed into the page ourselves

  addEventListener('wheel', (e) => { e.preventDefault(); pushWheel(m, e.deltaY); }, { passive: false });
  addEventListener('keydown', (e) => pushKey(m, e.key, innerHeight));
  addEventListener('scroll', () => {
    if (Math.round(scrollY) === written) return; // our own write coming back
    m.current = m.target = scrollY; // scrollbar drag, anchor jump or a scripted scrollTo
  }, { passive: true });

  let last = performance.now();
  const frame = (now: number) => {
    const dt = Math.min((now - last) / 1000, 1 / 15);
    last = now;
    const y = step(m, dt);
    if (y !== Math.round(scrollY)) {
      written = y;
      scrollTo({ top: y, behavior: 'instant' });
    }
    onFrame(y, dt);
    requestAnimationFrame(frame);
  };
  requestAnimationFrame(frame);
}
```

The native `scroll` listener is the detail that makes the model robust. A scrollbar drag or a scripted `window.scrollTo(0, 2400)` lands in the model instead of being overwritten on the next frame. That same property is what lets a test script drive the page to exact positions, which we use in [stage 8 of the playbook](../../playbook/08-compare.md).

### `stagger.ts`: windows inside a group

```ts
// lab/stagger.ts
import { ease, fit, type Ease } from './math';

/**
 * Local progress (0..1) of item i of n, given the group's progress 0..1.
 * Item k = i/(n-1) starts at k*offset and takes `width` of the group. offset + width <= 1.
 * reverse: the last item goes first (used for exits).
 */
export function staggerWindow(
  group: number, i: number, n: number,
  offset = 0.3, width = 0.6, e: Ease = ease.linear, reverse = false,
): number {
  const k = n > 1 ? i / (n - 1) : 0;
  const start = (reverse ? 1 - k : k) * offset;
  return fit(group, start, start + width, 0, 1, e);
}
```

### `reveal.ts`: split and drive letters

```ts
// lab/reveal.ts
import { ease } from './math';
import { staggerWindow } from './stagger';

/** Wrap each word, then each letter, in spans. Words stay unbroken. Screen readers get the original text. */
export function splitWords(el: HTMLElement): HTMLElement[] {
  const text = el.textContent ?? '';
  el.setAttribute('aria-label', text);
  el.textContent = '';
  const chars: HTMLElement[] = [];
  for (const part of text.split(/(\s+)/)) {
    if (!part) continue;
    if (/^\s+$/.test(part)) { el.append(part); continue; }
    const word = document.createElement('span');
    word.setAttribute('aria-hidden', 'true');
    word.style.cssText = 'display:inline-block;white-space:nowrap';
    for (const ch of part) {
      const c = document.createElement('span');
      c.style.display = 'inline-block';
      c.textContent = ch;
      word.append(c);
      chars.push(c);
    }
    el.append(word);
  }
  return chars;
}

/** enter and exit are group progress values (0..1). Letters arrive first-to-last and leave last-to-first. */
export function driveHeadline(chars: HTMLElement[], enter: number, exit: number, calm = false) {
  const n = chars.length;
  chars.forEach((c, i) => {
    const pin = staggerWindow(enter, i, n);
    const pout = staggerWindow(exit, i, n, 0.2, 0.8, ease.linear, true);
    c.style.opacity = (ease.expoOut(pin) * (1 - pout)).toFixed(3);
    if (calm) return; // prefers-reduced-motion: fade only
    c.style.transform = `translateX(${((1 - pin) * 0.25).toFixed(3)}ex)`;
    c.style.filter = pin < 1 ? `blur(${((1 - pin) * 0.1).toFixed(3)}em)` : 'none';
  });
}
```

Splitting by word first is not decoration. If every letter is a bare `inline-block`, the browser may break a line in the middle of a word. In the full version of this lab you would swap this for GSAP's `SplitText`, which also handles lines, ligatures and re-splitting on resize. The live site uses SplitText only for splitting; all of its reveals are written by hand per frame, as here.

### `index.html` and `main.ts`

```html
<!-- lab/index.html -->
<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>L1: scroll is a number</title>
<style>
  html, body { margin: 0; background: #140304; color: #fff6f4; font: 16px/1.4 system-ui, sans-serif; }
  #story { height: 400vh; position: relative; }
  .pin { position: fixed; inset: 0; display: grid; place-content: center; gap: 1.5rem; padding: 0 6vw; }
  #headline { margin: 0; font-size: clamp(2.5rem, 9vw, 8rem); line-height: 0.95; letter-spacing: -0.03em; }
  #kicker { margin: 0; max-width: 32ch; opacity: 0; }
  #hud { position: fixed; left: 12px; bottom: 12px; font: 12px/1 ui-monospace, monospace; opacity: 0.7; }
</style>
<section id="story">
  <div class="pin">
    <p id="kicker">Every value on this page is a function of one number.</p>
    <h1 id="headline">Scroll is just a number</h1>
  </div>
</section>
<div id="hud"></div>
<script type="module" src="./main.ts"></script>
```

```ts
// lab/main.ts
import { fit } from './math';
import { sectionR } from './section';
import { attach, createScroll } from './scroll-engine';
import { driveHeadline, splitWords } from './reveal';

const story = document.getElementById('story')!;
const kicker = document.getElementById('kicker')!;
const hud = document.getElementById('hud')!;
const chars = splitWords(document.getElementById('headline')!);
const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;

const model = createScroll(story.offsetHeight - innerHeight);

attach(model, (y) => {
  const r = sectionR(y, story.offsetTop, innerHeight);
  const enter = fit(r, 1, 2.2); //   headline arrives between r = 1 and 2.2
  const exit = fit(r, 3, 3.8); //    and leaves between r = 3 and 3.8
  driveHeadline(chars, enter, exit, calm);
  kicker.style.opacity = String(fit(r, 1.6, 2.4) * (1 - fit(r, 3, 3.6)));
  hud.textContent = `y ${y}  r ${r.toFixed(3)}`;
});
```

## Exercises

1. **Draw the choreography.** On paper, list every `fit` window in `main.ts` as a bar on an `r` axis from 1 to 4, then check the bars against what you see at `r = 1.5, 2.5, 3.5`. This is the same chart [media/f03-choreography.png](../../media/f03-choreography.png) draws for the whole of Oryzo's first section.
2. **Prove reversibility.** Scroll to `y = 1000`, note the letters' opacities, scroll to 3000 and back to 1000. They must be identical. If they are not, something in your code keeps state between frames.
3. **Change the feel.** Set `EASE_RATE` to 7, then 20. The live site measured about 12 for keys and about 7 for the wheel. Which feels like a product page, and which like a text editor?
4. **Add lines.** Give the kicker a second line and stagger the two lines with `staggerWindow(group, 0, 2)` and `(group, 1, 2)`.
5. **Reduced motion.** Turn on the OS setting and confirm that only opacity moves.

## Common traps

- **Smoothing twice.** If a component also lerps toward the scroll value, you get lag stacked on lag, and a screenshot at `y` no longer matches a screenshot at the same `y` after a pause. Smooth in the engine only.
- **Reading `scrollY` instead of the engine's `y`.** They differ by up to one frame and a rounding step.
- **Letters that break mid-word** (see above).
- **Forgetting the `scroll` mirror.** Anchor links and scripted jumps then fight the engine.

## You're done when

- [ ] `y` and `r` in the HUD move as you scroll, and `r` reads 1.000 at the top of the page.
- [ ] At `y = 0` the headline is invisible; at `r = 2.2` every letter is fully opaque; at `r = 3.8` all are gone.
- [ ] Scrolling up replays the page backwards with no reverse code.
- [ ] `window.scrollTo(0, 1500)` from the console lands exactly there and the HUD agrees.
- [ ] With reduced motion on, nothing slides or blurs.

Next: [Lab L2, a fixed stage](lab-l2-fixed-stage.md).
