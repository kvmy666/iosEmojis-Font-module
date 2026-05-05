#!/system/bin/sh
# Quick action triggered from KernelSU manager.
# Safely clears font caches only — does NOT restart zygote or reboot.
# After running, reboot manually from KernelSU manager if needed.

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
echo "Manual reboot required to see font changes."
echo "==================================="
