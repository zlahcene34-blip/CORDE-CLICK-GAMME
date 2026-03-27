<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DUEL DE CLICS — ARCADE</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<style>
  :root {
    --neon-green: #00ff41;
    --neon-pink: #ff2d78;
    --neon-blue: #00d4ff;
    --neon-yellow: #ffe600;
    --neon-orange: #ff6b00;
    --bg: #050510;
    --panel: #0a0a1a;
    --grid: rgba(0,212,255,0.04);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--neon-green);
    font-family: 'Press Start 2P', monospace;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
  }

  /* Scanlines */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,0,0,0.25) 2px,
      rgba(0,0,0,0.25) 4px
    );
    pointer-events: none;
    z-index: 100;
  }

  /* CRT vignette */
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    background: radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,0.7) 100%);
    pointer-events: none;
    z-index: 99;
  }

  /* Grid floor */
  .grid-bg {
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(var(--grid) 1px, transparent 1px),
      linear-gradient(90deg, var(--grid) 1px, transparent 1px);
    background-size: 40px 40px;
    perspective: 400px;
    z-index: 0;
  }

  .cabinet {
    position: relative;
    z-index: 10;
    width: min(720px, 96vw);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0;
  }

  /* === TITLE === */
  .title-block {
    text-align: center;
    margin-bottom: 18px;
  }
  .title-main {
    font-size: clamp(14px, 3.5vw, 22px);
    color: var(--neon-yellow);
    text-shadow: 0 0 8px var(--neon-yellow), 0 0 30px rgba(255,230,0,0.4);
    letter-spacing: 4px;
    animation: flicker 4s infinite;
  }
  .title-sub {
    font-size: clamp(6px, 1.5vw, 8px);
    color: var(--neon-blue);
    letter-spacing: 6px;
    margin-top: 6px;
    opacity: 0.8;
  }

  @keyframes flicker {
    0%,95%,100% { opacity: 1; }
    96% { opacity: 0.4; }
    97% { opacity: 1; }
    98% { opacity: 0.2; }
    99% { opacity: 1; }
  }

  /* === SCORE BOARD === */
  .scoreboard {
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;
    padding: 10px 24px;
    border: 2px solid var(--neon-blue);
    border-bottom: none;
    background: var(--panel);
    box-shadow: 0 0 20px rgba(0,212,255,0.3), inset 0 0 30px rgba(0,212,255,0.03);
  }

  .score-player {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }
  .score-label {
    font-size: clamp(5px, 1.2vw, 7px);
    letter-spacing: 2px;
  }
  .score-label.left { color: var(--neon-green); }
  .score-label.right { color: var(--neon-pink); }
  .score-num {
    font-size: clamp(18px, 4vw, 28px);
  }
  .score-num.left {
    color: var(--neon-green);
    text-shadow: 0 0 10px var(--neon-green);
  }
  .score-num.right {
    color: var(--neon-pink);
    text-shadow: 0 0 10px var(--neon-pink);
  }
  .score-vs {
    font-size: clamp(8px, 2vw, 12px);
    color: var(--neon-yellow);
    text-shadow: 0 0 8px var(--neon-yellow);
  }

  /* === ARENA === */
  .arena {
    width: 100%;
    height: clamp(160px, 28vw, 220px);
    background: var(--panel);
    border: 2px solid var(--neon-blue);
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 40px rgba(0,212,255,0.15), inset 0 0 60px rgba(0,0,0,0.5);
  }

  /* Danger zones */
  .zone {
    position: absolute;
    top: 0; bottom: 0;
    width: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .zone.left {
    left: 0;
    background: linear-gradient(90deg, rgba(0,255,65,0.12), transparent);
    border-right: 1px dashed rgba(0,255,65,0.3);
  }
  .zone.right {
    right: 0;
    background: linear-gradient(270deg, rgba(255,45,120,0.12), transparent);
    border-left: 1px dashed rgba(255,45,120,0.3);
  }
  .zone-txt {
    font-size: 7px;
    letter-spacing: 1px;
    writing-mode: vertical-lr;
    opacity: 0.5;
  }
  .zone.left .zone-txt { color: var(--neon-green); }
  .zone.right .zone-txt { color: var(--neon-pink); }

  /* Center line */
  .center-line {
    position: absolute;
    left: 50%;
    top: 10%;
    bottom: 10%;
    width: 2px;
    background: rgba(255,230,0,0.4);
    transform: translateX(-50%);
    box-shadow: 0 0 6px var(--neon-yellow);
  }

  /* Power bar at top */
  .power-bar {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 8px;
    background: #111;
  }
  .power-fill-left {
    position: absolute;
    top: 0; left: 0;
    height: 100%;
    background: var(--neon-green);
    box-shadow: 0 0 8px var(--neon-green);
    transition: width 0.07s;
  }
  .power-fill-right {
    position: absolute;
    top: 0; right: 0;
    height: 100%;
    background: var(--neon-pink);
    box-shadow: 0 0 8px var(--neon-pink);
    transition: width 0.07s;
  }

  /* Rope */
  .rope-track {
    position: absolute;
    top: 50%;
    left: 10%;
    right: 10%;
    height: 16px;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
  }
  .rope {
    width: 100%;
    height: 10px;
    background: repeating-linear-gradient(
      90deg,
      #8B5E3C 0px, #8B5E3C 8px,
      #6B4423 8px, #6B4423 16px
    );
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.6), 0 0 4px rgba(139,94,60,0.4);
    position: relative;
  }

  /* Flag / foulard */
  .flag {
    position: absolute;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 24px;
    height: 36px;
    background: var(--neon-pink);
    box-shadow: 0 0 12px var(--neon-pink), 0 0 30px rgba(255,45,120,0.5);
    transition: left 0.07s;
    z-index: 5;
    image-rendering: pixelated;
    clip-path: polygon(0% 0%, 100% 0%, 100% 75%, 50% 100%, 0% 75%);
  }

  /* Players pixel art */
  .player-sprite {
    position: absolute;
    bottom: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2px;
    transition: transform 0.05s;
  }
  .player-sprite.left { left: 10px; }
  .player-sprite.right { right: 10px; }

  .sprite-canvas {
    width: 32px;
    height: 48px;
    image-rendering: pixelated;
  }

  .player-sprite.pulling-left { transform: translateX(-3px); }
  .player-sprite.pulling-right { transform: translateX(3px); }

  /* === STATUS / OVERLAY === */
  .overlay {
    position: absolute;
    inset: 0;
    background: rgba(5,5,16,0.88);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 16px;
    z-index: 20;
  }
  .overlay.hidden { display: none; }

  .overlay-title {
    font-size: clamp(10px, 2.5vw, 16px);
    color: var(--neon-yellow);
    text-shadow: 0 0 16px var(--neon-yellow);
    text-align: center;
    animation: blink 1s step-end infinite;
  }
  .overlay-winner {
    font-size: clamp(8px, 2vw, 11px);
    text-align: center;
    line-height: 2;
  }
  .overlay-hint {
    font-size: clamp(5px, 1.3vw, 7px);
    color: var(--neon-blue);
    text-align: center;
    letter-spacing: 2px;
    opacity: 0.8;
  }

  @keyframes blink {
    50% { opacity: 0; }
  }

  /* === CONTROL PANEL === */
  .control-panel {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: stretch;
    border: 2px solid var(--neon-blue);
    border-top: none;
    background: var(--panel);
    box-shadow: 0 0 20px rgba(0,212,255,0.2);
    padding: 16px 20px;
    gap: 12px;
  }

  .ctrl-side {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    flex: 1;
  }

  .arcade-btn {
    width: clamp(56px, 12vw, 72px);
    height: clamp(56px, 12vw, 72px);
    border-radius: 50%;
    border: 3px solid;
    font-family: 'Press Start 2P', monospace;
    font-size: clamp(14px, 3vw, 20px);
    cursor: pointer;
    transition: transform 0.07s, box-shadow 0.07s;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }

  .arcade-btn.green {
    background: radial-gradient(circle at 35% 35%, #00ff80, #006622);
    border-color: #00ff41;
    color: #fff;
    box-shadow: 0 4px 0 #003311, 0 0 16px rgba(0,255,65,0.5), inset 0 1px 0 rgba(255,255,255,0.3);
    text-shadow: 0 1px 2px rgba(0,0,0,0.5);
  }

  .arcade-btn.red {
    background: radial-gradient(circle at 35% 35%, #ff5599, #881133);
    border-color: #ff2d78;
    color: #fff;
    box-shadow: 0 4px 0 #440011, 0 0 16px rgba(255,45,120,0.5), inset 0 1px 0 rgba(255,255,255,0.3);
    text-shadow: 0 1px 2px rgba(0,0,0,0.5);
  }

  .arcade-btn.green:active, .arcade-btn.green.pressed {
    transform: translateY(3px);
    box-shadow: 0 1px 0 #003311, 0 0 24px rgba(0,255,65,0.9), inset 0 2px 4px rgba(0,0,0,0.3);
  }
  .arcade-btn.red:active, .arcade-btn.red.pressed {
    transform: translateY(3px);
    box-shadow: 0 1px 0 #440011, 0 0 24px rgba(255,45,120,0.9), inset 0 2px 4px rgba(0,0,0,0.3);
  }

  .btn-label {
    font-size: clamp(5px, 1.2vw, 7px);
    letter-spacing: 1px;
  }
  .btn-label.left { color: var(--neon-green); }
  .btn-label.right { color: var(--neon-pink); }

  .ctrl-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }

  .insert-coin {
    font-size: clamp(5px, 1.2vw, 7px);
    color: var(--neon-yellow);
    letter-spacing: 2px;
    animation: blink 1.2s step-end infinite;
  }

  .start-btn {
    background: transparent;
    border: 2px solid var(--neon-yellow);
    color: var(--neon-yellow);
    font-family: 'Press Start 2P', monospace;
    font-size: clamp(5px, 1.3vw, 8px);
    padding: 8px 14px;
    cursor: pointer;
    letter-spacing: 2px;
    box-shadow: 0 0 10px rgba(255,230,0,0.3);
    transition: background 0.1s, box-shadow 0.1s;
  }
  .start-btn:hover {
    background: rgba(255,230,0,0.1);
    box-shadow: 0 0 20px rgba(255,230,0,0.6);
  }

  /* === COMBO METER === */
  .combo-row {
    display: flex;
    gap: 4px;
    align-items: center;
  }
  .combo-pip {
    width: 8px; height: 8px;
    border: 1px solid;
    transition: background 0.1s;
  }
  .combo-pip.left-pip { border-color: var(--neon-green); }
  .combo-pip.right-pip { border-color: var(--neon-pink); }
  .combo-pip.active-left { background: var(--neon-green); box-shadow: 0 0 4px var(--neon-green); }
  .combo-pip.active-right { background: var(--neon-pink); box-shadow: 0 0 4px var(--neon-pink); }

  /* Shake animation */
  @keyframes shake { 0%,100%{transform:translateX(0)} 20%{transform:translateX(-4px)} 60%{transform:translateX(4px)} 80%{transform:translateX(-2px)} }
  .arena.shake { animation: shake 0.3s; }

  /* Win flash */
  @keyframes win-flash { 0%,100%{opacity:1} 50%{opacity:0.3} }
</style>
</head>
<body>

<div class="grid-bg"></div>

<div class="cabinet">
  <div class="title-block">
    <div class="title-main">★ DUEL DE CLICS ★</div>
    <div class="title-sub">TIREUSE DE CORDE</div>
  </div>

  <!-- Score -->
  <div class="scoreboard">
    <div class="score-player">
      <div class="score-label left">P1 — GAUCHE</div>
      <div class="score-num left" id="left-score">00</div>
    </div>
    <div class="score-vs">VS</div>
    <div class="score-player">
      <div class="score-label right">P2 — DROIT</div>
      <div class="score-num right" id="right-score">00</div>
    </div>
  </div>

  <!-- Arena -->
  <div class="arena" id="arena">
    <div class="power-bar">
      <div class="power-fill-left" id="bar-left" style="width:50%"></div>
      <div class="power-fill-right" id="bar-right" style="width:50%"></div>
    </div>

    <div class="zone left"><span class="zone-txt">ZONE P1</span></div>
    <div class="zone right"><span class="zone-txt">ZONE P2</span></div>
    <div class="center-line"></div>

    <!-- Sprites -->
    <div class="player-sprite left" id="sprite-left">
      <canvas class="sprite-canvas" id="canvas-left" width="32" height="48"></canvas>
    </div>
    <div class="player-sprite right" id="sprite-right">
      <canvas class="sprite-canvas" id="canvas-right" width="32" height="48"></canvas>
    </div>

    <div class="rope-track">
      <div class="rope">
        <div class="flag" id="flag" style="left:50%"></div>
      </div>
    </div>

    <!-- Overlay -->
    <div class="overlay" id="overlay">
      <div class="overlay-title" id="overlay-title">DUEL DE CLICS</div>
      <div class="overlay-winner" id="overlay-winner" style="display:none"></div>
      <div class="overlay-hint" id="overlay-hint">APPUYEZ SUR START</div>
    </div>
  </div>

  <!-- Controls -->
  <div class="control-panel">
    <div class="ctrl-side">
      <button class="arcade-btn green" id="btn-a" onclick="pressLeft()">A</button>
      <div class="btn-label left">JOUEUR 1</div>
      <div class="combo-row" id="combo-left"></div>
    </div>

    <div class="ctrl-center">
      <div class="insert-coin">INSERT COIN</div>
      <button class="start-btn" id="start-btn" onclick="startGame()">▶ START</button>
    </div>

    <div class="ctrl-side">
      <button class="arcade-btn red" id="btn-p" onclick="pressRight()">P</button>
      <div class="btn-label right">JOUEUR 2</div>
      <div class="combo-row" id="combo-right"></div>
    </div>
  </div>
</div>

<script>
const LIMITE = 250;
const VITESSE = 15;
const MAX_COMBO = 8;

let pos = 0;
let state = 'menu';
let leftScore = 0, rightScore = 0;
let comboLeft = 0, comboRight = 0;
let frame = 0;
let animFrame;

const flag = document.getElementById('flag');
const barLeft = document.getElementById('bar-left');
const barRight = document.getElementById('bar-right');
const overlay = document.getElementById('overlay');
const overlayTitle = document.getElementById('overlay-title');
const overlayWinner = document.getElementById('overlay-winner');
const overlayHint = document.getElementById('overlay-hint');
const arena = document.getElementById('arena');
const spriteLeft = document.getElementById('sprite-left');
const spriteRight = document.getElementById('sprite-right');
const comboRowLeft = document.getElementById('combo-left');
const comboRowRight = document.getElementById('combo-right');

// Build combo pips
function buildPips() {
  comboRowLeft.innerHTML = '';
  comboRowRight.innerHTML = '';
  for (let i = 0; i < MAX_COMBO; i++) {
    const pl = document.createElement('div');
    pl.className = 'combo-pip left-pip';
    pl.id = 'lp-' + i;
    comboRowLeft.appendChild(pl);
    const pr = document.createElement('div');
    pr.className = 'combo-pip right-pip';
    pr.id = 'rp-' + i;
    comboRowRight.appendChild(pr);
  }
}
buildPips();

function updatePips(side, count) {
  const prefix = side === 'left' ? 'lp' : 'rp';
  const cls = side === 'left' ? 'active-left' : 'active-right';
  for (let i = 0; i < MAX_COMBO; i++) {
    const el = document.getElementById(prefix + '-' + i);
    if (i < count) el.classList.add(cls);
    else el.classList.remove(cls);
  }
}

// Pixel art sprites
function drawSprite(canvasId, color, mirrored, pulling) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, 32, 48);
  ctx.imageSmoothingEnabled = false;

  if (mirrored) { ctx.save(); ctx.scale(-1, 1); ctx.translate(-32, 0); }

  // Body pixels (simple 16x24 pixel man)
  const c = color;
  const skin = '#F4A46A';
  const dark = color === '#00ff41' ? '#003311' : '#440011';

  // head
  ctx.fillStyle = skin;
  ctx.fillRect(10, 2, 12, 10);
  // hair
  ctx.fillStyle = '#333';
  ctx.fillRect(10, 2, 12, 3);
  // eyes
  ctx.fillStyle = '#111';
  ctx.fillRect(13, 5, 2, 2);
  ctx.fillRect(18, 5, 2, 2);
  // body
  ctx.fillStyle = c;
  ctx.fillRect(8, 12, 16, 14);
  // arms - animate
  const armY = pulling ? 2 : 0;
  ctx.fillStyle = skin;
  ctx.fillRect(2, 12 + armY, 6, 8);
  ctx.fillRect(24, 12 + armY, 6, 8);
  // legs - animate
  const legOff = (frame % 4 < 2 && pulling) ? 2 : 0;
  ctx.fillStyle = '#1a1a6e';
  ctx.fillRect(9, 26, 6, 14 - legOff);
  ctx.fillRect(17, 26, 6, 14 + legOff);
  // feet
  ctx.fillStyle = '#222';
  ctx.fillRect(8, 38 - legOff, 8, 4);
  ctx.fillRect(16, 38 + legOff, 8, 4);

  if (mirrored) ctx.restore();
}

