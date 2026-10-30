---
title: "Lab L3: a skinned character, springs and a post chain"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Lab L3: a skinned character, springs and a post chain

*Level 3 of the [level ladder](level-ladder.md). Needs L1 and L2. Two to three days if you start from nothing.*

**Goal.** Play a baked character animation by scroll with the skinning done on the GPU. Let the pointer nudge parts of it through springs, not raycasts. Add an edge glow driven by scroll, a bloom, a final grade, and keep the whole thing at 60 fps.

**Case.** The hand in oryzo.ai (by Lusion) is a custom mesh with 36 bones. Our reading of the code: baked frames 71 to 115 are played by scroll, and the bone transforms go to the shader through two small float textures, not through three.js's own skinning. Hover moves only the fingers, through four horizontal bands of mouse height and a spring, with no raycasting. The glow around the screen edge is a post pass driven by scroll, not hover; the same number tints the hand and raises the bloom. The post chain ends with bloom, a grade and a card blur. All the code on this page is ours, and none of it ships their format.

## Concepts

**GPU skinning from data textures.** Each vertex lists up to four bones and four weights. Each frame the CPU interpolates two baked poses into one pose, writes it into two `N × 1` float textures (translation and rotation per bone), and the vertex shader fetches the bones it needs with `texelFetch`. There is no bone matrix uniform array and no limit from uniform space.

**Baked, not simulated.** The bone data is the skinning transform for each bone relative to the bind pose, per frame, computed offline. Playback is a lookup by `ratio` (the same idea as the camera clip in L2).

**Springs.** A second-order spring takes a target and returns a smoothed value with a chosen response (frequency), overshoot (damping) and anticipation. One spring per band gives the fingers weight and a little life with a dozen lines.

**Bands, not raycasts.** If the question is "is the pointer near the hand and roughly at the height of this finger", you do not need geometry picking. Slice the screen into horizontal bands and give each finger a triangular weight along mouse height.

**Edge glow as a post pass.** Distance to the screen edge shapes a rim. A radial pulse leaves a chosen point on a fixed period. A four-colour cyclic gradient colours it. One scalar, `amount`, comes from scroll.

**Bloom and grade.** Bloom is a bright-pass, a few blur levels of growing width, and an add. The grade is the last pass: saturation, a vignette, and dither, so gradients do not band.

**Performance is a design input.** Cap the DPR, warm the shaders up before showing anything, and measure the 95th percentile, not the mean.

## The code

### `bone-pose.ts`: baked poses into two textures

```ts
// lab/bone-pose.ts
import { clamp } from './math';

/** frames[f][bone] = { t: [x,y,z], q: [x,y,z,w] }: the skinning transform that takes the bind pose to frame f. */
export interface BoneClip {
  boneCount: number;
  frameCount: number;
  data: Float32Array; // frame-major, bone-major, 7 floats: tx ty tz qx qy qz qw
}

export const BONE_STRIDE = 7;

export function createBoneClip(boneCount: number, frameCount: number): BoneClip {
  return { boneCount, frameCount, data: new Float32Array(boneCount * frameCount * BONE_STRIDE) };
}

/**
 * Interpolate frames at `ratio` (0..1) into two RGBA float buffers of boneCount texels each:
 * posOut  = (tx, ty, tz, 0)
 * rotOut  = (qx, qy, qz, qw)
 */
export function poseAt(clip: BoneClip, ratio: number, posOut: Float32Array, rotOut: Float32Array) {
  const x = clamp(ratio) * (clip.frameCount - 1);
  const f0 = Math.floor(x), f1 = Math.min(f0 + 1, clip.frameCount - 1), t = x - f0;
  for (let b = 0; b < clip.boneCount; b++) {
    const a = (f0 * clip.boneCount + b) * BONE_STRIDE;
    const c = (f1 * clip.boneCount + b) * BONE_STRIDE;
    const d = clip.data;
    for (let k = 0; k < 3; k++) posOut[b * 4 + k] = d[a + k] + (d[c + k] - d[a + k]) * t;
    posOut[b * 4 + 3] = 0;
    const dot = d[a + 3] * d[c + 3] + d[a + 4] * d[c + 4] + d[a + 5] * d[c + 5] + d[a + 6] * d[c + 6];
    const s = dot < 0 ? -1 : 1;
    let len = 0;
    for (let k = 0; k < 4; k++) {
      const v = d[a + 3 + k] + (s * d[c + 3 + k] - d[a + 3 + k]) * t;
      rotOut[b * 4 + k] = v;
      len += v * v;
    }
    len = Math.sqrt(len) || 1;
    for (let k = 0; k < 4; k++) rotOut[b * 4 + k] /= len;
  }
}

/** CPU reference for the shader: linear blend skinning of one point. Used by the tests. */
export function skinPoint(
  p: [number, number, number], bones: number[], weights: number[],
  pos: Float32Array, rot: Float32Array,
): [number, number, number] {
  const out: [number, number, number] = [0, 0, 0];
  bones.forEach((b, i) => {
    const w = weights[i];
    if (!w) return;
    const [qx, qy, qz, qw] = [rot[b * 4], rot[b * 4 + 1], rot[b * 4 + 2], rot[b * 4 + 3]];
    const cx = qy * p[2] - qz * p[1] + qw * p[0];
    const cy = qz * p[0] - qx * p[2] + qw * p[1];
    const cz = qx * p[1] - qy * p[0] + qw * p[2];
    const r = [
      p[0] + 2 * (qy * cz - qz * cy),
      p[1] + 2 * (qz * cx - qx * cz),
      p[2] + 2 * (qx * cy - qy * cx),
    ];
    for (let k = 0; k < 3; k++) out[k] += w * (r[k] + pos[b * 4 + k]);
  });
  return out;
}
```

