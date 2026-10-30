import { chromium } from 'playwright-core';
import assert from 'node:assert/strict';
const b = await chromium.launch({ channel:'chrome', headless:true, args:['--use-angle=metal','--ignore-gpu-blocklist'] });
const page = await b.newPage({ viewport:{width:1440,height:900} }); const errs=[]; page.on('console',m=>{ if(['error','warning'].includes(m.type())) errs.push(m.text()); }); page.on('pageerror',e=>errs.push(String(e)));
await page.goto('file://' + process.cwd() + '/page-l2m/index.html');
for (const y of [0, 900, 1400, 2700]) { await page.evaluate(y=>scrollTo(0,y), y); await page.waitForTimeout(250); await page.screenshot({ path:`l2m-${y}.png` }); }
console.log('errs', JSON.stringify(errs)); assert.deepEqual(errs,[]); await b.close(); console.log('main-l2 OK');
