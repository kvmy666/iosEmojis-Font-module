# Apple Fonts & Emoji — KernelSU / Magisk Module

Replace your Android system fonts and emoji with genuine Apple iOS typefaces — systemlessly, with a live WebUI to tweak weight and toggle fonts without reflashing.

**Authors:** Abdulkarim & M

![Downloads](https://img.shields.io/github/downloads/kvmy666/apple-fonts-module/total?style=flat-square&label=Total%20Downloads&color=blue)
![Version](https://img.shields.io/github/v/release/kvmy666/apple-fonts-module?style=flat-square&label=Latest&color=green)
![Android](https://img.shields.io/badge/Android-9%2B-brightgreen?style=flat-square)

> **v1.3.0** — Emoji now works correctly on Android 16 / OxygenOS. KernelSU will notify you automatically if you have an older version installed.

---

## What it replaces

| Android stock | iOS replacement | Notes |
|---|---|---|
| System Latin font | **SF Pro Variable** | Full weight axis (Thin → Black), patchable per-boot |
| NotoColorEmoji.ttf | **Apple Color Emoji** | macOS 26 emoji set, 115 MB CBDT — overlays stock Noto |
| NotoNaskhArabic-*.ttf | **SF Arabic Variable** | Full weight axis; mutually exclusive with Geeza / Cocon |
| NotoNaskhArabic-*.ttf | **Geeza Pro** | Classic iOS Arabic, static weight |
| NotoNaskhArabic-*.ttf | **Cocon Next Arabic** | Rounded modern Arabic, static weight |

All fonts are **individually toggleable** from the WebUI. Arabic fonts are mutually exclusive (one active at a time).

---

## Requirements

- **Root manager:** KernelSU Next (recommended) or Magisk (v25+)
- **Android:** 9+ (API 28). Full variable-weight support on Android 12+ (API 31+)
- **Architecture:** arm64-v8a (tested); other architectures should work — fonts are arch-independent
- **Free space:** 200 MB in `/data`

---

## Installation

1. Download `AppleFonts-v1.3.0.zip` from the [Releases](../../releases) page
2. Open **KernelSU** (or **Magisk**) → **Modules** → **Install from storage**
3. Select the zip → confirm → **reboot**
4. After reboot: KernelSU → Modules → **Apple Fonts & Emoji** → **Open WebUI**

> **Updating:** Flash v1.3.0 over the old version. KernelSU will also show an update banner automatically if you have a previous version installed.

---

## WebUI controls

| Control | Description |
|---|---|
| **SF Pro toggle** | Enable / disable the iOS Latin font system-wide |
| **SF Arabic toggle** | Enable SF Arabic Variable for all Arabic text |
| **Geeza Pro toggle** | Switch Arabic rendering to Geeza Pro (classic iOS style) |
| **Cocon toggle** | Switch Arabic rendering to Cocon Next Arabic (modern rounded) |
| **Apple Emoji toggle** | Enable / disable Apple Color Emoji |
| **Weight slider** | Set default font weight (100 Thin → 1000 Black). Only affects variable fonts. |
| **Apply to System** | Save settings — reboot required |
| **Reset Defaults** | Restore: weight 400, SF Pro + SF Arabic + Emoji on |

---

## OEM compatibility

| Device / ROM | Latin | Emoji | Arabic | Notes |
|---|---|---|---|---|
| OnePlus / OxygenOS | ✅ | ✅ | ✅ | Primary dev device (Android 16) |
| Samsung One UI | ✅ | ✅ | ✅ | OEM aliases auto-detected at install |
| Xiaomi MIUI / HyperOS | ✅ | ✅ | ✅ | fonts.xml + customization.xml |
| Google Pixel / AOSP | ✅ | ✅ | ✅ | Clean AOSP font stack |
| Other brands | ✅ | ✅ | ✅ | OEM font names detected from system fonts.xml |

---

## How it works

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for a full walkthrough with diagrams, boot sequence, and annotated code — written as a learning guide.

Short version: KernelSU magic-mounts our font files over `/system/fonts/` before Zygote starts. `post-fs-data.sh` runs as root to patch font weights and rewrite config files. No daemons, no persistent processes.

---

## Diagnostics

```bash
adb shell sh /data/adb/modules/AppleFonts/scripts/debug.sh
adb pull /sdcard/applefonts_debug.log
```

---

## Recovery

If the device fails to boot: hold **Power + Volume Down** → KernelSU recovery → Disable all modules → boot → uninstall.

The module self-disables after 90 seconds if boot fails — most cases auto-recover on the second attempt.

---

## Building from source

You need the Apple font DMG files (SF Pro and SF Arabic, from [developer.apple.com](https://developer.apple.com/fonts/)) and an Apple Color Emoji TTF.

```sh
sudo apt install p7zip-full libarchive-tools zip
pip install fonttools --break-system-packages

# Place:  sources/dmg/SF-Pro.dmg
#         sources/dmg/SF-Arabic.dmg
#         sources/emoji/AppleColorEmoji.ttf
#         sources/geeza/GeezaPro.ttf   (optional)
#         sources/cocon/Cocon-Regular.ttf  (optional)

bash build.sh
# Output: output/AppleFonts-v1.3.0.zip
```

---

## Changelog

### v1.3.0
- **Fix:** Apple emoji now works on Android 16 / OxygenOS (and other devices)
- **Root cause:** `font_fallback.xml` (Minikin's real config) references `NotoColorEmoji.ttf` — the v1.2.0 rename to `AppleColorEmoji.ttf` was invisible to the font resolver
- Apple emoji ships as `NotoColorEmoji.ttf` (115 MB CBDT, macOS 26) — overlays the stock 2.8 MB COLRv0 Noto via magic-mount
- Removed arm64 hard block (fonts are architecture-independent)
- Added `updateJson` — KernelSU/Magisk now notifies installed users of updates automatically
- Simplified `fonts.xml` awk (emoji injection no longer needed)

### v1.2.0
- Real Apple Color Emoji (macOS 26 build, U+1FAEA distorted face present)
- APEX bypass attempt via `AppleColorEmoji.ttf` rename (superseded by v1.3.0)

### v1.1.0
- fonts.xml injection for emoji promotion
- Improved OEM alias detection

### v1.0.0
- Initial release: SF Pro Variable, SF Arabic, Geeza Pro, Cocon, Noto emoji
- WebUI with weight slider, boot watchdog (90 s self-disable)

---

## Compatibility

- Tested on **OnePlus CPH2747** (OxygenOS V16 / Android 16, KernelSU Next)
- Works with standard Magisk (no WebUI — use `action.sh` quick action instead)
- Conflicts with: MFGA, EvilFont, iOS_Emoji, Magisk-iOS-Emoji — disable them first

---

## Keywords

android font module · apple font android · sf pro android · ios font android · apple emoji android · kernelsu font module · magisk font module · sf arabic android · geeza pro android · root font replacement · android emoji replacement · ios 18 font · variable font android · kernelsu module · magisk module
