import fs from 'node:fs/promises';
import path from 'node:path';
import { cli, number, pageURL, openBrowser, navigate, networkRecorder, sha256, json, main } from './lib.mjs';

main(async () => {
  const options = cli({ mode: { type: 'string', default: 'record' }, origin: { type: 'string', multiple: true },
    'observe-ms': { type: 'string', default: '3000' }, 'max-bytes': { type: 'string', default: '20971520' },
    'scroll-end': { type: 'string' }, step: { type: 'string', default: '450' } });
  if (options.help) { console.log('mirror.mjs --mode record|replay --url URL --out DIR [--mirror DIR --offline --origin https://cdn.example --observe-ms 3000 --scroll-end PX --step 450]'); return; }
  if (!['record', 'replay'].includes(options.mode)) throw new Error('--mode must be record or replay');
  const target = pageURL(options.url), out = path.resolve(options.out);
  if (options.mode === 'record' && options.mirror) throw new Error('Record the live network without --mirror');
  if (options.mode === 'replay' && !options.mirror) throw new Error('Replay requires --mirror DIR');
  const allowed = new Set([new URL(target).origin, ...(options.origin ?? []).map(url => new URL(pageURL(url)).origin)]);
  const maxBytes = number(options['max-bytes'], 'max-bytes', { min: 1, max: 1000000000 });
  const observeMs = number(options['observe-ms'], 'observe-ms', { max: 60000 });
  const step = number(options.step, 'step', { min: 1 });
  const session = await openBrowser(options), { browser, context, page } = session;
  const pending = new Set(), entries = new Map(), failures = [];
  const headersAllowed = new Set(['content-type', 'content-language', 'access-control-allow-origin',
    'cross-origin-resource-policy', 'content-security-policy', 'x-content-type-options', 'cache-control']);
  let recording = true;
  try {
    await fs.mkdir(out, { recursive: true });
    const network = await networkRecorder(context, page);
    if (options.mode === 'record') {
      await fs.mkdir(path.join(out, 'blobs'), { recursive: true });
      page.on('response', response => {
        if (!recording) return;
        const request = response.request(), url = response.url();
        if (request.method() !== 'GET' || !allowed.has(new URL(url).origin)) return;
        const job = (async () => {
          if (response.status() !== 200) { failures.push({ url, reason: `HTTP ${response.status()} not mirrored` }); return; }
          try {
            const headers = response.headers();
            if (Number(headers['content-length']) > maxBytes) throw new Error('Body exceeds --max-bytes');
            // Headerless/streamed responses are bounded by the browser request timeout and the drain below.
            const body = await response.body();
            if (body.length > maxBytes) throw new Error('Body exceeds --max-bytes');
            const digest = sha256(body), file = `${digest}.bin`;
            await fs.writeFile(path.join(out, 'blobs', file), body);
            entries.set(url, { url, status: response.status(), file, sha256: digest, bytes: body.length,
              headers: Object.fromEntries(Object.entries(headers).filter(([key]) => headersAllowed.has(key))) });
          } catch (error) { failures.push({ url, reason: error.message }); }
        })();
        pending.add(job); job.finally(() => pending.delete(job));
      });
    }
    const navigation = await navigate(page, options);
    if (options['scroll-end'] !== undefined) {
      const end = number(options['scroll-end'], 'scroll-end');
      if (Math.ceil(end / step) > 10000) throw new Error('Too many mirror scroll steps');
      for (let y = 0; y <= end; y += step) {
        await page.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y);
        await page.waitForTimeout(200);
      }
      await page.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), end);
    }
    await page.waitForTimeout(observeMs);
    recording = false;
    // Finish bodies already in flight; never keep a recorder alive indefinitely.
    const drained = await Promise.race([Promise.allSettled([...pending]).then(() => true),
      new Promise(resolve => { const timer = setTimeout(() => resolve(false), 10000); timer.unref(); })]);
    const records = await network.stop();
    if (options.mode === 'record') {
      await json(path.join(out, 'mirror.json'), { version: 1, url: target, recordedAt: new Date().toISOString(),
        allowedOrigins: [...allowed], entries: [...entries.values()], failures, drained });
    }
    await json(path.join(out, 'network.json'), { url: target, mode: options.mode, navigation,
      records, failures, drained, replay: session.replay, errors: session.errors });
    if (options.mode === 'replay') await page.screenshot({ path: path.join(out, 'replay.png') });
    console.log(JSON.stringify({ mode: options.mode, requests: records.length, mirrored: entries.size,
      failures: failures.length, drained, replayHits: session.replay?.hits ?? null }));
    if (!drained) process.exitCode = 2;
  } finally { await browser.close(); }
});
