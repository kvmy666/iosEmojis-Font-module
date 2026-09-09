#!/system/bin/sh
# Runs before zygote. Reads config, handles font toggles, patches fvar default
# weight directly in the font binary (guaranteed to work regardless of whether
# OxygenOS supports fonts_customization.xml), then writes fonts_customization.xml
# as a belt-and-suspenders fallback. No daemon.

MODDIR=${0%/*}
CONFIG=/data/adb/AppleFonts/config.json
LOG=/data/adb/AppleFonts/post-fs.log
ACTIVE_XML=$MODDIR/system/etc/fonts_customization.xml
FONTS=$MODDIR/system/fonts
STORE=$MODDIR/fonts_store

mkdir -p /data/adb/AppleFonts
: > "$LOG"

log() { printf '%s %s\n' "$(date '+%H:%M:%S')" "$1" >> "$LOG"; }
log "post-fs-data.sh started (MODDIR=$MODDIR)"

# ── Read config ──────────────────────────────────────────────────────────────
WGHT=400; LATIN=true; ARABIC=true; GEEZA=false; COCON=false; EMOJI=true
if [ -f "$CONFIG" ]; then
  _W=$(grep -o '"wght":[0-9]*'   "$CONFIG" | grep -o '[0-9]*$')
  _L=$(grep -o '"latin":[a-z]*'  "$CONFIG" | grep -o '[a-z]*$')
  _A=$(grep -o '"arabic":[a-z]*' "$CONFIG" | grep -o '[a-z]*$')
  _G=$(grep -o '"geeza":[a-z]*'  "$CONFIG" | grep -o '[a-z]*$')
  _C=$(grep -o '"cocon":[a-z]*'  "$CONFIG" | grep -o '[a-z]*$')
  _E=$(grep -o '"emoji":[a-z]*'  "$CONFIG" | grep -o '[a-z]*$')
  [ -n "$_W" ] && WGHT=$_W
  [ -n "$_L" ] && LATIN=$_L
  [ -n "$_A" ] && ARABIC=$_A
  [ -n "$_G" ] && GEEZA=$_G
  [ -n "$_C" ] && COCON=$_C
  [ -n "$_E" ] && EMOJI=$_E
fi
WGHT=$(printf '%s' "$WGHT" | tr -cd '0-9'); [ -z "$WGHT" ] && WGHT=400
[ "$WGHT" -lt 100  ] && WGHT=100
[ "$WGHT" -gt 1000 ] && WGHT=1000
log "config: wght=$WGHT latin=$LATIN arabic=$ARABIC geeza=$GEEZA cocon=$COCON emoji=$EMOJI"

mkdir -p "$STORE"

# ── Latin font toggle (SF Pro + any OEM aliases created at install time) ─────
ALIAS_LIST="$MODDIR/fonts_aliases.txt"
if [ "$LATIN" = "false" ]; then
  [ -f "$FONTS/SysFont-Regular.ttf" ] && mv "$FONTS/SysFont-Regular.ttf" "$STORE/"
  [ -f "$FONTS/Roboto-Regular.ttf"  ] && mv "$FONTS/Roboto-Regular.ttf"  "$STORE/"
  if [ -f "$ALIAS_LIST" ]; then
    while IFS= read -r _AF; do
      [ -n "$_AF" ] && [ -f "$FONTS/$_AF" ] && mv "$FONTS/$_AF" "$STORE/"
    done < "$ALIAS_LIST"
  fi
  log "Latin: SF Pro + OEM aliases moved to store (disabled)"
else
  [ -f "$STORE/SysFont-Regular.ttf" ] && mv "$STORE/SysFont-Regular.ttf" "$FONTS/"
  [ -f "$STORE/Roboto-Regular.ttf"  ] && mv "$STORE/Roboto-Regular.ttf"  "$FONTS/"
  if [ -f "$ALIAS_LIST" ]; then
    while IFS= read -r _AF; do
      [ -n "$_AF" ] && [ -f "$STORE/$_AF" ] && mv "$STORE/$_AF" "$FONTS/"
    done < "$ALIAS_LIST"
  fi
fi

# ── Arabic font toggle (SF Arabic | Geeza Pro | Cocon — mutually exclusive) ───
# Priority when multiple are set: ARABIC > GEEZA > COCON (UI enforces mutual exclusion)
_arabic_restore_all() {
  [ -f "$STORE/SF-Arabic.ttf"    ] && mv "$STORE/SF-Arabic.ttf"    "$FONTS/"
  [ -f "$STORE/GeezaPro.ttf"     ] && mv "$STORE/GeezaPro.ttf"     "$FONTS/"
  [ -f "$STORE/Cocon-Regular.ttf"] && mv "$STORE/Cocon-Regular.ttf" "$FONTS/"
  for f in "$STORE"/NotoNaskhArabic*.ttf; do [ -f "$f" ] && mv "$f" "$FONTS/"; done
}

if [ "$ARABIC" = "true" ]; then
  _arabic_restore_all
  log "Arabic: SF Arabic active"
elif [ "$GEEZA" = "true" ] && [ -f "$FONTS/GeezaPro.ttf" ]; then
  _arabic_restore_all
  log "Arabic: Geeza Pro active"
elif [ "$GEEZA" = "true" ] && [ -f "$STORE/GeezaPro.ttf" ]; then
  _arabic_restore_all
  log "Arabic: Geeza Pro active"
elif [ "$COCON" = "true" ] && [ -f "$FONTS/Cocon-Regular.ttf" ]; then
  _arabic_restore_all
  log "Arabic: Cocon active"
elif [ "$COCON" = "true" ] && [ -f "$STORE/Cocon-Regular.ttf" ]; then
  _arabic_restore_all
  log "Arabic: Cocon active"
else
  [ -f "$FONTS/SF-Arabic.ttf"     ] && mv "$FONTS/SF-Arabic.ttf"     "$STORE/"
  [ -f "$FONTS/GeezaPro.ttf"      ] && mv "$FONTS/GeezaPro.ttf"      "$STORE/"
  [ -f "$FONTS/Cocon-Regular.ttf" ] && mv "$FONTS/Cocon-Regular.ttf" "$STORE/"
  for f in "$FONTS"/NotoNaskhArabic*.ttf; do [ -f "$f" ] && mv "$f" "$STORE/"; done
  log "Arabic: all moved to store (disabled)"
fi

# ── Emoji toggle ──────────────────────────────────────────────────────────────
# Apple emoji ships as NotoColorEmoji.ttf — Android's font_fallback.xml references
# this name directly. The stock system NotoColorEmoji is a 2.8 MB COLRv0 file;
# our 115 MB CBDT Apple emoji overlays it via KernelSU magic-mount.
if [ "$EMOJI" = "false" ]; then
  [ -f "$FONTS/NotoColorEmoji.ttf" ] && mv "$FONTS/NotoColorEmoji.ttf" "$STORE/"
  log "Emoji: NotoColorEmoji.ttf moved to store (disabled)"
else
  [ -f "$STORE/NotoColorEmoji.ttf" ] && mv "$STORE/NotoColorEmoji.ttf" "$FONTS/"
fi

# ── Patch fonts.xml: universal OEM compatibility ──────────────────────────────
# Replaces <family name="sans-serif"> with SF Pro for Samsung/Xiaomi/OEM support.
# Emoji no longer needs injection here: the module overlays NotoColorEmoji.ttf
# (Apple CBDT) directly, so font_fallback.xml picks up Apple emoji via the same
# filename it already references.
MOD_XML="$MODDIR/system/etc/fonts.xml"
if [ -f /system/etc/fonts.xml ] && [ "$LATIN" != "false" ]; then
  awk -v do_latin="$LATIN" -v wght="$WGHT" '
    { lines[NR] = $0 }
    END {
      ss = 0; se = 0
      for (i = 1; i <= NR; i++) {
        if (!ss && lines[i] ~ /name="sans-serif"/) {
          for (j = i; j >= (i > 3 ? i-3 : 1); j--)
            if (lines[j] ~ /<family/) { ss = j; break }
          for (k = i; k <= NR; k++)
            if (lines[k] ~ /<\/family>/) { se = k; break }
        }
      }

      w[1]=100; w[2]=200; w[3]=300; w[4]=400
      w[5]=500; w[6]=600; w[7]=700; w[8]=800; w[9]=900
      sf = "  <family name=\"sans-serif\">\n"
      for (n = 1; n <= 9; n++) {
        wv = (w[n] == 400) ? wght : w[n]
        sf = sf "    <font weight=\"" w[n] "\" style=\"normal\">SysFont-Regular.ttf"
        sf = sf "<axis tag=\"wght\" stylevalue=\"" wv "\"/>"
        sf = sf "<axis tag=\"wdth\" stylevalue=\"100\"/>"
        sf = sf "<axis tag=\"opsz\" stylevalue=\"28\"/></font>\n"
      }
      sf = sf "  </family>"

      skip_ss = (do_latin != "false" && ss > 0 && se > 0)

      for (i = 1; i <= NR; i++) {
        if (skip_ss && i >= ss && i <= se) {
          if (i == ss) printf "%s\n", sf
          continue
        }
        print lines[i]
      }
    }
  ' /system/etc/fonts.xml > "$MOD_XML"
  if [ -s "$MOD_XML" ]; then
    log "fonts.xml overlay: sans-serif→SFPro(latin=$LATIN,wght=$WGHT) emoji=NotoColorEmoji.ttf(overlay) [$(wc -l < "$MOD_XML")L]"
  else
    rm -f "$MOD_XML"
    log "fonts.xml overlay: awk produced empty output — discarded"
  fi
else
  rm -f "$MOD_XML"
  log "fonts.xml: no overlay needed (latin=$LATIN)"
fi

# ── fvar binary patching ──────────────────────────────────────────────────────
# Only SF Pro (Latin) and SF Arabic support variable weight — both have fvar tables.
# Geeza Pro and Cocon are static fonts; their NotoNaskhArabic-* copies are made as-is.

# Read N bytes from FILE at OFFSET, return as hex string (no spaces)
_rbytes() { dd if="$1" bs=1 skip="$2" count="$3" 2>/dev/null | od -An -tx1 | tr -d ' \n'; }

# Hex string → decimal (handles up to 8 hex digits)
_hex2dec() { printf '%d' "0x${1:-0}"; }

# Write 4 bytes (Fixed 16.16) encoding INTEGER value into FONT at OFFSET
_write_fixed16() {
  local FONT="$1" OFFSET="$2" VAL="$3"
  local B3=$(( VAL / 256 )) B2=$(( VAL % 256 ))
  printf '%b' \
    "$(printf '\\x%02x' "$B3")$(printf '\\x%02x' "$B2")\\x00\\x00" | \
    dd of="$FONT" bs=1 seek="$OFFSET" count=4 conv=notrunc 2>/dev/null
}

patch_fvar_default() {
  local FONT="$1" AXIS_TAG_HEX="$2" NEW_VAL="$3"
  [ -f "$FONT" ] || { log "  $FONT not found"; return 1; }

  local N
  N=$(_hex2dec "$(_rbytes "$FONT" 4 2)")

  local FVAR_OFF=-1 i=0
  while [ "$i" -lt "$N" ]; do
    local BASE=$((12 + i * 16))
    if [ "$(_rbytes "$FONT" "$BASE" 4)" = "66766172" ]; then
      FVAR_OFF=$(_hex2dec "$(_rbytes "$FONT" $((BASE + 8)) 4)")
      break
    fi
    i=$((i + 1))
  done

  if [ "$FVAR_OFF" -lt 0 ]; then
    log "  $FONT: no fvar table (static font, skipping weight patch)"
    return 1
  fi
  log "  fvar table at offset $FVAR_OFF"

  local AOFF ACOUNT ASIZE
  AOFF=$(_hex2dec   "$(_rbytes "$FONT" $((FVAR_OFF + 4))  2)")
  ACOUNT=$(_hex2dec "$(_rbytes "$FONT" $((FVAR_OFF + 8))  2)")
  ASIZE=$(_hex2dec  "$(_rbytes "$FONT" $((FVAR_OFF + 10)) 2)")
  [ "$ASIZE" -lt 18 ] && ASIZE=20

  local AXES_START=$((FVAR_OFF + AOFF))
  local j=0
  while [ "$j" -lt "$ACOUNT" ]; do
    local AB=$((AXES_START + j * ASIZE))
    local TAG
    TAG=$(_rbytes "$FONT" "$AB" 4)
    if [ "$TAG" = "$AXIS_TAG_HEX" ]; then
      local DEF_OFF=$((AB + 8))
      local CUR_HEX
      CUR_HEX=$(_rbytes "$FONT" "$DEF_OFF" 4)
      log "  axis $AXIS_TAG_HEX found at $AB, defaultValue=$CUR_HEX → patching to $NEW_VAL"
      _write_fixed16 "$FONT" "$DEF_OFF" "$NEW_VAL"
      local NEW_HEX
      NEW_HEX=$(_rbytes "$FONT" "$DEF_OFF" 4)
      log "  verify: defaultValue now = $NEW_HEX"
      return 0
    fi
    j=$((j + 1))
  done

  log "  axis $AXIS_TAG_HEX not found in $FONT"
  return 1
}

WGHT_HEX="77676874"  # "wght" in ASCII hex

# ── Patch SF Pro (Latin) ──────────────────────────────────────────────────────
if [ "$LATIN" != "false" ] && [ -f "$FONTS/SysFont-Regular.ttf" ]; then
  PRISTINE_LA="$MODDIR/SysFont-Regular.pristine.ttf"
  if [ ! -f "$PRISTINE_LA" ]; then
    cp "$FONTS/SysFont-Regular.ttf" "$PRISTINE_LA"
    log "Created pristine backup: SysFont-Regular.ttf"
  fi
  cp "$PRISTINE_LA" "$FONTS/SysFont-Regular.ttf"
  log "Patching SysFont-Regular.ttf wght default → $WGHT"
  patch_fvar_default "$FONTS/SysFont-Regular.ttf" "$WGHT_HEX" "$WGHT"
  [ -f "$FONTS/Roboto-Regular.ttf" ] && cp "$FONTS/SysFont-Regular.ttf" "$FONTS/Roboto-Regular.ttf"
  # Propagate patched binary to any OEM alias files (Samsung, Xiaomi, etc.)
  if [ -f "$ALIAS_LIST" ]; then
    while IFS= read -r _AF; do
      [ -n "$_AF" ] && [ -f "$FONTS/$_AF" ] && cp "$FONTS/SysFont-Regular.ttf" "$FONTS/$_AF"
    done < "$ALIAS_LIST"
    log "OEM aliases weight-patched from fonts_aliases.txt"
  fi
fi

# ── Patch / apply Arabic font to NotoNaskhArabic-* alias slots ────────────────
if [ "$ARABIC" = "true" ] && [ -f "$FONTS/SF-Arabic.ttf" ]; then
  # SF Arabic: variable — patch fvar then propagate
  PRISTINE_AR="$MODDIR/SF-Arabic.pristine.ttf"
  if [ ! -f "$PRISTINE_AR" ]; then
    cp "$FONTS/SF-Arabic.ttf" "$PRISTINE_AR"
    log "Created pristine backup: SF-Arabic.ttf"
  fi
  cp "$PRISTINE_AR" "$FONTS/SF-Arabic.ttf"
  log "Patching SF-Arabic.ttf wght default → $WGHT"
  patch_fvar_default "$FONTS/SF-Arabic.ttf" "$WGHT_HEX" "$WGHT"
  for f in "$FONTS"/NotoNaskhArabic*.ttf; do
    [ -f "$f" ] && cp "$FONTS/SF-Arabic.ttf" "$f"
  done

elif [ "$GEEZA" = "true" ] && [ -f "$FONTS/GeezaPro.ttf" ]; then
  # Geeza Pro: static — copy directly to alias slots (no fvar patch)
  log "Applying Geeza Pro to Arabic alias slots (static font)"
  for f in "$FONTS"/NotoNaskhArabic*.ttf; do
    [ -f "$f" ] && cp "$FONTS/GeezaPro.ttf" "$f"
  done

elif [ "$COCON" = "true" ] && [ -f "$FONTS/Cocon-Regular.ttf" ]; then
  # Cocon Next Arabic: static — copy directly to alias slots (no fvar patch)
  log "Applying Cocon to Arabic alias slots (static font)"
  for f in "$FONTS"/NotoNaskhArabic*.ttf; do
    [ -f "$f" ] && cp "$FONTS/Cocon-Regular.ttf" "$f"
  done
fi

# ── fonts_customization.xml (belt-and-suspenders) ─────────────────────────────
mkdir -p "$MODDIR/system/etc"
{
  printf '<?xml version="1.0" encoding="utf-8"?>\n'
  printf '<fonts-modification version="1">\n\n'
  if [ "$LATIN" != "false" ]; then
    cat << LATINEOF
  <family customizationType="new-named-family" name="sans-serif">
    <font weight="100" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="100"/></font>
    <font weight="200" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="200"/></font>
    <font weight="300" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="300"/></font>
    <font weight="400" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="$WGHT"/></font>
    <font weight="500" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="500"/></font>
    <font weight="600" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="600"/></font>
    <font weight="700" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="700"/></font>
    <font weight="800" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="800"/></font>
    <font weight="900" style="normal">SysFont-Regular.ttf<axis tag="wght" stylevalue="900"/></font>
  </family>
LATINEOF
  fi
  if [ "$ARABIC" = "true" ]; then
    cat << ARABICEOF
  <family customizationType="new-named-family" lang="und-Arab">
    <font weight="100" style="normal">SF-Arabic.ttf<axis tag="wght" stylevalue="100"/></font>
    <font weight="300" style="normal">SF-Arabic.ttf<axis tag="wght" stylevalue="300"/></font>
    <font weight="400" style="normal">SF-Arabic.ttf<axis tag="wght" stylevalue="$WGHT"/></font>
    <font weight="500" style="normal">SF-Arabic.ttf<axis tag="wght" stylevalue="500"/></font>
    <font weight="700" style="normal">SF-Arabic.ttf<axis tag="wght" stylevalue="700"/></font>
    <font weight="900" style="normal">SF-Arabic.ttf<axis tag="wght" stylevalue="900"/></font>
  </family>
ARABICEOF
  elif [ "$GEEZA" = "true" ] || [ "$COCON" = "true" ]; then
    cat << STATICEOF
  <family customizationType="new-named-family" lang="und-Arab">
    <font weight="400" style="normal">NotoNaskhArabic-Regular.ttf</font>
  </family>
STATICEOF
  fi
  printf '\n</fonts-modification>\n'
} > "$ACTIVE_XML"
log "fonts_customization.xml written"

log "post-fs-data.sh done"
exit 0
