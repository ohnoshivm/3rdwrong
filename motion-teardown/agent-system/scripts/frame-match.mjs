import fs from 'node:fs/promises';
import path from 'node:path';
import { cli, number, json, main } from './lib.mjs';
import { imageFiles, grayscale, ssim, detail, execFileAsync, METHOD } from './image-metrics.mjs';

main(async () => {
  const options = cli({ video: { type: 'string' }, frames: { type: 'string' }, steps: { type: 'string' },
    fps: { type: 'string', default: '1' }, top: { type: 'string', default: '3' },
    'start-y': { type: 'string', default: '0' }, step: { type: 'string', default: '90' } });
  if (options.help) { console.log('frame-match.mjs --video FILE|--frames DIR --steps DIR --out DIR [--fps 1 --top 3 --start-y 0 --step 90]'); return; }
  if (!!options.video === !!options.frames || !options.steps) throw new Error('Supply exactly one of --video/--frames and also --steps');
  const fps = number(options.fps, 'fps', { min: 0.01, max: 10 });
  const top = number(options.top, 'top', { min: 1, max: 10, integer: true });
  const step = number(options.step, 'step', { min: 0.01 }), startY = number(options['start-y'], 'start-y');
  const out = path.resolve(options.out);
  await fs.mkdir(out, { recursive: true });
  let framesDir = options.frames, timestamps = [];
  if (options.video) {
    framesDir = await fs.mkdtemp(path.join(out, 'video-frames-'));
    // showinfo supplies actual resampled presentation timestamps; do not invent source frame indices.
    const { stderr } = await execFileAsync('ffmpeg', ['-hide_banner', '-nostdin', '-i', path.resolve(options.video),
      '-an', '-vf', `fps=${fps},showinfo`, '-frames:v', '1000', path.join(framesDir, 'frame-%06d.png')],
    { timeout: 300000, maxBuffer: 10485760 });
    timestamps = [...stderr.matchAll(/\bn:\s*\d+[^\n]*?\bpts_time:\s*([\d.e+-]+)/g)].map(match => Number(match[1]));
  }
  const frames = await imageFiles(framesDir), steps = await imageFiles(options.steps);
  if (frames.length > 1000 || steps.length > 1000) throw new Error('Limit matching to 1000 frames and 1000 steps per run');
  const candidates = [];
  for (const file of steps) candidates.push({ file, image: await grayscale(file) });
  const matches = [];
  console.warn('Frame matches are candidates only. Dark/low-resolution frames can produce false matches. Inspect full-size anchors; recording direction is not assumed.');
  for (let index = 0; index < frames.length; index++) {
    const frame = frames[index], image = await grayscale(frame), stats = detail(image);
    const ranked = candidates.map(candidate => ({ file: candidate.file,
      score: ssim(image, candidate.image), detailWarning: detail(candidate.image).warning }))
      .sort((a, b) => b.score - a.score).slice(0, top);
    for (const candidate of ranked) {
      const id = /step-(\d+)/.exec(path.basename(candidate.file));
      // Prefer exact capture metadata; numeric names may represent a non-uniform final step.
      try { candidate.y = JSON.parse(await fs.readFile(candidate.file.replace(/\.[^.]+$/, '.json'), 'utf8')).actualY; }
      catch { candidate.y = id ? startY + Number(id[1]) * step : null; candidate.ySource = 'filename-and-cli-assumption'; }
    }
    matches.push({ frame, timeSeconds: timestamps[index] ?? null, detail: stats, candidates: ranked,
      ambiguity: ranked.length > 1 && ranked[0].score - ranked[1].score < 0.01 });
    await json(path.join(out, 'frame-matches.json'), { method: { ...METHOD, ranking: 'luminance SSIM' },
      video: options.video ?? null, fps: options.video ? fps : null,
      extractionLimit: 1000, limitReached: frames.length === 1000, matches });
    console.log(`${path.basename(frame)} -> ${path.basename(ranked[0].file)} (${ranked[0].score.toFixed(4)})${stats.warning ? ' WARNING' : ''}`);
  }
});
