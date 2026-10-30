// t-dd.ts
import assert from "node:assert/strict";

// lab/mesh-pack.ts
var pad4 = (n2) => n2 + 3 & ~3;
function pack(mesh) {
  const vertexCount = mesh.positions.length / 3;
  const min = [Infinity, Infinity, Infinity];
  const max = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < mesh.positions.length; i++) {
    const a = i % 3;
    min[a] = Math.min(min[a], mesh.positions[i]);
    max[a] = Math.max(max[a], mesh.positions[i]);
  }
  const indexBytes = vertexCount < 65536 ? 2 : 4;
  const manifest = { vertexCount, indexCount: mesh.indices.length, min, max, indexBytes };
  const json = new TextEncoder().encode(JSON.stringify(manifest));
  const jsonLen = pad4(json.length);
  const posBytes = pad4(vertexCount * 3 * 2);
  const idxBytes = pad4(mesh.indices.length * indexBytes);
  const buf2 = new ArrayBuffer(4 + jsonLen + posBytes + idxBytes);
  const view = new DataView(buf2);
  view.setUint32(0, jsonLen, true);
  new Uint8Array(buf2, 4, jsonLen).fill(32).set(json);
  const q = new Uint16Array(buf2, 4 + jsonLen, vertexCount * 3);
  for (let i = 0; i < q.length; i++) {
    const a = i % 3;
    const span2 = max[a] - min[a] || 1;
    q[i] = Math.round((mesh.positions[i] - min[a]) / span2 * 65535);
  }
  const idx = new (indexBytes === 2 ? Uint16Array : Uint32Array)(buf2, 4 + jsonLen + posBytes, mesh.indices.length);
  idx.set(mesh.indices);
  return buf2;
}
function unpack(buf2) {
  const jsonLen = new DataView(buf2).getUint32(0, true);
  const m3 = JSON.parse(new TextDecoder().decode(new Uint8Array(buf2, 4, jsonLen)));
  const q = new Uint16Array(buf2, 4 + jsonLen, m3.vertexCount * 3);
  const positions2 = new Float32Array(q.length);
  for (let i = 0; i < q.length; i++) {
    const a = i % 3;
    positions2[i] = m3.min[a] + q[i] / 65535 * (m3.max[a] - m3.min[a]);
  }
  const posBytes = pad4(q.length * 2);
  const Idx = m3.indexBytes === 2 ? Uint16Array : Uint32Array;
  const indices2 = Uint32Array.from(new Idx(buf2, 4 + jsonLen + posBytes, m3.indexCount));
  return { positions: positions2, indices: indices2 };
}

// lab/resilient-loader.ts
function loadAll(items, opts = {}) {
  const { itemTimeoutMs = 8e3, totalTimeoutMs = 1e4, onProgress } = opts;
  const start = performance.now();
  const report = { loaded: [], failed: [], timedOut: [], fallbacks: [], ms: 0, values: /* @__PURE__ */ new Map() };
  const total = items.length;
  let settled = 0;
  let finished = false;
  return new Promise((resolve) => {
    const finish = () => {
      if (finished) return;
      finished = true;
      for (const it of items) {
        if (!report.values.has(it.name)) {
          if (!report.timedOut.includes(it.name) && !report.failed.some((f) => f.name === it.name)) report.timedOut.push(it.name);
          if (it.fallback) {
            report.values.set(it.name, it.fallback());
            report.fallbacks.push(it.name);
          }
        }
      }
      report.ms = performance.now() - start;
      clearTimeout(deadline);
      resolve(report);
    };
    const deadline = setTimeout(finish, totalTimeoutMs);
    if (total === 0) return finish();
    const settle = () => {
      settled++;
      onProgress?.(settled, total);
      if (settled === total) finish();
    };
    for (const it of items) {
      let done = false;
      const once = (fn) => {
        if (done || finished) return;
        done = true;
        fn();
        settle();
      };
      const timer = setTimeout(() => once(() => {
        report.timedOut.push(it.name);
        if (it.fallback) {
          report.values.set(it.name, it.fallback());
          report.fallbacks.push(it.name);
        }
      }), itemTimeoutMs);
      new Promise((res) => res(it.load())).then(
        // a synchronous throw becomes a rejection too
        (v) => {
          clearTimeout(timer);
          once(() => {
            report.values.set(it.name, v);
            report.loaded.push(it.name);
          });
        },
        (e) => {
          clearTimeout(timer);
          once(() => {
            report.failed.push({ name: it.name, reason: String(e?.message ?? e) });
            if (it.fallback) {
              report.values.set(it.name, it.fallback());
              report.fallbacks.push(it.name);
            }
          });
        }
      );
    }
  });
}

