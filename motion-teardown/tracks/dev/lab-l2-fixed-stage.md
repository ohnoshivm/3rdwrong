---
title: "Lab L2: a fixed stage under the page"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Lab L2: a fixed stage under the page

*Level 2 of the [level ladder](level-ladder.md). Needs L1 and three.js. About half a day.*

**Goal.** Put one fixed WebGL canvas behind the page. Render the scene into an offscreen target, play one baked camera move by scrolling, and add a post pass that blurs and tints the picture only underneath a block of text, so the copy appears to sit on frosted glass.

**Case.** On oryzo.ai by Lusion the canvas is fixed, full-screen and behind every piece of DOM text. Our reading of the code: the frosted card on the hero is not CSS `backdrop-filter`. It is a post pass, which is why the blur can follow a rounded rectangle, ramp with scroll, and never touch the layout. The hero copy sits on a rectangular mask whose blur radius grows with the cube of the mask value and whose colour mixes 80% toward an olive tint at full strength. The camera path of the first scroll section is baked offline and sampled by scroll. All the code on this page is ours.

## Concepts

**A fixed stage.** `position: fixed; inset: 0; z-index: 0` for the canvas, and normal DOM above it. The page scrolls; the canvas never moves. Scroll becomes a number (L1) and the number goes into uniforms.

**Render to target.** Draw the scene into a `WebGLRenderTarget` first, not the screen. The target is a texture. A second full-screen draw reads that texture, does whatever it likes with it (blur, grade, glow) and writes the canvas. Every later effect in [L3](lab-l3-character-and-post.md) is another pass of this kind.

**A masked blur.** The mask is a signed-distance rounded rectangle taken from the real DOM rect of the text block, so layout and glass stay in step at any viewport. Blur radius is `mask³ × maxRadius`: the cube keeps the edge soft and the centre strong. The taps follow a golden-angle spiral, which spreads a modest tap count evenly over the disc.

**A baked animation, played by scroll.** An artist (or a script) records a camera or object path once, as one pose per frame. At runtime you never run a clock; you turn scroll into a ratio from 0 to 1 and interpolate between two stored poses. Scrubbing backwards is free.

**Linear in, encoded out.** Inside the target, colour is linear. The last pass encodes for the screen. If you skip it the picture looks too dark and the blur looks wrong.

## The code

### `mask-blur.ts`: the shaders

```ts
// lab/mask-blur.ts
// Raw shaders: we declare everything ourselves, so the same strings also run in plain WebGL2.
// three adds the "#version 300 es" line when the material has glslVersion: THREE.GLSL3.

export const FULLSCREEN_VERT = /* glsl */ `
precision highp float;
in vec3 position;
out vec2 vUv;
void main() {
  vUv = position.xy * 0.5 + 0.5;
  gl_Position = vec4(position.xy, 0.0, 1.0);
}`;

export const MASK_BLUR_FRAG = /* glsl */ `
precision highp float;
uniform sampler2D uScene;
uniform vec2  uRes;        // target size in device pixels
uniform vec4  uRect;       // centre x, centre y, half width, half height (device px, y down)
uniform float uCorner;     // corner radius in px
uniform float uFeather;    // px over which the mask fades outside the rectangle
uniform float uBlur;       // 0..1, from scroll
uniform float uMaxRadius;  // px, blur radius at full mask
uniform vec3  uTint;
uniform float uTintMix;    // how far the tint can take over (0.8 in our reading of the original)
in vec2 vUv;
out vec4 outColor;

float roundedBox(vec2 p, vec2 halfSize, float r) {
  vec2 q = abs(p) - halfSize + r;
  return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
}

const int TAPS = 32;
const float GOLDEN = 2.39996323;

void main() {
  vec2 px = vec2(vUv.x, 1.0 - vUv.y) * uRes;               // y down, like the DOM
  float d = roundedBox(px - uRect.xy, uRect.zw, uCorner);   // < 0 inside the rectangle
  float mask = (1.0 - smoothstep(0.0, uFeather, d)) * uBlur;
  float radius = mask * mask * mask * uMaxRadius;

  vec3 sum = vec3(0.0);
  for (int i = 0; i < TAPS; i++) {
    float fi = float(i) + 0.5;
    float rr = sqrt(fi / float(TAPS)) * radius;             // even density over the disc
    float a = fi * GOLDEN;
    sum += texture(uScene, vUv + vec2(cos(a), sin(a)) * rr / uRes).rgb;
  }
  vec3 col = mix(sum / float(TAPS), uTint, mask * uTintMix);
  outColor = vec4(pow(col, vec3(1.0 / 2.2)), 1.0);           // encode for the screen
}`;
```

### `baked-clip.ts`: one animation, played by a number

