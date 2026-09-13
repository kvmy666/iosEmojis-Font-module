#!/usr/bin/env python3
"""Repair the macOS 26 Apple Color Emoji CBDT build for Android.

Fixes two regressions in the upstream ``samuelngs/apple-emoji-ttf`` Linux
build (release ``macos-26-*``):

1. Size. Upstream labels each CBDT strike's ``ppem`` as the bitmap pixel size,
   dropping Apple's ~1.168 em overshoot, so every glyph renders ~14% too small
   (upstream issue #103, "Emoji are smaller in new builds"). We scale every
   strike's ``ppem`` (and its line metrics) by 137/160, which restores the size
   of the reference iOS 18.4 build without touching any bitmap.

2. Variation selectors. The Linux build dropped the cmap format-14 (Unicode
   Variation Sequences) table. Android/Minikin's ``FontFamily::hasGlyph(cp,
   FE0F)`` reads that table, so without it our family cannot outrank the stock
   colour-emoji family for text-default emoji (heart, frown, infinity, ...).
   We rebuild a format-14 table using default UVS mappings for the 371
   standardized U+FE0F sequences.

Usage:
    python3 tools/fix_emoji.py \
        --input  sources/emoji/AppleColorEmoji.ttf \
        --output sources/emoji/AppleColorEmoji.fixed.ttf
"""

from __future__ import annotations

import argparse
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable

# The reference font (iOS 18.4 build) stores 160 px bitmaps at ppem 137.
PPEM_SCALE = 137.0 / 160.0
VS16 = 0xFE0F

# 371 base codepoints that form standardized emoji variation sequences with
# U+FE0F. Extracted from the reference Apple Color Emoji build (format-14).
VS16_BASES = [
    35, 42, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 169, 174, 8252, 8265, 8482,
    8505, 8596, 8597, 8598, 8599, 8600, 8601, 8617, 8618, 8986, 8987, 9000, 9167,
    9193, 9194, 9195, 9196, 9197, 9198, 9199, 9200, 9201, 9202, 9203, 9208, 9209,
    9210, 9410, 9642, 9643, 9654, 9664, 9723, 9724, 9725, 9726, 9728, 9729, 9730,
    9731, 9732, 9742, 9745, 9748, 9749, 9752, 9757, 9760, 9762, 9763, 9766, 9770,
    9774, 9775, 9784, 9785, 9786, 9792, 9794, 9800, 9801, 9802, 9803, 9804, 9805,
    9806, 9807, 9808, 9809, 9810, 9811, 9823, 9824, 9827, 9829, 9830, 9832, 9851,
    9854, 9855, 9874, 9875, 9876, 9877, 9878, 9879, 9881, 9883, 9884, 9888, 9889,
    9895, 9898, 9899, 9904, 9905, 9917, 9918, 9924, 9925, 9928, 9934, 9935, 9937,
    9939, 9940, 9961, 9962, 9968, 9969, 9970, 9971, 9972, 9973, 9975, 9976, 9977,
    9978, 9981, 9986, 9989, 9992, 9993, 9994, 9995, 9996, 9997, 9999, 10002,
    10004, 10006, 10013, 10017, 10024, 10035, 10036, 10052, 10055, 10060, 10062,
    10067, 10068, 10069, 10071, 10083, 10084, 10133, 10134, 10135, 10145, 10160,
    10175, 10548, 10549, 11013, 11014, 11015, 11035, 11036, 11088, 11093, 12336,
    12349, 12951, 12953, 126980, 127344, 127345, 127358, 127359, 127490, 127514,
    127535, 127543, 127757, 127758, 127759, 127765, 127772, 127777, 127780,
    127781, 127782, 127783, 127784, 127785, 127786, 127787, 127788, 127798,
    127864, 127869, 127891, 127894, 127895, 127897, 127898, 127899, 127902,
    127903, 127911, 127916, 127917, 127918, 127938, 127940, 127942, 127946,
    127947, 127948, 127949, 127950, 127956, 127957, 127958, 127959, 127960,
    127961, 127962, 127963, 127964, 127965, 127966, 127967, 127968, 127981,
    127987, 127989, 127991, 128008, 128021, 128031, 128038, 128063, 128065,
    128066, 128070, 128071, 128072, 128073, 128077, 128078, 128083, 128106,
    128125, 128163, 128176, 128179, 128187, 128191, 128203, 128218, 128223,
    128228, 128229, 128230, 128234, 128235, 128236, 128237, 128247, 128249,
    128250, 128251, 128253, 128264, 128269, 128274, 128275, 128329, 128330,
    128336, 128337, 128338, 128339, 128340, 128341, 128342, 128343, 128344,
    128345, 128346, 128347, 128348, 128349, 128350, 128351, 128352, 128353,
    128354, 128355, 128356, 128357, 128358, 128359, 128367, 128368, 128371,
    128372, 128373, 128374, 128375, 128376, 128377, 128391, 128394, 128395,
    128396, 128397, 128400, 128421, 128424, 128433, 128434, 128444, 128450,
    128451, 128452, 128465, 128466, 128467, 128476, 128477, 128478, 128481,
    128483, 128488, 128495, 128499, 128506, 128528, 128647, 128653, 128657,
    128660, 128664, 128685, 128690, 128697, 128698, 128700, 128715, 128717,
    128718, 128719, 128736, 128737, 128738, 128739, 128740, 128741, 128745,
    128752, 128755,
]


