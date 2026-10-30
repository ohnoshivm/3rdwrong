import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { cli, number, viewport, openBrowser, navigate, json, main } from './lib.mjs';

export function stepPositions(start, end, step) {
  if (![start, end, step].every(Number.isFinite) || start < 0 || end < start || step <= 0) throw new Error('Invalid capture range');
  const count = Math.ceil((end - start) / step);
  if (count > 10000) throw new Error('Capture exceeds 10,001 positions; increase --step');
  return Array.from({ length: count + 1 }, (_, index) => Math.min(end, start + index * step));
}

async function prepare(page, selectors, limit) {
  return page.evaluate(({ selectors, limit }) => {
    const nodes = new Set();
    const matched = {};
    for (const selector of selectors) {
      const roots = [...document.querySelectorAll(selector)];
      matched[selector] = roots.length;
      for (const root of roots) { nodes.add(root); for (const child of root.querySelectorAll('*')) nodes.add(child); }
    }
    const pathOf = element => {
      if (element.id) return '#' + CSS.escape(element.id);
      const parts = [];
      for (let node = element; node?.nodeType === 1; node = node.parentElement) {
        if (node.id) { parts.unshift('#' + CSS.escape(node.id)); break; }
        const siblings = node.parentElement ? [...node.parentElement.children].filter(x => x.tagName === node.tagName) : [node];
        parts.unshift(node.localName + ':nth-of-type(' + (siblings.indexOf(node) + 1) + ')');
      }
      return parts.join(' > ');
    };
    const all = [...nodes];
    window.__MT_ELEMENTS = all.slice(0, limit).map((element, index) => ({ element, id: index, selector: pathOf(element) }));
    window.__MT_SNAPSHOT = ignoreUniforms => ({
      y: scrollY, docHeight: document.documentElement.scrollHeight,
      dom: window.__MT_ELEMENTS.map(({ element, id, selector }) => {
        if (!element.isConnected) return { id, selector, disconnected: true };
        const c = getComputedStyle(element), r = element.getBoundingClientRect();
        return { id, selector, rect: { x: r.x, y: r.y, width: r.width, height: r.height },
          transform: c.transform, opacity: Number(c.opacity), filter: c.filter, clipPath: c.clipPath,
          color: c.color, backgroundColor: c.backgroundColor, visibility: c.visibility, display: c.display,
          fontFamily: c.fontFamily, fontSize: c.fontSize, lineHeight: c.lineHeight,
          fontWeight: c.fontWeight, letterSpacing: c.letterSpacing, zIndex: c.zIndex };
      }),
      three: window.__MOTION_TEARDOWN__?.sample(ignoreUniforms) ?? { available: false },
    });
    return { matched, count: window.__MT_ELEMENTS.length, total: all.length, truncated: all.length > limit };
  }, { selectors, limit });
}

