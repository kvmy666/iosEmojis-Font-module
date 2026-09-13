# PLAN — Apple Fonts & Emoji (adaptive)

If an assumption fails, edit this file before changing code.
Last updated: 2026-09-13

## Goal
Fix v1.3.0's two regressions while keeping the module bootloop-safe:
1. Emoji render at the v1.1.0 natural size (~1.168 em).
2. Text-default emoji (❤️ etc.) render Apple, not Android.
Keep iOS 26 (macOS 26) emoji, including the newer glyphs.

## Strategy
Patch the existing 115 MB macOS-26 CBDT font at build time; do not re-convert.
Primary fixes only; treat X/Snapchat EmojiCompat as a separate phase.

## Steps
1. `tools/fix_emoji.py`
   - scale every CBLC strike `ppemX/ppemY` and strike line metrics by 137/160
   - add a cmap format-14 table: selector U+FE0F, 371 default-UVS sequences
   - recompute `hhea.advanceWidthMax`
   - write `sources/emoji/AppleColorEmoji.fixed.ttf`, then reload + assert
2. `build.sh` — run the tool, ship the fixed file as `NotoColorEmoji.ttf`.
3. `AppleFonts/post-fs-data.sh` — insert the Apple emoji family at the top of
   the generated `fonts.xml` (as v1.1.0 did), pointing at `NotoColorEmoji.ttf`.
4. `AppleFonts/scripts/debug.sh` — report format-14 presence, CBLC strikes,
   `font_fallback.xml` emoji families.
5. Version bump to v1.3.1.

## Verification
- Offline: reload fixed font, check strikes/format-14/coverage; no reboot.
- Reboot 0 (now): baseline logcat + debug while reproducing the heart.
- Reboot 1: flash, verify size, system hearts, new emoji.
- Reboot 2 (conditional): EmojiCompat cache/provider fix.

## Rollback
Keep `output/AppleFonts-v1.3.0.zip`; flash it to revert. The 90 s boot watchdog
in `service.sh` is untouched.
