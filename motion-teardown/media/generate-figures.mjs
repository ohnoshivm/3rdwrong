import { playwright } from '../agent-system/scripts/lib.mjs';
const { chromium } = await playwright();
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const media = path.dirname(fileURLToPath(import.meta.url));
const rebuildDir = path.join(media, 'rebuild-steps');
const handDir = path.join(media, 'hand-sequence');
const chromePath = process.env.CHROME_PATH;
const selected = new Set(process.argv.slice(2).length ? process.argv.slice(2) : ['f01', 'f06', 'f07', 'f08']);
const geometryCredit = 'the hand and coaster geometry come from oryzo.ai by Lusion, recoloured';
const ink = '#140304';
const paper = '#fff6f4';
const accent = '#e3141b';
const muted = '#c7acae';

async function dataUri(file) {
  const bytes = await fs.readFile(file);
  const ext = path.extname(file).toLowerCase();
  const mime = ext === '.png' ? 'image/png' : ext === '.webp' ? 'image/webp' : 'image/jpeg';
  return `data:${mime};base64,${bytes.toString('base64')}`;
}

const font = process.env.FIGURE_FONT ? (await fs.readFile(process.env.FIGURE_FONT)).toString('base64') : '';

const css = `
@font-face{font-family:Albert;src:url(data:font/woff2;base64,${font}) format('woff2');font-weight:100 900}
*{box-sizing:border-box}html,body{margin:0;padding:0;background:${ink};color:${paper};font-family:Albert,Arial,sans-serif}
body{width:1600px;padding:68px 76px 54px}.eyebrow{font-size:15px;letter-spacing:.08em;color:#e9797d;text-transform:uppercase;font-weight:650}
h1{font-size:42px;line-height:1.08;letter-spacing:-.035em;margin:14px 0 12px;font-weight:650;max-width:1250px}
.dek{color:${muted};font-size:19px;line-height:1.45;margin:0 0 34px;max-width:1180px}.credit{display:block;margin:24px 0 0 auto;text-align:right;color:#d5babb;font-size:13px;letter-spacing:.02em}
.fig{position:relative;width:1448px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px}.image-panel{position:relative;border:1px solid #56383b;background:#20090c;padding:10px}.image-panel img{width:100%;display:block;object-fit:cover;aspect-ratio:16/10}.tag{position:absolute;left:22px;top:20px;background:${ink};padding:8px 12px;font-size:14px;letter-spacing:.05em;text-transform:uppercase}
.legend{display:flex;gap:22px;margin:14px 0 0;color:${muted};font-size:15px}.legend span:before{content:'';display:inline-block;width:9px;height:9px;border-radius:50%;background:${accent};margin-right:8px}
.frames{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.frame{border:1px solid #56383b;background:#20090c;padding:8px}.frame img{width:100%;height:250px;object-fit:cover;display:block}.frame-label{display:flex;justify-content:space-between;gap:8px;padding:9px 2px 3px;font-size:14px}.frame-label span:last-child{color:${muted};text-align:right}
.table{display:grid;grid-template-columns:1fr 1fr;gap:14px}.agent-column{border:1px solid #56383b;background:#1c070a;padding:24px}.agent-column h2{font-size:23px;margin:0 0 14px}.agent{border-top:1px solid #45272b;padding:13px 0}.agent strong{font-size:17px}.agent small{display:block;color:${muted};font-size:14px;margin-top:4px}.skills{display:flex;gap:9px;margin-top:18px}.skill{border:1px solid #7c4148;border-radius:100px;padding:7px 12px;color:#ffdfe0;font-size:14px}
.atlas-row{display:grid;grid-template-columns:1fr 1fr;gap:20px}.atlas-block{border:1px solid #56383b;background:#20090c;padding:16px}.atlas-block h2{font-size:20px;margin:0 0 12px}.atlas-block img{width:100%;height:275px;object-fit:contain;background:#100507}.props{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:12px}.prop{background:#100507;border:1px solid #56383b;height:132px;display:flex;align-items:center;justify-content:center}.prop img{height:100%;width:100%;object-fit:contain}.prop span{position:absolute;align-self:flex-end;font-size:12px;background:#140304dd;padding:5px 8px}
.grid-compare{display:grid;grid-template-columns:110px 1fr 1fr;gap:9px;align-items:center}.grid-head{color:#edbabe;font-size:13px;text-transform:uppercase;letter-spacing:.07em;padding:0 10px 7px}.row-y{font-size:16px;color:${muted};font-variant-numeric:tabular-nums}.compare-img{position:relative;background:#20090c;border:1px solid #56383b;padding:4px}.compare-img img{display:block;width:100%;height:157px;object-fit:cover}
.timeline{display:grid;grid-template-columns:170px 1fr;gap:0 22px;position:relative}.event{display:contents}.time{font-variant-numeric:tabular-nums;font-size:16px;color:#ffd2d4;padding:12px 0;border-bottom:1px solid #45272b}.event-copy{position:relative;font-size:16px;line-height:1.38;color:${paper};padding:12px 16px;border-bottom:1px solid #45272b}.event-copy:before{content:'';position:absolute;left:-18px;top:19px;width:9px;height:9px;background:${accent};border-radius:50%}.event-copy.fail:before{width:8px;height:8px;background:#ffb34f;border:2px solid ${ink};box-shadow:0 0 0 1px #ffb34f}.event-copy em{font-style:normal;color:#ffc97a;font-size:12px;text-transform:uppercase;letter-spacing:.06em;margin-left:8px}
.comparison{display:grid;grid-template-columns:420px 1fr;gap:22px;align-items:start}.comparison img{width:100%;height:340px;object-fit:contain;background:#20090c;border:1px solid #56383b;padding:12px}.generated-props{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.generated-props figure{margin:0;border:1px solid #56383b;background:#20090c;padding:6px}.generated-props img{height:130px;width:100%;object-fit:contain;border:0;padding:0;background:#100507}.generated-props figcaption{font-size:13px;color:${muted};padding:6px 2px}
.bars{width:100%;border-collapse:collapse;font-size:15px}.bars td{padding:8px 9px;border-bottom:1px solid #45272b}.bars td:first-child{width:250px;color:${paper}}.bars td:last-child{color:${muted};font-variant-numeric:tabular-nums}.bar{height:8px;background:#321015;position:relative}.bar i{position:absolute;left:var(--left);width:var(--width);top:0;height:8px;background:${accent};border-radius:4px}.axis{display:flex;justify-content:space-between;color:${muted};font-size:12px;margin:8px 0 0 260px}
.arch{display:grid;grid-template-columns:1fr;gap:20px}.arch-panel{border:1px solid #56383b;background:#1c070a;padding:22px}.arch-panel h2{font-size:20px;margin:0 0 16px}.layers{display:grid;grid-template-columns:1fr 1fr;gap:12px}.layer{border:1px solid #87464d;padding:15px;background:#25090d}.layer canvas{display:block;width:100%;height:80px;background:#100507;border:1px solid #56383b;margin-bottom:10px}.stack{height:176px;position:relative;border:1px solid #87464d;background:linear-gradient(135deg,#22090d,#100507);overflow:hidden}.canvas-label{position:absolute;inset:0;display:grid;place-items:center;color:#83585d;font-size:18px;letter-spacing:.08em}.overlay-label{position:absolute;left:18%;top:47%;padding:14px 20px;background:#2b0b10;border:1px solid #e3141b;color:#fff6f4;font-size:17px;box-shadow:0 8px 24px #0008}.flow{display:flex;align-items:center;justify-content:space-between;gap:7px;flex-wrap:wrap}.flow span{border:1px solid #87464d;border-radius:7px;padding:12px 11px;font-size:14px;background:#25090d}.arrow{color:#e9797d;font-size:20px}.chain{display:flex;align-items:center;gap:7px;flex-wrap:wrap}.chain span{padding:12px 12px;background:#25090d;border:1px solid #87464d;border-radius:7px;font-size:14px}.chain .disabled{opacity:.5;text-decoration:line-through}.notes{color:${muted};font-size:14px;line-height:1.5;margin-top:12px}
.hand-strip{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.hand-frame{border:1px solid #56383b;background:#20090c;padding:8px}.hand-frame img{width:100%;height:225px;object-fit:cover}.hand-frame div{padding:8px 2px 1px;display:flex;justify-content:space-between;font-size:15px}.hand-frame b{color:#ffb8bc;font-weight:600}
.assets{display:grid;grid-template-columns:repeat(5,1fr);gap:11px}.asset{border:1px solid #56383b;background:#20090c;padding:8px}.asset img{width:100%;height:180px;object-fit:contain;background:#100507;display:block}.asset span{display:block;color:${muted};font-size:12px;overflow-wrap:anywhere;padding-top:7px}
`;

