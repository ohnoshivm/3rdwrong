/* Original pre-load study hooks. MIT © 2026 3RDWRONG.
 * Shader text stays in browser memory; public capture JSON omits it.
 * Instrumentation changes timing. Use an uninstrumented run for performance.
 */
(() => {
  if (window.__MOTION_TEARDOWN__) return;
  const state = window.__MOTION_TEARDOWN__ = {
    scenes: [], cameras: [], renderers: [], contexts: [], shaders: [], programs: [],
    frames: [], errors: [], draws: 0, shaderLimitReached: false,
  };
  const seenContexts = new WeakSet(), seenRenderers = new WeakSet();
  const shaders = new WeakMap(), programs = new WeakMap();
  const unique = (list, item) => { if (!list.includes(item)) list.push(item); };
  const error = value => { if (state.errors.length < 30) state.errors.push(String(value)); };
  let shaderId = 0, programId = 0, contextId = 0;
  function wrap(object, key, observer) {
    const original = object[key];
    if (typeof original !== 'function') return;
    object[key] = function (...args) {
      const result = original.apply(this, args);
      try { observer.call(this, args, result); } catch (cause) { error(cause); }
      return result;
    };
  }
  function observe(object) {
    if (!object) return;
    if (object.isScene) unique(state.scenes, object);
    if (object.isCamera) unique(state.cameras, object);
    if (!object.isWebGLRenderer || seenRenderers.has(object)) return;
    seenRenderers.add(object); unique(state.renderers, object);
    // Render calls reveal cameras even when the engine never emits camera observe events.
    const render = object.render;
    object.render = function (scene, camera, ...rest) {
      if (scene?.isScene) unique(state.scenes, scene);
      if (camera?.isCamera) unique(state.cameras, camera);
      return render.call(this, scene, camera, ...rest);
    };
  }
  const channel = window.__THREE_DEVTOOLS__ || new EventTarget();
  window.__THREE_DEVTOOLS__ = channel;
  channel.addEventListener('observe', event => { try { observe(event.detail); } catch (cause) { error(cause); } });

  function hookGL(gl, kind, attributes) {
    if (seenContexts.has(gl)) return;
    seenContexts.add(gl);
    const id = contextId++;
    const debug = gl.getExtension('WEBGL_debug_renderer_info');
    state.contexts.push({ id, kind, requestedAttributes: attributes ?? null,
      actualAttributes: gl.getContextAttributes(),
      vendor: gl.getParameter(debug ? debug.UNMASKED_VENDOR_WEBGL : gl.VENDOR),
      renderer: gl.getParameter(debug ? debug.UNMASKED_RENDERER_WEBGL : gl.RENDERER),
      version: gl.getParameter(gl.VERSION) });
    wrap(gl, 'createShader', ([type], shader) => { if (shader) shaders.set(shader, { id: shaderId++, type, contextId: id, source: null }); });
    wrap(gl, 'shaderSource', ([shader, source]) => {
      const record = shaders.get(shader);
      if (!record) return;
      if (state.shaders.length >= 128 || String(source).length > 1048576) { state.shaderLimitReached = true; return; }
      record.source = String(source);
      if (!state.shaders.includes(record)) state.shaders.push(record);
    });
    wrap(gl, 'createProgram', (_, program) => {
      if (program) programs.set(program, { id: programId++, contextId: id, shaderIds: [] });
    });
    wrap(gl, 'attachShader', ([program, shader]) => {
      const p = programs.get(program), s = shaders.get(shader);
      if (p && s) unique(p.shaderIds, s.id);
    });
    wrap(gl, 'linkProgram', ([program]) => {
      const record = programs.get(program);
      if (!record || state.programs.length >= 128) return;
      record.linked = !!gl.getProgramParameter(program, gl.LINK_STATUS);
      record.uniforms = [];
      if (record.linked) {
        const count = gl.getProgramParameter(program, gl.ACTIVE_UNIFORMS);
        for (let i = 0; i < count; i++) {
          const u = gl.getActiveUniform(program, i);
          if (u) record.uniforms.push({ name: u.name, type: u.type, size: u.size });
        }
      }
      unique(state.programs, record);
    });
    for (const method of ['drawArrays', 'drawElements', 'drawArraysInstanced', 'drawElementsInstanced']) {
      wrap(gl, method, () => { state.draws++; });
    }
    // WebGL 1 instancing uses an extension rather than the core methods.
    wrap(gl, 'getExtension', ([name], extension) => {
      if (name === 'ANGLE_instanced_arrays' && extension && !seenContexts.has(extension)) {
        seenContexts.add(extension);
        for (const key of ['drawArraysInstancedANGLE', 'drawElementsInstancedANGLE']) wrap(extension, key, () => { state.draws++; });
      }
    });
  }
  for (const prototype of [window.HTMLCanvasElement?.prototype, window.OffscreenCanvas?.prototype].filter(Boolean)) {
    const getContext = prototype.getContext;
    prototype.getContext = function (kind, attributes) {
      const context = getContext.call(this, kind, attributes);
      if (context && /^(webgl2?|experimental-webgl)$/.test(kind)) {
        try { hookGL(context, kind, attributes); } catch (cause) { error(cause); }
      }
      return context;
    };
  }
  let previous = null;
  // One independent heartbeat per display opportunity; never count app callbacks as frames.
  function heartbeat(timestamp) {
    state.frames.push({ timestamp, intervalMs: previous === null ? null : timestamp - previous, drawCalls: state.draws });
    if (state.frames.length > 300) state.frames.shift();
    state.draws = 0; previous = timestamp;
    requestAnimationFrame(heartbeat);
  }
  requestAnimationFrame(heartbeat);

  function value(v) {
    if (v == null || ['number', 'boolean', 'string'].includes(typeof v)) return v ?? null;
    if (v.isTexture) return { texture: true, width: v.image?.width ?? null, height: v.image?.height ?? null };
    if (typeof v.toArray === 'function') return v.toArray().slice(0, 16);
    if (Array.isArray(v) || ArrayBuffer.isView(v)) return Array.from(v).slice(0, 64).map(item => typeof item === 'number' ? item : null);
    return null;
  }
  state.sample = (ignoreUniforms = []) => {
    const objects = [], seen = new Set();
    let truncated = false;
    for (const scene of state.scenes) {
      scene.updateMatrixWorld?.(true);
      scene.traverse?.(object => {
        if (seen.has(object)) return;
        seen.add(object);
        if (objects.length >= 2000) { truncated = true; return; }
        const materials = (Array.isArray(object.material) ? object.material : [object.material]).filter(Boolean);
        const record = { id: object.uuid ?? object.id, name: object.name, type: object.type, visible: object.visible,
          position: value(object.position), quaternion: value(object.quaternion), scale: value(object.scale),
          worldPosition: object.getWorldPosition ? value(object.getWorldPosition(object.position.clone())) : null,
          worldQuaternion: object.getWorldQuaternion ? value(object.getWorldQuaternion(object.quaternion.clone())) : null,
          worldScale: object.getWorldScale ? value(object.getWorldScale(object.scale.clone())) : null,
          materials: materials.map(m => ({ type: m.type, opacity: m.opacity, colour: value(m.color),
            uniforms: Object.fromEntries(Object.entries(m.uniforms ?? {}).filter(([key]) => !ignoreUniforms.includes(key))
              .map(([key, uniform]) => [key, value(uniform?.value)])) })) };
        if (object.isLight) record.light = { colour: value(object.color), intensity: object.intensity };
        if (object.isSkinnedMesh) record.bones = object.skeleton.bones.map(bone => ({ name: bone.name,
          position: value(bone.position), quaternion: value(bone.quaternion) }));
        if (object.animations?.length) record.clips = object.animations.map(clip => ({ name: clip.name, duration: clip.duration }));
        objects.push(record);
      });
    }
    return { available: state.scenes.length > 0, objects, truncated,
      cameras: state.cameras.map(c => ({ id: c.uuid, type: c.type, fov: c.fov, zoom: c.zoom,
        position: value(c.position), quaternion: value(c.quaternion),
        worldPosition: c.getWorldPosition ? value(c.getWorldPosition(c.position.clone())) : null })),
      renderers: state.renderers.map(r => ({ pixelRatio: r.getPixelRatio?.(), toneMapping: r.toneMapping,
        outputColorSpace: r.outputColorSpace, exposure: r.toneMappingExposure,
        render: r.info ? { ...r.info.render } : null })),
      contexts: state.contexts, lastFrame: state.frames.at(-1) ?? null,
      programs: state.programs, shaderCount: state.shaders.length,
      shaderLimitReached: state.shaderLimitReached, errors: state.errors };
  };
})();
