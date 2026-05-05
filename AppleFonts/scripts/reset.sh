#!/system/bin/sh
# Resets all font settings to defaults.
CONFIG=/data/adb/AppleFonts/config.json
mkdir -p /data/adb/AppleFonts
printf '{"wght":400,"wdth":100,"opsz":28,"latin":true,"arabic":true,"geeza":false,"cocon":false,"emoji":true}\n' > "$CONFIG"
echo "Reset to defaults. Reboot to apply."
