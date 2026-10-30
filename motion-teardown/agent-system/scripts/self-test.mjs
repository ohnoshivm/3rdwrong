import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import { once } from 'node:events';
import { stepPositions, runCapture } from './capture-steps.mjs';
import { fitFollower } from './scroll-physics.mjs';
import { ssim, sobel, grayscale, scorePair, detail, execFileAsync } from './image-metrics.mjs';
import { number, viewport, pageURL, HERE, openBrowser } from './lib.mjs';

assert.deepEqual(stepPositions(0, 95, 30), [0, 30, 60, 90, 95]);
assert.deepEqual(stepPositions(0, 0, 90), [0]);
assert.throws(() => stepPositions(1, 0, 1));
assert.throws(() => stepPositions(0, 10, 0));
assert.throws(() => number('NaN', 'test'));
assert.throws(() => pageURL('file:///etc/passwd'));
assert.throws(() => pageURL('https://user:pass@localhost'));
assert.deepEqual(viewport({ viewport: '390x844' }), { width: 390, height: 844 });
assert.throws(() => viewport({ viewport: '0x900' }));
const series = Array.from({ length: 240 }, (_, i) => ({ t: i * 1000 / 60, y: 100 * (1 - Math.exp(-7 * i / 60)) }));
const fit = fitFollower(series);
assert.ok(fit.valid);
assert.ok(Math.abs(fit.cPerSecond - 7) < 0.11);
assert.equal(fitFollower(series.map(row => ({ ...row, y: 0 }))).valid, false);
assert.equal(fitFollower(Array.from({ length: 30 }, (_, i) => ({ t: i * 16, y: i ? 100 : 0 }))).valid, false);
assert.equal(fitFollower(Array.from({ length: 30 }, (_, i) => ({ t: i * 16, y: i * 5 }))).reason, 'endpoint-not-settled');
const image = Float64Array.from({ length: 16 * 16 }, (_, i) => (i % 17) / 16);
const other = Float64Array.from(image, v => 1 - v);
assert.ok(Math.abs(ssim(image, image, 1, 16, 16) - 1) < 1e-10);
assert.ok(ssim(image, other, 1, 16, 16) < 0.5);
assert.ok([...sobel(new Float64Array(16 * 16).fill(0.2), 16, 16)].every(v => v === 0));
assert.ok(detail(new Float64Array(16 * 16).fill(0.01)).warning);
console.log('PASS unit checks: ranges, argument boundaries, exponential fit, non-fit cases, SSIM and Sobel');

if (process.argv.includes('--browser')) {
  const directory = path.join(HERE, '_checks/fixture');
  await fs.mkdir(directory, { recursive: true });
  const html = `<!doctype html><meta charset="utf-8"><style>body{margin:0;height:2400px;font:20px sans-serif}#box{position:fixed;top:20px;left:20px;width:140px;height:100px;background:crimson}canvas{position:fixed;bottom:10px}</style><div id="box">Fixture</div><canvas width="16" height="16"></canvas><script>
  const box=document.querySelector('#box'); addEventListener('scroll',()=>{box.style.transform='translateX('+scrollY/10+'px)';box.style.opacity=1-scrollY/2400;});
  const gl=document.querySelector('canvas').getContext('webgl2');
  if(gl){const vertex=gl.createShader(gl.VERTEX_SHADER);gl.shaderSource(vertex,'#version 300 es\\nvoid main(){gl_Position=vec4(0.0);gl_PointSize=1.0;}');gl.compileShader(vertex);const fragment=gl.createShader(gl.FRAGMENT_SHADER);gl.shaderSource(fragment,'#version 300 es\\nprecision mediump float;out vec4 color;void main(){color=vec4(1.0);}');gl.compileShader(fragment);const program=gl.createProgram();gl.attachShader(program,vertex);gl.attachShader(program,fragment);gl.linkProgram(program);gl.useProgram(program);gl.drawArrays(gl.POINTS,0,1);}
  </script>`;
  const server = http.createServer((request, response) => { response.writeHead(200, { 'content-type': 'text/html' }); response.end(html); });
  server.listen(0, '127.0.0.1'); await once(server, 'listening');
  const url = `http://127.0.0.1:${server.address().port}/`;
  const options = { url, out: path.join(directory, 'capture'), viewport: '800x600', dpr: '1', headed: false,
    timeout: '15000', 'boot-ms': '100', start: '0', end: '300', step: '150',
    'settle-ms': '1500', 'max-elements': '100', selector: ['#box'], 'round-trip': true };
  try {
    const report = await runCapture(options);
    assert.equal(report.steps.length, 6);
    assert.equal(report.summary.unsettled, 0);
    const step = JSON.parse(await fs.readFile(path.join(options.out, 'forward/step-0002.json'), 'utf8'));
    assert.equal(step.actualY, 300);
    assert.equal(step.state.dom[0].transform, 'matrix(1, 0, 0, 1, 30, 0)');
    assert.ok(step.state.three.contexts.length > 0, 'WebGL context hook');
    assert.ok(step.state.three.programs.some(p => p.linked && p.shaderIds.length === 2), 'shader/program pairing');
    assert.equal(JSON.stringify(step).includes('gl_Position'), false, 'capture must not export shader source');
    await execFileAsync('ffmpeg', ['-v', 'error', '-y', '-f', 'lavfi', '-i', 'color=c=black@0:s=16x16,format=rgba', '-frames:v', '1', path.join(directory, 'transparent.png')]);
    const transparent = await grayscale(path.join(directory, 'transparent.png'));
    assert.ok([...transparent].every(value => value > 0.999), 'transparent pixels composite onto opaque white');
    const image = await grayscale(path.join(options.out, 'forward/step-0000.png'));
    const identical = scorePair(image, image);
    assert.ok(identical.structure > 0.999999 && identical.luminance > 0.999999);
    await execFileAsync(process.execPath, [path.join(HERE, 'scroll-physics.mjs'), '--url', url,
      '--out', path.join(directory, 'physics'), '--wheel', '100', '--key', 'PageDown', '--duration-ms', '800', '--boot-ms', '100']);
    const physics = JSON.parse(await fs.readFile(path.join(directory, 'physics/scroll-physics.json'), 'utf8'));
    assert.equal(physics.tests.length, 2);
    assert.ok(physics.tests.every(test => test.rows.at(-1).y > 0), 'trusted wheel and key move the native scroller');
    await execFileAsync(process.execPath, [path.join(HERE, 'mirror.mjs'), '--mode', 'record', '--url', url,
      '--out', path.join(directory, 'mirror'), '--boot-ms', '100', '--observe-ms', '100']);
    // Remove the network source to prove route fulfil replays the document offline.
    await new Promise(resolve => server.close(resolve));
    const replay = await openBrowser({ ...options, mirror: path.join(directory, 'mirror'), offline: true });
    try {
      const response = await replay.page.goto(url);
      assert.equal(response.status(), 200);
      assert.equal(await replay.page.locator('#box').textContent(), 'Fixture');
      assert.ok(replay.replay.hits > 0);
    } finally { await replay.browser.close(); }
    console.log('PASS browser checks: 6 forward/reverse captures, requested y, computed transform, WebGL shader pairing, no shader export, FFmpeg decode, identity/alpha checks, trusted wheel + key input, mirror record + offline replay');
  } finally {
    if (server.listening) await new Promise(resolve => server.close(resolve));
  }
}