const browser = await chromium.launch({ ...(chromePath ? { executablePath: chromePath } : { channel: 'chrome' }), headless: true, args: ['--use-angle=metal', '--ignore-gpu-blocklist', '--enable-gpu-rasterization'] });
const page = await browser.newPage({ viewport: { width: 1600, height: 1200 }, deviceScaleFactor: 1 });

async function render(name, title, description, content, credit = false, ext = 'png') {
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><main class="fig"><div class="eyebrow">3RDWRONG · MOTION TEARDOWN</div><h1>${title}</h1><p class="dek">${description}</p>${content}${credit ? `<div class="credit">${geometryCredit}</div>` : ''}</main></body></html>`;
  await page.setContent(html, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const dimensions = await page.evaluate(() => ({ width: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight }));
  await page.screenshot({ path: path.join(media, `${name}.${ext}`), type: ext === 'jpg' ? 'jpeg' : 'png', quality: ext === 'jpg' ? 90 : undefined, fullPage: true });
  return dimensions;
}

const y000 = (idx) => String(idx).padStart(3, '0');
if (selected.has('f01')) {
  const rebuild0 = await dataUri(path.join(rebuildDir, 'step-000.jpg'));
  await render('f01-rebuild-hero', 'The rebuild hero at scroll position zero', 'Our crimson-and-white study. Original-site screenshots are omitted; see https://oryzo.ai and the Substack edition for comparisons.', `<div class="image-panel"><img src="${rebuild0}"></div>`, true);
}

if (selected.has('f03')) {
const effects = [
  ['Hero exit', 0, 450], ['Coaster + camera path', 0, 4950], ['“Isn’t just a coaster” in', 450, 1125],
  ['“Isn’t just a coaster” out', 2475, 3150], ['Powered by AI* in', 3150, 4500], ['Hand animation · frames 71→115', 3056, 4950],
  ['Caption in', 4050, 4950], ['Try to hover hand', 4950, 5400], ['Edge glow on', 4950, 5400],
  ['Edge glow off', 6750, 7200], ['Hand fade-out', 7200, 8100],
];
const x0 = 350, x1 = 1420, plotW = x1 - x0;
const grid = Array.from({ length: 10 }, (_, i) => {
  const x = x0 + plotW * i / 9;
  return `<line x1="${x}" y1="56" x2="${x}" y2="${effects.length * 47 + 82}" stroke="#76484d" stroke-opacity=".48"/><text x="${x}" y="38" text-anchor="middle" fill="${muted}" font-size="12">r = ${i}</text><text x="${x}" y="${effects.length * 47 + 105}" text-anchor="middle" fill="${muted}" font-size="12">${i * 900}</text>`;
}).join('');
const bars = effects.map(([name, start, end], i) => {
  const y = 74 + i * 47;
  const x = x0 + plotW * start / 8100;
  const width = plotW * (end - start) / 8100;
  const labelX = end === 8100 ? x + width - 8 : x + width + 8;
  const anchor = end === 8100 ? 'end' : 'start';
  const colour = end === 8100 ? paper : '#f1c6c8';
  return `<text x="0" y="${y + 5}" fill="${paper}" font-size="15">${name}</text><rect x="${x0}" y="${y - 8}" width="${plotW}" height="16" rx="8" fill="#261014"/><rect x="${x}" y="${y - 8}" width="${width}" height="16" rx="8" fill="${accent}"/><text x="${labelX}" y="${y + 5}" text-anchor="${anchor}" fill="${colour}" font-size="12">${start.toLocaleString()}–${end.toLocaleString()}</text>`;
}).join('');
const choreography = `<svg viewBox="0 0 1450 ${effects.length * 47 + 145}" width="100%" role="img"><text x="${x0}" y="18" fill="#e9797d" font-size="13">SECTION PROGRESS · r = 1 + (y − 900) / 900</text>${grid}${bars}<text x="${x0}" y="${effects.length * 47 + 132}" fill="${muted}" font-size="12">SCROLL POSITION · PIXELS</text></svg>`;
await render('f03-choreography', 'Every effect answers to scroll', 'A single section scalar makes the motion reversible. Each bar shows the measured scroll window; the upper axis shows section progress r.', choreography);

}

if (selected.has('f04')) {
const agentColumn = (heading, agents) => `<section class="agent-column"><h2>${heading}</h2>${agents.map(([name, model, files]) => `<div class="agent"><strong>${name}</strong><small>${model}</small><small>Owned: ${files}</small></div>`).join('')}</section>`;
const orchestration = `<div class="table">${agentColumn('Teardown · parallel evidence', [
  ['Director · Claude Opus 5.5', 'Frames, briefs, reconciliation, QA and packaging', 'MOTION-PLAN.md, briefs and RE-REPORT.md'],
  ['Agent A · DeepSeek V4.1 Flash', 'Static code analysis', 'notes/A-code.md'],
  ['Agent B · DeepSeek V4.1 Flash', 'Runtime scroll capture', 'notes/B-runtime.md'],
  ['Agent C · DeepSeek V4.1 Flash', 'Tokens, network, mobile and performance', 'notes/C-tokens.md'],
])}${agentColumn('Build · separate file ownership', [
  ['IMG · GPT-6 Luna', 'Generated imagery and derived maps', 'public/gen/** · scripts/gen/**'],
  ['DOM · DeepSeek scaffold → GPT-6 Luna', 'Scroll, layout, text choreography and preloader', 'package.json · vite.config.ts · tsconfig.json · index.html · src/main.ts · src/contract.ts · src/core/** · src/dom/** · src/styles/** · public/fonts/**'],
  ['GL · GPT-6.1 Sol', 'Renderer, scenes, shaders and post chain', 'src/gl/** · public/ref (linked reference assets)'],
  ['Shared contract', 'FrameState boundary passed from DOM to GL', 'src/contract.ts · shared with GL'],
])}</div><div class="skills"><span class="skill">watch · video to frames</span><span class="skill">reverse-engineer-anything · REA</span><span class="skill">T3 Code orchestration</span></div>`;
await render('f04-orchestration', 'Parallel work needs a shared contract', 'The director split observation from implementation, gave each agent its own files, and made the DOM–GL boundary explicit.', orchestration);

}

if (selected.has('f05')) {
const milestones = [
  ['19:29', 'Founder records the site · 12 seconds'], ['19:34', 'Session resumes after usage limit'], ['~19:40', 'Gemini 503; local frame extraction takes over', 'fail'],
  ['20:05', 'Reverse-engineering prompt sent'], ['~20:07', 'TokenHarbor allowance exhausted', 'fail'], ['~20:10', 'OpenCode run hits transient DNS failure', 'fail'],
  ['20:25', 'Single-agent investigation stalls at preloader', 'fail'], ['21:22', 'Work splits across three teardown agents'], ['21:47', 'Agent A completes static analysis'],
  ['21:55', 'Agent C completes'], ['~22:13', 'Agent B stream drops after files complete', 'fail'], ['~22:45', 'Findings reconciled into the report'],
  ['23:06', 'Founder requests the crimson-and-white rebuild'], ['~23:40', 'IMG, DOM and GL build agents start'], ['~23:50', 'DOM free-tier limit; GPT fallback', 'fail'],
  ['23:51', 'IMG finishes 27 files'], ['00:29', 'Parallel QA; founder accepts strong red glow'], ['~00:45', 'GL reports 20/20 functional tests'],
  ['00:56', 'Localhost preview shown'], ['01:20', 'Founder approves the rebuild'], ['01:29', 'Shareable zip verified · six hours after recording'],
];
const timeline = `<div class="timeline">${milestones.map(([time, event, fail]) => `<div class="event"><div class="time">${time}</div><div class="event-copy ${fail ?? ''}">${event}${fail ? '<em>recovered</em>' : ''}</div></div>`).join('')}</div>`;
await render('f05-timeline', 'A six-hour build, with the failures left in', 'The recording began at 19:29 on 30 October. The verified share zip was ready at 01:29 on 31 October; the route between them was not linear.', timeline);

}

if (selected.has('f06')) {
  const props = await dataUri(path.join(media, 'generated-props.png'));
  await render('f06-props', 'Seven generated props', 'The original four-cell atlas idea uses three lighting views and a height cell. Its image is omitted; our seven generated props use single views with derived alpha and height maps.', `<div class="image-panel"><img style="aspect-ratio:auto;object-fit:contain" src="${props}"></div>`);
}

if (selected.has('f07')) {
  const comparisonYs = [0, 270, 1530, 3060, 4320, 5130, 6000, 7200];
  const rows = await Promise.all(comparisonYs.map(async (y) => {
    const file = y % 90 === 0 ? path.join(rebuildDir, `step-${y000(y / 90)}.jpg`) : path.join(handDir, `scroll-y${y}.jpg`);
    return `<div><div class="grid-head">y = ${y.toLocaleString()} px</div><img style="width:100%;display:block" src="${await dataUri(file)}"></div>`;
  }));
  await render('f07-rebuild-grid', 'Eight rebuild moments across the scroll', 'Original comparisons are omitted from this repository. See https://oryzo.ai and the Substack edition.', `<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">${rows.join('')}</div>`, true, 'jpg');
}

