#!/usr/bin/env bash
# AppleFonts build script — run on your Linux machine (Zenbook).
# Requires: p7zip-full (7za), libarchive-tools (bsdtar), python3 with fonttools
#   Install: sudo apt install p7zip-full libarchive-tools
#            pip install fonttools --break-system-packages

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MOD_DIR="$SCRIPT_DIR/AppleFonts"
SRC_DMG="$SCRIPT_DIR/sources/dmg"
SRC_EMOJI="$SCRIPT_DIR/sources/emoji"
OUT_DIR="$SCRIPT_DIR/output"
TMP_DIR="$SCRIPT_DIR/tmp"
LOG="$OUT_DIR/install-log.txt"
FONT_DEST="$MOD_DIR/system/fonts"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
ok()   { echo -e "${GREEN}  OK${NC}  $*"; echo "[OK]  $*" >> "$LOG"; }
warn() { echo -e "${YELLOW}WARN${NC}  $*"; echo "[WARN] $*" >> "$LOG"; }
fail() { echo -e "${RED}FAIL${NC}  $*"; echo "[FAIL] $*" >> "$LOG"; exit 1; }
info() { echo "      $*"; echo "      $*" >> "$LOG"; }

mkdir -p "$OUT_DIR" "$TMP_DIR"
: > "$LOG"  # truncate log

echo ""
echo "====================================="
echo "  AppleFonts v1.3.0 — Build Script"
echo "====================================="
echo ""
echo "$(date)" >> "$LOG"
echo "" >> "$LOG"

# ─── Step 1: Check prerequisites ───────────────────────────────────────────
echo "[ Step 1 ] Checking prerequisites..."

# Detect 7z binary — p7zip-full ships as 7za; newer 7zip package ships as 7z
SEVENZ=""
for candidate in 7z 7za 7zz; do
  if command -v "$candidate" &>/dev/null; then
    SEVENZ="$candidate"
    break
  fi
done
if [ -z "$SEVENZ" ]; then
  fail "No 7z binary found (tried: 7z, 7za, 7zz).
      Install with: sudo apt install p7zip-full
      Then re-run this script."
fi
ok "7z binary: $SEVENZ ($(command -v "$SEVENZ"))"

# bsdtar (from libarchive-tools) replaces xar — supports Apple .pkg (xar format)
if ! command -v bsdtar &>/dev/null; then
  fail "bsdtar not found. Install with: sudo apt install libarchive-tools"
fi
ok "bsdtar found at $(command -v bsdtar)"

if ! command -v python3 &>/dev/null; then
  fail "python3 not found."
fi
ok "python3 found at $(command -v python3)"

if ! python3 -c "from fontTools.ttLib import TTFont" 2>/dev/null; then
  fail "fonttools not found. Install with: pip install fonttools --break-system-packages"
fi
ok "fonttools found"

# ─── Helper: extract .pkg (xar) then cpio Payload ──────────────────────────
extract_pkg() {
  local pkg="$1" out_pkg="$2" out_fonts="$3"
  rm -rf "$out_pkg" "$out_fonts"
  mkdir -p "$out_pkg" "$out_fonts"

  info "  Extracting pkg (xar/bsdtar): $(basename "$pkg")"
  bsdtar -xf "$pkg" -C "$out_pkg" >> "$LOG" 2>&1 \
    || fail "bsdtar failed on $(basename "$pkg")"

  local payload
  payload=$(find "$out_pkg" -name "Payload" | head -1)
  [ -n "$payload" ] || fail "No Payload found inside $(basename "$pkg")"

  info "  Extracting cpio Payload..."
  ( cd "$out_fonts" && gunzip -dc "$payload" | cpio -idm >> "$LOG" 2>&1 ) \
    || fail "cpio failed for $(basename "$pkg")"
}

# ─── Step 2: Extract SF-Pro.dmg ────────────────────────────────────────────
echo ""
echo "[ Step 2 ] Extracting SF-Pro.dmg..."

