// extract fenced blocks whose first line is "// lab/<name>" or "<!-- lab/<name> -->" from md files
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
const out = 'lab';
let n = 0;
for (const f of process.argv.slice(2)) {
  const md = readFileSync(f, 'utf8');
  for (const m of md.matchAll(/```(\w+)\n(?:\/\/ |<!-- )lab\/([\w./-]+?)(?: -->)?\n([\s\S]*?)```/g)) {
    const path = join(out, m[2]);
    mkdirSync(dirname(path), { recursive: true });
    const first = md.slice(m.index).split('\n')[1];
    writeFileSync(path, first + '\n' + m[3]);
    n++; console.log('extracted', m[2]);
  }
}
console.log(n, 'files');