```ts
// lab/baked-clip.ts
import { clamp } from './math';

export const STRIDE = 7; // px py pz qx qy qz qw per frame

export type Pose = { p: [number, number, number]; q: [number, number, number, number] };

export class BakedClip {
  constructor(readonly frames: Float32Array, readonly count: number) {}

  /** Record f(t) at `count` evenly spaced t in 0..1. Done once, offline or at load time. */
  static bake(count: number, f: (t: number) => Pose): BakedClip {
    const frames = new Float32Array(count * STRIDE);
    for (let i = 0; i < count; i++) {
      const { p, q } = f(i / (count - 1));
      frames.set(p, i * STRIDE);
      frames.set(q, i * STRIDE + 3);
    }
    return new BakedClip(frames, count);
  }

  /** ratio 0..1 -> interpolated pose. Pure function of ratio, so scrubbing backwards is free. */
  sample(ratio: number, p: number[] = [0, 0, 0], q: number[] = [0, 0, 0, 1]) {
    const x = clamp(ratio) * (this.count - 1);
    const i = Math.floor(x);
    const j = Math.min(i + 1, this.count - 1);
    const t = x - i;
    const a = i * STRIDE, b = j * STRIDE, f = this.frames;
    for (let k = 0; k < 3; k++) p[k] = f[a + k] + (f[b + k] - f[a + k]) * t;
    // normalised lerp; flip the second quaternion if it sits on the far side of the hypersphere
    const dot = f[a + 3] * f[b + 3] + f[a + 4] * f[b + 4] + f[a + 5] * f[b + 5] + f[a + 6] * f[b + 6];
    const s = dot < 0 ? -1 : 1;
    let len = 0;
    for (let k = 0; k < 4; k++) {
      q[k] = f[a + 3 + k] + (s * f[b + 3 + k] - f[a + 3 + k]) * t;
      len += q[k] * q[k];
    }
    len = Math.sqrt(len) || 1;
    for (let k = 0; k < 4; k++) q[k] /= len;
    return { p, q };
  }
}

/** A stand-in for an artist's camera move: a slow orbit that rises, looking at the origin. */
export const orbit = (t: number): Pose => {
  const a = t * Math.PI * 0.9;
  return {
    p: [Math.sin(a) * 8, 0.5 + t * 3, Math.cos(a) * 8],
    q: [0, Math.sin(a / 2), 0, Math.cos(a / 2)],
  };
};
```

### `stage.ts`: fixed canvas, target, post pass

```ts
// lab/stage.ts
import * as THREE from 'three';
import { FULLSCREEN_VERT, MASK_BLUR_FRAG } from './mask-blur';
import { BakedClip, orbit } from './baked-clip';

export interface StageState {
  ratio: number; //                                    0..1: where the baked camera move is
  blur: number; //                                     0..1: how much glass
  rect: { x: number; y: number; w: number; h: number }; // CSS px, y down: the text block
}

export function createStage(canvas: HTMLCanvasElement) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: false });
  const dpr = () => Math.min(1.5, devicePixelRatio); // a cap is the cheapest speed-up there is
  renderer.setPixelRatio(dpr());

  // The world: a checkered floor (so blur is easy to see) and one solid object.
  const scene = new THREE.Scene();
  scene.background = new THREE.Color('#5a0c12');
  const checker = document.createElement('canvas');
  checker.width = checker.height = 256;
  const g = checker.getContext('2d')!;
  for (let y = 0; y < 8; y++) for (let x = 0; x < 8; x++) {
    g.fillStyle = (x + y) % 2 ? '#fff6f4' : '#e3141b';
    g.fillRect(x * 32, y * 32, 32, 32);
  }
  const tex = new THREE.CanvasTexture(checker);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
  tex.repeat.set(6, 6);
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.MeshBasicMaterial({ map: tex }));
  floor.rotation.x = -Math.PI / 2;
  const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(1, 0.35, 128, 16), new THREE.MeshNormalMaterial());
  knot.position.y = 1.2;
  scene.add(floor, knot);

  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 100);
  const clip = BakedClip.bake(116, orbit);

  // Render target: the scene lands here first, in linear half-float colour.
  const target = new THREE.WebGLRenderTarget(1, 1, { type: THREE.HalfFloatType });

  const post = new THREE.RawShaderMaterial({
    glslVersion: THREE.GLSL3,
    vertexShader: FULLSCREEN_VERT,
    fragmentShader: MASK_BLUR_FRAG,
    depthTest: false,
    depthWrite: false,
    uniforms: {
      uScene: { value: target.texture },
      uRes: { value: new THREE.Vector2(1, 1) },
      uRect: { value: new THREE.Vector4() },
      uCorner: { value: 24 },
      uFeather: { value: 40 },
      uBlur: { value: 0 },
      uMaxRadius: { value: 36 },
      uTint: { value: new THREE.Color('#7a1a20') },
      uTintMix: { value: 0.8 },
    },
  });
  const postScene = new THREE.Scene();
  postScene.add(new THREE.Mesh(new THREE.PlaneGeometry(2, 2), post));
  postScene.children[0].frustumCulled = false;
  const postCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);

  function resize(w: number, h: number) {
    renderer.setPixelRatio(dpr());
    renderer.setSize(w, h, false);
    const pw = Math.round(w * dpr()), ph = Math.round(h * dpr());
    target.setSize(pw, ph);
    post.uniforms.uRes.value.set(pw, ph);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }

  function update(s: StageState, time: number) {
    const { p, q } = clip.sample(s.ratio);
    camera.position.set(p[0], p[1], p[2]);
    camera.quaternion.set(q[0], q[1], q[2], q[3]);
    knot.rotation.y = time * 0.4;

    const k = dpr();
    post.uniforms.uRect.value.set((s.rect.x + s.rect.w / 2) * k, (s.rect.y + s.rect.h / 2) * k, (s.rect.w / 2) * k, (s.rect.h / 2) * k);
    post.uniforms.uBlur.value = s.blur;

    renderer.setRenderTarget(target);
    renderer.render(scene, camera);
    renderer.setRenderTarget(null);
    renderer.render(postScene, postCam);
  }

  return { renderer, resize, update, post };
}
```