SF_PRO_DMG="$SRC_DMG/SF-Pro.dmg"
[ -f "$SF_PRO_DMG" ] || fail "SF-Pro.dmg not found at $SF_PRO_DMG"

SF_PRO_TMP="$TMP_DIR/sf-pro"
rm -rf "$SF_PRO_TMP"
mkdir -p "$SF_PRO_TMP"

info "Extracting DMG (this takes ~30s for a 213 MB file)..."
"$SEVENZ" x "$SF_PRO_DMG" -o"$SF_PRO_TMP" -y >> "$LOG" 2>&1 \
  || fail "7z extraction failed for SF-Pro.dmg"

# Locate the .pkg inside the extracted DMG
SF_PKG=$(find "$SF_PRO_TMP" \( -name "SFProFonts*.pkg" -o -name "SF-Pro*.pkg" \) 2>/dev/null | head -1)
[ -n "$SF_PKG" ] || \
  SF_PKG=$(find "$SF_PRO_TMP" -name "*.pkg" 2>/dev/null | grep -i "SF.Pro\|SFPro\|Fonts" | head -1)
[ -n "$SF_PKG" ] || \
  SF_PKG=$(find "$SF_PRO_TMP" -name "*.pkg" 2>/dev/null | head -1)
[ -n "$SF_PKG" ] || fail "Could not find any .pkg inside SF-Pro.dmg. Contents of $SF_PRO_TMP:
$(find "$SF_PRO_TMP" -maxdepth 4 | head -40)"
ok "Found pkg: $(basename "$SF_PKG")"

extract_pkg "$SF_PKG" "$TMP_DIR/sf-pro-pkg" "$TMP_DIR/sf-pro-fonts"

SF_PRO_TTF=$(find "$TMP_DIR/sf-pro-fonts" -name "SF-Pro.ttf" 2>/dev/null | head -1)
[ -n "$SF_PRO_TTF" ] || \
  SF_PRO_TTF=$(find "$TMP_DIR/sf-pro-fonts" -name "*.ttf" 2>/dev/null | grep -v "Arabic\|Compact\|Display\|Text" | grep "Pro" | head -1)
[ -n "$SF_PRO_TTF" ] || fail "SF-Pro.ttf not found after extraction.
Fonts found: $(find "$TMP_DIR/sf-pro-fonts" -name "*.ttf" -o -name "*.otf" 2>/dev/null | head -20)"
ok "SF-Pro.ttf found: $(du -sh "$SF_PRO_TTF" | cut -f1)"

# ─── Step 3: Extract SF-Arabic.dmg ─────────────────────────────────────────
echo ""
echo "[ Step 3 ] Extracting SF-Arabic.dmg..."

SF_ARABIC_DMG="$SRC_DMG/SF-Arabic.dmg"
[ -f "$SF_ARABIC_DMG" ] || fail "SF-Arabic.dmg not found at $SF_ARABIC_DMG"

SF_ARABIC_TMP="$TMP_DIR/sf-arabic"
rm -rf "$SF_ARABIC_TMP"
mkdir -p "$SF_ARABIC_TMP"

"$SEVENZ" x "$SF_ARABIC_DMG" -o"$SF_ARABIC_TMP" -y >> "$LOG" 2>&1 \
  || fail "7z extraction failed for SF-Arabic.dmg"

ARABIC_PKG=$(find "$SF_ARABIC_TMP" -name "*.pkg" 2>/dev/null | head -1)
[ -n "$ARABIC_PKG" ] || fail "Could not find .pkg inside SF-Arabic.dmg"
ok "Found pkg: $(basename "$ARABIC_PKG")"

extract_pkg "$ARABIC_PKG" "$TMP_DIR/sf-arabic-pkg" "$TMP_DIR/sf-arabic-fonts"

