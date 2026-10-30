---
title: "Deep dive: capturing three.js scenes and shaders from a live page"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Deep dive: capturing three.js scenes and shaders from a live page

This is the capture method for inspecting a WebGL site you are allowed to study. It publishes a method, not anyone's assets: you run it yourself, on your own machine, and keep the output private.

On oryzo.ai (by Lusion) it gave us the scene graph, 19 dumped shader programs of about 25, and the draw-call picture. Everything below is general.

## What you can and cannot capture

| Want | Method | Works when |
| --- | --- | --- |
| Scenes, renderers, objects, materials, uniforms | The three.js devtools hook | The site uses three.js, even a modified build (the hook fired on Lusion's) |
| Every GLSL source, paired by program | Wrap `shaderSource`, `attachShader`, `linkProgram` | Any WebGL site |
| Draw calls per frame, context attributes | Wrap `drawElements`, `drawArrays`, `getContext` | Any WebGL site |
| Real GPU timing | A real GPU, headed Chrome | Headless software rendering would mislead you |
| Scene state at each scroll position | Evaluate in the page after each scripted scroll | You can drive the page (see [the playbook](../../../playbook/03-teardown.md)) |

## 1. The hook must run before the page's scripts

Three.js announces its scenes and renderers to a global named `__THREE_DEVTOOLS__` if one exists when they are constructed. Create it first, with Playwright's `addInitScript`. The init script below is ours; it also wraps the shader functions.

```js
// lab/capture-init.js
// Run before any page script: context.addInitScript({ path: 'capture-init.js' })
window.__THREE_DEVTOOLS__ = new EventTarget();
window.__RE = { scenes: [], renderers: [], programs: [], contexts: [], draws: 0 };

window.__THREE_DEVTOOLS__.addEventListener('observe', (e) => {
  const o = e.detail;
  if (o.isScene) window.__RE.scenes.push(o);
  if (o.isWebGLRenderer) window.__RE.renderers.push(o);
});

const sources = new WeakMap(); // shader  -> source text
const attached = new WeakMap(); // program -> [shaders]

for (const Ctx of [window.WebGLRenderingContext, window.WebGL2RenderingContext]) {
  if (!Ctx) continue;
  const proto = Ctx.prototype;
  const { shaderSource, attachShader, linkProgram, drawArrays, drawElements } = proto;

  proto.shaderSource = function (shader, src) {
    sources.set(shader, src);
    return shaderSource.call(this, shader, src);
  };
  proto.attachShader = function (program, shader) {
    if (!attached.has(program)) attached.set(program, []);
    attached.get(program).push(shader);
    return attachShader.call(this, program, shader);
  };
  proto.linkProgram = function (program) {
    const parts = (attached.get(program) ?? []).map((s) => sources.get(s));
    window.__RE.programs.push({ vertex: parts[0] ?? null, fragment: parts[1] ?? null });
    return linkProgram.call(this, program);
  };
  proto.drawArrays = function (...a) { window.__RE.draws++; return drawArrays.apply(this, a); };
  proto.drawElements = function (...a) { window.__RE.draws++; return drawElements.apply(this, a); };
}

const getContext = HTMLCanvasElement.prototype.getContext;
HTMLCanvasElement.prototype.getContext = function (type, attrs) {
  const gl = getContext.call(this, type, attrs);
  if (gl && /webgl/.test(type)) window.__RE.contexts.push({ type, attrs: attrs ?? null });
  return gl;
};

/** Flat list of the scene graph, safe to JSON.stringify. */
window.__RE.dump = (scene = window.__RE.scenes[0]) => {
  const rows = [];
  const walk = (o, depth) => {
    rows.push({
      depth, type: o.type, name: o.name || null,
      vertices: o.geometry?.attributes?.position?.count ?? null,
      material: Array.isArray(o.material) ? o.material.map((m) => m.type) : o.material?.type ?? null,
      position: o.position ? o.position.toArray() : null,
    });
    o.children.forEach((c) => walk(c, depth + 1));
  };
  if (scene) walk(scene, 0);
  return rows;
};
```

**The paste trap.** If you give this code to an agent in a chat message, check how Markdown renders it. In our case, the double underscores in `__THREE_DEVTOOLS__` were turned into bold text and the name lost its underscores. Always put code in a fenced block, and tell agents to paste it into files as plain text.

## 2. Launch like a person with a GPU

Headless software rendering changes frame times and sometimes behaviour. Use headed system Chrome and record what GPU you got. Ours was ANGLE Metal on an Apple M3, with no software fallback.

```js
// lab/capture.mjs
import { chromium } from 'playwright-core';
const browser = await chromium.launch({
  channel: 'chrome',
  headless: false,
  args: ['--use-angle=metal', '--ignore-gpu-blocklist'], // macOS; adjust for your platform
});
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
await context.addInitScript({ path: 'capture-init.js' });
const page = await context.newPage();
page.on('requestfailed', (r) => console.log('FAIL', r.url(), r.failure()?.errorText));
page.on('response', (r) => { if (r.status() >= 400) console.log('HTTP', r.status(), r.url()); });
await page.goto(process.argv[2]);
await page.waitForFunction(() => window.__RE.renderers.length > 0, null, { timeout: 30_000 });
const info = await page.evaluate(() => ({
  scenes: window.__RE.scenes.length,
  graph: window.__RE.dump(),
  programs: window.__RE.programs.length,
  renderer: window.__RE.renderers[0] && {
    pixelRatio: window.__RE.renderers[0].getPixelRatio(),
    toneMapping: window.__RE.renderers[0].toneMapping,
  },
}));
console.log(JSON.stringify(info).slice(0, 2000));
await browser.close();
```

Log failed and non-2xx requests from the start. A missing asset is the most common reason a heavy site never finishes loading in automation (see [the resilient loader](resilient-loader.md)).

## 3. Save shaders to files, never to the conversation

```js
// after the page has loaded and you have scrolled through the scope
import { writeFileSync, mkdirSync } from 'node:fs';
const programs = await page.evaluate(() => window.__RE.programs);
mkdirSync('captures/shaders', { recursive: true });
programs.forEach((p, i) => {
  writeFileSync(`captures/shaders/${String(i).padStart(2, '0')}.vert.glsl`, p.vertex ?? '');
  writeFileSync(`captures/shaders/${String(i).padStart(2, '0')}.frag.glsl`, p.fragment ?? '');
});
```

Then read them as a physicist reads a spectrum: first the **uniform names** (they tell you what is parameterised: `u_blurRect`, `u_time`, `u_fingerWeights`), then the **texture samplers** (what is read), then the maths. Pair each program with the effect it implements and note it in a `shaders/README.md`. Programs that were compiled before your hook ran, or lazily on first use, are missing: note them by the line in the bundle that builds them (see [reading a minified bundle](reading-a-minified-bundle.md)).

These dumps are third-party shader code. **Keep them private**, describe the technique in your own words, and write your own GLSL (the [L2](../lab-l2-fixed-stage.md) and [L3](../lab-l3-character-and-post.md) labs are examples).

## 4. Read scene state at each scroll position

After each scripted `window.scrollTo`, evaluate the objects you care about:

```js
const state = await page.evaluate(() => {
  const o = window.__RE.scenes[0].getObjectByName('hand'); // use a name you found in the graph dump
  return o && { position: o.position.toArray(), quaternion: o.quaternion.toArray(), scale: o.scale.toArray() };
});
```

Custom engines often keep state in their own classes, not in three.js objects. When `getObjectByName` finds nothing, use the bundle to find the owner, or read **uniform values** off the program instead. In our case the useful channels (an animation ratio on one object, glow amount, finger weights) were all uniforms.

## 5. Traps

- **Hook after the engine.** If the init script runs late, `__THREE_DEVTOOLS__` is never seen. Use `addInitScript`, not `evaluate`.
- **Modified builds.** The site's three.js may be forked. The event fired on Lusion's, but property names inside objects may differ. Dump and look.
- **Contended machines.** Our agents B and C ran Chrome at the same time, so their frame-rate figures are floors, not measurements. Say so in the notes.
- **Partial shader coverage.** 19 of about 25 programs dumped. Write that in the report instead of implying completeness.
- **Capturing what you may not keep.** Models, textures and shaders are the owner's. Record them for study, never publish them.

## You're done when

- [ ] The init script runs before page scripts, and `__RE.scenes` and `__RE.renderers` are non-empty.
- [ ] A scene-graph JSON, a renderer settings note (pixel ratio, antialias, tone mapping) and a draw-call count exist as files.
- [ ] Every dumped program is saved as a pair of files and mapped to an effect in a README, with unmapped ones listed by line number.
- [ ] You noted which GPU you used and whether anything else was competing for it.
- [ ] Nothing captured is staged for publication.
