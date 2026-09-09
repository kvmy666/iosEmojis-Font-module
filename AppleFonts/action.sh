#!/system/bin/sh
# Quick action triggered from KernelSU manager.
# Clears font caches AND runs the diagnostic script.
# After running, pull the debug log:  adb pull /data/adb/AppleFonts/debug.log

MODDIR=${0%/*}

echo ""
echo "=== Apple Fonts — Quick Action ==="
echo ""

# Clear the GMS font download cache (/data/fonts overrides our overlay)
if [ -d /data/fonts ]; then
  rm -rf /data/fonts
  echo "OK  Cleared /data/fonts (GMS font cache)"
else
  echo "--  /data/fonts not present"
fi

# Clear font typeface disk cache (Skia/HarfBuzz cache)
COUNT=0
for f in /data/system/font_*.dat /data/system/font_*.log; do
  [ -f "$f" ] || continue
  rm -f "$f" && COUNT=$((COUNT + 1))
done
echo "OK  Cleared $COUNT typeface cache entries"

echo ""
echo "--- Running diagnostics ---"
sh "$MODDIR/scripts/debug.sh" 2>/dev/null | tail -40

# Copy log to sdcard so it can be pulled without root
if [ -f /data/adb/AppleFonts/debug.log ]; then
  cp /data/adb/AppleFonts/debug.log /sdcard/applefonts_debug.log 2>/dev/null && \
    echo "Log copied → /sdcard/applefonts_debug.log" || \
    echo "sdcard copy failed — pull from /data/adb/AppleFonts/debug.log with root"
fi
echo ""
echo "Manual reboot required to see font changes."
echo "==================================="
