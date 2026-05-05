'use strict';

// Build-time flag — build.sh replaces this line with the actual value.
// Fallback to true (optimistic). Do not change manually.
const IS_VARIABLE = true;

const MOD_DATA    = '/data/adb/AppleFonts';
const MOD_DIR     = '/data/adb/modules/AppleFonts';
const APPLY_SH    = MOD_DIR + '/scripts/apply.sh';
const RESET_SH    = MOD_DIR + '/scripts/reset.sh';
const PERF_SH     = MOD_DIR + '/scripts/perf_monitor.sh';
const CONFIG      = MOD_DATA + '/config.json';
const BOOT_LOG    = MOD_DIR + '/boot.log';
const PERF_LOG    = MOD_DATA + '/perf.log';
const POST_FS_LOG = MOD_DATA + '/post-fs.log';
const DISABLE_F   = MOD_DIR + '/disable';

// KernelSU WebView exec bridge.
// Android WebView calls back into JS by evaluating a string: callbackName(exitCode, out, err).
// Passing a JS function reference silently fails — we must pass the callback as a global name.
let _ksuCbId = 0;
async function ksExec(cmd, args = []) {
  return new Promise((resolve) => {
    if (typeof ksu === 'undefined' || !ksu.exec) {
      resolve({ out: '(no ksu)', err: '', exitCode: 0 });
      return;
    }
    const escaped = args.map(a => "'" + String(a).replace(/'/g, "'\\''") + "'");
    const fullCmd = args.length ? cmd + ' ' + escaped.join(' ') : cmd;
    const cbName  = '__kseCb' + (++_ksuCbId);

    const timer = setTimeout(() => {
      delete window[cbName];
      resolve({ out: '', err: 'exec timeout', exitCode: -1 });
    }, 10000);

    window[cbName] = function(exitCode, stdout, stderr) {
      clearTimeout(timer);
      delete window[cbName];
      resolve({ out: stdout || '', err: stderr || '', exitCode: +exitCode || 0 });
    };

    try {
      ksu.exec(fullCmd, cbName);
    } catch (e) {
      clearTimeout(timer);
      delete window[cbName];
      resolve({ out: '', err: String(e), exitCode: -1 });
    }
  });
}

// --- State ---
// arabic / geeza / cocon are mutually exclusive — enabling one disables the others.
let state = { wght: 400, latin: true, arabic: true, geeza: false, cocon: false, emoji: true };

// --- DOM ---
const $ = (id) => document.getElementById(id);

// --- Init ---
function init() {
  if (!IS_VARIABLE) $('controls-section').style.display = 'none';
  bindSliders();
  bindToggles();
  bindButtons();
  renderToggles();
  updatePreview();
  Promise.all([loadConfig(), loadStatus(), loadPerfLog()]);
}

// --- Weight slider + number input (synced) ---
function bindSliders() {
  const slider = $('wght-slider');
  const input  = $('wght-input');

  slider.addEventListener('input', () => {
    state.wght = +slider.value;
    input.value = state.wght;
    updatePreview();
  });

  input.addEventListener('input', () => {
    const v = parseInt(input.value, 10);
    if (isNaN(v)) return;
    state.wght = Math.max(100, Math.min(1000, v));
    slider.value = state.wght;
    updatePreview();
  });

  input.addEventListener('change', () => {
    let v = parseInt(input.value, 10);
    if (isNaN(v)) v = state.wght;
    state.wght = Math.max(100, Math.min(1000, v));
    input.value = state.wght;
    slider.value = state.wght;
    updatePreview();
  });
}

function setSliders(wght) {
  state.wght = wght;
  $('wght-slider').value = wght;
  $('wght-input').value  = wght;
  updatePreview();
}

// --- Live preview (CSS only — instant, no root) ---
function updatePreview() {
  const settings = `'wght' ${state.wght}`;
  $('preview-latin').style.fontVariationSettings  = settings;
  $('preview-arabic').style.fontVariationSettings = settings;

  // Switch Arabic preview font based on which Arabic font is active
  let arabicFamily;
  if (state.geeza)      arabicFamily = "'Geeza Var', system-ui, sans-serif";
  else if (state.cocon) arabicFamily = "'Cocon', system-ui, sans-serif";
  else                  arabicFamily = "'SF Arabic Var', 'SF Pro Var', system-ui, sans-serif";
  $('preview-arabic').style.fontFamily = arabicFamily;
}

// --- Toggles ---
// Arabic fonts (SF Arabic / Geeza Pro / Cocon) share the same overlay slots —
// enabling any one auto-disables the other two.
function bindToggles() {
  $('toggle-latin').addEventListener('click', () => {
    state.latin = !state.latin;
    renderToggles();
  });

  $('toggle-arabic').addEventListener('click', () => {
    state.arabic = !state.arabic;
    if (state.arabic) { state.geeza = false; state.cocon = false; }
    renderToggles();
    updatePreview();
  });

  $('toggle-geeza').addEventListener('click', () => {
    state.geeza = !state.geeza;
    if (state.geeza) { state.arabic = false; state.cocon = false; }
    renderToggles();
    updatePreview();
  });

  $('toggle-cocon').addEventListener('click', () => {
    state.cocon = !state.cocon;
    if (state.cocon) { state.arabic = false; state.geeza = false; }
    renderToggles();
    updatePreview();
  });

  $('toggle-emoji').addEventListener('click', () => {
    state.emoji = !state.emoji;
    renderToggles();
  });
}

function renderToggles() {
  const defs = [
    { id: 'toggle-latin',  on: state.latin,  label: 'SF Pro' },
    { id: 'toggle-arabic', on: state.arabic, label: 'SF Arabic' },
    { id: 'toggle-geeza',  on: state.geeza,  label: 'Geeza Pro' },
    { id: 'toggle-cocon',  on: state.cocon,  label: 'Cocon' },
    { id: 'toggle-emoji',  on: state.emoji,  label: 'Apple Emoji' },
  ];
  for (const d of defs) {
    const el = $(d.id);
    el.className   = 'toggle-btn ' + (d.on ? 'toggle-on' : 'toggle-off');
    el.textContent = d.label + ' — ' + (d.on ? 'On' : 'Off');
  }
}

// --- Load config ---
async function loadConfig() {
  const r = await ksExec('cat', [CONFIG]);
  if (r.exitCode !== 0 || !r.out.trim()) return;
  try {
    const cfg = JSON.parse(r.out.trim());
    setSliders(cfg.wght || 400);
    state.latin  = cfg.latin  !== false;
    state.arabic = cfg.arabic !== false;
    state.geeza  = cfg.geeza  === true;
    state.cocon  = cfg.cocon  === true;
    state.emoji  = cfg.emoji  !== false;
    renderToggles();
    updatePreview();
    $('diag-config').textContent = `wght=${cfg.wght || 400}`;
  } catch (_) {}
}

// --- Module status ---
async function loadStatus() {
  const [dis, boot, patch] = await Promise.all([
    ksExec('test', ['-f', DISABLE_F]),
    ksExec('cat',  [BOOT_LOG]),
    ksExec('tail', ['-1', POST_FS_LOG]),
  ]);
  const log = boot.out.trim();
  if (dis.exitCode === 0) {
    setStatus('disabled'); $('diag-status').textContent = 'Disabled';
  } else if (log.includes('BOOT TIMEOUT')) {
    setStatus('failed');   $('diag-status').textContent = 'Boot timeout (auto-disabled)';
  } else if (log.includes('Boot completed') || log.includes('Perf snapshot')) {
    setStatus('active');   $('diag-status').textContent = 'Active';
  } else {
    setStatus('loading');  $('diag-status').textContent = log ? 'Booting…' : 'Unknown';
  }
  $('diag-boot').textContent  = log.split('\n').filter(Boolean).pop() || '—';
  $('diag-patch').textContent = patch.out.trim() || '—';
}

function setStatus(s) {
  const b = $('status-badge');
  b.className = 'badge badge-' + s;
  b.textContent = { active: 'Active', disabled: 'Disabled', failed: 'Boot Failed', loading: 'Loading…' }[s] || s;
}

// --- Perf log ---
async function loadPerfLog() {
  const r = await ksExec('tail', ['-5', PERF_LOG]);
  $('diag-perf').textContent = r.out.trim() || '(no perf data yet)';
}

// --- Buttons ---
function bindButtons() {
  $('btn-apply').addEventListener('click', applySettings);
  $('btn-reset').addEventListener('click', resetSettings);
  $('btn-perf').addEventListener('click', async () => {
    $('diag-perf').textContent = 'Capturing…';
    await ksExec('sh', [PERF_SH]);
    await loadPerfLog();
  });
}

async function applySettings() {
  const btn  = $('btn-apply');
  const note = $('apply-note');
  const err  = $('apply-error');
  btn.disabled = true;
  btn.textContent = 'Saving…';
  note.hidden = true;
  err.hidden  = true;

  const r = await ksExec('sh', [APPLY_SH,
    String(state.wght), '100', '28',
    state.latin  ? 'true' : 'false',
    state.arabic ? 'true' : 'false',
    state.geeza  ? 'true' : 'false',
    state.cocon  ? 'true' : 'false',
    state.emoji  ? 'true' : 'false',
  ]);

  btn.disabled = false;
  btn.textContent = 'Apply to System';

  if (r.exitCode === 0) {
    $('diag-config').textContent = `wght=${state.wght}`;
    note.hidden = false;
  } else {
    err.textContent = 'Save failed: ' + (r.err || r.out || 'exit ' + r.exitCode);
    err.hidden = false;
  }
}

async function resetSettings() {
  const btn = $('btn-reset');
  btn.disabled = true;
  const r = await ksExec('sh', [RESET_SH]);
  btn.disabled = false;
  if (r.exitCode === 0) {
    setSliders(400);
    state.latin = true; state.arabic = true; state.geeza = false;
    state.cocon = false; state.emoji = true;
    renderToggles();
    updatePreview();
    $('apply-note').hidden  = false;
    $('apply-error').hidden = true;
    $('diag-config').textContent = 'wght=400 (defaults)';
  }
}

document.addEventListener('DOMContentLoaded', init);
