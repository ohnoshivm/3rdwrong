import * as THREE from 'three';
const r = new THREE.WebGLRenderer({ canvas: document.getElementById('c') as HTMLCanvasElement });
const s = new THREE.Scene(); s.name = 'main';
const m = new THREE.Mesh(new THREE.BoxGeometry(), new THREE.ShaderMaterial({ vertexShader: 'void main(){ gl_Position = projectionMatrix*modelViewMatrix*vec4(position,1.); }', fragmentShader: 'void main(){ gl_FragColor = vec4(1.,0.,0.,1.); }' }));
m.name = 'hand'; s.add(m); const cam = new THREE.PerspectiveCamera(); cam.position.z = 3; r.render(s, cam);
