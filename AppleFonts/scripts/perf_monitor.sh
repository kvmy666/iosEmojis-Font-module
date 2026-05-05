#!/system/bin/sh
# On-demand perf snapshot called from WebUI Diagnostics tab.
PERFLOG=/data/adb/AppleFonts/perf.log
mkdir -p /data/adb/AppleFonts

MEM_AVAIL=$(grep '^MemAvailable' /proc/meminfo 2>/dev/null | awk '{print $2}')
MEM_TOTAL=$(grep '^MemTotal'     /proc/meminfo 2>/dev/null | awk '{print $2}')
LOAD=$(uptime 2>/dev/null | awk -F'load average:' '{print $2}' | tr -d ' ')
CPU_SS=$(top -n 1 -b 2>/dev/null | grep -i 'system_server' | head -1 | awk '{print "system_server cpu="$9"%"}')
CPU_SF=$(top -n 1 -b 2>/dev/null | grep -i 'surfaceflinger' | head -1 | awk '{print "surfaceflinger cpu="$9"%"}')

printf '%s|on_demand|MemAvail=%skB|MemTotal=%skB|Load=%s|%s|%s\n' \
  "$(date '+%Y-%m-%d %H:%M:%S')" \
  "$MEM_AVAIL" "$MEM_TOTAL" "$LOAD" "$CPU_SS" "$CPU_SF" \
  >> "$PERFLOG"

echo "=== Last 10 perf entries ==="
tail -10 "$PERFLOG"
