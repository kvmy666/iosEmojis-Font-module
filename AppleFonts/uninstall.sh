#!/system/bin/sh
# Runs when the user uninstalls the module from KernelSU manager.
rm -rf /data/adb/AppleFonts
rm -rf /data/system/font_* 2>/dev/null || true
