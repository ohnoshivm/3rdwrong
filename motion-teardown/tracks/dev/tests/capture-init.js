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
