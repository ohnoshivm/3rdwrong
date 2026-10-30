import * as THREE from 'three';
import { FULLSCREEN_VERT } from './mask-blur';
import { SKIN_VERT } from './skin-shader';
import { EDGE_GLOW_FRAG } from './edge-glow';
import { BRIGHT_FRAG, BLUR_FRAG, GRADE_FRAG, gaussianKernel } from './bloom-grade';
import { createBoneClip, BONE_STRIDE } from './bone-pose';
import { createSkinned } from './skinned-mesh';
(window as any).LAB = { THREE, FULLSCREEN_VERT, SKIN_VERT, EDGE_GLOW_FRAG, BRIGHT_FRAG, BLUR_FRAG, GRADE_FRAG, gaussianKernel, createBoneClip, BONE_STRIDE, createSkinned };
