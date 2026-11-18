#!/usr/bin/env python3
"""Validate every relative href and in-page anchor in the generated HTML preview."""
import os, re, sys, glob
SITE = os.path.abspath(sys.argv[1])
HREF = re.compile(r'href="([^"]+)"')
IDS  = re.compile(r'<h[1-6][^>]*\sid="([^"]+)"')

files = glob.glob(os.path.join(SITE, "**", "*.html"), recursive=True)
ids_cache = {}
def ids(p):
    if p not in ids_cache:
        try: ids_cache[p] = set(IDS.findall(open(p, encoding="utf-8").read()))
        except Exception: ids_cache[p] = set()
    return ids_cache[p]

bad, rel, ext, anch = [], 0, 0, 0
for f in files:
    txt = open(f, encoding="utf-8").read()
    for h in HREF.findall(txt):
        if h.startswith(("http://", "https://", "mailto:")):
            ext += 1; continue
        if h.startswith("#"):
            anch += 1
            if h[1:] not in ids(f):
                bad.append(f"{os.path.relpath(f,SITE)}: missing in-page anchor {h}")
            continue
        rel += 1
        path, _, a = h.partition("#")
        tgt = os.path.normpath(os.path.join(os.path.dirname(f), path))
        if not (os.path.isfile(tgt) or os.path.isdir(tgt)):
            bad.append(f"{os.path.relpath(f,SITE)}: broken -> {h}"); continue
        if a and tgt.endswith(".html"):
            anch += 1
            if a not in ids(tgt):
                bad.append(f"{os.path.relpath(f,SITE)}: missing anchor -> {h}")
print(f"html pages:        {len(files)}")
print(f"relative hrefs:    {rel}")
print(f"anchor targets:    {anch}")
print(f"external hrefs:    {ext} (not fetched)")
print(f"problems:          {len(bad)}")
for b in bad[:25]: print("  !", b)
if len(bad) > 25: print(f"  ... {len(bad)-25} more")
sys.exit(1 if bad else 0)
