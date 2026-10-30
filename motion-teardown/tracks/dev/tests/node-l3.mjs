// t-l3.ts
import assert from "node:assert/strict";

// lab/spring.ts
var Spring = class {
  k1;
  k2;
  k3;
  xp;
  y;
  yd = 0;
  constructor(f, z, r, x0 = 0) {
    const w3 = Math.PI * f;
    this.k1 = z / w3;
    this.k2 = 1 / (2 * w3) ** 2;
    this.k3 = r * z / (2 * w3);
    this.xp = x0;
    this.y = x0;
  }
  update(dt, x) {
    if (dt <= 0) return this.y;
    const xd = (x - this.xp) / dt;
    this.xp = x;
    const k2 = Math.max(this.k2, dt * dt / 2 + dt * this.k1 / 2, dt * this.k1);
    this.y += dt * this.yd;
    this.yd += dt * (x + this.k3 * xd - this.y - this.k1 * this.yd) / k2;
    return this.y;
  }
};

// lab/math.ts
var clamp = (x, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, x));
var lerp = (a2, b2, t) => a2 + (b2 - a2) * t;
var ease = {
  linear: (t) => t,
  cubicIn: (t) => t * t * t,
  cubicOut: (t) => 1 - (1 - t) ** 3,
  sineIn: (t) => 1 - Math.cos(t * Math.PI / 2),
  expoOut: (t) => t >= 1 ? 1 : 1 - 2 ** (-10 * t),
  backOut: (t) => {
    const c = 1.70158;
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2;
  }
};
function fit(x, a2, b2, c = 0, d = 1, e = ease.linear) {
  const t = a2 === b2 ? x >= b2 ? 1 : 0 : clamp((x - a2) / (b2 - a2));
  return lerp(c, d, e(t));
}

// lab/bands.ts
function bandWeights(mouseX, mouseY, n = 4, inner = 0.2, outer = 0.3, out2 = new Array(n)) {
  const gate = fit(Math.abs(mouseX), inner, outer, 1, 0);
  const half = 2 / n;
  for (let j = 0; j < n; j++) {
    const centre = -1 + (j + 0.5) * half;
    out2[j] = Math.max(0, 1 - Math.abs(mouseY - centre) / half) * gate;
  }
  return out2;
}

// lab/bone-pose.ts
var BONE_STRIDE = 7;
function createBoneClip(boneCount, frameCount) {
  return { boneCount, frameCount, data: new Float32Array(boneCount * frameCount * BONE_STRIDE) };
}
function poseAt(clip2, ratio, posOut, rotOut) {
  const x = clamp(ratio) * (clip2.frameCount - 1);
  const f0 = Math.floor(x), f1 = Math.min(f0 + 1, clip2.frameCount - 1), t = x - f0;
  for (let b2 = 0; b2 < clip2.boneCount; b2++) {
    const a2 = (f0 * clip2.boneCount + b2) * BONE_STRIDE;
    const c = (f1 * clip2.boneCount + b2) * BONE_STRIDE;
    const d = clip2.data;
    for (let k = 0; k < 3; k++) posOut[b2 * 4 + k] = d[a2 + k] + (d[c + k] - d[a2 + k]) * t;
    posOut[b2 * 4 + 3] = 0;
    const dot = d[a2 + 3] * d[c + 3] + d[a2 + 4] * d[c + 4] + d[a2 + 5] * d[c + 5] + d[a2 + 6] * d[c + 6];
    const s2 = dot < 0 ? -1 : 1;
    let len = 0;
    for (let k = 0; k < 4; k++) {
      const v = d[a2 + 3 + k] + (s2 * d[c + 3 + k] - d[a2 + 3 + k]) * t;
      rotOut[b2 * 4 + k] = v;
      len += v * v;
    }
    len = Math.sqrt(len) || 1;
    for (let k = 0; k < 4; k++) rotOut[b2 * 4 + k] /= len;
  }
}
function skinPoint(p, bones, weights, pos3, rot3) {
  const out2 = [0, 0, 0];
  bones.forEach((b2, i) => {
    const w3 = weights[i];
    if (!w3) return;
    const [qx, qy, qz, qw] = [rot3[b2 * 4], rot3[b2 * 4 + 1], rot3[b2 * 4 + 2], rot3[b2 * 4 + 3]];
    const cx = qy * p[2] - qz * p[1] + qw * p[0];
    const cy = qz * p[0] - qx * p[2] + qw * p[1];
    const cz = qx * p[1] - qy * p[0] + qw * p[2];
    const r = [
      p[0] + 2 * (qy * cz - qz * cy),
      p[1] + 2 * (qz * cx - qx * cz),
      p[2] + 2 * (qx * cy - qy * cx)
    ];
    for (let k = 0; k < 3; k++) out2[k] += w3 * (r[k] + pos3[b2 * 4 + k]);
  });
  return out2;
}

// lab/bloom-grade.ts
function gaussianKernel(sigma, radius = Math.min(15, Math.ceil(sigma * 3))) {
  const w3 = Array.from({ length: radius + 1 }, (_, i) => Math.exp(-(i * i) / (2 * sigma * sigma)));
  const total = w3[0] + 2 * w3.slice(1).reduce((a2, b2) => a2 + b2, 0);
  return w3.map((v) => v / total);
}
var BLOOM_LEVELS = [2, 4, 8, 16, 32];
var BLOOM_SIGMA = 4;