### `skin-shader.ts`: the vertex shader

```ts
// lab/skin-shader.ts
export const SKIN_VERT = /* glsl */ `
precision highp float;
precision highp sampler2D;
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;
uniform sampler2D uBonePos;   // boneCount x 1, xyz = translation
uniform sampler2D uBoneRot;   // boneCount x 1, xyzw = quaternion
uniform vec4  uFingers;       // four band weights, 0..1
uniform float uLift;          // how far a finger perks up along its normal (world units)
in vec3 position;
in vec3 normal;
in vec4 aBones;               // four bone indices, stored as floats
in vec4 aWeights;
in float aFinger;             // -1: not a finger, 0..3: which band moves it
out vec3 vNormal;

vec3 rotate(vec4 q, vec3 v) {
  return v + 2.0 * cross(q.xyz, cross(q.xyz, v) + q.w * v);
}

void main() {
  vec3 p = vec3(0.0);
  vec3 n = vec3(0.0);
  for (int i = 0; i < 4; i++) {
    float w = aWeights[i];
    if (w <= 0.0) continue;
    int b = int(aBones[i] + 0.5);
    vec3 t = texelFetch(uBonePos, ivec2(b, 0), 0).xyz;
    vec4 q = texelFetch(uBoneRot, ivec2(b, 0), 0);
    p += w * (rotate(q, position) + t);
    n += w * rotate(q, normal);
  }
  n = normalize(n);
  float band = aFinger < 0.0 ? 0.0 : uFingers[int(aFinger + 0.5)];
  p += n * uLift * band;
  vNormal = n;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
}`;
```

### `skinned-mesh.ts`: wiring it into three.js

```ts
// lab/skinned-mesh.ts
import * as THREE from 'three';
import { SKIN_VERT } from './skin-shader';
import { type BoneClip, poseAt } from './bone-pose';

const FRAG = /* glsl */ `
precision highp float;
uniform vec3 uBase;
uniform vec3 uRim;
uniform float uHighlight;   // 0..1, scroll-driven tint
in vec3 vNormal;
out vec4 outColor;
void main() {
  vec3 n = normalize(vNormal);
  float rim = pow(1.0 - clamp(n.z, 0.0, 1.0), 3.0);
  outColor = vec4(uBase * (0.35 + 0.65 * max(n.y * 0.5 + 0.5, 0.0)) + uRim * rim * (0.4 + uHighlight), 1.0);
}`;

export function createSkinned(geometry: THREE.BufferGeometry, clip: BoneClip) {
  const posData = new Float32Array(clip.boneCount * 4);
  const rotData = new Float32Array(clip.boneCount * 4);
  const mk = (data: Float32Array) => {
    const t = new THREE.DataTexture(data, clip.boneCount, 1, THREE.RGBAFormat, THREE.FloatType);
    t.minFilter = t.magFilter = THREE.NearestFilter; // never filter bone data
    t.needsUpdate = true;
    return t;
  };
  const bonePos = mk(posData), boneRot = mk(rotData);

  const material = new THREE.RawShaderMaterial({
    glslVersion: THREE.GLSL3,
    vertexShader: SKIN_VERT,
    fragmentShader: FRAG,
    uniforms: {
      uBonePos: { value: bonePos },
      uBoneRot: { value: boneRot },
      uFingers: { value: new THREE.Vector4() },
      uLift: { value: 0.03 },
      uBase: { value: new THREE.Color('#f4eeee') },
      uRim: { value: new THREE.Color('#ff3030') },
      uHighlight: { value: 0 },
    },
  });
  const mesh = new THREE.Mesh(geometry, material);
  mesh.frustumCulled = false; // the bounding sphere is the bind pose's, not the animated one

  return {
    mesh,
    /** Call once per frame. */
    pose(ratio: number, fingers: ArrayLike<number>, highlight: number) {
      poseAt(clip, ratio, posData, rotData);
      bonePos.needsUpdate = true;
      boneRot.needsUpdate = true;
      material.uniforms.uFingers.value.fromArray(fingers as number[]);
      material.uniforms.uHighlight.value = highlight;
    },
  };
}
```

