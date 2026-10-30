---
title: "Deep dive: why a site ships its own binary model format"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Deep dive: why a site ships its own binary model format

When you open the network panel on an award-level WebGL site, you often do not see `.glb`. You see something with an unfamiliar extension and a few hundred kilobytes. oryzo.ai (by Lusion) is an example: no glTF, no Draco, no KTX2. Its geometry and its baked animation clips ship as a custom binary container with a `.buf` extension. In the in-scope part of the page, `hand.buf` is 381 KB, `coaster.buf` 67 KB and `hand_animation.buf` 42 KB.

This page explains the idea and lets you build a small version of your own. **We describe the concept only.** We do not publish their format, their loader or their assets, and nothing here will let you read their files.

## Why bother

A general-purpose format has to carry everything a modelling tool might say: names, materials, cameras, extensions. A site that controls both ends needs only what its renderer reads. These are the usual reasons to go custom (we did not measure the original's gains, so read them as the case for the idea, not as findings):

- **Size.** Store positions as 16-bit integers inside the model's bounding box instead of 32-bit floats. That halves the largest array with no visible change at screen scale.
- **Load time.** One fetch, one `ArrayBuffer`, typed-array views onto it. No JSON scene parse, no extra decoder to download.
- **Fit to the renderer.** Interleave or order attributes the way your shader consumes them. Bake the animation into the same container, as one pose per frame (see [L3](../lab-l3-character-and-post.md)).
- **Fewer dependencies.** No Draco decoder (a WebAssembly module) and no KTX2 transcoder. The preloader has less to wait for.

## The shape of the idea

Three parts, in order:

1. A small **header** that says how long the manifest is.
2. A **manifest** (JSON is fine): counts, bounding box, which attributes follow and how each is stored.
3. The **attribute arrays**, back to back, in the order the manifest lists them.

The decoder reads the header, parses the manifest, and creates typed-array views at the right byte offsets. If an attribute is stored quantised, it expands each value back into the bounding box.

## A format of our own

This is a deliberately tiny container, written from scratch for this guide. It stores positions as unsigned 16-bit values and indices as 16- or 32-bit integers. It is not compatible with anything else.

```ts
// lab/mesh-pack.ts
export interface Mesh {
  positions: Float32Array; // x y z per vertex
  indices: Uint32Array;
}

interface Manifest {
  vertexCount: number;
  indexCount: number;
  min: [number, number, number];
  max: [number, number, number];
  indexBytes: 2 | 4;
}

const pad4 = (n: number) => (n + 3) & ~3;

export function pack(mesh: Mesh): ArrayBuffer {
  const vertexCount = mesh.positions.length / 3;
  const min: [number, number, number] = [Infinity, Infinity, Infinity];
  const max: [number, number, number] = [-Infinity, -Infinity, -Infinity];
  for (let i = 0; i < mesh.positions.length; i++) {
    const a = i % 3;
    min[a] = Math.min(min[a], mesh.positions[i]);
    max[a] = Math.max(max[a], mesh.positions[i]);
  }
  const indexBytes: 2 | 4 = vertexCount < 65536 ? 2 : 4;
  const manifest: Manifest = { vertexCount, indexCount: mesh.indices.length, min, max, indexBytes };

  const json = new TextEncoder().encode(JSON.stringify(manifest));
  const jsonLen = pad4(json.length);
  const posBytes = pad4(vertexCount * 3 * 2);
  const idxBytes = pad4(mesh.indices.length * indexBytes);

  const buf = new ArrayBuffer(4 + jsonLen + posBytes + idxBytes);
  const view = new DataView(buf);
  view.setUint32(0, jsonLen, true);
  new Uint8Array(buf, 4, jsonLen).fill(0x20).set(json); // pad the JSON with spaces

  const q = new Uint16Array(buf, 4 + jsonLen, vertexCount * 3);
  for (let i = 0; i < q.length; i++) {
    const a = i % 3;
    const span = max[a] - min[a] || 1;
    q[i] = Math.round(((mesh.positions[i] - min[a]) / span) * 65535);
  }
  const idx = new (indexBytes === 2 ? Uint16Array : Uint32Array)(buf, 4 + jsonLen + posBytes, mesh.indices.length);
  idx.set(mesh.indices);
  return buf;
}

export function unpack(buf: ArrayBuffer): Mesh {
  const jsonLen = new DataView(buf).getUint32(0, true);
  const m: Manifest = JSON.parse(new TextDecoder().decode(new Uint8Array(buf, 4, jsonLen)));
  const q = new Uint16Array(buf, 4 + jsonLen, m.vertexCount * 3);
  const positions = new Float32Array(q.length);
  for (let i = 0; i < q.length; i++) {
    const a = i % 3;
    positions[i] = m.min[a] + (q[i] / 65535) * (m.max[a] - m.min[a]);
  }
  const posBytes = pad4(q.length * 2);
  const Idx = m.indexBytes === 2 ? Uint16Array : Uint32Array;
  const indices = Uint32Array.from(new Idx(buf, 4 + jsonLen + posBytes, m.indexCount));
  return { positions, indices };
}
```

Two details worth keeping. **Alignment:** a typed array's byte offset must be a multiple of its element size, so we pad the manifest and each block to four bytes. **Error bound:** quantising to 16 bits inside a bounding box has a worst-case error of half a step, `(max − min) / 65535 / 2` per axis. For a model 2 units wide that is about 0.000015 units, far below a pixel.

## What a real one adds (and what you may not need)

- Per-attribute quantisation settings, so normals, UVs and skin weights each choose their own precision.
- Several sub-meshes in one buffer, split by face range, so one fetch serves a whole scene.
- A baked animation clip in the same container, as in the L3 lab's `BoneClip`.
- An offline exporter in your own tool chain. That is where the real work is: the format is the easy half.

Start with glTF. Move to your own container only when a measured size or load-time problem needs it.

## Exercises

1. Encode a sphere with the `pack` above and compare byte counts with a plain `Float32Array` layout.
2. Add a 16-bit octahedral-encoded normal attribute and measure the angular error.
3. Write the exporter: read a glTF with three.js's `GLTFLoader` in a Node script and call `pack`.
4. Load the result in the L2 stage in place of the torus knot.

## You're done when

- [ ] A mesh round-trips through `pack` and `unpack` with every position inside the stated error bound and identical indices.
- [ ] Your packed file is smaller than the equivalent `Float32Array` layout, and you know by how much.
- [ ] You can explain in two sentences why the original shipped a custom format, and what it cost them (a tool chain of their own).
- [ ] You did not try to read anyone else's files with it.
