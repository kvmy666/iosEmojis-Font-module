# MEMORY — Apple Fonts & Emoji (reverse-engineering log)

Adaptable memory file. Update whenever a finding is confirmed or disproven.
Last updated: 2026-09-13

## Device under test
- OnePlus CPH2747 (OxygenOS V16 / Android 16, API 36, arm64-v8a)
- KernelSU Next. `su` is NOT reachable from adb/Termux; all diagnostics run over
  `adb connect 192.168.100.245:6666` reading world-readable paths only.
- Module is installed and active: `/system/fonts/NotoColorEmoji.ttf` is the
  115,969,256-byte Apple font (magic-mount works).

## The two reported regressions (v1.3.0)

### Issue 1 — emoji render shrunk (~14%)
Root cause: the macOS-26 font is upstream `samuelngs/apple-emoji-ttf`
`AppleColorEmoji-Linux.ttf` (release `macos-26-20260722`). Its v2 build labels
each CBDT strike's `ppem` as the bitmap pixel size, dropping Apple's overshoot.

Measured on the two fonts:
| | v1.1.0 (iOS 18.4 ref) | v1.3.0 (macOS 26) |
|---|---|---|
| CBLC strikes | 1 @ ppem 137 | 8 @ 20/26/32/40/48/52/64/96 |
| bitmap vs ppem | 160 px / 137 = **1.168 em** | N px / N = **1.00 em** |
| artwork / ppem | ~1.09–1.17 em | ~0.94–1.00 em |
| `cmap` format-14 | 371 VS16 sequences | **missing** |
| `GSUB` | present | **missing** (only `morx`, ignored by Android) |
| `hmtx` advance | 2400 (1.171 em) | 2400 (patched 2048→2400) |

The commit message "patch hmtx 2048→2400" was treating the wrong variable: the
advance is fine, the **glyph scale** is small. Upstream issue #103
("Emoji are smaller in new builds") confirms this is a known v2 build bug.

Fix: multiply every strike `ppem` by 137/160 (metadata only, lossless), which
scales the rendered glyph back to ~1.168 em. Also scale the strike line metrics.

### Issue 2 — text-default emoji render Android (❤️ etc.)
Root cause (confirmed in AOSP source): `FontFamily::hasGlyph(cp, FE0F)` reads
the **cmap format-14** coverage. Minikin's font scoring gives:
- 3 = family supports the variation sequence (format-14)
- 2 = family is a colour-emoji family (FE0F requested)
- 1 = family only has the base char

v1.3.0's font has no format-14, so our Apple family only scores 2 and can lose to
another colour-emoji family. v1.1.0's font had format-14 (371 sequences) and won.
v1.3.0 also removed the v1.1.0 `fonts.xml` emoji-family promotion.

Fix: rebuild a format-14 table (default UVS, `glyphName=None`) for the 371
standardized U+FE0F sequences, and restore the `fonts.xml` emoji promotion.

### Issue 3 — X / Snapchat show Google emoji (app-level, separate)
Not a system-font problem. Both apps use EmojiCompat with Google's downloadable
`NotoColorEmojiCompat`:
- X: `androidx.emoji` + `FontRequestEmojiCompatConfig` + `EmojiCompatInitializer`
- Snapchat: `EmojiCompat` + `com.google.android.gms.fonts`
Neither bundles a colour emoji font (Snapchat's 20 bundled fonts are text fonts).
The module already disables the GMS FontsProvider, but a cached font persists.
Fixing this needs a separate, more invasive step (clear GMS/app font cache).
Status: deferred until the primary fix is verified.

## Key file locations
- `sources/emoji/AppleColorEmoji.ttf` — macOS-26 input (115 MB, gitignored)
- `AppleColorEmoji.ttf` (repo root) — iOS 18.4 reference with format-14 (43 MB)
- `tools/fix_emoji.py` — builds `sources/emoji/AppleColorEmoji.fixed.ttf`
- `AppleFonts/post-fs-data.sh` — runtime font/XML logic
- `AppleFonts/scripts/debug.sh` — on-device diagnostics

## Lessons / traps
- Do not trust the `hmtx`-advance theory; size is driven by CBDT ppem vs bitmap.
- `fonts.xml` is deprecated; `font_fallback.xml` is root-only on this device.
- Minikin merges defaultUVS + nonDefaultUVS into VS coverage, so default (None)
  mappings are sufficient.
- Security: `.git/config` remote URLs embed a live GitHub token — rotate it.
