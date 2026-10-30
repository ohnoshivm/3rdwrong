// t-l2.ts
import assert from "node:assert/strict";

// lab/math.ts
var clamp = (x, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, x));

// lab/baked-clip.ts
var STRIDE = 7;
var BakedClip = class _BakedClip {
  constructor(frames, count) {
    this.frames = frames;
    this.count = count;
  }
  frames;
  count;
  /** Record f(t) at `count` evenly spaced t in 0..1. Done once, offline or at load time. */
  static bake(count, f) {
    const frames = new Float32Array(count * STRIDE);
    for (let i = 0; i < count; i++) {
      const { p, q } = f(i / (count - 1));
      frames.set(p, i * STRIDE);
      frames.set(q, i * STRIDE + 3);
    }
    return new _BakedClip(frames, count);
  }
  /** ratio 0..1 -> interpolated pose. Pure function of ratio, so scrubbing backwards is free. */
  sample(ratio, p = [0, 0, 0], q = [0, 0, 0, 1]) {
    const x = clamp(ratio) * (this.count - 1);
    const i = Math.floor(x);
    const j = Math.min(i + 1, this.count - 1);
    const t = x - i;
    const a2 = i * STRIDE, b2 = j * STRIDE, f = this.frames;
    for (let k = 0; k < 3; k++) p[k] = f[a2 + k] + (f[b2 + k] - f[a2 + k]) * t;
    const dot = f[a2 + 3] * f[b2 + 3] + f[a2 + 4] * f[b2 + 4] + f[a2 + 5] * f[b2 + 5] + f[a2 + 6] * f[b2 + 6];
    const s2 = dot < 0 ? -1 : 1;
    let len = 0;
    for (let k = 0; k < 4; k++) {
      q[k] = f[a2 + 3 + k] + (s2 * f[b2 + 3 + k] - f[a2 + 3 + k]) * t;
      len += q[k] * q[k];
    }
    len = Math.sqrt(len) || 1;
    for (let k = 0; k < 4; k++) q[k] /= len;
    return { p, q };
  }
};
var orbit = (t) => {
  const a2 = t * Math.PI * 0.9;
  return {
    p: [Math.sin(a2) * 8, 0.5 + t * 3, Math.cos(a2) * 8],
    q: [0, Math.sin(a2 / 2), 0, Math.cos(a2 / 2)]
  };
};

// t-l2.ts
var near = (a2, b2, e = 1e-3) => assert.ok(Math.abs(a2 - b2) < e, `${a2} vs ${b2}`);
var c = BakedClip.bake(116, orbit);
assert.equal(c.frames.length, 116 * STRIDE);
var s = c.sample(0);
var f0 = orbit(0);
near(s.p[0], f0.p[0]);
near(s.p[2], f0.p[2]);
near(s.q[3], f0.q[3]);
s = c.sample(1);
var f1 = orbit(1);
near(s.p[0], f1.p[0]);
near(s.p[1], f1.p[1]);
near(s.q[1], f1.q[1]);
s = c.sample(0.5);
var fm = orbit(0.5);
near(s.p[0], fm.p[0], 0.01);
near(s.p[1], fm.p[1], 0.01);
var n = Math.hypot(...s.q);
near(n, 1);
var a = c.sample(0.37);
var b0 = c.sample(0.9);
var b = c.sample(0.37);
assert.deepEqual(a.p, b.p);
assert.deepEqual(a.q, b.q);
assert.deepEqual(c.sample(-5).p, c.sample(0).p);
assert.deepEqual(c.sample(9).p, c.sample(1).p);
var flip = BakedClip.bake(2, (t) => ({ p: [0, 0, 0], q: t === 0 ? [0, 0, 0, 1] : [0, 0, 0, -1] }));
var m = flip.sample(0.5);
near(Math.abs(m.q[3]), 1);
console.log("L2 pure tests OK");
