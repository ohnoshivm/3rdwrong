import { playwright } from '../agent-system/scripts/lib.mjs';
import { fileURLToPath } from 'node:url';
const { chromium } = await playwright();
import fs from 'node:fs/promises';
import path from 'node:path';

const origin = process.env.REBUILD_URL ?? 'http://127.0.0.1:5190/';
const captureUrl = new URL(origin);
captureUrl.searchParams.set('debug', '1');
const media = path.dirname(fileURLToPath(import.meta.url));
const output = path.join(media, 'rebuild-steps');
const handOutput = path.join(media, 'hand-sequence');
const chrome = process.env.CHROME_PATH;
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

await fs.mkdir(output, { recursive: true });
await fs.mkdir(handOutput, { recursive: true });
const browser = await chromium.launch({
  ...(chrome ? { executablePath: chrome } : { channel: 'chrome' }),
  headless: true,
  args: ['--use-angle=metal', '--ignore-gpu-blocklist', '--enable-gpu-rasterization', '--disable-features=CalculateNativeWinOcclusion'],
});
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, reducedMotion: 'no-preference' });
const page = await context.newPage();
const consoleErrors = [];
const pageErrors = [];
page.on('console', (message) => { if (message.type() === 'error') consoleErrors.push(message.text()); });
page.on('pageerror', (error) => pageErrors.push(String(error)));
await page.addInitScript(() => {
  history.scrollRestoration = 'manual';
  const extendStudyTail = () => {
    const spacer = document.querySelector('#scroll-spacer');
    if (spacer) spacer.style.height = 'calc(var(--vh) * 200)';
  };
  new MutationObserver(extendStudyTail).observe(document, { childList: true, subtree: true });
  document.addEventListener('DOMContentLoaded', extendStudyTail, { once: true });
});

async function waitForReady() {
  await page.goto(captureUrl.href, { waitUntil: 'networkidle', timeout: 60000 });
  await page.waitForFunction(() => document.querySelector('#canvas')?.getContext('webgl2') && document.querySelector('#preloader')?.hidden, { timeout: 30000 });
  await page.evaluate(() => document.fonts.ready);
  await wait(1500);
}

await waitForReady();

const gpu = await page.evaluate(() => {
  const gl = document.querySelector('#canvas').getContext('webgl2');
  const extension = gl.getExtension('WEBGL_debug_renderer_info');
  return {
    vendor: extension ? gl.getParameter(extension.UNMASKED_VENDOR_WEBGL) : gl.getParameter(gl.VENDOR),
    renderer: extension ? gl.getParameter(extension.UNMASKED_RENDERER_WEBGL) : gl.getParameter(gl.RENDERER),
    dpr: window.devicePixelRatio,
    viewport: [window.innerWidth, window.innerHeight],
  };
});

async function capture(y, destination) {
  let lastFailure;
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      if (y === 0) await waitForReady();
      await page.evaluate((scrollY) => window.scrollTo({ top: scrollY, left: 0, behavior: 'instant' }), y);
      await page.waitForFunction((scrollY) => window.scrollY === scrollY, y, { timeout: 5000 });
      await page.waitForFunction((scrollY) => {
        const match = document.querySelector('#debug-hud')?.textContent?.match(/scrollY\s+(-?\d+)/);
        return match && Number(match[1]) === scrollY;
      }, y, { timeout: 5000 });
      await page.evaluate((scrollY) => new Promise((resolve, reject) => {
        let stable = 0;
        let previous = '';
        const sample = () => {
          const hud = document.querySelector('#debug-hud')?.textContent ?? '';
          const nativeY = window.scrollY;
          const hero = document.querySelector('#hero');
          const heroRect = hero?.getBoundingClientRect();
          const heroVisible = Boolean(heroRect && heroRect.bottom > 0 && heroRect.top < innerHeight
            && getComputedStyle(hero).visibility !== 'hidden' && getComputedStyle(hero).display !== 'none');
          if (nativeY !== scrollY || (scrollY < 450 && !heroVisible)) {
            reject(new Error(`capture guard failed at y=${scrollY}: native=${nativeY}, heroVisible=${heroVisible}`));
            return;
          }
          const state = `${nativeY}|${hud}`;
          stable = state === previous ? stable + 1 : 0;
          previous = state;
          if (stable >= 6) resolve();
          else requestAnimationFrame(sample);
        };
        requestAnimationFrame(sample);
      }), y);
      await wait(350);
      const bytes = await page.screenshot({ type: 'jpeg', quality: 80, scale: 'device' });
      await fs.writeFile(destination, bytes);
      return;
    } catch (error) {
      lastFailure = error;
      if (attempt < 3 && y === 0) await wait(500);
    }
  }
  throw new Error(`Unable to capture verified frame y=${y} after 3 attempts: ${lastFailure}`);
}

for (let index = 0; index <= 100; index++) {
  const y = index * 90;
  await capture(y, path.join(output, `step-${String(index).padStart(3, '0')}.jpg`));
  if (index % 10 === 0) console.log(`captured step ${index}/100 (y=${y})`);
}
for (const y of [3060, 3600, 4200, 4950, 5400]) {
  await capture(y, path.join(handOutput, `hand-y${y}.jpg`));
  console.log(`captured hand sequence y=${y}`);
}
await capture(6000, path.join(handOutput, 'scroll-y6000.jpg'));

const report = { origin, gpu, swiftshader: /swiftshader|llvmpipe|software/i.test(gpu.renderer), consoleErrors, pageErrors };
await fs.writeFile(path.join(media, 'capture-report.json'), `${JSON.stringify(report, null, 2)}\n`);
await context.close();
await browser.close();
console.log(JSON.stringify(report, null, 2));