function animateSprites() {
  frame++;
  const pulling = state === 'game';
  drawSprite('canvas-left', '#00ff41', false, pulling);
  drawSprite('canvas-right', '#ff2d78', true, pulling);
  animFrame = requestAnimationFrame(animateSprites);
}
animateSprites();

function updateVisual() {
  const pct = 50 + (pos / LIMITE) * 50;
  const clamped = Math.min(97, Math.max(3, pct));
  flag.style.left = clamped + '%';
  const leftPct = Math.max(0, 50 - (pos / LIMITE) * 50);
  barLeft.style.width = leftPct + '%';
  barRight.style.width = Math.max(0, 100 - leftPct) + '%';
}

function startGame() {
  pos = 0;
  comboLeft = 0;
  comboRight = 0;
  state = 'game';
  overlay.classList.add('hidden');
  overlayWinner.style.display = 'none';
  updatePips('left', 0);
  updatePips('right', 0);
  updateVisual();
}

function shakeArena() {
  arena.classList.add('shake');
  setTimeout(() => arena.classList.remove('shake'), 300);
}

function endGame(winner) {
  state = 'menu';
  shakeArena();

  if (winner === 'left') {
    leftScore++;
    document.getElementById('left-score').textContent = String(leftScore).padStart(2, '0');
    overlayTitle.textContent = '★ VICTOIRE ★';
    overlayTitle.style.color = '#00ff41';
    overlayWinner.style.color = '#00ff41';
    overlayWinner.textContent = 'JOUEUR GAUCHE GAGNE !';
  } else {
    rightScore++;
    document.getElementById('right-score').textContent = String(rightScore).padStart(2, '0');
    overlayTitle.textContent = '★ VICTOIRE ★';
    overlayTitle.style.color = '#ff2d78';
    overlayWinner.style.color = '#ff2d78';
    overlayWinner.textContent = 'JOUEUR DROIT GAGNE !';
  }

  overlayWinner.style.display = 'block';
  overlayHint.textContent = 'APPUYEZ SUR START / ENTER';
  overlay.classList.remove('hidden');
}