SF_ARABIC_TTF=$(find "$TMP_DIR/sf-arabic-fonts" -name "SF-Arabic.ttf" 2>/dev/null | head -1)
[ -n "$SF_ARABIC_TTF" ] || \
  SF_ARABIC_TTF=$(find "$TMP_DIR/sf-arabic-fonts" -name "*.ttf" 2>/dev/null | grep -i "arabic" | head -1)
[ -n "$SF_ARABIC_TTF" ] || fail "SF-Arabic.ttf not found after extraction.
Fonts found: $(find "$TMP_DIR/sf-arabic-fonts" -name "*.ttf" -o -name "*.otf" 2>/dev/null | head -20)"
ok "SF-Arabic.ttf found: $(du -sh "$SF_ARABIC_TTF" | cut -f1)"

# ─── Step 4: Inspect fonts (variable detection) ────────────────────────────
echo ""
echo "[ Step 4 ] Inspecting fonts for variable axes..."

BRANCH_A=false

python3 - "$SF_PRO_TTF" "$SF_ARABIC_TTF" <<'PYEOF' | tee -a "$LOG"
import sys
from fontTools.ttLib import TTFont

def inspect(path):
    try:
        f = TTFont(path, lazy=True)
        if 'fvar' in f:
            axes = [(a.axisTag, a.minValue, a.defaultValue, a.maxValue)
                    for a in f['fvar'].axes]
            print(f"  VARIABLE: {path}")
            for tag, mn, default, mx in axes:
                print(f"    axis '{tag}': {mn} – {default} (default) – {mx}")
            return True
        else:
            print(f"  STATIC:   {path}")
            return False
    except Exception as e:
        print(f"  ERROR reading {path}: {e}")
        return False

inspect(sys.argv[1])
inspect(sys.argv[2])
PYEOF

if python3 -c "
from fontTools.ttLib import TTFont
f = TTFont('$SF_PRO_TTF', lazy=True)
import sys; sys.exit(0 if 'fvar' in f else 1)
" 2>/dev/null; then
  BRANCH_A=true
  ok "Branch A — variable SF Pro confirmed. Weight slider will be enabled in WebUI."
else
  warn "Branch B — SF-Pro.ttf is STATIC. Weight slider will be hidden in WebUI."
fi

# ─── Step 5: Validate and copy primary fonts into module ───────────────────
echo ""
echo "[ Step 5 ] Validating and copying fonts into module..."