### `spring.ts` and `bands.ts`: hover without raycasting

```ts
// lab/spring.ts
/**
 * Second-order dynamics (the "t3ssel8r" formulation).
 * f: response in Hz. z: damping (0 = never settles, 1 = no overshoot, < 1 overshoots).
 * r: initial response. r > 1 anticipates, r < 0 pulls back first.
 */
export class Spring {
  private k1: number; private k2: number; private k3: number;
  private xp: number; private y: number; private yd = 0;

  constructor(f: number, z: number, r: number, x0 = 0) {
    const w = Math.PI * f;
    this.k1 = z / w;
    this.k2 = 1 / (2 * w) ** 2;
    this.k3 = (r * z) / (2 * w);
    this.xp = x0;
    this.y = x0;
  }

  update(dt: number, x: number): number {
    if (dt <= 0) return this.y;
    const xd = (x - this.xp) / dt;
    this.xp = x;
    // clamp k2 so large frame gaps (a background tab, a long frame) cannot blow the integration up
    const k2 = Math.max(this.k2, (dt * dt) / 2 + (dt * this.k1) / 2, dt * this.k1);
    this.y += dt * this.yd;
    this.yd += (dt * (x + this.k3 * xd - this.y - this.k1 * this.yd)) / k2;
    return this.y;
  }
}
```

```ts
// lab/bands.ts
import { fit } from './math';

/**
 * n horizontal bands across the screen. mouseY in NDC (-1 bottom .. 1 top).
 * Each band has a triangular weight centred on its own height.
 * mouseX gates the whole hand: full strength within `inner`, none beyond `outer` (NDC).
 */
export function bandWeights(mouseX: number, mouseY: number, n = 4, inner = 0.2, outer = 0.3, out: number[] = new Array(n)) {
  const gate = fit(Math.abs(mouseX), inner, outer, 1, 0);
  const half = 2 / n;
  for (let j = 0; j < n; j++) {
    const centre = -1 + (j + 0.5) * half;
    out[j] = Math.max(0, 1 - Math.abs(mouseY - centre) / half) * gate;
  }
  return out;
}
```

In the frame loop: `const w = bandWeights(mx, my); springs.forEach((s, j) => fingers[j] = s.update(dt, w[j]));` and pass `fingers` to `skinned.pose`. Gate the whole thing by a scroll window, as the original does, so the hand is inert until the instruction text has arrived.

### `edge-glow.ts`: a scroll-driven rim with a pulse

```ts
// lab/edge-glow.ts
export const EDGE_GLOW_FRAG = /* glsl */ `
precision highp float;
uniform sampler2D uScene;
uniform vec2  uRes;        // px
uniform float uAmount;     // 0..1: comes from scroll, not from hover
uniform float uTime;       // s
uniform vec2  uOrigin;     // pulse origin in uv; we use a point on the scrollbar
uniform float uPad;        // px: how far the rim reaches in from the edge
uniform vec3  uColors[4];
in vec2 vUv;
out vec4 outColor;

vec3 palette(float t) {    // cyclic four-stop gradient
  float x = fract(t) * 4.0;
  int i = int(floor(x));
  float f = smoothstep(0.0, 1.0, fract(x));
  return mix(uColors[i], uColors[(i + 1) & 3], f);
}

