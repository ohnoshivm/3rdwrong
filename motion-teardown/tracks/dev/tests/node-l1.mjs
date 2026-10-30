// t-l1.ts
import assert from "node:assert/strict";

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

// lab/section.ts
var sectionR = (scrollY2, sectionTop, vh) => 1 + (scrollY2 - sectionTop) / vh;
var exitR = (scrollY2, sectionTop, sectionH, vh) => (scrollY2 - sectionTop - sectionH) / vh;

// lab/scroll-engine.ts
var WHEEL_CLAMP = 200;
var EASE_RATE = 12;
var KEY_STEP = 100;
var createScroll = (max) => ({ target: 0, current: 0, max });
function pushWheel(m2, deltaY) {
  m2.target = clamp(m2.target + clamp(deltaY, -WHEEL_CLAMP, WHEEL_CLAMP), 0, m2.max);
}
function pushKey(m2, key, viewportH) {
  const d = key === "ArrowDown" ? KEY_STEP : key === "ArrowUp" ? -KEY_STEP : key === "PageDown" || key === " " ? viewportH : key === "PageUp" ? -viewportH : 0;
  m2.target = clamp(m2.target + d, 0, m2.max);
}
function step(m2, dt) {
  m2.current += (m2.target - m2.current) * (1 - Math.exp(-EASE_RATE * dt));
  if (Math.abs(m2.target - m2.current) < 0.1) m2.current = m2.target;
  return Math.round(m2.current);
}

// lab/stagger.ts
function staggerWindow(group, i, n, offset = 0.3, width = 0.6, e = ease.linear, reverse = false) {
  const k = n > 1 ? i / (n - 1) : 0;
  const start = (reverse ? 1 - k : k) * offset;
  return fit(group, start, start + width, 0, 1, e);
}

// t-l1.ts
var near = (a2, b2, e = 1e-3) => assert.ok(Math.abs(a2 - b2) < e, `${a2} vs ${b2}`);
near(fit(5, 0, 10), 0.5);
near(fit(-1, 0, 10), 0);
near(fit(11, 0, 10), 1);
near(fit(0.5, 1, 0, 1, 0.95), 0.975);
near(fit(0.5, 0, 1, 0, 100, ease.cubicOut), 87.5);
near(ease.backOut(1), 1);
near(ease.expoOut(1), 1);
near(ease.sineIn(1), 1);
near(ease.backOut(0), 0);
assert.ok(ease.backOut(0.8) > 1, "backOut overshoots");
near(exitR(0, 0, 900, 900), -1);
near(exitR(450, 0, 900, 900), -0.5);
near(fit(exitR(225, 0, 900, 900), -1, -0.5, 1, 0), 0.5);
var r = sectionR(3056, 900, 900);
near(r, 3.3956, 1e-3);
near(fit(r, 0, 5.5), 0.6174, 1e-3);
near(sectionR(900, 900, 900), 1);
var m = createScroll(5e3);
pushWheel(m, 1e3);
assert.equal(m.target, 200);
pushWheel(m, -1e3);
assert.equal(m.target, 0);
for (let i = 0; i < 40; i++) pushWheel(m, 200);
assert.equal(m.target, 5e3);
pushKey(m, "ArrowUp", 900);
assert.equal(m.target, 4900);
pushKey(m, "PageDown", 900);
assert.equal(m.target, 5e3);
var a = createScroll(9999);
var b = createScroll(9999);
a.target = b.target = 1e3;
for (let i = 0; i < 60; i++) step(a, 1 / 60);
for (let i = 0; i < 30; i++) step(b, 1 / 30);
near(a.current, b.current, 1e-6);
assert.ok(a.current > 999 && a.current <= 1e3);
var y = 0;
for (let i = 0; i < 600; i++) y = step(a, 1 / 60);
assert.equal(y, 1e3);
assert.equal(a.current, 1e3);
near(staggerWindow(0, 0, 10), 0);
near(staggerWindow(0.6, 0, 10), 1);
near(staggerWindow(0.9, 9, 10), 1);
near(staggerWindow(0.29, 9, 10), 0);
assert.ok(staggerWindow(0.5, 0, 10) > staggerWindow(0.5, 9, 10));
near(staggerWindow(0, 9, 10, 0.2, 0.8, ease.linear, true), 0);
assert.ok(staggerWindow(0.3, 9, 10, 0.2, 0.8, ease.linear, true) > staggerWindow(0.3, 0, 10, 0.2, 0.8, ease.linear, true));
near(staggerWindow(1, 3, 10, 0.2, 0.8), 1);
console.log("L1 pure tests OK");
