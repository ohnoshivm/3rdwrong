import fs from 'node:fs/promises';
import path from 'node:path';
import { cli, number, openBrowser, json, main } from './lib.mjs';
import { imageFiles, grayscale, scorePair, METHOD } from './image-metrics.mjs';

const stem = file => path.basename(file).replace(/\.[^.]+$/, '');
const escapeHTML = value => String(value).replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));
async function dataURL(file) {
  const ext = path.extname(file).slice(1).toLowerCase();
  return `data:image/${ext === 'jpg' ? 'jpeg' : ext};base64,${(await fs.readFile(file)).toString('base64')}`;
}
main(async () => {
  const options = cli({ reference: { type: 'string' }, candidate: { type: 'string' },
    'sheet-rows': { type: 'string', default: '4' }, 'start-y': { type: 'string', default: '0' },
    step: { type: 'string', default: '90' }, caption: { type: 'string', default: 'Reference study / original rebuild' } });
  if (options.help) { console.log('compare.mjs --reference DIR --candidate DIR --out DIR [--sheet-rows 4 --start-y 0 --step 90 --caption TEXT]'); return; }
  if (!options.reference || !options.candidate) throw new Error('--reference and --candidate are required');
  const rowsPerSheet = number(options['sheet-rows'], 'sheet-rows', { min: 1, max: 10, integer: true });
  const startY = number(options['start-y'], 'start-y'), step = number(options.step, 'step', { min: 0.01 });
  const references = await imageFiles(options.reference), candidates = await imageFiles(options.candidate);
  // Pair explicit numeric step identities, preserving gaps rather than shifting later rows.
  const key = file => { const match = /^step-(\d+)$/.exec(stem(file)); return match ? `step:${Number(match[1])}` : stem(file); };
  const byKey = new Map();
  for (const file of candidates) {
    if (byKey.has(key(file))) throw new Error(`Ambiguous candidate identity: ${key(file)}`);
    byKey.set(key(file), file);
  }
  const seenReference = new Set(), rows = [], missing = [];
  const out = path.resolve(options.out);
  await fs.mkdir(out, { recursive: true });
  for (const reference of references) {
    const identity = key(reference);
    if (seenReference.has(identity)) throw new Error(`Ambiguous reference identity: ${identity}`);
    seenReference.add(identity);
    const candidate = byKey.get(identity);
    if (!candidate) { missing.push(identity); continue; }
    let referenceMeta = null, candidateMeta = null;
    for (const [file, side] of [[reference, 'reference'], [candidate, 'candidate']]) {
      try {
        const meta = JSON.parse(await fs.readFile(file.replace(/\.[^.]+$/, '.json'), 'utf8'));
        if (side === 'reference') referenceMeta = meta; else candidateMeta = meta;
      } catch { /* Legacy captures have no per-step JSON. */ }
    }
    if ([referenceMeta, candidateMeta].some(meta => meta && (meta.targetReached === false || meta.settled === false))) {
      throw new Error(`Unsettled or unreachable capture for ${identity}; inspect the raw capture before scoring`);
    }
    if (referenceMeta && candidateMeta && Math.abs(referenceMeta.actualY - candidateMeta.actualY) > 1) {
      throw new Error(`Scroll mismatch for ${identity}: ${referenceMeta.actualY} vs ${candidateMeta.actualY}`);
    }
    const match = /^step:(\d+)$/.exec(identity);
    const row = { id: identity, y: referenceMeta?.actualY ?? (match ? startY + Number(match[1]) * step : null),
      ySource: referenceMeta ? 'capture-metadata' : 'filename-and-cli-assumption', reference, candidate,
      ...scorePair(await grayscale(reference), await grayscale(candidate)) };
    rows.push(row);
    console.log(`${identity}: structure ${row.structure.toFixed(4)}, luminance ${row.luminance.toFixed(4)}`);
  }
  if (!rows.length) throw new Error('No matching image identities');
  const mean = channel => rows.reduce((sum, row) => sum + row[channel], 0) / rows.length;
  const report = { method: METHOD, overall: { structure: mean('structure'), luminance: mean('luminance') },
    missingCandidates: missing, unusedCandidates: [...byKey.keys()].filter(id => !seenReference.has(id)),
    steps: rows, sheets: [], warning: 'Scores are structural indicators, not a percentage of fidelity. Inspect native-size anchors, palette changes and dark frames.' };
  await json(path.join(out, 'comparison.json'), report);
  const { browser, page } = await openBrowser({ ...options, viewport: '1024x768', dpr: '1' });
  try {
    for (let offset = 0; offset < rows.length; offset += rowsPerSheet) {
      const batch = rows.slice(offset, offset + rowsPerSheet), html = [];
      for (const row of batch) html.push(`<section><p>${escapeHTML(row.id)} · y ${row.y ?? 'unknown'} · structure ${row.structure.toFixed(4)} · luminance ${row.luminance.toFixed(4)}</p><div><img alt="Reference" src="${await dataURL(row.reference)}"><img alt="Rebuild" src="${await dataURL(row.candidate)}"></div></section>`);
      // Fixed report styling only; no target website code, assets or layout are copied.
      await page.setContent(`<!doctype html><meta charset="utf-8"><title>Motion comparison</title><style>body{margin:0;padding:24px;background:#fff;color:#161616;font:14px system-ui}h1{font-size:22px;margin:0 0 12px}p{margin:10px 0 6px}div{display:flex;gap:8px}img{width:480px;height:300px;object-fit:fill}section{break-inside:avoid}footer{font-size:12px;margin-top:16px}</style><h1>${escapeHTML(options.caption)}</h1><p>Reference (left) / rebuild (right)</p>${html.join('')}<footer>480×300 analysis sheet. Inspect native-resolution captures before making visual claims.</footer>`);
      await page.evaluate(() => Promise.all([...document.images].map(image => image.decode())));
      const name = `sheet-${String(offset / rowsPerSheet).padStart(3, '0')}.png`;
      await page.screenshot({ path: path.join(out, name), fullPage: true });
      report.sheets.push(name);
    }
  } finally { await browser.close(); }
  await json(path.join(out, 'comparison.json'), report);
  if (missing.length || report.unusedCandidates.length) process.exitCode = 2;
});
