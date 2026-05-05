#!/system/bin/sh
# Called from WebUI via ksu.exec.
# Args: $1=wght $2=wdth $3=opsz $4=latin $5=arabic $6=geeza $7=cocon $8=emoji
WGHT=${1:-400}
WDTH=${2:-100}
OPSZ=${3:-28}
LATIN=${4:-true}
ARABIC=${5:-true}
GEEZA=${6:-false}
COCON=${7:-false}
EMOJI=${8:-true}

# Clamp axis values
[ "$WGHT" -lt 100  ] 2>/dev/null && WGHT=100
[ "$WGHT" -gt 1000 ] 2>/dev/null && WGHT=1000
[ "$WDTH" -lt 30   ] 2>/dev/null && WDTH=30
[ "$WDTH" -gt 150  ] 2>/dev/null && WDTH=150
[ "$OPSZ" -lt 17   ] 2>/dev/null && OPSZ=17
[ "$OPSZ" -gt 28   ] 2>/dev/null && OPSZ=28

# Sanitize toggle values — only accept "true" or "false"
case "$LATIN"  in true|false) ;; *) LATIN=true  ;; esac
case "$ARABIC" in true|false) ;; *) ARABIC=true ;; esac
case "$GEEZA"  in true|false) ;; *) GEEZA=false ;; esac
case "$COCON"  in true|false) ;; *) COCON=false ;; esac
case "$EMOJI"  in true|false) ;; *) EMOJI=true  ;; esac

CONFIG=/data/adb/AppleFonts/config.json
mkdir -p /data/adb/AppleFonts
printf '{"wght":%s,"wdth":%s,"opsz":%s,"latin":%s,"arabic":%s,"geeza":%s,"cocon":%s,"emoji":%s}\n' \
  "$WGHT" "$WDTH" "$OPSZ" "$LATIN" "$ARABIC" "$GEEZA" "$COCON" "$EMOJI" > "$CONFIG"
echo "Saved: wght=$WGHT latin=$LATIN arabic=$ARABIC geeza=$GEEZA cocon=$COCON emoji=$EMOJI — Reboot to apply."
