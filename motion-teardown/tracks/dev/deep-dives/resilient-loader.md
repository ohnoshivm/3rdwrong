---
title: "Deep dive: the resilient loader"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Deep dive: the resilient loader

*A lesson in building loaders that cannot hang. It is not a recipe for getting past anyone's preloader.*

## What happened

For about 50 minutes on the night of 30 October, our first reverse-engineering agent could not get oryzo.ai (by Lusion) to leave its preloader in automation. The page stayed locked, scroll stayed at 0, and nothing in the console said why.

The code explained it once our static-analysis agent read it. In our reading, the loader reports completion only when the weight it has loaded **exactly equals** the total weight it was asked to load. Image and request items install a success handler and no failure handler. So if one file fails, is blocked, or simply never resolves, the item never reports anything and the sum never matches. There is no timeout and no error. In our runs one file (a Rive animation file used by a later section) never resolved, and the loader sat at about 53%.

Our reading adds two more weaknesses, both worth knowing as design smells:

- **Late additions.** Items added after loading has started count toward the total but are never loaded in that batch.
- **Float equality.** Weights are summed as floating-point numbers and compared with `===`. A post-processing weight split of 0.9 + 0.1 can add up to 1.0000000000000002. We flagged this one as `[inferred]`: we did not log the two numbers at hang time to prove it.

The lesson is for the people who build loaders, including the agents you brief to build them. **A loader is a promise to the visitor that the page will start.**

## The five rules

1. **Every asset settles.** Success, failure and timeout all count as done. Nothing may wait forever.
2. **A total deadline.** Whatever happens to individual assets, `ready` resolves within a fixed time. Our rebuild's spec says 10 seconds, and `stage.ready` settles within that even with missing files.
3. **A fallback per asset.** A flat colour of the right size is better than a hung page. Each asset declares what to show if it fails.
4. **Progress from counts.** Count settled items against total items (integers). Do not compare summed floats for equality.
5. **Report, don't swallow.** The loader returns what loaded, what failed and what timed out, so the page (and your QA) can say so.

## A loader that follows them

```ts
// lab/resilient-loader.ts
export interface Item<T = unknown> {
  name: string;
  load: () => Promise<T>;
  fallback?: () => T; // what to use if loading fails or times out
}

export interface Report {
  loaded: string[];
  failed: { name: string; reason: string }[];
  timedOut: string[];
  fallbacks: string[];
  ms: number;
  values: Map<string, unknown>;
}

export interface Options {
  itemTimeoutMs?: number; // each asset's own limit
  totalTimeoutMs?: number; // the page's limit: ready is never later than this
  onProgress?: (settled: number, total: number) => void;
}

/** Never rejects. Always resolves within totalTimeoutMs (plus one timer tick). */
export function loadAll(items: Item[], opts: Options = {}): Promise<Report> {
  const { itemTimeoutMs = 8000, totalTimeoutMs = 10000, onProgress } = opts;
  const start = performance.now();
  const report: Report = { loaded: [], failed: [], timedOut: [], fallbacks: [], ms: 0, values: new Map() };
  const total = items.length;
  let settled = 0;
  let finished = false;

  return new Promise<Report>((resolve) => {
    const finish = () => {
      if (finished) return;
      finished = true;
      // anything still pending at the deadline gets its fallback
      for (const it of items) {
        if (!report.values.has(it.name)) {
          if (!report.timedOut.includes(it.name) && !report.failed.some((f) => f.name === it.name)) report.timedOut.push(it.name);
          if (it.fallback) { report.values.set(it.name, it.fallback()); report.fallbacks.push(it.name); }
        }
      }
      report.ms = performance.now() - start;
      clearTimeout(deadline);
      resolve(report);
    };
    const deadline = setTimeout(finish, totalTimeoutMs);

    if (total === 0) return finish();

    const settle = () => {
      settled++;
      onProgress?.(settled, total);
      if (settled === total) finish();
    };

    for (const it of items) {
      let done = false;
      const once = (fn: () => void) => { if (done || finished) return; done = true; fn(); settle(); };
      const timer = setTimeout(() => once(() => {
        report.timedOut.push(it.name);
        if (it.fallback) { report.values.set(it.name, it.fallback()); report.fallbacks.push(it.name); }
      }), itemTimeoutMs);

      new Promise((res) => res(it.load())).then( // a synchronous throw becomes a rejection too
        (v) => { clearTimeout(timer); once(() => { report.values.set(it.name, v); report.loaded.push(it.name); }); },
        (e) => { clearTimeout(timer); once(() => {
          report.failed.push({ name: it.name, reason: String(e?.message ?? e) });
          if (it.fallback) { report.values.set(it.name, it.fallback()); report.fallbacks.push(it.name); }
        }); },
      );
    }
  });
}
```

Use it like this, and drive your preloader from `onProgress`:

```ts
const report = await loadAll(
  [
    { name: 'desk', load: () => loadTexture('/gen/desk.jpg'), fallback: () => flatTexture('#fff6f4', 3296, 1460) },
    { name: 'hand', load: () => loadBuf('/models/hand.buf') }, // no fallback: the hand simply stays hidden
  ],
  { totalTimeoutMs: 10_000, onProgress: (n, t) => setBar(n / t) },
);
if (report.failed.length || report.timedOut.length) console.warn('loaded with gaps', report);
```

The preloader's hand-off is then a decision your code makes on purpose, not a state it falls into by accident.

## How we used the lesson

- **Spec.** The build spec requires that `stage.ready` resolves or rejects within 10 seconds ("no silent hangs"), and that missing images fall back to flat-colour placeholders of the right size.
- **GL agent brief.** The brief names the original's loader as "the original's fatal bug; don't reproduce it", and asks for a per-asset timeout plus an error handler.
- **QA.** The acceptance checks include running with a deliberately missing asset and confirming that `stage.ready` settles within 10 seconds.
- **Warm-up inside the budget.** Before ready, the rebuild compiles and draws every material once off-screen (about 250 ms), which cut a 913 ms first-use spike out of the scroll.

## Exercises

1. Make one of your own assets 404. Does your page still start? How long does it take?
2. Make one hang (a request that never completes). When does `ready` fire?
3. Write a test with fake items (a never-resolving promise, a rejecting one, a fast one) and assert the report. The loader above is written so that is easy.
4. Add a retry with backoff for transient failures, such as the DNS error that interrupted one of our agents. Decide where retries end and the deadline begins.

## You're done when

- [ ] No single failed or stalled asset can keep the page from starting; the worst case is a fixed, known time.
- [ ] Progress is computed from integer counts and reaches 1 on every path (success, failure, timeout).
- [ ] Each asset has a stated fallback, or a stated reason for having none.
- [ ] A QA script exercises both a missing and a stalled asset.
- [ ] The report of what failed is visible to developers (console or HUD), not swallowed.
