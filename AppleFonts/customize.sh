#!/sbin/sh

ui_print "==================================="
ui_print "  Apple Fonts v1.0.0"
ui_print "  by Abdulkarim"
ui_print "==================================="
ui_print ""

abort_with_log() {
  ui_print "ERROR: $1"
  abort "$1"
}

# Android version check
ui_print "- Checking Android version (API $API)..."
if [ "$API" -lt 28 ]; then
  abort_with_log "Need Android 9+ (API 28). You have API $API."
fi
if [ "$API" -lt 31 ]; then
  ui_print "  WARN: Android < 12 (API $API) — variable font axes disabled."
  ui_print "  Weight slider in WebUI will be hidden."
fi

# ABI check — fonts are architecture-independent; warn only
ui_print "- Checking ABI ($ARCH)..."
if [ "$ARCH" != "arm64" ]; then
  ui_print "  WARN: Module tested on arm64. Your ABI ($ARCH) may work — proceeding."
fi

# Free space check — need room for font copies created below (~500 MB with Apple emoji)
ui_print "- Checking free space..."
FREE_KB=$(df /data 2>/dev/null | tail -1 | awk '{print $4}')
if [ -n "$FREE_KB" ] && [ "$FREE_KB" -lt 512000 ]; then
  abort_with_log "Need 500MB free in /data. Have ${FREE_KB}KB."
fi

# Conflicting module check
ui_print "- Checking for conflicting font modules..."
for m in MFGA EvilFont iOS_Emoji Magisk-iOS-Emoji MagiskAppleEmoji Root-iOS-Emoji; do
  if [ -d "/data/adb/modules/$m" ] && [ ! -f "/data/adb/modules/$m/disable" ]; then
    ui_print "  WARN: Active conflicting module: $m — disable it to avoid conflicts."
  fi
done

# Font file validation (only the 3 primary files shipped in the zip)
ui_print "- Validating font files..."
FONT_OK=0
FONT_BAD=0