void main() {
  vec4 scene = texture(uScene, vUv);
  vec2 px = vUv * uRes;
  float edge = min(min(px.x, uRes.x - px.x), min(px.y, uRes.y - px.y));
  float rim = pow(1.0 - clamp(edge / uPad, 0.0, 1.0), 3.0);

  float aspect = uRes.x / uRes.y;
  vec2 d = (vUv - uOrigin) * vec2(aspect, 1.0);
  float front = fract(uTime * 0.5) * 2.5;                  // one pulse every 2 s
  float wave = exp(-pow((length(d) - front) * 6.0, 2.0));

  float angle = atan(vUv.y - 0.5, (vUv.x - 0.5) * aspect);
  vec3 glow = palette(angle / 6.2831853 + uTime * 0.1);
  outColor = vec4(scene.rgb + glow * rim * (0.6 + 1.2 * wave) * uAmount, scene.a);
}`;
```

Drive it with a window you author in `r`, the same way as in L1: `amount = fit(r, a, a + 0.5) * fit(r, b, b + 0.5, 1, 0)`. In the case, the glow turns on over 450 px of scroll (4,950 to 5,400) and off over 450 px (6,750 to 7,200), and that same scalar raises the bloom and tints the hand.

### `bloom-grade.ts`: kernel, blur, grade

```ts
// lab/bloom-grade.ts

/** One-sided gaussian weights for offsets 0..radius (at most 15, the shader's limit), normalised so the two-sided kernel sums to 1. */
export function gaussianKernel(sigma: number, radius = Math.min(15, Math.ceil(sigma * 3))): number[] {
  const w = Array.from({ length: radius + 1 }, (_, i) => Math.exp(-(i * i) / (2 * sigma * sigma)));
  const total = w[0] + 2 * w.slice(1).reduce((a, b) => a + b, 0);
  return w.map((v) => v / total);
}

/**
 * Five levels at 1/2, 1/4, 1/8, 1/16 and 1/32 of the screen. The same narrow kernel on a smaller texture
 * is a wider blur on screen, so one kernel is enough. (The original's five levels used sigmas of 3 to 11.)
 */
export const BLOOM_LEVELS = [2, 4, 8, 16, 32];
export const BLOOM_SIGMA = 4; // in texels of each level; radius 12 fits the 16-tap shader

export const BRIGHT_FRAG = /* glsl */ `
precision highp float;
uniform sampler2D uScene;
uniform float uThreshold;   // luminance where bloom starts
uniform float uKnee;        // softness of the start
in vec2 vUv;
out vec4 outColor;
void main() {
  vec3 c = texture(uScene, vUv).rgb;
  float l = dot(c, vec3(0.2126, 0.7152, 0.0722));
  float k = clamp((l - uThreshold + uKnee) / (2.0 * uKnee + 1e-4), 0.0, 1.0);
  outColor = vec4(c * k * k, 1.0);
}`;

export const BLUR_FRAG = /* glsl */ `
precision highp float;
uniform sampler2D uSrc;
uniform vec2  uDir;          // (1/width, 0) or (0, 1/height)
uniform float uWeights[16];  // one-sided kernel from gaussianKernel
uniform int   uRadius;       // <= 15
in vec2 vUv;
out vec4 outColor;
void main() {
  vec3 sum = texture(uSrc, vUv).rgb * uWeights[0];
  for (int i = 1; i < 16; i++) {
    if (i > uRadius) break;
    vec2 o = uDir * float(i);
    sum += (texture(uSrc, vUv + o).rgb + texture(uSrc, vUv - o).rgb) * uWeights[i];
  }
  outColor = vec4(sum, 1.0);
}`;

export const GRADE_FRAG = /* glsl */ `
precision highp float;
uniform sampler2D uScene;
uniform sampler2D uBloom;
uniform vec2  uRes;
uniform float uBloomAmount;
uniform float uSaturation;     // 1 = unchanged
uniform vec3  uTint;
uniform float uTintAmount;     // small: 0.015 is already visible
uniform vec2  uVignette;       // inner and outer radius, in half-heights
uniform float uSeed;           // change every frame so the dither does not freeze
in vec2 vUv;
out vec4 outColor;
void main() {
  vec3 c = texture(uScene, vUv).rgb + texture(uBloom, vUv).rgb * uBloomAmount;
  float l = dot(c, vec3(0.2126, 0.7152, 0.0722));
  c = mix(vec3(l), c, uSaturation);
  c = mix(c, c + uTint - c * uTint, uTintAmount);                 // screen blend
  vec2 q = (vUv - 0.5) * vec2(uRes.x / uRes.y, 1.0) * 2.0;        // aspect-correct
  c *= 1.0 - smoothstep(uVignette.x, uVignette.y, length(q)) * 0.6;
  c = pow(max(c, 0.0), vec3(1.0 / 2.2));
  float n = fract(52.9829189 * fract(dot(gl_FragCoord.xy + uSeed * vec2(17.0, 31.0), vec2(0.06711056, 0.00583715))));
  outColor = vec4(c + (n - 0.5) / 255.0, 1.0);                    // one 8-bit step of noise
}`;
```

