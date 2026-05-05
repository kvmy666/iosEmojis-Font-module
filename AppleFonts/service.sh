#!/system/bin/sh
# Runs after magic mount. Waits for full boot, cleans up font overrides that
# would shadow our overlay, takes one perf snapshot, then exits permanently.
# No daemon. No loop. No persistent process.

MODDIR=${0%/*}
LOG=$MODDIR/boot.log
PERFLOG=/data/adb/AppleFonts/perf.log

log() { printf '%s: %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$1" >> "$LOG"; }

log "service.sh started"

# Wait for full boot (up to 90 seconds), auto-disable on timeout
ELAPSED=0
while [ "$ELAPSED" -lt 90 ]; do
  if [ "$(getprop sys.boot_completed 2>/dev/null)" = "1" ]; then
    break
  fi
  sleep 1
  ELAPSED=$((ELAPSED + 1))
done

if [ "$(getprop sys.boot_completed 2>/dev/null)" != "1" ]; then
  log "BOOT TIMEOUT after 90s — auto-disabling module"
  touch "$MODDIR/disable"
  exit 1
fi

log "Boot completed at ${ELAPSED}s"

# Wait for /sdcard to be ready (GMS font provider may not be ready otherwise)
SDCARD_WAIT=0
while [ ! -d /sdcard ] && [ "$SDCARD_WAIT" -lt 30 ]; do
  sleep 1
  SDCARD_WAIT=$((SDCARD_WAIT + 1))
done

# ── Critical: remove /data/fonts ───────────────────────────────────────────
# Android 12+ downloads GMS font packs here. They shadow our system/fonts
# overlay and override our custom fonts. Must delete on every boot.
if [ -d /data/fonts ]; then
  rm -rf /data/fonts
  log "Removed /data/fonts (GMS font cache cleared)"
else
  log "/data/fonts not present — nothing to clear"
fi

# ── Disable GMS font provider for all users ─────────────────────────────────
PM="$(command -v pm)"
GMSF_BASE="com.google.android.gms/com.google.android.gms.fonts"

for UP in $(ls -d /data/user/* 2>/dev/null); do
  USER_ID="${UP##*/}"
  "$PM" disable --user "$USER_ID" "${GMSF_BASE}.update.UpdateSchedulerService" >>"$LOG" 2>&1 || true
  "$PM" disable --user "$USER_ID" "${GMSF_BASE}.provider.FontsProvider" >>"$LOG" 2>&1 || true
done
log "GMS font services disabled"

# ── Single perf snapshot then exit ─────────────────────────────────────────
sleep 30   # let system stabilise
MEM_AVAIL=$(grep '^MemAvailable' /proc/meminfo 2>/dev/null | awk '{print $2}')
MEM_TOTAL=$(grep '^MemTotal'     /proc/meminfo 2>/dev/null | awk '{print $2}')
LOAD=$(uptime 2>/dev/null | awk -F'load average:' '{print $2}' | tr -d ' ')
mkdir -p /data/adb/AppleFonts
printf '%s|post_boot|MemAvail=%skB|MemTotal=%skB|Load=%s\n' \
  "$(date '+%Y-%m-%d %H:%M:%S')" \
  "$MEM_AVAIL" "$MEM_TOTAL" "$LOAD" >> "$PERFLOG"

log "Perf snapshot written. Exiting."
exit 0
