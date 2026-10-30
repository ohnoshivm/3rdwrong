import { chromium } from 'playwright-core';
import assert from 'node:assert/strict';
const b = await chromium.launch({ channel:'chrome', headless:true }); const ctx = await b.newContext(); await ctx.addInitScript({ path:'capture-init.js' });
const page = await ctx.newPage(); await page.goto('file://' + process.cwd() + '/page-cap/index.html');
const r = await page.evaluate(() => ({ programs: window.__RE.programs.filter(p=>p.vertex&&p.fragment).length, hasMain: /projectionMatrix/.test(window.__RE.programs.map(p=>p.vertex).join('')), draws: window.__RE.draws, ctx: window.__RE.contexts.length, hand: window.__RE.scenes[0].getObjectByName('hand').position.toArray(), dump: window.__RE.dump().map(d=>d.type+':'+d.vertices) }));
console.log(JSON.stringify(r)); assert.ok(r.programs>=1 && r.hasMain && r.draws>=1 && r.ctx>=1);
assert.deepEqual(r.dump,['Scene:null','Mesh:24']);
await b.close(); console.log('capture-init OK');
