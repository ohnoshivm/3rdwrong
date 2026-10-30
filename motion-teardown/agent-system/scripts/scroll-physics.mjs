import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { cli, number, openBrowser, navigate, json, main } from './lib.mjs';

export function fitFollower(series) {
  if (series.length < 12) return { valid: false, reason: 'too-few-samples' };
  const start = series[0].y, target = series.at(-1).y, displacement = target - start;
  if (Math.abs(displacement) < 2) return { valid: false, reason: 'no-observable-movement', displacement };
  const tail = series.slice(-10).map(row => row.y);
  if (Math.max(...tail) - Math.min(...tail) > 1) return { valid: false, reason: 'endpoint-not-settled', displacement };
  const onset = series.findIndex(row => Math.abs(row.y - start) > 0.5);
  // Exclude input latency and the instantaneous first jump. Fit only the transient.
  const pairs = [];
  for (let index = Math.max(1, onset + 1); index < series.length; index++) {
    const previous = series[index - 1], current = series[index];
    const progress = (previous.y - start) / displacement, dt = (current.t - previous.t) / 1000;
    if (progress > 0.02 && progress < 0.95 && dt > 0 && dt < 0.2) pairs.push({ previous, current, dt });
  }
  if (pairs.length < 4) return { valid: false, reason: 'insufficient-transient-native-or-instant-scroll', displacement };
  let best = { cPerSecond: null, sse: Infinity };
  for (let c = 0.1; c <= 60; c += 0.1) {
    const sse = pairs.reduce((sum, { previous, current, dt }) => {
      const predicted = previous.y + (target - previous.y) * (1 - Math.exp(-c * dt));
      return sum + (predicted - current.y) ** 2;
    }, 0);
    if (sse < best.sse) best = { cPerSecond: Math.round(c * 10) / 10, sse };
  }
  return { valid: true, model: 'first-order exponential candidate, not proof of engine',
    start, target, displacement, onsetMs: series[onset].t, samplesFit: pairs.length,
    cPerSecond: best.cPerSecond, tauMs: 1000 / best.cPerSecond,
    rmsePx: Math.sqrt(best.sse / pairs.length), boundaryFit: best.cPerSecond <= 0.1 || best.cPerSecond >= 59.9 };
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main(async () => {
  const options = cli({ start: { type: 'string', default: '0' }, wheel: { type: 'string', default: '100,300' },
    key: { type: 'string', multiple: true }, 'duration-ms': { type: 'string', default: '2600' } });
  if (options.help) { console.log('scroll-physics.mjs --url URL --out DIR [--wheel 100,300 --key PageDown --start 0 --selector WRAPPER --duration-ms 2600 --mirror DIR]'); return; }
  const duration = number(options['duration-ms'], 'duration-ms', { min: 500, max: 30000 });
  const startY = number(options.start, 'start');
  const deltas = options.wheel.split(',').map(value => number(value, 'wheel delta', { min: -10000, max: 10000 }));
  const tests = [...deltas.map(delta => ({ kind: 'wheel', delta })),
    ...(options.key ?? ['PageDown', 'ArrowDown']).map(key => ({ kind: 'key', key }))];
  const { browser, page, errors, replay } = await openBrowser(options);
  const out = path.resolve(options.out);
  try {
    const navigation = await navigate(page, options);
    const report = { url: options.url, viewport: options.viewport, dpr: Number(options.dpr), navigation,
      browser: browser.version(), tests: [], notes: ['Trusted browser input; rAF samples are scheduling observations.',
        'Fit uses native y. A transformed virtual wrapper is recorded but its internal position is not inferred from a matrix.'] };
    for (const test of tests) {
      await page.evaluate(y => { window.scrollTo({ top: y, behavior: 'instant' }); document.activeElement?.blur?.(); }, startY);
      await page.mouse.move(20, 20);
      await page.waitForTimeout(600);
      const baseline = await page.evaluate(() => scrollY);
      if (Math.abs(baseline - startY) > 1) throw new Error('Start scroll not reached; verify loader/native-scroll route');
      await page.evaluate(({ duration, selector }) => {
        window.__MT_PHYSICS = { rows: [], done: false, started: performance.now() };
        const record = window.__MT_PHYSICS;
        const wrapper = selector ? document.querySelector(selector) : null;
        const tick = time => {
          record.rows.push({ t: time - record.started, y: scrollY,
            nativeTop: document.documentElement.scrollTop,
            wrapperTransform: wrapper ? getComputedStyle(wrapper).transform : null });
          if (time - record.started < duration) requestAnimationFrame(tick);
          else record.done = true;
        };
        record.rows.push({ t: 0, y: scrollY, nativeTop: document.documentElement.scrollTop,
          wrapperTransform: wrapper ? getComputedStyle(wrapper).transform : null });
        requestAnimationFrame(tick);
      }, { duration, selector: options.selector?.[0] });
      if (test.kind === 'wheel') await page.mouse.wheel(0, test.delta);
      else await page.keyboard.press(test.key);
      await page.waitForFunction(() => window.__MT_PHYSICS.done, null, { timeout: duration + 5000 });
      const rows = await page.evaluate(() => window.__MT_PHYSICS.rows);
      const fit = fitFollower(rows);
      report.tests.push({ ...test, fit, rows });
      await json(path.join(out, 'scroll-physics.json'), { ...report, errors, replay });
      console.log(`${test.kind} ${test.delta ?? test.key}: ${fit.valid ? `c=${fit.cPerSecond}/s, RMSE=${fit.rmsePx.toFixed(3)}px` : fit.reason}`);
    }
  } finally { await browser.close(); }
});