### `main-l2.ts`: wire it to L1's engine

Add a `<canvas id="gl">` with `position: fixed; inset: 0; z-index: 0` to your L1 `index.html`, raise `.pin` to `z-index: 1`, and replace `main.ts` with:

```ts
// lab/main-l2.ts
import { fit } from './math';
import { sectionR } from './section';
import { attach, createScroll } from './scroll-engine';
import { driveHeadline, splitWords } from './reveal';
import { createStage } from './stage';

const story = document.getElementById('story')!;
const copy = document.getElementById('kicker')!; // the text block that sits "under glass"
const chars = splitWords(document.getElementById('headline')!);
const stage = createStage(document.getElementById('gl') as HTMLCanvasElement);

const onResize = () => stage.resize(innerWidth, innerHeight);
addEventListener('resize', onResize);
onResize();

const model = createScroll(story.offsetHeight - innerHeight);
let time = 0;

attach(model, (y, dt) => {
  time += dt;
  const r = sectionR(y, story.offsetTop, innerHeight);
  driveHeadline(chars, fit(r, 1, 2.2), fit(r, 3, 3.8));
  copy.style.opacity = String(fit(r, 1.6, 2.4));
  const b = copy.getBoundingClientRect();
  stage.update(
    { ratio: fit(r, 1, 4), blur: fit(r, 1.4, 2.2), rect: { x: b.x - 24, y: b.y - 24, w: b.width + 48, h: b.height + 48 } },
    time,
  );
});
```

## Exercises

1. **Find the cube.** Change `mask * mask * mask` to `mask * mask`, then to plain `mask`. Look at the edge of the glass in each. Explain in one sentence why the cube reads as "frosted" rather than "smeared".
2. **Bake your own move.** Replace `orbit` with a path of your own (a dolly in, a crane up). `BakedClip.bake` does not care where poses come from. If you have Blender, export a camera animation as JSON and fill the `Float32Array` from it.
3. **Add a second mask.** Pass a second rectangle (a card) and take the larger of the two masks.
4. **Tint to your palette.** The tint, `uTintMix` and the background colour are three uniforms. Pick a palette first, then see how few values change the mood.
5. **Measure.** Sample frame times for ten seconds of scrolling (the `FrameStats` class in [L3](lab-l3-character-and-post.md)). Cap the DPR at 1.0 and compare.

## Common traps

- **Mask in the wrong units.** The rect comes from the DOM in CSS pixels and the shader works in device pixels. Multiply by the DPR you actually render at, not `devicePixelRatio`. We capped ours at 1.5.
- **Y flipped.** The DOM is y-down; texture coordinates are y-up. The shader flips once, explicitly.
- **Colour space.** A half-float target is linear. Without the final encode, everything looks crushed.
- **Quaternion flips.** Interpolating two quaternions on opposite sides of the hypersphere sends the camera the long way round. The sign test in `sample` is there for that.
- **Visible taps.** 32 taps show as faint streaks at the full radius. Raise `TAPS`, or rotate the spiral by a per-pixel noise value, if that bothers you.
- **Layout thrash.** `getBoundingClientRect` each frame is fine for a few elements, but never write styles between reads.

## You're done when

- [ ] The canvas stays put while the page scrolls, and DOM text stays crisp above it.
- [ ] The camera orbit is driven only by scroll: scrubbing back plays it in reverse, and stopping stops it.
- [ ] At `blur = 0` the picture is untouched; at `blur = 1` the region under the copy is soft and tinted, and everything outside it is sharp.
- [ ] Resizing the window keeps the glass aligned with the text.
- [ ] A frame-time sample over a scroll from top to bottom has a 95th percentile under 17 ms on your machine, or you can say what stops it.

Next: [Lab L3, a character and a post chain](lab-l3-character-and-post.md).
