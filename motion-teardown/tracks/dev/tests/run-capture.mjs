// lab/capture.mjs
import { chromium } from 'playwright-core';
const browser = await chromium.launch({
  channel: 'chrome',
  headless: true,
  args: ['--use-angle=metal', '--ignore-gpu-blocklist'], // macOS; adjust for your platform
});
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
await context.addInitScript({ path: 'capture-init.js' });
const page = await context.newPage();
page.on('requestfailed', (r) => console.log('FAIL', r.url(), r.failure()?.errorText));
page.on('response', (r) => { if (r.status() >= 400) console.log('HTTP', r.status(), r.url()); });
await page.goto('file://' + process.cwd() + '/page-cap/index.html');
await page.waitForFunction(() => window.__RE.renderers.length > 0, null, { timeout: 30_000 });
const info = await page.evaluate(() => ({
  scenes: window.__RE.scenes.length,
  graph: window.__RE.dump(),
  programs: window.__RE.programs.length,
  renderer: window.__RE.renderers[0] && {
    pixelRatio: window.__RE.renderers[0].getPixelRatio(),
    toneMapping: window.__RE.renderers[0].toneMapping,
  },
}));
console.log(JSON.stringify(info).slice(0, 2000));
await browser.close();
