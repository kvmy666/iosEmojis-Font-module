#!/system/bin/sh
# AppleFonts diagnostic script.
# Run from ADB:  adb shell su -c sh /data/adb/modules/AppleFonts/scripts/debug.sh
# Or via KernelSU WebUI action button if wired up.
# Output is written to /data/adb/AppleFonts/debug.log — pull with:
#   adb pull /data/adb/AppleFonts/debug.log

OUT=/data/adb/AppleFonts/debug.log
MODDIR=${0%/*}/..
mkdir -p /data/adb/AppleFonts
: > "$OUT"

h() { printf '\n━━━ %s ━━━\n' "$1" >> "$OUT"; }
p() { printf '%s\n' "$1" >> "$OUT"; }
cmd() { printf '$ %s\n' "$1" >> "$OUT"; eval "$1" >> "$OUT" 2>&1 || true; }

p "AppleFonts debug log — $(date)"
p "Script: $0"

# ── Device ───────────────────────────────────────────────────────────────────
h "Device"
cmd "getprop ro.product.manufacturer"
cmd "getprop ro.product.model"
cmd "getprop ro.build.version.release"
cmd "getprop ro.build.version.sdk"
cmd "getprop ro.product.cpu.abi"

# ── Module config & logs ─────────────────────────────────────────────────────
h "Config (/data/adb/AppleFonts/config.json)"
cat /data/adb/AppleFonts/config.json >> "$OUT" 2>/dev/null || p "(not found)"

h "post-fs-data log"
cat /data/adb/AppleFonts/post-fs.log >> "$OUT" 2>/dev/null || p "(not found)"

# ── fonts.xml analysis ───────────────────────────────────────────────────────
h "System /system/etc/fonts.xml — structure overview"
if [ -f /system/etc/fonts.xml ]; then
  p "Total lines: $(wc -l < /system/etc/fonts.xml)"
  p ""
  p "--- Key lines (familyset, sans-serif, emoji) ---"
  grep -En 'AppleColorEmoji|NotoColorEmoji|<familyset|name="sans-serif"|und-Zsye|lang=' /system/etc/fonts.xml >> "$OUT" 2>/dev/null || p "(no matches)"
  p ""
  p "--- Emoji family block (context around NotoColorEmoji) ---"
  grep -n 'NotoColorEmoji' /system/etc/fonts.xml | while IFS=: read -r LNUM REST; do
    START=$(( LNUM - 3 )); [ "$START" -lt 1 ] && START=1
    END=$(( LNUM + 3 ))
    awk "NR>=$START && NR<=$END { printf \"%d: %s\n\", NR, \$0 }" /system/etc/fonts.xml >> "$OUT"
  done
else
  p "/system/etc/fonts.xml NOT FOUND"
fi

h "System fallback fonts listing"
p "Fonts in /system/fonts/ that could be in the text fallback chain:"
ls /system/fonts/Noto*.ttf /system/fonts/DroidSans*.ttf 2>/dev/null | while read -r F; do
  SZ=$(stat -c%s "$F" 2>/dev/null || echo "?")
  p "  $(basename "$F") (${SZ}B)"
done

h "Module fonts.xml overlay — existence and emoji position"
MOD_XML="$MODDIR/system/etc/fonts.xml"
if [ -f "$MOD_XML" ]; then
  p "Overlay exists: $MOD_XML ($(wc -l < "$MOD_XML") lines)"
  p ""
  p "--- First 30 lines (emoji should appear here right after <familyset>) ---"
  head -30 "$MOD_XML" >> "$OUT"
  p ""
  p "--- AppleColorEmoji/NotoColorEmoji position in overlay ---"
  grep -n 'AppleColorEmoji\|NotoColorEmoji\|<familyset\|name="sans-serif"' "$MOD_XML" >> "$OUT" 2>/dev/null || p "(no matches)"
else
  p "NO overlay fonts.xml found at: $MOD_XML"
  p "This means post-fs-data.sh did not generate it."
  p "Check post-fs-data log above for errors."
fi

# ── Verify magic mount is working ────────────────────────────────────────────
h "Magic mount verification"
p "Checking if module system/etc is overlaid on /system/etc..."
# If magic mount works, /system/etc/fonts.xml should match our overlay
# We compare the first 5 lines (the familyset opening + any injected emoji family)
SYS_HEAD=$(head -6 /system/etc/fonts.xml 2>/dev/null | md5sum 2>/dev/null | awk '{print $1}')
MOD_HEAD=$(head -6 "$MOD_XML"            2>/dev/null | md5sum 2>/dev/null | awk '{print $1}')
p "System fonts.xml header md5 : $SYS_HEAD"
p "Module fonts.xml header md5 : $MOD_HEAD"
if [ "$SYS_HEAD" = "$MOD_HEAD" ] && [ -f "$MOD_XML" ]; then
  p "MATCH — magic mount is active and our overlay is being read."
else
  p "DIFFER — either magic mount is NOT active, or comparison method failed."
  p "  (Note: on some kernels /system/etc/fonts.xml seen here is already the overlay)"
fi

# ── Font files ───────────────────────────────────────────────────────────────
h "Font files in module (system/fonts/)"
ls -la "$MODDIR/system/fonts/" >> "$OUT" 2>/dev/null || p "(directory missing)"

h "Font files in module store (fonts_store/)"
ls -la "$MODDIR/fonts_store/" >> "$OUT" 2>/dev/null || p "(empty or missing)"

h "OEM alias list (fonts_aliases.txt)"
cat "$MODDIR/fonts_aliases.txt" >> "$OUT" 2>/dev/null || p "(not found)"

# ── Apple emoji font identity check ─────────────────────────────────────────
h "NotoColorEmoji.ttf identity check (should be Apple CBDT, not stock COLR)"
EMOJI_FILE="$MODDIR/system/fonts/NotoColorEmoji.ttf"
if [ -f "$EMOJI_FILE" ]; then
  SIZE=$(stat -c%s "$EMOJI_FILE" 2>/dev/null || echo "?")
  p "File: $EMOJI_FILE"
  p "Size: $SIZE bytes"
  # Apple CBDT is ~115MB; stock OxygenOS COLR NotoColorEmoji is ~2.8MB
  [ "$SIZE" -gt 30000000 ] 2>/dev/null && p "Size check: PASS (>30MB — Apple CBDT)" || p "Size check: WARN (<=30MB — stock COLRv0 Noto, Apple emoji not overlaid)"
  # Apple Color Emoji (CBDT repack for Linux) uses CBDT table
  CBDT=$(od -An -tx1 "$EMOJI_FILE" 2>/dev/null | tr -d ' \n' | grep -o '43424454' | head -1)
  [ -n "$CBDT" ] && p "CBDT table: FOUND (Apple CBDT repack — correct)" || p "CBDT table: NOT found — unexpected format"
  # Stock Noto COLRv0 uses COLR table
  COLR=$(od -An -tx1 "$EMOJI_FILE" 2>/dev/null | tr -d ' \n' | grep -o '434f4c52' | head -1)
  [ -n "$COLR" ] && p "COLR table: FOUND — this is stock COLRv0 Noto, Apple overlay failed" || p "COLR table: not found (good — not the stock Noto)"
else
  p "EMOJI FILE NOT FOUND: $EMOJI_FILE"
  STORE_FILE="$MODDIR/fonts_store/NotoColorEmoji.ttf"
  [ -f "$STORE_FILE" ] && p "Found in fonts_store/ — emoji toggle is disabled in config." || p "Not in fonts_store/ either — emoji font is missing entirely."
fi

# ── Check /data/fonts (GMS override) ─────────────────────────────────────────
h "/data/fonts (GMS font override — should be absent)"
if [ -d /data/fonts ]; then
  p "WARNING: /data/fonts EXISTS. GMS downloaded fonts override our emoji!"
  ls /data/fonts/ >> "$OUT" 2>/dev/null
  p ""
  p "Fix: run the module action button (clears this) and reboot."
else
  p "Not present. Good — GMS is not overriding our fonts."
fi

# ── Typeface cache ────────────────────────────────────────────────────────────
h "Typeface cache files (/data/system/font_*)"
ls /data/system/font_* >> "$OUT" 2>/dev/null || p "(no cache files found)"

# ── Logcat: emoji and font rendering ─────────────────────────────────────────
h "Logcat — Minikin / emoji / font (last 200 lines, relevant tags)"
# Minikin is Android's text layout engine — it decides which font renders each glyph
logcat -d -b main 2>/dev/null \
  | grep -iE 'minikin|emoji|FontsContract|TypefaceCompat|Typeface|font.*select|select.*font' \
  | tail -200 >> "$OUT" 2>/dev/null || p "(logcat unavailable or no matches)"

# ── Minikin verbose (may be empty on production builds) ──────────────────────
h "Logcat — Minikin verbose (production builds suppress this)"
logcat -d -s "Minikin:V" 2>/dev/null | tail -100 >> "$OUT" 2>/dev/null || p "(no Minikin verbose output)"

# ── Emoji codepoint check via Python (if available) ──────────────────────────
h "Apple emoji codepoint coverage check (requires python3 + fonttools on device)"
if command -v python3 > /dev/null 2>&1; then
  python3 - "$EMOJI_FILE" >> "$OUT" 2>/dev/null << 'PYEOF'
import sys, struct
try:
    from fontTools.ttLib import TTFont
    font = TTFont(sys.argv[1], lazy=True)
    cmap = font.getBestCmap()
    # Key "text-default" emoji that commonly break
    CHECK = {
        0x267E: "♾ (U+267E PERMANENT PAPER SIGN — the ∞ emoji)",
        0x2639: "☹ (U+2639 WHITE FROWNING FACE)",
        0x263A: "☺ (U+263A WHITE SMILING FACE)",
        0x00A9: "© (U+00A9 COPYRIGHT SIGN)",
        0x00AE: "® (U+00AE REGISTERED SIGN)",
        0x2122: "™ (U+2122 TRADE MARK SIGN)",
        0x2620: "☠ (U+2620 SKULL AND CROSSBONES)",
        0x2764: "❤ (U+2764 HEAVY BLACK HEART)",
        0x2665: "♥ (U+2665 BLACK HEART SUIT)",
        0x2660: "♠ (U+2660 BLACK SPADE SUIT)",
    }
    print(f"Font cmap has {len(cmap)} entries")
    for cp, label in CHECK.items():
        status = "PRESENT" if cp in cmap else "MISSING"
        print(f"  {status}: {label}")
except ImportError:
    print("fonttools not available on device — skipping codepoint check")
except Exception as e:
    print(f"Error: {e}")
PYEOF
else
  p "python3 not available on device — skipping codepoint check."
  p "Run on PC: python3 -c \"from fontTools.ttLib import TTFont; f=TTFont('AppleColorEmoji.ttf'); print(hex(0x267E) in [hex(k) for k in f.getBestCmap()])\""
fi

# ── Summary ───────────────────────────────────────────────────────────────────
h "Summary — things to look for"
p "1. post-fs log should end with 'post-fs-data.sh done' with no ERRORs."
p "2. fonts.xml overlay should exist AND have NotoColorEmoji in the first ~10 lines."
p "3. Magic mount: header md5 should MATCH if the overlay is active."
p "4. /data/fonts should NOT exist (GMS override)."
p "5. NotoColorEmoji.ttf in module/system/fonts should be >30MB with CBDT table (Apple CBDT repack)."
p "6. Python check: U+267E (♾) should be PRESENT in the emoji font cmap."
p ""
p "Pull this log with:  adb pull /sdcard/applefonts_debug.log"
p ""
p "Done: $(date)"

# Copy to sdcard so ADB can pull without root
cp "$OUT" /sdcard/applefonts_debug.log 2>/dev/null && \
  p "Copied to /sdcard/applefonts_debug.log" || true

# Also print to stdout so KernelSU action shows output
cat "$OUT"