for ttf in "$MODPATH"/system/fonts/*.ttf; do
  [ -f "$ttf" ] || continue
  FNAME=$(basename "$ttf")
  SIZE=$(stat -c%s "$ttf" 2>/dev/null || echo 0)

  # Emoji font cap: Apple CBDT is ~111 MB; stock Noto is ~2.8 MB
  case "$FNAME" in
    *ColorEmoji*|*Emoji*) SIZE_MAX=157286400 ;;  # 150 MB
    *)                    SIZE_MAX=31457280 ;;   # 30 MB
  esac

  if [ "$SIZE" -lt 10240 ]; then
    ui_print "  SKIP: $FNAME is tiny (${SIZE} bytes) — skipping validation of alias."
    continue
  fi
  if [ "$SIZE" -gt "$SIZE_MAX" ]; then
    ui_print "  WARN: $FNAME too large (${SIZE}B, max ${SIZE_MAX}B). Removing."
    rm -f "$ttf"
    FONT_BAD=$((FONT_BAD + 1))
    continue
  fi

  MAGIC=$(dd if="$ttf" bs=1 count=4 2>/dev/null | od -An -tx1 | tr -d ' \n')
  case "$MAGIC" in
    00010000|4f54544f|74727565|74746366)
      ui_print "  OK: $FNAME ($(( SIZE / 1024 )) KB)"
      FONT_OK=$((FONT_OK + 1))
      ;;
    *)
      ui_print "  WARN: $FNAME bad magic ($MAGIC). Removing."
      rm -f "$ttf"
      FONT_BAD=$((FONT_BAD + 1))
      ;;
  esac
done

ui_print "  Accepted: $FONT_OK | Rejected: $FONT_BAD"
if [ "$FONT_OK" -eq 0 ]; then
  abort_with_log "No valid font files found. Cannot continue."
fi

# ── Create system-filename copies on-device ─────────────────────────────────
# Android unzip does not support zip symlinks — they become tiny text files.
# We do all aliasing HERE in customize.sh which runs in a real shell on the device.
ui_print "- Creating font name overlays..."
FONTS="$MODPATH/system/fonts"

# SF Pro → covers all Latin weight requests via fonts.xml axis mapping
# SysFont-Regular.ttf is the primary OxygenOS Latin variable font
# Roboto-Regular.ttf is the target of DroidSans-Bold.ttf symlink in fonts.xml
if [ -f "$FONTS/SysFont-Regular.ttf" ]; then
  cp "$FONTS/SysFont-Regular.ttf" "$FONTS/Roboto-Regular.ttf"
  ui_print "  OK: Roboto-Regular.ttf (DroidSans-Bold alias)"
fi

# Arabic slot aliases — default to SF Arabic at install time.
# post-fs-data.sh overwrites these with Geeza Pro or Cocon when those are toggled on.
if [ -f "$FONTS/SF-Arabic.ttf" ]; then
  for ARABIC_NAME in \
    NotoNaskhArabic-Regular \
    NotoNaskhArabic-Bold \
    NotoNaskhArabic-Black \
    NotoNaskhArabicUI-Regular \
    NotoNaskhArabicUI-Bold \
    NotoNaskhArabicUI-Medium \
    NotoNaskhArabicUI-SemiBold \
    NotoNaskhArabicUI-Light \
    NotoNaskhArabicUI-Thin \
    NotoNaskhArabicUI-Black; do
    cp "$FONTS/SF-Arabic.ttf" "$FONTS/${ARABIC_NAME}.ttf"
    ui_print "  OK: ${ARABIC_NAME}.ttf"
  done
fi

# ── OEM font name aliasing (Samsung, Xiaomi, etc.) ─────────────────────────
# The fonts.xml overlay in post-fs-data.sh is the primary mechanism for OEM
# compatibility. These aliases are a secondary safety net: they create SF Pro
# copies using the device's actual font filenames so the magic-mount overlay
# catches any app or subsystem that loads fonts by name directly.
ui_print "- Detecting OEM font names..."
ALIAS_LIST="$MODPATH/fonts_aliases.txt"
: > "$ALIAS_LIST"
if [ -f /system/etc/fonts.xml ]; then
  awk '
    /name="sans-serif"/ { in_ss=1 }
    in_ss && /style="normal"/ {
      # Inline: <font ...>Name.ttf</font> or <font ...>Name.ttf<axis
      if (match($0, />[A-Za-z0-9._-]+\.ttf/))
        print substr($0, RSTART+1, RLENGTH-1)
      else
        in_font = 1
    }
    in_ss && in_font && /^[[:space:]]*[A-Za-z0-9._-]+\.ttf/ {
      match($0, /[A-Za-z0-9._-]+\.ttf/)
      print substr($0, RSTART, RLENGTH)
      in_font = 0
    }
    in_ss && (/<\/font>/ || /<\/family>/) { in_font = 0 }
    in_ss && /<\/family>/ { in_ss=0; exit }
  ' /system/etc/fonts.xml 2>/dev/null | sort -u | while IFS= read -r OEM_FONT; do
    case "$OEM_FONT" in
      SysFont*|Roboto*|NotoColor*|NotoNaskh*|SF-*|Geeza*|Cocon*) continue ;;
    esac
    [ -f "$FONTS/$OEM_FONT" ] && continue  # already exists
    if [ -f "$FONTS/SysFont-Regular.ttf" ]; then
      cp "$FONTS/SysFont-Regular.ttf" "$FONTS/$OEM_FONT"
      echo "$OEM_FONT" >> "$ALIAS_LIST"
      ui_print "  alias: $OEM_FONT"
    fi
  done
  COUNT=$(wc -l < "$ALIAS_LIST" 2>/dev/null | tr -d ' ')
  [ "${COUNT:-0}" -gt 0 ] && ui_print "  Created $COUNT OEM alias(es)." || ui_print "  No OEM aliases needed (AOSP/OxygenOS font names)."
else
  ui_print "  /system/etc/fonts.xml not found — skipping alias detection."
fi
set_perm "$ALIAS_LIST" 0 0 0644 2>/dev/null || true

# ── WebUI fonts directory ────────────────────────────────────────────────────
# KernelSU WebView serves files from $MODPATH/webroot/.
# Copy (not symlink) the fonts the CSS @font-face references.
ui_print "- Setting up WebUI fonts..."
mkdir -p "$MODPATH/webroot/fonts"
[ -f "$FONTS/SysFont-Regular.ttf" ] && \
  cp "$FONTS/SysFont-Regular.ttf" "$MODPATH/webroot/fonts/SysFont-Regular.ttf"
[ -f "$FONTS/SF-Arabic.ttf" ] && \
  cp "$FONTS/SF-Arabic.ttf" "$MODPATH/webroot/fonts/SF-Arabic.ttf"
[ -f "$FONTS/GeezaPro.ttf" ] && \
  cp "$FONTS/GeezaPro.ttf" "$MODPATH/webroot/fonts/GeezaPro.ttf" && \
  ui_print "  OK: GeezaPro.ttf → webroot/fonts/"
[ -f "$FONTS/Cocon-Regular.ttf" ] && \
  cp "$FONTS/Cocon-Regular.ttf" "$MODPATH/webroot/fonts/Cocon-Regular.ttf" && \
  ui_print "  OK: Cocon-Regular.ttf → webroot/fonts/"

# ── Persistent data ──────────────────────────────────────────────────────────
ui_print "- Initialising /data/adb/AppleFonts..."
mkdir -p /data/adb/AppleFonts
if [ ! -f /data/adb/AppleFonts/config.json ]; then
  printf '{"wght":400,"wdth":100,"opsz":28,"latin":true,"arabic":true,"geeza":false,"cocon":false,"emoji":true}' > /data/adb/AppleFonts/config.json
fi

printf '%s|baseline|%s\n' \
  "$(date '+%Y-%m-%d %H:%M:%S')" \
  "$(grep -E '^Mem(Total|Available)' /proc/meminfo | tr '\n' '|')" \
  > /data/adb/AppleFonts/perf.log

# No directory replacement — overlay only
REPLACE=""

# ── Permissions ──────────────────────────────────────────────────────────────
ui_print "- Setting permissions..."
set_perm_recursive "$MODPATH"              0 0 0755 0644
set_perm_recursive "$MODPATH/system/fonts" 0 0 0755 0644 u:object_r:system_file:s0
set_perm_recursive "$MODPATH/scripts"      0 0 0755 0755
set_perm             "$MODPATH/scripts/debug.sh"     0 0 0755
set_perm_recursive "$MODPATH/webroot"      0 0 0755 0644
set_perm             "$MODPATH/service.sh"       0 0 0755
set_perm             "$MODPATH/action.sh"        0 0 0755
set_perm             "$MODPATH/post-fs-data.sh"  0 0 0755
set_perm             "$MODPATH/uninstall.sh"     0 0 0755

ui_print ""
ui_print "  Installation complete."
ui_print "  REBOOT to apply fonts."
ui_print "  Then open KernelSU > Modules > AppleFonts > WebUI"
ui_print "==================================="