if (selected.has('f08')) {
const fidelity = JSON.parse(await fs.readFile(path.join(media, 'fidelity/fidelity.json'), 'utf8'));
const chartW = 1448, chartH = 610, chartX = 72, chartY = 114, chartPlotW = 1345, chartPlotH = 388;
const chartXPos = (y) => chartX + chartPlotW * y / 9000;
const chartYPos = (value) => chartY + chartPlotH * (1 - value);
const chartSections = [
  ['hero', 0, 450], ['ai-pre', 450, 3150], ['title + hand', 3150, 4950], ['glow hold', 4950, 7200], ['fade', 7200, 8100], ['out of scope', 8100, 9000],
];
const bandSvg = chartSections.map(([name, start, end], index) => {
  const x = chartXPos(start), width = chartXPos(end) - x, mean = fidelity.sections[name];
  return `<rect x="${x}" y="${chartY}" width="${width}" height="${chartPlotH}" fill="${index % 2 ? '#211014' : '#321015'}"/><text x="${x + width / 2}" y="30" text-anchor="middle" fill="${paper}" font-size="13" font-weight="600">${name}</text><text x="${x + width / 2}" y="52" text-anchor="middle" fill="#efafb3" font-size="12">S ${mean.structure.toFixed(2)} · L ${mean.luminance.toFixed(2)}</text>`;
}).join('');
const chartGrid = [0, .2, .4, .6, .8, 1].map((v) => `<line x1="${chartX}" y1="${chartYPos(v)}" x2="${chartX + chartPlotW}" y2="${chartYPos(v)}" stroke="#fff6f4" stroke-opacity=".13"/><text x="${chartX - 14}" y="${chartYPos(v) + 4}" text-anchor="end" fill="${muted}" font-size="12">${v.toFixed(1)}</text>`).join('');
const chartXTicks = Array.from({ length: 11 }, (_, index) => {
  const value = index * 900, x = chartXPos(value);
  return `<line x1="${x}" y1="${chartY}" x2="${x}" y2="${chartY + chartPlotH}" stroke="#fff6f4" stroke-opacity=".07"/><text x="${x}" y="${chartY + chartPlotH + 23}" text-anchor="middle" fill="${muted}" font-size="11">${value.toLocaleString()}</text>`;
}).join('');
const seriesPath = (key) => fidelity.steps.map((row, index) => `${index ? 'L' : 'M'}${chartXPos(row.y).toFixed(1)},${chartYPos(row[key]).toFixed(1)}`).join(' ');
const fidelitySvg = `<svg viewBox="0 0 ${chartW} ${chartH}" width="100%" role="img"><text x="${chartX}" y="80" fill="${muted}" font-size="12">SIMILARITY · SSIM</text>${bandSvg}${chartGrid}${chartXTicks}<path d="${seriesPath('luminance')}" fill="none" stroke="${paper}" stroke-width="1.6" stroke-opacity=".76"/><path d="${seriesPath('structure')}" fill="none" stroke="${accent}" stroke-width="3"/>${fidelity.steps.map((row) => `<circle cx="${chartXPos(row.y)}" cy="${chartYPos(row.structure)}" r="2.5" fill="${accent}"/>`).join('')}<text x="${chartX + chartPlotW / 2}" y="${chartH - 12}" text-anchor="middle" fill="${muted}" font-size="12">SCROLL POSITION · PIXELS</text><line x1="${chartX + 5}" y1="${chartH - 43}" x2="${chartX + 33}" y2="${chartH - 43}" stroke="${accent}" stroke-width="3"/><text x="${chartX + 40}" y="${chartH - 39}" fill="${paper}" font-size="12">Structure · Sobel-gradient SSIM</text><line x1="${chartX + 290}" y1="${chartH - 43}" x2="${chartX + 318}" y2="${chartH - 43}" stroke="${paper}" stroke-width="2"/><text x="${chartX + 325}" y="${chartH - 39}" fill="${paper}" font-size="12">Luminance SSIM</text></svg>`;
await render('f08-fidelity', 'Fidelity changes with the section', `Across 101 pairs, overall structure SSIM is ${fidelity.overall.structure.toFixed(3)} and luminance SSIM is ${fidelity.overall.luminance.toFixed(3)}. Section means make the weak and strong stretches plain.`, fidelitySvg);

}