def scale_strikes(font: TTFont) -> None:
    """Scale every CBDT strike's ppem and line metrics by PPEM_SCALE."""
    if "CBLC" not in font:
        raise SystemExit("ERROR: font has no CBLC table")
    for index, strike in enumerate(font["CBLC"].strikes):
        bst = strike.bitmapSizeTable
        old_x, old_y = bst.ppemX, bst.ppemY
        bst.ppemX = max(1, round(bst.ppemX * PPEM_SCALE))
        bst.ppemY = max(1, round(bst.ppemY * PPEM_SCALE))
        for metrics in (bst.hori, bst.vert):
            if metrics is None:
                continue
            if metrics.ascender:
                metrics.ascender = round(metrics.ascender * PPEM_SCALE)
            if metrics.descender:
                metrics.descender = round(metrics.descender * PPEM_SCALE)
            if metrics.widthMax:
                metrics.widthMax = round(metrics.widthMax * PPEM_SCALE)
        print("  strike %d: ppem %dx%d -> %dx%d" % (
            index, old_x, old_y, bst.ppemX, bst.ppemY))


def add_format14(font: TTFont) -> int:
    """Add a cmap format-14 table for the standardized U+FE0F sequences."""
    cmap = font["cmap"]
    if any(sub.format == 14 for sub in cmap.tables):
        print("  format-14 already present; leaving it untouched")
        return sum(len(s) for t in cmap.tables if t.format == 14
                   for s in t.uvsDict.values())

    best = cmap.getBestCmap()
    sequences = [(cp, best[cp]) for cp in VS16_BASES if cp in best]
    missing = [cp for cp in VS16_BASES if cp not in best]

    sub = CmapSubtable.newSubtable(14)
    sub.platformID = 0
    sub.platEncID = 5
    sub.language = 0
    sub.cmap = {}  # required by the cmap table compiler (dedup step)
    # glyphName=None => default UVS mapping (use the base codepoint's glyph).
    sub.uvsDict = {VS16: [(cp, None) for cp, _ in sequences]}
    cmap.tables.append(sub)

    print("  format-14: added %d sequences (%d base codepoints missing from cmap)"
          % (len(sequences), len(missing)))
    if missing:
        print("    missing: %s" % " ".join("U+%04X" % cp for cp in missing))
    return len(sequences)


def fix_advance_width_max(font: TTFont) -> int:
    """Keep hhea.advanceWidthMax consistent with the (patched) hmtx table."""
    if "hmtx" not in font or "hhea" not in font:
        return 0
    width = max(advance for advance, _lsb in font["hmtx"].metrics.values())
    font["hhea"].advanceWidthMax = width
    return width


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="sources/emoji/AppleColorEmoji.ttf")
    parser.add_argument("--output", default="sources/emoji/AppleColorEmoji.fixed.ttf")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        raise SystemExit("ERROR: input not found: %s" % args.input)

    print("Loading %s (%.1f MB) ..." % (args.input, os.path.getsize(args.input) / 1e6))
    font = TTFont(args.input, lazy=False)

    print("Scaling CBDT strike ppem by %.4f ..." % PPEM_SCALE)
    scale_strikes(font)

    print("Rebuilding cmap format-14 ...")
    add_format14(font)

    width = fix_advance_width_max(font)
    print("hhea.advanceWidthMax -> %d" % width)

    print("Writing %s ..." % args.output)
    font.save(args.output)
    font.close()

    # ---- self validation -------------------------------------------------
    print("Validating %s ..." % args.output)
    check = TTFont(args.output, lazy=False)
    strikes = check["CBLC"].strikes
    ppems = [s.bitmapSizeTable.ppemX for s in strikes]
    f14 = [t for t in check["cmap"].tables if t.format == 14]
    count = sum(len(s) for t in f14 for s in t.uvsDict.values())
    base_cmap = check.getBestCmap()

    errors = []
    if len(strikes) != 8:
        errors.append("expected 8 strikes, got %d" % len(strikes))
    if ppems != sorted(ppems):
        errors.append("strike ppem not ascending: %s" % ppems)
    if not f14:
        errors.append("format-14 missing after write")
    if count < 300:
        errors.append("format-14 has only %d sequences" % count)
    for cp in (0x2764, 0x267E, 0x2639, 0x1F600, 0x1FAEA):
        if cp not in base_cmap:
            errors.append("base cmap lost U+%04X" % cp)

    check.close()

    if errors:
        print("VALIDATION FAILED:")
        for err in errors:
            print("  - %s" % err)
        return 1

    print("OK: strikes=%s, format-14 sequences=%d, output=%.1f MB"
          % (ppems, count, os.path.getsize(args.output) / 1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main())
