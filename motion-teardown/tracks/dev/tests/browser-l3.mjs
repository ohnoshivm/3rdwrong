import { chromium } from 'playwright-core';
import assert from 'node:assert/strict';
const browser = await chromium.launch({ channel:'chrome', headless:true, args:['--use-angle=metal','--ignore-gpu-blocklist'] });
const page = await browser.newPage();
const errs=[]; page.on('console',m=>{ if(['error','warning'].includes(m.type())) errs.push(m.text()); }); page.on('pageerror',e=>errs.push(String(e)));
await page.goto('file://' + process.cwd() + '/page-l3/index.html');
const res = await page.evaluate(() => {
  const L = window.LAB, W = 100;
  const c = document.getElementById('c'); const gl = c.getContext('webgl2', { preserveDrawingBuffer:true, antialias:false });
  const out = {};
  const compile = (type, src) => { const s = gl.createShader(type); gl.shaderSource(s, '#version 300 es\n' + src); gl.compileShader(s); if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s)); return s; };
  const program = (vs, fs) => { const p = gl.createProgram(); gl.attachShader(p, compile(gl.VERTEX_SHADER, vs)); gl.attachShader(p, compile(gl.FRAGMENT_SHADER, fs)); gl.bindAttribLocation(p,0,'position'); gl.linkProgram(p); if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p)); gl.useProgram(p); return p; };
  const px = (x, y) => { const b = new Uint8Array(4); gl.readPixels(x, y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, b); return [...b]; };
  const ndc = (x, y) => [Math.round((x * 0.5 + 0.5) * W), Math.round((y * 0.5 + 0.5) * W)];
  const clear = () => { gl.viewport(0,0,W,W); gl.clearColor(0,0,0,1); gl.clear(gl.COLOR_BUFFER_BIT); };
  const tex = (w, h, data, float=false) => { gl.activeTexture(gl.TEXTURE7); const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    if (float) gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA32F,w,h,0,gl.RGBA,gl.FLOAT,data); else gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA8,w,h,0,gl.RGBA,gl.UNSIGNED_BYTE,data); return t; };
  const bindTex = (p, name, t, unit) => { gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t); gl.uniform1i(gl.getUniformLocation(p, name), unit); };
  const u1 = (p,n,v)=>gl.uniform1f(gl.getUniformLocation(p,n),v), u2=(p,n,a,b)=>gl.uniform2f(gl.getUniformLocation(p,n),a,b), u3=(p,n,a,b,c)=>gl.uniform3f(gl.getUniformLocation(p,n),a,b,c);
  const quad = () => { const vao = gl.createVertexArray(); gl.bindVertexArray(vao); const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,0, 3,-1,0, -1,3,0]), gl.STATIC_DRAW); gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0,3,gl.FLOAT,false,0,0); return vao; };

  // ---- skinning: translate, rotate, finger lift -------------------------------------------------
  {
    const p = program(L.SKIN_VERT, 'precision highp float; in vec3 vNormal; out vec4 o; void main(){ o = vec4(1.); }');
    const loc = (n) => gl.getAttribLocation(p, n);
    const vao = gl.createVertexArray(); gl.bindVertexArray(vao);
    const attr = (name, data, size) => { const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(data), gl.STATIC_DRAW); const l = loc(name); gl.enableVertexAttribArray(l); gl.vertexAttribPointer(l, size, gl.FLOAT, false, 0, 0); };
    attr('position', [-.3,-.3,0, .3,-.3,0, 0,.3,0], 3); attr('normal', [0,1,0, 0,1,0, 0,1,0], 3);
    attr('aBones', [1,0,0,0, 1,0,0,0, 1,0,0,0], 4); attr('aWeights', [1,0,0,0, 1,0,0,0, 1,0,0,0], 4); attr('aFinger', [0,0,0], 1);
    const ident = new Float32Array([1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]);
    gl.uniformMatrix4fv(gl.getUniformLocation(p,'modelViewMatrix'), false, ident); gl.uniformMatrix4fv(gl.getUniformLocation(p,'projectionMatrix'), false, ident);
    const run = (bone1T, bone1Q, fingers, lift) => {
      bindTex(p,'uBonePos', tex(2,1,new Float32Array([0,0,0,0, ...bone1T,0]),true),0);
      bindTex(p,'uBoneRot', tex(2,1,new Float32Array([0,0,0,1, ...bone1Q]),true),1);
      gl.uniform4f(gl.getUniformLocation(p,'uFingers'), ...fingers); u1(p,'uLift',lift);
      clear(); gl.drawArrays(gl.TRIANGLES,0,3);
    };
    const on = (x,y)=>px(...ndc(x,y))[0] > 200;
    run([0,0,0],[0,0,0,1],[0,0,0,0],0); out.skinRest = [on(0,0), on(0.5,-0.1)];
    run([0.5,0,0],[0,0,0,1],[0,0,0,0],0); out.skinMoved = [on(0,-0.2), on(0.5,-0.1), on(-0.2,-0.2)];
    const s = Math.SQRT1_2; run([0,0,0],[0,0,s,s],[0,0,0,0],0); out.skinRot = [on(0.2,0.2), on(0,0.25), on(0.1,0)];
    run([0,0,0],[0,0,0,1],[0,0,0,0],0.2); out.liftOff = on(0,0.45);
    run([0,0,0],[0,0,0,1],[1,0,0,0],0.2); out.liftOn = on(0,0.45);
  }
  // ---- fragment passes ---------------------------------------------------------------------------
  const fragPass = (frag, setup) => { const p = program(L.FULLSCREEN_VERT, frag); gl.bindVertexArray(quad()); clear(); setup(p); gl.drawArrays(gl.TRIANGLES,0,3); return p; };
  const solid = (r,g,b) => tex(1,1,new Uint8Array([r,g,b,255]));
  // edge glow
  const glow = (amount) => { fragPass(L.EDGE_GLOW_FRAG, (p) => { bindTex(p,'uScene',solid(0,0,0),0); u2(p,'uRes',W,W); u1(p,'uAmount',amount); u1(p,'uTime',0.7); u2(p,'uOrigin',1,0.5); u1(p,'uPad',20);
      gl.uniform3fv(gl.getUniformLocation(p,'uColors'), new Float32Array([1,.8,.9, 1,.2,.2, 1,1,1, 1,.5,.6])); }); return { edge: px(2,50), mid: px(50,50) }; };
  out.glowOn = glow(1); out.glowOff = glow(0);
  // grade
  const grade = (sat, vig) => { fragPass(L.GRADE_FRAG, (p) => { bindTex(p,'uScene',solid(200,50,50),0); bindTex(p,'uBloom',solid(0,0,0),1); u2(p,'uRes',W,W); u1(p,'uBloomAmount',1); u1(p,'uSaturation',sat); u3(p,'uTint',1,0.1,0.3); u1(p,'uTintAmount',0); u2(p,'uVignette',0.5,1.3); u1(p,'uSeed',1); }); return { mid: px(50,50), corner: px(1,1) }; };
  out.gradeGrey = grade(0); out.gradeColour = grade(1);
  // bright pass + blur: a constant image stays constant through blur; bright pass drops dark pixels
  fragPass(L.BRIGHT_FRAG, (p) => { bindTex(p,'uScene',solid(20,20,20),0); u1(p,'uThreshold',0.6); u1(p,'uKnee',0.1); }); out.brightDark = px(50,50);
  fragPass(L.BRIGHT_FRAG, (p) => { bindTex(p,'uScene',solid(250,250,250),0); u1(p,'uThreshold',0.6); u1(p,'uKnee',0.1); }); out.brightLit = px(50,50);
  const k = L.gaussianKernel(4); const kk = new Float32Array(16); kk.set(k);
  fragPass(L.BLUR_FRAG, (p) => { bindTex(p,'uSrc',solid(128,128,128),0); u2(p,'uDir',1/W,0); gl.uniform1fv(gl.getUniformLocation(p,'uWeights'),kk); gl.uniform1i(gl.getUniformLocation(p,'uRadius'),k.length-1); }); out.blurConst = px(50,50);

  // ---- the three.js wiring: createSkinned compiles and draws -------------------------------------
  {
    const T = L.THREE; const cv = document.createElement('canvas'); cv.width = cv.height = 64;
    const r = new T.WebGLRenderer({ canvas: cv, antialias:false, preserveDrawingBuffer:true }); r.setSize(64,64,false);
    const g = new T.BufferGeometry();
    g.setAttribute('position', new T.Float32BufferAttribute([-.5,-.5,0, .5,-.5,0, 0,.5,0],3));
    g.setAttribute('normal', new T.Float32BufferAttribute([0,0,1, 0,0,1, 0,0,1],3));
    g.setAttribute('aBones', new T.Float32BufferAttribute([0,0,0,0, 0,0,0,0, 0,0,0,0],4));
    g.setAttribute('aWeights', new T.Float32BufferAttribute([1,0,0,0, 1,0,0,0, 1,0,0,0],4));
    g.setAttribute('aFinger', new T.Float32BufferAttribute([-1,-1,-1],1));
    const clip = L.createBoneClip(1, 2); clip.data.set([0,0,0, 0,0,0,1], 0); clip.data.set([0.5,0,0, 0,0,0,1], L.BONE_STRIDE);
    const sk = L.createSkinned(g, clip);
    const sc = new T.Scene(); sc.add(sk.mesh); const cam = new T.OrthographicCamera(-1,1,1,-1,0.1,10); cam.position.z = 3;
    const shot = (ratio) => { sk.pose(ratio,[0,0,0,0],0); r.setClearColor(0x000000,1); r.render(sc,cam); const g2 = r.getContext(); const b = new Uint8Array(4); g2.readPixels(32+16,32,1,1,g2.RGBA,g2.UNSIGNED_BYTE,b); return b[0]+b[1]+b[2]; };
    out.threeRest = shot(0); out.threeMoved = shot(1);   // pixel at x=+0.5: outside at rest, inside once moved 0.5 right
    out.threeErr = r.info.programs.length;
  }
  return out;
});
console.log(JSON.stringify(res)); console.log('console:', JSON.stringify(errs));
const A = assert.deepEqual;
A(res.skinRest,[true,false]); A(res.skinMoved,[false,true,false]); A(res.skinRot,[true,false,true]);
assert.equal(res.liftOff,false); assert.equal(res.liftOn,true);
assert.ok(res.glowOn.edge[0] > 60 && res.glowOn.mid[0] === 0, 'glow hugs the edge'); assert.deepEqual(res.glowOff.edge.slice(0,3),[0,0,0]);
assert.ok(Math.abs(res.gradeGrey.mid[0]-res.gradeGrey.mid[1]) <= 2 && Math.abs(res.gradeGrey.mid[1]-res.gradeGrey.mid[2]) <= 2, 'grey');
assert.ok(res.gradeColour.mid[0] > res.gradeColour.mid[1] + 40, 'colour kept'); assert.ok(res.gradeColour.corner[0] < res.gradeColour.mid[0] - 20, 'vignette');
assert.equal(res.brightDark[0],0); assert.ok(res.brightLit[0] > 200); assert.ok(Math.abs(res.blurConst[0]-128)<=2, 'blur keeps energy '+res.blurConst[0]);
assert.ok(res.threeRest === 0 && res.threeMoved > 100, 'three wiring');
assert.deepEqual(errs,[]);
await browser.close(); console.log('L3 browser OK');