async function settle(page, target, timeoutMs, ignoreUniforms) {
  return page.evaluate(async ({ target, timeoutMs, ignoreUniforms }) => {
    const start = performance.now();
    let previous = null, stableSince = null, samples = 0, matched = false;
    const quantise = (_, value) => typeof value === 'number' ? Math.round(value * 1000) / 1000 : value;
    while (performance.now() - start < timeoutMs) {
      const snap = window.__MT_SNAPSHOT(ignoreUniforms);
      // Exclude counters and time metadata; include actual observable animation state.
      const signature = JSON.stringify({ y: snap.y, dom: snap.dom, objects: snap.three.objects,
        cameras: snap.three.cameras }, quantise);
      matched = Math.abs(snap.y - target) <= 1;
      if (signature === previous && matched) stableSince ??= performance.now();
      else stableSince = null;
      samples++; previous = signature;
      if (stableSince !== null && performance.now() - stableSince >= 300) {
        return { settled: true, targetReached: true, elapsedMs: performance.now() - start, samples };
      }
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    return { settled: false, targetReached: matched, elapsedMs: performance.now() - start, samples,
      reason: matched ? 'state-changing-or-timeout' : 'requested-scroll-not-reached' };
  }, { target, timeoutMs, ignoreUniforms });
}

export async function runCapture(options) {
  const out = path.resolve(options.out);
  const start = number(options.start, 'start'), step = number(options.step, 'step', { min: 0.01 });
  const settleMs = number(options['settle-ms'], 'settle-ms', { min: 400, max: 60000 });
  const session = await openBrowser(options);
  const { browser, page } = session;
  try {
    await fs.mkdir(out, { recursive: true });
    const navigation = await navigate(page, options);
    const maxY = await page.evaluate(() => Math.max(0, document.documentElement.scrollHeight - innerHeight));
    const end = options.end === undefined ? maxY : number(options.end, 'end');
    if (end > maxY || start > maxY) throw new Error(`Range exceeds current native maximum ${maxY}px. Verify boot/height, or choose a smaller --end.`);
    const positions = stepPositions(start, end, step);
    const elements = await prepare(page, options.selector ?? ['body'], number(options['max-elements'], 'max-elements', { min: 1, max: 20000, integer: true }));
    if (!elements.count) throw new Error('Selectors matched no elements');
    const report = { version: 1, url: options.url, capturedAt: new Date().toISOString(),
      browser: browser.version(), viewport: { ...viewport(options), dpr: Number(options.dpr) }, navigation,
      maxY, positions, elements, reducedMotion: options['reduced-motion'],
      ignoredSettleUniforms: options['ignore-uniform'] ?? [], steps: [],
      limits: ['Three state depends on exposed devtools events; worker-owned canvases are not observed.',
        'Clip playback time in custom engines is unknown unless exposed as a uniform.',
        'No ready-selector means application readiness is not asserted.'] };
    for (const direction of options['round-trip'] ? ['forward', 'reverse'] : ['forward']) {
      const sequence = direction === 'reverse' ? [...positions].reverse() : positions;
      await fs.mkdir(path.join(out, direction), { recursive: true });
      for (const y of sequence) {
        const index = positions.indexOf(y), stem = `step-${String(index).padStart(4, '0')}`;
        await page.evaluate(y => window.scrollTo({ top: y, left: 0, behavior: 'instant' }), y);
        const stability = await settle(page, y, settleMs, options['ignore-uniform'] ?? []);
        const state = await page.evaluate(() => window.__MT_SNAPSHOT([]));
        const screenshot = `${direction}/${stem}.png`, data = `${direction}/${stem}.json`;
        const row = { index, direction, requestedY: y, actualY: state.y, ...stability, screenshot, data };
        await page.screenshot({ path: path.join(out, screenshot), animations: 'allow', caret: 'hide' });
        await json(path.join(out, data), { ...row, capturedAt: new Date().toISOString(), state });
        report.steps.push(row);
        await json(path.join(out, 'capture.json'), { ...report, errors: session.errors, replay: session.replay });
        console.log(`${direction} ${stem}: requested ${y}, actual ${state.y}, settled ${stability.settled}`);
      }
    }
    report.summary = { steps: report.steps.length, unsettled: report.steps.filter(x => !x.settled).length,
      unreachable: report.steps.filter(x => !x.targetReached).length, errors: session.errors.length };
    await json(path.join(out, 'capture.json'), { ...report, errors: session.errors, replay: session.replay });
    console.log(JSON.stringify(report.summary));
    if (report.summary.unsettled) process.exitCode = 2;
    return report;
  } finally { await browser.close(); }
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main(async () => {
  const options = cli({ start: { type: 'string', default: '0' }, end: { type: 'string' },
    step: { type: 'string', default: '90' }, 'settle-ms': { type: 'string', default: '3000' },
    'max-elements': { type: 'string', default: '4000' }, 'round-trip': { type: 'boolean', default: false },
    'ignore-uniform': { type: 'string', multiple: true } });
  if (options.help) { console.log('capture-steps.mjs --url URL --out DIR [--viewport 1440x900 --start 0 --end PX --step 90 --selector CSS --round-trip --mirror DIR --offline --ready-selector CSS --settle-ms 3000 --ignore-uniform NAME]'); return; }
  await runCapture(options);
});
