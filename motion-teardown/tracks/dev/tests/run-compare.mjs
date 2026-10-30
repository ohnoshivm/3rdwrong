// lab/compare-steps.mjs
// usage: node compare-steps.mjs <urlA> <urlB> [outDir]
// Needs: playwright-core, Chrome, ffmpeg. Writes a-<y>.png, b-<y>.png, pair-<y>.png, report.json.
import { chromium } from 'playwright-core';
import { mkdirSync, writeFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';

const [urlA, urlB, out = 'qa/compare'] = process.argv.slice(2);
const ys = [0, 270, 900, 1530, 2250, 3060, 3600, 4320, 5130, 6000, 7200, 8100];
mkdirSync(out, { recursive: true });

const twoFrames = () => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)));

const browser = await chromium.launch({ channel: 'chrome' });
const report = { a: {}, b: {}, ssim: {} };

for (const [tag, url] of [['a', urlA], ['b', urlB]]) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const problems = [];
  page.on('console', (m) => { if (['error', 'warning'].includes(m.type())) problems.push(m.text()); });
  page.on('pageerror', (e) => problems.push(String(e)));
  await page.goto(url, { waitUntil: 'load' });

  for (const y of ys) {
    await page.evaluate((y) => scrollTo(0, y), y);
    await page.evaluate(twoFrames);
    await page.screenshot({ path: `${out}/${tag}-${y}.png` });
  }

  // frame times over one sweep of the whole page
  const frames = await page.evaluate(async () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    const dts = [];
    let last = performance.now();
    for (let i = 0; i <= 300; i++) {
      scrollTo(0, (max * i) / 300);
      await new Promise((r) => requestAnimationFrame(r));
      const now = performance.now();
      dts.push(now - last);
      last = now;
    }
    dts.shift();
    dts.sort((x, y) => x - y);
    return { p50: dts[Math.floor(dts.length * 0.5)], p95: dts[Math.floor(dts.length * 0.95)] };
  });
  report[tag] = { ...frames, consoleProblems: problems };
  await page.close();
}
await browser.close();

for (const y of ys) {
  const a = `${out}/a-${y}.png`, b = `${out}/b-${y}.png`;
  spawnSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', a, '-i', b, '-filter_complex', 'hstack', `${out}/pair-${y}.png`]);
  const r = spawnSync('ffmpeg', ['-i', a, '-i', b, '-lavfi',
    '[0:v]scale=720:-2,format=gray[a];[1:v]scale=720:-2,format=gray[b];[a][b]ssim', '-f', 'null', '-'], { encoding: 'utf8' });
  report.ssim[y] = Number(/All:([0-9.]+)/.exec(r.stderr)?.[1] ?? NaN);
}
writeFileSync(`${out}/report.json`, JSON.stringify(report, null, 2));
console.log(JSON.stringify({ a: report.a, b: report.b, ssim: report.ssim }));