// t-dd.ts
var n = 500;
var positions = new Float32Array(n * 3);
for (let i = 0; i < positions.length; i++) positions[i] = Math.sin(i * 1.7) * 1 + (i % 3 === 1 ? 0.5 : 0);
var indices = Uint32Array.from({ length: n * 3 - 6 }, (_, i) => i % n);
var buf = pack({ positions, indices });
var m = unpack(buf);
assert.equal(m.positions.length, positions.length);
assert.deepEqual(Array.from(m.indices), Array.from(indices));
var maxErr = 0;
for (let i = 0; i < positions.length; i++) maxErr = Math.max(maxErr, Math.abs(m.positions[i] - positions[i]));
var span = 2;
assert.ok(maxErr <= span / 65535 / 2 + 1e-6, "err " + maxErr);
assert.ok(buf.byteLength < positions.byteLength + indices.byteLength, `${buf.byteLength} < ${positions.byteLength + indices.byteLength}`);
var big = 65540;
var p2 = new Float32Array(big * 3).map((_, i) => i % 7);
var i2 = Uint32Array.from([0, big - 1, 5]);
var m2 = unpack(pack({ positions: p2, indices: i2 }));
assert.deepEqual(Array.from(m2.indices), [0, big - 1, 5]);
var never = () => new Promise(() => {
});
var prog = [];
var t0 = performance.now();
var rep = await loadAll([
  { name: "ok", load: async () => 1 },
  { name: "slow", load: () => new Promise((r) => setTimeout(() => r(2), 20)) },
  { name: "bad", load: async () => {
    throw new Error("404");
  }, fallback: () => "flat" },
  { name: "sync", load: () => {
    throw new Error("sync boom");
  } },
  { name: "hang", load: never, fallback: () => "flat2" }
], { itemTimeoutMs: 60, totalTimeoutMs: 500, onProgress: (s, t) => prog.push(s / t) });
assert.deepEqual(rep.loaded.sort(), ["ok", "slow"]);
assert.deepEqual(rep.failed.map((f) => f.name).sort(), ["bad", "sync"]);
assert.equal(rep.failed.find((f) => f.name === "sync").reason, "sync boom");
assert.deepEqual(rep.timedOut, ["hang"]);
assert.deepEqual(rep.fallbacks.sort(), ["bad", "hang"]);
assert.equal(rep.values.get("hang"), "flat2");
assert.ok(!rep.values.has("sync"));
assert.equal(prog.at(-1), 1);
assert.deepEqual([...prog], [...prog].sort((a, b) => a - b));
assert.ok(performance.now() - t0 < 300, "item timeout bounds it: " + (performance.now() - t0));
var t1 = performance.now();
var r2 = await loadAll([{ name: "hang", load: never }], { itemTimeoutMs: 6e4, totalTimeoutMs: 80 });
assert.ok(performance.now() - t1 < 250);
assert.deepEqual(r2.timedOut, ["hang"]);
var r3 = await loadAll([]);
assert.equal(r3.loaded.length, 0);
console.log("deep-dive pure tests OK");
