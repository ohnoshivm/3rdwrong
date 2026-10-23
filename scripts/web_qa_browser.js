// Function expression consumed by playwright-cli run-code; no Node dependency.
async page => {
  const config = __WEB_QA_CONFIG__;
  const result = {measurements: {}, screenshots: [], console: [], errors: [], views: []};
  const browser = page.context().browser();
  result.browserVersion = browser.version();
  let motionCount = 0;
  let complete = true;
  for (const reduced of [false, true]) {
    for (const width of [375, 768, 1440]) {
      const context = await browser.newContext({
        viewport: {width, height: 900}, deviceScaleFactor: 1,
        reducedMotion: reduced ? 'reduce' : 'no-preference', serviceWorkers: 'block'
      });
      try {
        const probe = await context.newPage();
        probe.on('console', msg => {
          if (msg.type() === 'error') result.console.push({width, reduced, type: 'console', text: msg.text()});
        });
        probe.on('pageerror', err => result.console.push({width, reduced, type: 'pageerror', text: String(err)}));
        const response = await probe.goto(config.url, {waitUntil: 'load', timeout: 30000});
        if (!response || !response.ok()) throw new Error(`Navigation HTTP ${response ? response.status() : 'no response'}`);
        const view = await probe.evaluate(() => ({
          title: document.title, url: location.href,
          reduced: matchMedia('(prefers-reduced-motion: reduce)').matches,
          viewport: innerWidth, scrollWidth: document.documentElement.scrollWidth,
          scrollHeight: document.documentElement.scrollHeight,
          userAgent: navigator.userAgent
        }));
        result.views.push(view);
        if (reduced && !view.reduced) throw new Error('Reduced-motion emulation did not take effect');
        if (reduced) {
          const scan = await probe.evaluate(async () => {
            let maximum = 0;
            const samples = [];
            for (let i = 0; i < 15; i++) {
              // Dwell at top, midpoint and three-quarter depth; allow scroll triggers to run.
              if (i % 5 === 0) {
                const range = Math.max(0, document.documentElement.scrollHeight - innerHeight);
                window.scrollTo(0, range * [0, 0.5, 0.75][Math.floor(i / 5)]);
                await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
              }
              const animations = document.getAnimations().filter(a => a.playState === 'running' || a.pending);
              const media = [...document.querySelectorAll('video,audio')].filter(m => !m.paused && !m.ended);
              maximum = Math.max(maximum, animations.length + media.length);
              samples.push({timeMs: performance.now(), scrollY, animations: animations.map(a => ({
                playState: a.playState, name: a.animationName || a.constructor.name
              })), playingMedia: media.length});
              await new Promise(resolve => setTimeout(resolve, 100));
            }
            window.scrollTo(0, 0);
            return {maximum, samples};
          });
          motionCount = Math.max(motionCount, scan.maximum);
          view.motion = scan;
        }
        // Disable Playwright's default screenshot animation fast-forwarding.
        const name = `screenshots-${width}${reduced ? '-reduced' : ''}.png`;
        await probe.screenshot({path: `${config.out}/${name}`, fullPage: false, animations: 'allow', timeout: 15000});
        result.screenshots.push(name);
        if (!reduced && width === 375) {
          const frames = await probe.evaluate(async () => {
            const range = Math.max(0, document.documentElement.scrollHeight - innerHeight);
            if (!range) return {fps: null, reason: 'No scroll range'};
            return await new Promise(resolve => {
              const times = [];
              let first;
              function tick(now) {
                if (first === undefined) first = now;
                times.push(now);
                const progress = Math.min(1, (now - first) / 2000);
                window.scrollTo(0, range * progress);
                if (progress < 1) requestAnimationFrame(tick);
                else {
                  const intervals = times.slice(1).map((t, i) => t - times[i]);
                  const elapsed = times.at(-1) - times[0];
                  const sorted = [...intervals].sort((a, b) => a - b);
                  resolve({fps: intervals.length * 1000 / elapsed, frames: intervals.length,
                    elapsedMs: elapsed, p95FrameMs: sorted[Math.ceil(sorted.length * .95) - 1],
                    intervalsMs: intervals, scrollRange: range});
                }
              }
              requestAnimationFrame(tick);
            });
          });
          result.frames = frames;
          result.measurements.fps = frames.fps;
        }
      } catch (error) {
        complete = false;
        result.errors.push(`${width}px ${reduced ? 'reduced' : 'normal'}: ${String(error)}`);
      } finally {
        await context.close();
      }
    }
  }
  result.measurements.console_errors = complete || result.console.length ? result.console.length : null;
  result.measurements.active_reduced_animations = complete || motionCount ? motionCount : null;
  return result;
}
