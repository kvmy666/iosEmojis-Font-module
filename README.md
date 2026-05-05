# Apple Fonts & Emoji — KernelSU / Magisk Module

Replace your Android system fonts and emoji with genuine Apple iOS 18.4 typefaces — systemlessly, with a live WebUI to tweak weight and toggle fonts without reflashing.

**Authors:** Abdulkarim & M

---

## What it replaces

| Android stock | iOS replacement | Notes |
|---|---|---|
| System Latin font | **SF Pro Variable** | Full weight axis (Thin → Black), patchable per-boot |
| NotoNaskhArabic-*.ttf | **SF Arabic Variable** | Full weight axis; mutually exclusive with Geeza / Cocon |
| NotoNaskhArabic-*.ttf | **Geeza Pro** | Classic iOS Arabic, static weight |
| NotoNaskhArabic-*.ttf | **Cocon Next Arabic** | Rounded modern Arabic, static weight |
| NotoColorEmoji.ttf | **Apple Color Emoji** | iOS 18.4 emoji set |

All fonts are **individually toggleable** from the WebUI. Arabic fonts are mutually exclusive (one active at a time).

---

## Requirements

- **Root manager:** KernelSU Next (recommended) or Magisk (v25+)
- **Android:** 9+ (API 28). Full variable-weight support on Android 12+ (API 31+)
- **Architecture:** arm64-v8a only
- **Free space:** 300 MB in `/data`

---

## Installation

1. Download `AppleFonts-v1.0.0.zip` from the [Releases](../../releases) page
2. Open **KernelSU** (or **Magisk**) → **Modules** → **Install from storage**
3. Select the zip → confirm → **reboot**
4. After reboot: KernelSU → Modules → **Apple Fonts & Emoji** → **Open WebUI**

---

## WebUI controls

Open the WebUI from your root manager after the first reboot.

- **SF Pro toggle** — enable / disable the iOS Latin font system-wide
- **SF Arabic toggle** — enable SF Arabic Variable for all Arabic text
- **Geeza Pro toggle** — switch Arabic rendering to Geeza Pro (classic iOS style)
- **Cocon toggle** — switch Arabic rendering to Cocon Next Arabic (modern rounded style)
- **Apple Emoji toggle** — enable / disable Apple Color Emoji
- **Weight slider + input** — set the default font weight (100 Thin → 1000 Black); applies to SF Pro and SF Arabic only (variable fonts). Geeza Pro and Cocon are static fonts — weight slider has no effect on them.
- **Apply to System** — saves settings; a reboot is required for changes to take effect
- **Reset Defaults** — restores weight 400, SF Pro + SF Arabic + Emoji on

---

## How it works

This is a **systemless overlay module** — it never modifies `/system` directly.

1. **`customize.sh`** (runs at install time): validates font files, creates filename aliases (`cp` on-device, since Android's unzip doesn't handle zip symlinks), initialises `config.json`.
2. **`post-fs-data.sh`** (runs before zygote on every boot): reads `config.json`, moves disabled fonts out of the overlay into a private store, binary-patches the OpenType `fvar` table's default weight in SF Pro and SF Arabic, writes `fonts_customization.xml` as a belt-and-suspenders fallback.
3. **`service.sh`** (runs after boot): polls for `sys.boot_completed`, writes a performance snapshot to `perf.log`, then exits — no daemons, no persistent processes.
4. **`scripts/apply.sh`** (called by WebUI): writes `config.json`; next reboot picks up the new values.

**Boot watchdog:** if the device doesn't fully boot within 90 seconds, the module touches `$MODDIR/disable` and exits — it self-disables so you always get a second boot attempt with fonts removed.

---

## Diagnostics

The WebUI **Diagnostics** section shows:
- Module status (Active / Disabled / Boot Failed)
- Current applied config (weight)
- Last boot log line
- Last `post-fs-data.sh` patch log line
- Last 5 performance log entries (tap ↺ to capture a new snapshot)

---

## Recovery

If the device fails to boot after installation:

1. Hold **Power + Volume Down** to enter recovery
2. In KernelSU / Magisk recovery → **Disable all modules**
3. Boot normally → open the manager → uninstall **Apple Fonts & Emoji**

The boot watchdog (90-second timeout) means most users recover automatically on the second boot attempt.

---

## Building from source

You need the Apple font DMG files (SF Pro and SF Arabic, downloadable from [developer.apple.com](https://developer.apple.com/fonts/)) and an Apple Color Emoji TTF.

```sh
# Prerequisites (Ubuntu / Debian)
sudo apt install p7zip-full libarchive-tools zip
pip install fonttools --break-system-packages

# Place files:
#   sources/dmg/SF-Pro.dmg
#   sources/dmg/SF-Arabic.dmg
#   sources/emoji/AppleColorEmoji.ttf
#   sources/geeza/GeezaPro.ttf        (optional)
#   sources/cocon/Cocon-Regular.ttf   (optional)

bash build.sh
# Output: output/AppleFonts-v1.0.0.zip
```

---

## Compatibility notes

- Tested on **OnePlus CPH2747** (OxygenOS V16 / Android 16)
- KernelSU Next (`com.rifsxd.ksunext`) — fully supported
- Standard Magisk — supported (no WebUI; use `action.sh` quick action instead)
- Conflicts with other font modules (MFGA, EvilFont, iOS_Emoji, Magisk-iOS-Emoji) — disable them before installing

---

## Keywords

android font module · apple font android · sf pro android · ios font android · apple emoji android · kernelsu font module · magisk font module · sf arabic android · geeza pro android · root font replacement · android emoji replacement · ios 18 font · variable font android · kernelsu module · magisk module · apple fonts root · systemless font · oneplus font mod · oxygen os font
