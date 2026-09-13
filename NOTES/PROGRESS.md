# PROGRESS — Apple Fonts & Emoji

Adaptable status board. Move items between sections as facts change.
Last updated: 2026-09-13

## Done
- [x] Static diff v1.1.0 vs v1.3.0 (fonts, scripts, build).
- [x] Confirmed root cause of Issue 1 (CBDT ppem/bitmap = 1.00 em vs 1.168 em).
- [x] Confirmed root cause of Issue 2 (missing cmap format-14 + removed
      `fonts.xml` emoji promotion) against AOSP Minikin source.
- [x] Confirmed on-device via adb: active font was the 115 MB Apple font, 8
      strikes, no format-14; no `NotoColorEmojiLegacy.ttf`.
- [x] Identified Issue 3 (X/Snapchat EmojiCompat/Google font) as app-level.
- [x] Web search: no better prebuilt iOS 26 font exists.
- [x] Created `NOTES/` tracking files.
- [x] `tools/fix_emoji.py` written + validated:
      strikes 17/22/27/34/41/45/55/82, format-14 371 seqs, bitmaps byte-identical.
- [x] `build.sh` integrated; final-report text corrected.
- [x] `post-fs-data.sh` emoji promotion restored; awk validated against the real
      device `fonts.xml` (valid XML, emoji family first, sans-serif replaced).
- [x] `debug.sh` extended (format-14 shell parser + python strikes/format-14 +
      `font_fallback.xml` dump); shell parser tested locally on both fonts.
- [x] Version bumped to v1.3.1 (module.prop, update.json, README).
- [x] `output/AppleFonts-v1.3.1.zip` built, verified, pushed to
      `/sdcard/Download/`.
- [x] **User flashed v1.3.1 and reports size + the emoji conflict fixed.**

## Not verified automatically
- adb dropped off Wi-Fi (`No route to host`) right after the user's test, so the
  post-reboot `debug.sh`/logcat capture was not collected. Offline validation of
  the built font already confirmed strikes `[17,22,27,34,41,45,55,82]` and
  format-14 with 371 sequences.

## TODO
- [ ] (Optional) Reconnect adb and run `debug.sh` for a clean post-reboot record.
- [ ] (Optional, app-level) EmojiCompat fix for X/Snapchat — needs clearing the
      GMS `FontsProvider` cache and/or shipping a compat font.

## Reboot budget
Used: 1 / target max 2.

## Open questions
- Does the EmojiCompat 20% in Snapchat clear after disabling the GMS provider
  and clearing its cached font? (only relevant if the user wants X/Snapchat fixed)