if (selected.has('f09')) {
const architecture = `<div class="arch"><section class="arch-panel"><h2>Two visual layers · one viewport</h2><div class="stack"><div class="canvas-label">FIXED WEBGL CANVAS</div><div class="overlay-label">DOM TEXT · OVERLAY</div></div><div class="notes">The canvas carries the desk composite, coaster, camera, hand and post-processing. HTML copy sits above it; SplitText follows the same scroll state.</div></section><section class="arch-panel"><h2>Per-frame path</h2><div class="flow"><span>native scroll</span><b class="arrow">→</b><span>section progress r</span><b class="arrow">→</b><span>fit()</span><b class="arrow">→</b><span>DOM styles + GL uniforms</span><b class="arrow">→</b><span>render</span></div><div class="notes">r = 1 + (scrollY − sectionTop) / viewportHeight. Motion reverses because every frame is derived from scroll position.</div></section><section class="arch-panel"><h2>Post chain · in order</h2><div class="chain"><span>FXAA / SMAA</span><b class="arrow">→</b><span class="disabled">Bokeh · off</span><b class="arrow">→</b><span>Edge glow</span><b class="arrow">→</b><span>Bloom · 5 levels</span><b class="arrow">→</b><span>Final grade</span><b class="arrow">→</b><span class="disabled">Smudge · off</span><b class="arrow">→</b><span>Card blur</span></div><div class="notes">Bloom σ: 3 / 5 / 7 / 9 / 11 · final grade: vignette, tint, saturation and dither.</div></section></div>`;
await render('f09-architecture', 'Scroll state links the DOM and WebGL', 'The rebuild keeps copy in HTML and imagery on a fixed canvas. One frame state updates both before the render chain runs. Diagram is our implementation, not Lusion source.', architecture);

}

if (selected.has('f10')) {
const handYs = [3060, 3600, 4200, 4950, 5400];
const handFrames = await Promise.all(handYs.map(async (y) => `<div class="hand-frame"><img src="${await dataUri(path.join(handDir, `hand-y${y}.jpg`))}"><div><span>Scroll y</span><b>${y.toLocaleString()} px</b></div></div>`));
await render('f10-hand-sequence', 'The hand enters, catches, then yields', 'Five rebuild frames show the hand around its measured 3,056–4,950 px animation window and the hover prompt that follows.', `<div class="hand-strip">${handFrames.join('')}</div>`, true, 'jpg');
await fs.unlink(path.join(media, 'f10-hand-sequence.png')).catch(() => {});

}

await browser.close();
console.log(`Rendered ${[...selected].join(', ')} from repository-owned inputs.`);
