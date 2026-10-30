/** {{PROJECT_NAME}} — contract {{CONTRACT_VERSION}}, owned by {{CONTRACT_OWNER}}.
 * Replace placeholders in comments; this file is valid TypeScript as supplied.
 * Freeze before parallel workers start. All lengths are CSS pixels unless noted.
 */
export interface Rect { x: number; y: number; width: number; height: number }
export interface SectionState {
  /** Unclamped section scalar; formula declared in {{MOTION_SPEC_PATH}}. */
  scalar: number;
  /** Per-effect clamped progress in [0, 1], keyed by reconciled effect ID. */
  effects: Readonly<Record<string, number>>;
}
export interface FrameState {
  readonly timeSeconds: number; // monotonic time since navigation
  readonly deltaSeconds: number; // integration owner clamps per spec
  readonly introSeconds: number; // since readiness/fallback; zero beforehand
  readonly scrollY: number; // rendered native y after the single scroll engine
  readonly viewport: Readonly<{ width: number; height: number; dpr: number }>;
  readonly sections: Readonly<Record<string, Readonly<SectionState>>>;
  readonly pointer: Readonly<{ x: number; y: number; active: boolean }>; // NDC, y up
  readonly rects: Readonly<Record<string, Readonly<Rect>>>; // viewport space
  readonly reducedMotion: boolean;
  readonly layout: 'mobile' | 'tablet' | 'desktop';
}
export interface ReadyState {
  status: 'ready' | 'degraded';
  failedAssets: readonly string[];
}
export interface Stage {
  /** Settles within {{READY_TIMEOUT_MS}} on success, timeout or asset error.
   * Rejection must be caught by the integration owner and expose a DOM fallback.
   */
  ready: Promise<ReadyState>;
  update(state: Readonly<FrameState>): void; // no private rAF or scroll controller
  resize(width: number, height: number, dpr: number): void;
  dispose(): void;
}
export type CreateStage = (canvas: HTMLCanvasElement) => Stage;
