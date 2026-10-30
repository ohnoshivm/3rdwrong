import fs from 'node:fs/promises';
import path from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
export const execFileAsync = promisify(execFile);
export const WIDTH = 480, HEIGHT = 300;
export const METHOD = {
  primary: 'Sobel gradient magnitude SSIM', secondary: 'grayscale luminance SSIM',
  resolution: [WIDTH, HEIGHT], colour: 'sRGB RGB float grayscale weights 0.2125/0.7154/0.0721',
  resize: 'FFmpeg Lanczos, stretched to 480x300; alpha composited onto white',
  ssim: '7x7 uniform window, sample covariance, K1=0.01 K2=0.03, crop 3px border',
  edgeRange: 'max of both gradient images, lower bound 1e-8',
  alignment: 'Same metric family, dimensions, channels and SSIM parameters as media/fidelity/score.py; FFmpeg resampling differs from Pillow and values are not bit-identical.',
};
export async function imageFiles(directory) {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const files = entries.filter(e => e.isFile() && /\.(png|jpe?g|webp)$/i.test(e.name))
    .map(e => path.join(directory, e.name)).sort((a, b) => a.localeCompare(b, 'en', { numeric: true }));
  if (!files.length) throw new Error(`No image files in ${directory}`);
  return files;
}
export async function grayscale(file) {
  const { stdout } = await execFileAsync('ffmpeg', ['-v', 'error', '-i', path.resolve(file),
    '-vf', `format=rgba,split[fg][bg];[bg]lutrgb=r=255:g=255:b=255:a=255[white];[white][fg]overlay=shortest=1:format=rgb,scale=${WIDTH}:${HEIGHT}:flags=lanczos,format=rgb24`,
    '-frames:v', '1', '-f', 'rawvideo', 'pipe:1'], { encoding: 'buffer', maxBuffer: WIDTH * HEIGHT * 3 + 1048576, timeout: 30000 });
  if (stdout.length !== WIDTH * HEIGHT * 3) throw new Error(`Unexpected decoded size for ${file}`);
  const values = new Float64Array(WIDTH * HEIGHT);
  for (let i = 0; i < values.length; i++) values[i] = (0.2125 * stdout[i * 3] + 0.7154 * stdout[i * 3 + 1] + 0.0721 * stdout[i * 3 + 2]) / 255;
  return values;
}
function reflect(index, size) {
  if (index < 0) return -index - 1;
  if (index >= size) return 2 * size - index - 1;
  return index;
}
export function sobel(image, width = WIDTH, height = HEIGHT) {
  if (image.length !== width * height) throw new Error('Invalid Sobel image dimensions');
  const output = new Float64Array(image.length), smooth = [1, 2, 1];
  for (let y = 0; y < height; y++) for (let x = 0; x < width; x++) {
    let dx = 0, dy = 0;
    for (let offset = -1; offset <= 1; offset++) {
      dx += smooth[offset + 1] * (image[reflect(y + offset, height) * width + reflect(x + 1, width)]
        - image[reflect(y + offset, height) * width + reflect(x - 1, width)]) / 4;
      dy += smooth[offset + 1] * (image[reflect(y + 1, height) * width + reflect(x + offset, width)]
        - image[reflect(y - 1, height) * width + reflect(x + offset, width)]) / 4;
    }
    output[y * width + x] = Math.hypot(dx, dy) / Math.SQRT2;
  }
  return output;
}
// Integral sums evaluate the same cropped uniform windows as default skimage SSIM.
function integral(image, width, height, transform) {
  const stride = width + 1, out = new Float64Array(stride * (height + 1));
  for (let y = 0; y < height; y++) {
    let sum = 0;
    for (let x = 0; x < width; x++) { sum += transform(image[y * width + x], y * width + x); out[(y + 1) * stride + x + 1] = sum + out[y * stride + x + 1]; }
  }
  return out;
}
export function ssim(first, second, range = 1, width = WIDTH, height = HEIGHT) {
  if (width < 7 || height < 7 || first.length !== width * height || second.length !== first.length || !(range > 0)) throw new Error('Invalid SSIM dimensions or range');
  const inputs = [integral(first, width, height, v => v), integral(second, width, height, v => v),
    integral(first, width, height, v => v * v), integral(second, width, height, v => v * v),
    integral(first, width, height, (v, i) => v * second[i])];
  const stride = width + 1, c1 = (0.01 * range) ** 2, c2 = (0.03 * range) ** 2;
  let total = 0, count = 0;
  for (let y = 0; y <= height - 7; y++) for (let x = 0; x <= width - 7; x++) {
    const [a, b, aa, bb, ab] = inputs.map(sum => (sum[(y + 7) * stride + x + 7] - sum[y * stride + x + 7]
      - sum[(y + 7) * stride + x] + sum[y * stride + x]) / 49);
    const va = Math.max(0, (aa - a * a) * 49 / 48), vb = Math.max(0, (bb - b * b) * 49 / 48), cov = (ab - a * b) * 49 / 48;
    const score = ((2 * a * b + c1) * (2 * cov + c2)) / ((a * a + b * b + c1) * (va + vb + c2));
    total += Math.max(-1, Math.min(1, score)); count++;
  }
  return total / count;
}
export function detail(image) {
  let mean = 0;
  for (const v of image) mean += v;
  mean /= image.length;
  let variance = 0;
  for (const v of image) variance += (v - mean) ** 2;
  return { mean, standardDeviation: Math.sqrt(variance / image.length),
    warning: mean < 0.08 || variance / image.length < 0.0025 ? 'dark-or-low-detail: inspect native-resolution anchors; nearest match may be ambiguous' : null };
}
export function scorePair(first, second) {
  const a = sobel(first), b = sobel(second);
  let edgeRange = 1e-8;
  for (let i = 0; i < a.length; i++) edgeRange = Math.max(edgeRange, a[i], b[i]);
  return { structure: ssim(a, b, edgeRange), luminance: ssim(first, second),
    referenceDetail: detail(first), candidateDetail: detail(second) };
}
