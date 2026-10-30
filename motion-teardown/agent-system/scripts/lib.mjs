// Original capture helpers. MIT © 2026 3RDWRONG.
import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { parseArgs } from 'node:util';
import { createHash } from 'node:crypto';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const sha256 = value => createHash('sha256').update(value).digest('hex');
export const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
export async function json(file, value) {
  await fs.mkdir(path.dirname(path.resolve(file)), { recursive: true });
  const tmp = `${file}.tmp`;
  await fs.writeFile(tmp, JSON.stringify(value, null, 2) + '\n');
  await fs.rename(tmp, file);
}
export function cli(extra = {}) {
  return parseArgs({ options: {
    url: { type: 'string' }, out: { type: 'string', default: 'motion-capture' },
    viewport: { type: 'string', default: '1440x900' }, dpr: { type: 'string', default: '1' },
    selector: { type: 'string', multiple: true }, headed: { type: 'boolean', default: false },
    executable: { type: 'string' }, timeout: { type: 'string', default: '15000' },
    'boot-ms': { type: 'string', default: '1000' }, 'ready-selector': { type: 'string' },
    mirror: { type: 'string' }, offline: { type: 'boolean', default: false },
    'reduced-motion': { type: 'boolean', default: false },
    help: { type: 'boolean', default: false }, ...extra,
  }, strict: true }).values;
}
export function number(value, name, { min = 0, max = Infinity, integer = false } = {}) {
  const result = Number(value);
  if (!Number.isFinite(result) || result < min || result > max || (integer && !Number.isInteger(result))) {
    throw new Error(`${name} must be ${integer ? 'an integer' : 'a number'} in [${min}, ${max}]`);
  }
  return result;
}
export function viewport(options) {
  const match = /^(\d+)x(\d+)$/.exec(options.viewport);
  if (!match) throw new Error('--viewport must be WIDTHxHEIGHT');
  return { width: number(match[1], 'width', { min: 1, max: 16384, integer: true }),
    height: number(match[2], 'height', { min: 1, max: 16384, integer: true }) };
}
export function pageURL(value) {
  if (!value) throw new Error('--url is required');
  const url = new URL(value);
  if (!['http:', 'https:'].includes(url.protocol) || url.username || url.password) {
    throw new Error('Use a public http(s) URL without embedded credentials');
  }
  url.hash = '';
  return url.href;
}
export async function playwright() {
  const require = createRequire(import.meta.url);
  const paths = [HERE];
  if (process.env.PLAYWRIGHT_CORE_PATH) paths.unshift(path.resolve(process.env.PLAYWRIGHT_CORE_PATH));
  try { return require(require.resolve('playwright-core', { paths })); }
  catch { throw new Error('playwright-core missing. Run npm install in scripts/, or set PLAYWRIGHT_CORE_PATH to a folder containing node_modules/playwright-core.'); }
}
export async function openBrowser(options) {
  const { chromium } = await playwright();
  const browser = await chromium.launch({ headless: !options.headed,
    ...(options.executable ? { executablePath: options.executable } : { channel: 'chrome' }) });
  try {
    const context = await browser.newContext({ viewport: viewport(options),
      deviceScaleFactor: number(options.dpr, 'dpr', { min: 0.1, max: 4 }),
      reducedMotion: options['reduced-motion'] ? 'reduce' : 'no-preference',
      serviceWorkers: 'block' });
    await context.addInitScript({ path: path.join(HERE, 'hooks.js') });
    const replay = options.mirror ? await attachMirror(context, options.mirror, options.offline) : null;
    if (options.offline && !options.mirror) throw new Error('--offline requires --mirror');
    const page = await context.newPage();
    page.setDefaultTimeout(number(options.timeout, 'timeout', { min: 1, max: 300000 }));
    const errors = [];
    page.on('pageerror', error => errors.push({ kind: 'pageerror', message: error.message }));
    page.on('console', message => { if (message.type() === 'error') errors.push({ kind: 'console', message: message.text() }); });
    return { browser, context, page, errors, replay };
  } catch (error) { await browser.close(); throw error; }
}
export async function navigate(page, options) {
  const response = await page.goto(pageURL(options.url), { waitUntil: 'domcontentloaded' });
  if (!response || response.status() >= 400) throw new Error(`Navigation failed: HTTP ${response?.status() ?? 'unknown'}`);
  await page.bringToFront();
  // This is a declared warm-up, never a claim that the app has booted.
  await page.waitForTimeout(number(options['boot-ms'], 'boot-ms', { max: 60000 }));
  if (options['ready-selector']) await page.waitForSelector(options['ready-selector'], { state: 'visible' });
  return { status: response.status(), url: page.url(), readySelector: options['ready-selector'] ?? null,
    readiness: options['ready-selector'] ? 'selector-visible' : 'not-asserted' };
}
export async function attachMirror(context, directory, offline = false) {
  const root = await fs.realpath(directory);
  const manifest = JSON.parse(await fs.readFile(path.join(root, 'mirror.json'), 'utf8'));
  if (manifest.version !== 1 || !Array.isArray(manifest.entries)) throw new Error('Unsupported mirror manifest');
  const entries = new Map();
  for (const item of manifest.entries) {
    if (!/^[a-f0-9]{64}\.bin$/.test(item.file) || !/^[a-f0-9]{64}$/.test(item.sha256)) throw new Error('Unsafe mirror blob identity');
    entries.set(pageURL(item.url), item);
  }
  const report = { hits: 0, misses: [], offline };
  const verified = new Map();
  await context.route('**/*', async route => {
    const request = route.request();
    const entry = request.method() === 'GET' ? entries.get(request.url()) : null;
    if (!entry) {
      report.misses.push({ url: request.url(), method: request.method() });
      return offline ? route.abort('blockedbyclient') : route.continue();
    }
    try {
      let body = verified.get(entry.file);
      if (!body) {
        const target = await fs.realpath(path.join(root, 'blobs', entry.file));
        if (!target.startsWith(root + path.sep)) throw new Error('Mirror symlink escapes root');
        body = await fs.readFile(target);
        if (sha256(body) !== entry.sha256) throw new Error('Mirror checksum mismatch');
        verified.set(entry.file, body);
      }
      report.hits++;
      await route.fulfill({ status: entry.status, headers: entry.headers, body });
    } catch (error) {
      report.misses.push({ url: request.url(), error: error.message });
      await route.abort('failed');
    }
  });
  return report;
}
export async function networkRecorder(context, page) {
  const cdp = await context.newCDPSession(page);
  await cdp.send('Network.enable');
  const records = [], active = new Map();
  cdp.on('Network.requestWillBeSent', event => {
    const previous = active.get(event.requestId);
    if (previous && event.redirectResponse) {
      previous.status = event.redirectResponse.status;
      previous.redirectTo = event.request.url;
    }
    const row = { id: `${event.requestId}:${records.length}`, url: event.request.url, method: event.request.method,
      type: event.type, initiator: event.initiator, status: null, mime: null,
      transferBytes: null, decodedBytes: null, startedSeconds: event.timestamp };
    active.set(event.requestId, row); records.push(row);
  });
  cdp.on('Network.responseReceived', event => {
    const row = active.get(event.requestId);
    if (row) Object.assign(row, { status: event.response.status, mime: event.response.mimeType,
      fromCache: !!(event.response.fromDiskCache || event.response.fromServiceWorker) });
  });
  cdp.on('Network.loadingFinished', event => {
    const row = active.get(event.requestId);
    if (row) row.transferBytes = event.encodedDataLength;
  });
  cdp.on('Network.loadingFailed', event => {
    const row = active.get(event.requestId);
    if (row) row.failure = event.errorText;
  });
  return { records, stop: async () => {
    const timings = await page.evaluate(() => [...performance.getEntriesByType('navigation'),
      ...performance.getEntriesByType('resource')].map(e => ({ url: e.name,
      decoded: e.decodedBodySize, encoded: e.encodedBodySize, transfer: e.transferSize })));
    for (const row of records) {
      const timing = timings.find(e => e.url === row.url);
      if (timing) {
        // Zero cross-origin values may mean unavailable timing, not zero-byte content.
        row.decodedBytes = timing.decoded || null;
        row.encodedBodyBytes = timing.encoded || null;
      }
    }
    await cdp.detach(); return records;
  } };
}
export function main(run) {
  run().catch(error => { console.error(error.message); process.exitCode = 1; });
}