In the chain, run: scene → target A; bright-pass → B; for each sigma: blur horizontally and vertically at its own size; sum into the bloom texture; grade reads `uScene` and `uBloom`. The shaders above are the building blocks; the ping-pong plumbing is the L2 pattern repeated. On the live site the order is anti-aliasing, glow, bloom, grade, card blur, and that order matters: the glow should bloom, and the grade should see everything.

### `perf.ts`: measure before you tune

```ts
// lab/perf.ts

/** Rolling frame-time sampler. Report p50 and p95, not the mean: a single 900 ms hitch barely moves an average taken over thousands of frames. */
export class FrameStats {
  private ms: number[] = [];
  constructor(private cap = 600) {}
  push(frameMs: number) {
    this.ms.push(frameMs);
    if (this.ms.length > this.cap) this.ms.shift();
  }
  percentile(p: number): number {
    const s = [...this.ms].sort((a, b) => a - b);
    return s.length ? s[Math.min(s.length - 1, Math.floor((p / 100) * s.length))] : 0;
  }
  get fps(): number {
    const m = this.ms.reduce((a, b) => a + b, 0) / (this.ms.length || 1);
    return m ? 1000 / m : 0;
  }
}

/** Device pixel ratio with a ceiling, and a ceiling on total pixels. */
export function renderScale(cssW: number, cssH: number, dpr: number, maxDpr = 1.5, maxPixels = 2560 * 1440): number {
  const budget = Math.sqrt(maxPixels / (cssW * cssH));
  return Math.min(dpr, maxDpr, budget);
}
```

Warm-up matters as much as the cap. Compile and draw every material once, off-screen, before you say "ready". In our rebuild a shader warm-up of about 250 ms before `ready` removed a 913 ms first-use hitch from the middle of the scroll.

## Exercises

1. **Bake a hand-sized rig.** Make a four-bone finger in Blender, bake it over 60 frames as skinning transforms, export to a flat `Float32Array`, and play it with `poseAt`. Start with two bones if four fights you.
2. **Prove the shader.** Write a test that skins one vertex on the CPU with `skinPoint` and checks the same vertex on screen after a draw. Our own test does this in a headless browser.
3. **Tune a spring by ear.** Try `(f=2, z=0.5, r=1)`, `(f=4, z=0.3, r=2)` and `(f=1, z=1, r=0)` on the finger weights. Describe each in one word.
4. **Pair the post chain.** Move the glow ahead of the bloom, then behind it. What changes on the rim? Which order would you keep?
5. **Budget it.** Run a scroll from top to bottom with `FrameStats`, and then at DPR 1.0, 1.5 and 2.0. Record p95 at each.

## Common traps

- **`frustumCulled`.** The bounding sphere belongs to the bind pose, so an animated mesh disappears when the bind pose leaves the screen. Turn culling off.
- **Float texture filtering.** Bone data must be `NearestFilter`. Linear filtering blends neighbouring bones.
- **Four influences, not five.** Normalise weights offline. A vertex whose weights sum to 0.9 sits 10% inside the origin.
- **Springs on a stalled tab.** After a long gap, `dt` can be seconds. Clamp `dt` in the loop (we clamp at 1/15 s) and keep the `k2` guard.
- **Dither that never moves.** A fixed noise pattern looks like a dirty screen. Re-seed it each frame.
- **Counting the mean.** A 913 ms hitch hides in an average over thousands of frames.

## You're done when

- [ ] Scrolling plays the baked animation forwards and backwards with no clock.
- [ ] The CPU reference and the shader agree to within one pixel on at least three poses.
- [ ] Moving the pointer to a band lifts the matching finger with a visible, settling overshoot, and does nothing outside the hand's horizontal gate.
- [ ] The glow is a function of scroll only: hovering with the page at rest changes nothing about it.
- [ ] A top-to-bottom scroll has p95 frame time at or under 17 ms on your machine at your DPR cap, or you can name the pass that costs the rest.
- [ ] With `prefers-reduced-motion`, idle wobble and the pulse stop; scroll-driven states remain.

Next: the deep dives ([reading a minified bundle](deep-dives/reading-a-minified-bundle.md), [capturing scenes and shaders](deep-dives/capturing-scenes-and-shaders.md), [custom binary models](deep-dives/custom-binary-models.md), [the resilient loader](deep-dives/resilient-loader.md)).