mkdir -p "$FONT_DEST"
# Remove stale fonts from previous builds before copying fonts this run.
rm -f "$FONT_DEST"/*.ttf "$FONT_DEST"/*.otf

# copy_font validates magic, size, then copies to $FONT_DEST.
copy_font() {
  local src="$1" name="$2" max_bytes="$3"
  [ -f "$src" ] || fail "Font file not found: $src"
  local size
  size=$(stat -c%s "$src")
  if [ "$size" -lt 10240 ]; then
    fail "$name is too small ($size bytes) — likely corrupt"
  fi
  if [ "$size" -gt "$max_bytes" ]; then
    fail "$name is too large ($size bytes, max $max_bytes)"
  fi
  local magic
  magic=$(head -c 4 "$src" | od -An -tx1 | tr -d ' \n')
  case "$magic" in
    00010000|4f54544f|74727565|74746366) : ;;
    *) fail "$name has unexpected magic bytes ($magic)" ;;
  esac
  cp "$src" "$FONT_DEST/$name"
  ok "$name copied ($(( size / 1024 )) KB)"
}

# Ship fonts under their PRIMARY system filenames.
# Android unzip does NOT handle zip symlinks — they become tiny text files and
# get rejected by customize.sh's validation. All system-name aliases are created
# by customize.sh which runs in a real shell on the device after extraction.
#
# Primary name mapping:
#   SF-Pro.ttf        → SysFont-Regular.ttf  (OxygenOS primary variable Latin font)
#   SF-Arabic.ttf     → SF-Arabic.ttf        (customize.sh expands to all NotoNaskhArabic names)
#   AppleColorEmoji   → NotoColorEmoji.ttf   (font_fallback.xml references NotoColorEmoji; no APEX on this device)
copy_font "$SF_PRO_TTF"    "SysFont-Regular.ttf"  31457280  # 30 MB — primary system name
copy_font "$SF_ARABIC_TTF" "SF-Arabic.ttf"        31457280  # 30 MB — customize.sh expands this

copy_font "$SRC_EMOJI/AppleColorEmoji.ttf" "NotoColorEmoji.ttf" 157286400  # 150 MB cap

# ─── Step 5.5: Geeza Pro (optional Arabic alternative) ─────────────────────
echo ""
echo "[ Step 5.5 ] Geeza Pro Arabic (optional)..."

GEEZA_SRC="$SCRIPT_DIR/sources/geeza/GeezaPro.ttf"
if [ -f "$GEEZA_SRC" ]; then
  copy_font "$GEEZA_SRC" "GeezaPro.ttf" 31457280
  python3 - "$GEEZA_SRC" <<'GEEZAPY' | tee -a "$LOG"
import sys
from fontTools.ttLib import TTFont
try:
    f = TTFont(sys.argv[1], lazy=True)
    if 'fvar' in f:
        axes = [(a.axisTag, a.minValue, a.defaultValue, a.maxValue)
                for a in f['fvar'].axes]
        print(f"  VARIABLE: GeezaPro.ttf")
        for tag, mn, default, mx in axes:
            print(f"    axis '{tag}': {mn} – {default} (default) – {mx}")
    else:
        print("  STATIC: GeezaPro.ttf (no fvar — weight patching skipped at boot)")
except Exception as e:
    print(f"  ERROR inspecting GeezaPro.ttf: {e}")
GEEZAPY
else
  warn "GeezaPro.ttf not found at $GEEZA_SRC — Geeza toggle shown in WebUI but inactive"
fi

# ─── Step 5.6: Cocon Next Arabic (optional Arabic alternative) ─────────────
echo ""
echo "[ Step 5.6 ] Cocon Next Arabic (optional)..."

COCON_SRC="$SCRIPT_DIR/sources/cocon/Cocon-Regular.ttf"
if [ -f "$COCON_SRC" ]; then
  copy_font "$COCON_SRC" "Cocon-Regular.ttf" 31457280
  python3 - "$COCON_SRC" <<'COCONPY' | tee -a "$LOG"
import sys
from fontTools.ttLib import TTFont
try:
    f = TTFont(sys.argv[1], lazy=True)
    full_name = ''
    if 'name' in f:
        for rec in f['name'].names:
            if rec.nameID == 4:
                full_name = rec.toUnicode()
                break
    if 'fvar' in f:
        axes = [(a.axisTag, a.minValue, a.defaultValue, a.maxValue)
                for a in f['fvar'].axes]
        print(f"  VARIABLE: Cocon-Regular.ttf ({full_name})")
        for tag, mn, default, mx in axes:
            print(f"    axis '{tag}': {mn} – {default} (default) – {mx}")
    else:
        print(f"  STATIC: Cocon-Regular.ttf ({full_name}) — no fvar, weight patching skipped")
except Exception as e:
    print(f"  ERROR inspecting Cocon-Regular.ttf: {e}")
COCONPY
else
  warn "Cocon-Regular.ttf not found at $COCON_SRC — Cocon toggle shown in WebUI but inactive"
fi

# ─── Step 6: Patch WebUI branch flag ───────────────────────────────────────
echo ""
echo "[ Step 6 ] Patching WebUI branch flag (IS_VARIABLE = $BRANCH_A)..."

sed -i "s/const IS_VARIABLE = APPLE_FONTS_BRANCH_A;/const IS_VARIABLE = $BRANCH_A;/" \
  "$MOD_DIR/webroot/app.js"
ok "app.js patched with IS_VARIABLE=$BRANCH_A"

# ─── Step 7: (skipped) Branch B XML — not used; filename overlay approach works ─

# ─── Step 9: Zip the module ────────────────────────────────────────────────
echo ""
echo "[ Step 9 ] Assembling AppleFonts-v1.3.0.zip..."

# Clean webroot/fonts — customize.sh recreates these on-device with real copies.
# Stale symlinks here become tiny garbage text files when unzipped by Android.
rm -f "$MOD_DIR/webroot/fonts/"*
info "Cleaned webroot/fonts/ (will be repopulated on-device by customize.sh)"

OUT_ZIP="$OUT_DIR/AppleFonts-v1.3.0.zip"
rm -f "$OUT_ZIP"

( cd "$MOD_DIR" && zip -ry "$OUT_ZIP" . \
    -x "*.DS_Store" \
    -x "*/__pycache__/*" \
    -x "*.pyc" \
    >> "$LOG" 2>&1 )

ok "Zip created: $OUT_ZIP  ($(du -sh "$OUT_ZIP" | cut -f1))"

echo ""
echo "[ Step 10 ] Verifying zip structure..."
unzip -l "$OUT_ZIP" | head -40 | tee -a "$LOG" || true
echo "(…)"

# ─── Final report ──────────────────────────────────────────────────────────
echo ""
echo "====================================="
echo "  BUILD COMPLETE"
echo "====================================="
echo ""
echo "Zip:     $OUT_ZIP"
echo "Log:     $LOG"
echo ""
echo "Font replacement table:"
echo "  AppleColorEmoji.ttf (primary)→ AppleColorEmoji.ttf  (iOS emoji, APEX-bypass via custom name)"
echo "  NotoColorEmoji.ttf (APEX)   → fallback for new Unicode codepoints not yet in Apple font"
echo "  SysFont-Regular.ttf (Latin)  → SF-Pro.ttf           (SF Pro $([ "$BRANCH_A" = true ] && echo 'Variable' || echo 'Static'), toggleable)"
echo "  NotoNaskhArabic-*.ttf        → SF-Arabic.ttf        (SF Arabic, toggleable)"
if [ -f "$FONT_DEST/GeezaPro.ttf" ]; then
  echo "  NotoNaskhArabic-*.ttf        → GeezaPro.ttf         (Geeza Pro, toggleable — alt Arabic)"
else
  echo "  GeezaPro.ttf                 *** NOT INCLUDED — add to sources/geeza/ and rebuild ***"
fi
if [ -f "$FONT_DEST/Cocon-Regular.ttf" ]; then
  echo "  NotoNaskhArabic-*.ttf        → Cocon-Regular.ttf    (Cocon Next Arabic, toggleable — alt Arabic)"
else
  echo "  Cocon-Regular.ttf            *** NOT INCLUDED — add to sources/cocon/ and rebuild ***"
fi
echo ""
echo "Branch:  $([ "$BRANCH_A" = true ] && echo 'A — variable font, full weight slider' || echo 'B — static fonts, weight slider disabled')"
echo ""
echo "Flash:   KernelSU Next → Modules → Install from storage → select the zip"
echo "WebUI:   After reboot → KernelSU Next → Modules → AppleFonts → Open WebUI"
echo ""
echo "━━━ RECOVERY INSTRUCTIONS ━━━"
echo "If the device fails to boot:"
echo "  1. Hold Power + Volume Down to enter recovery."
echo "  2. KernelSU Next recovery → Disable all modules."
echo "  3. Boot normally, open KSU manager, uninstall AppleFonts."
echo ""
echo "The module also self-disables if boot does not complete within 90 seconds,"
echo "so most cases auto-recover on the second boot attempt."
echo ""
{
  echo ""
  echo "====================================="
  echo "Final build: $(date)"
  echo "Zip: $OUT_ZIP ($(du -sh "$OUT_ZIP" | cut -f1))"
  echo "Branch: $([ "$BRANCH_A" = true ] && echo 'A (variable)' || echo 'B (static)')"
  echo "====================================="
} >> "$LOG"
