import { createStage } from './stage';
(window as any).__stage = createStage(document.getElementById('gl') as HTMLCanvasElement);
