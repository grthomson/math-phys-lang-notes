#!/usr/bin/env python3
"""
Minimal Obsidian vault checks:
- ERROR on duplicate note stems (e.g. two files both named 'logic.md').
- WARNING on orphan notes (no inbound or outbound [[wikilinks]]).
- Does NOT fail on orphans.

Usage: run from repo root. CI runs this on every push/PR.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MD_FILES = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
IGNORE_FILES = {"README.md"}  # add more here if needed

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")  # [[Note]] or [[Note#Heading]]

# 1) Index notes by stem (case-insensitive)
by_stem = {}
for p in MD_FILES:
    if p.name in IGNORE_FILES:
        continue
    by_stem.setdefault(p.stem.lower(), []).append(p)

# 2) Detect duplicates (same stem appears >1 time)
duplicates = {stem: paths for stem, paths in by_stem.items() if len(paths) > 1}

# 3) Build graph of references via [[wikilinks]]
refs_out = {p: set() for p in MD_FILES if p.name not in IGNORE_FILES}
refs_in = {p: set() for p in MD_FILES if p.name not in IGNORE_FILES}

# helper to resolve a stem to the unique file path (if unique)
def resolve_stem(stem: str):
    opts = by_stem.get(stem.lower(), [])
    return opts[0] if len(opts) == 1 else None

for p in refs_out.keys():
    text = p.read_text(encoding="utf-8", errors="ignore")
    for m in WIKILINK_RE.finditer(text):
        target = m.group(1)
        stem = target.split("#", 1)[0].strip()
        if not stem:
            continue
        dest = resolve_stem(stem)
        if dest:
            refs_out[p].add(dest)
            refs_in[dest].add(p)

# 4) Orphans: no inbound and no outbound refs
orphans = sorted(
    p for p in refs_out.keys()
    if len(refs_out[p]) == 0 and len(refs_in[p]) == 0
)

# --------- Report ---------
had_error = False

if duplicates:
    had_error = True
    print("❌ Duplicate note stems detected:")
    for stem, paths in duplicates.items():
        print(f"  • '{stem}':")
        for path in paths:
            print(f"     - {path.relative_to(ROOT)}")

if orphans:
    print("\n⚠️  Orphan notes (warning only):")
    for p in orphans:
        print(f"  - {p.relative_to(ROOT)}")

if not duplicates and not orphans:
    print("✅ No duplicates found; no orphans detected.")

# exit non-zero only on duplicates
sys.exit(1 if had_error else 0)