function pressLeft() {
  if (state !== 'game') return;
  const btn = document.getElementById('btn-a');
  btn.classList.add('pressed');
  setTimeout(() => btn.classList.remove('pressed'), 80);
  spriteLeft.classList.add('pulling-left');
  setTimeout(() => spriteLeft.classList.remove('pulling-left'), 100);

  comboLeft = Math.min(MAX_COMBO, comboLeft + 1);
  comboRight = Math.max(0, comboRight - 1);
  updatePips('left', comboLeft);
  updatePips('right', comboRight);

  const speed = VITESSE + Math.floor(comboLeft / 3);
  pos -= speed;
  if (pos <= -LIMITE) { pos = -LIMITE; updateVisual(); endGame('left'); return; }
  updateVisual();
}

function pressRight() {
  if (state !== 'game') return;
  const btn = document.getElementById('btn-p');
  btn.classList.add('pressed');
  setTimeout(() => btn.classList.remove('pressed'), 80);
  spriteRight.classList.add('pulling-right');
  setTimeout(() => spriteRight.classList.remove('pulling-right'), 100);

  comboRight = Math.min(MAX_COMBO, comboRight + 1);
  comboLeft = Math.max(0, comboLeft - 1);
  updatePips('right', comboRight);
  updatePips('left', comboLeft);

  const speed = VITESSE + Math.floor(comboRight / 3);
  pos += speed;
  if (pos >= LIMITE) { pos = LIMITE; updateVisual(); endGame('right'); return; }
  updateVisual();
}

document.addEventListener('keydown', (e) => {
  if (e.repeat) return;
  if (e.key === 'Enter') { startGame(); return; }
  if (e.key === 'a' || e.key === 'A') pressLeft();
  if (e.key === 'p' || e.key === 'P') pressRight();
});

updateVisual();
</script>
</body>
</html>