// lab/perf.ts
var FrameStats = class {
  constructor(cap = 600) {
    this.cap = cap;
  }
  cap;
  ms = [];
  push(frameMs) {
    this.ms.push(frameMs);
    if (this.ms.length > this.cap) this.ms.shift();
  }
  percentile(p) {
    const s2 = [...this.ms].sort((a2, b2) => a2 - b2);
    return s2.length ? s2[Math.min(s2.length - 1, Math.floor(p / 100 * s2.length))] : 0;
  }
  get fps() {
    const m = this.ms.reduce((a2, b2) => a2 + b2, 0) / (this.ms.length || 1);
    return m ? 1e3 / m : 0;
  }
};
function renderScale(cssW, cssH, dpr, maxDpr = 1.5, maxPixels = 2560 * 1440) {
  const budget = Math.sqrt(maxPixels / (cssW * cssH));
  return Math.min(dpr, maxDpr, budget);
}

// t-l3.ts
var near = (a2, b2, e = 1e-3) => assert.ok(Math.abs(a2 - b2) < e, `${a2} vs ${b2}`);
var s = new Spring(2, 0.5, 1);
var y = 0;
var peak = 0;
for (let i = 0; i < 300; i++) {
  y = s.update(1 / 60, 1);
  peak = Math.max(peak, y);
}
near(y, 1, 1e-3);
assert.ok(peak > 1.05, "overshoot " + peak);
s = new Spring(2, 1, 1);
peak = 0;
for (let i = 0; i < 300; i++) {
  y = s.update(1 / 60, 1);
  peak = Math.max(peak, y);
}
assert.ok(peak <= 1.0001);
near(y, 1, 1e-3);
s = new Spring(2, 0.5, 1);
y = s.update(1 / 60, 1);
y = s.update(0.5, 1);
assert.ok(Number.isFinite(y) && Math.abs(y) < 5);
var a = new Spring(2, 0.5, 1);
var b = new Spring(2, 0.5, 1);
var ya = 0;
var yb = 0;
for (let i = 0; i < 60; i++) ya = a.update(1 / 60, 1);
for (let i = 0; i < 30; i++) yb = b.update(1 / 30, 1);
assert.ok(Math.abs(ya - yb) < 0.08, `${ya} ${yb}`);
var pb = new Spring(2, 0.5, -1);
var mn = 0;
for (let i = 0; i < 60; i++) mn = Math.min(mn, pb.update(1 / 60, 1));
assert.ok(mn < -0.01);
var w = bandWeights(0, -0.75);
assert.equal(w.length, 4);
near(w[0], 1);
near(w[1], 0);
var w2 = bandWeights(0, 0);
near(w2[1], 0.5);
near(w2[2], 0.5);
assert.deepEqual(bandWeights(0.5, 0.3), [0, 0, 0, 0]);
near(bandWeights(0.25, -0.75)[0], 0.5);
var clip = createBoneClip(2, 3);
var setB = (f, b2, t, q2) => clip.data.set([...t, ...q2], (f * 2 + b2) * BONE_STRIDE);
for (let f = 0; f < 3; f++) {
  setB(f, 0, [0, 0, 0], [0, 0, 0, 1]);
  setB(f, 1, [f * 0.5, 0, 0], [0, 0, 0, 1]);
}
var pos = new Float32Array(8);
var rot = new Float32Array(8);
poseAt(clip, 0.25, pos, rot);
near(pos[4], 0.25);
near(rot[7], 1);
poseAt(clip, 1, pos, rot);
near(pos[4], 1);
var out = skinPoint([0.3, -0.3, 0], [1, 0, 0, 0], [1, 0, 0, 0], pos, rot);
near(out[0], 1.3);
near(out[1], -0.3);
var q = [0, 0, Math.SQRT1_2, Math.SQRT1_2];
var rot2 = new Float32Array([0, 0, 0, 1, ...q]);
var pos2 = new Float32Array(8);
var r2 = skinPoint([0.3, -0.3, 0], [1, 0, 0, 0], [1, 0, 0, 0], pos2, rot2);
near(r2[0], 0.3);
near(r2[1], 0.3);
var bl = skinPoint([0.2, 0, 0], [0, 1, 0, 0], [0.5, 0.5, 0, 0], pos2, rot2);
near(bl[0], 0.1);
near(bl[1], 0.1);
for (const sg of [1, 3, 4, 11]) {
  const k = gaussianKernel(sg);
  near(k[0] + 2 * k.slice(1).reduce((x, y2) => x + y2, 0), 1, 1e-9);
  assert.ok(k.length <= 16);
  assert.ok(k[0] >= k[1]);
}
assert.equal(BLOOM_LEVELS.length, 5);
assert.ok(gaussianKernel(BLOOM_SIGMA).length <= 16);
var fs = new FrameStats(100);
for (let i = 0; i < 99; i++) fs.push(16.6);
fs.push(913);
near(fs.percentile(50), 16.6);
assert.ok(fs.percentile(99) > 900);
assert.ok(fs.percentile(95) < 17);
assert.ok(fs.fps < 45);
near(renderScale(1440, 900, 2), 1.5);
near(renderScale(1440, 900, 1), 1);
near(renderScale(3840, 2160, 2, 1.5), Math.sqrt(2560 * 1440 / (3840 * 2160)), 1e-6);
console.log("L3 pure tests OK");
