#!/usr/bin/env python3
"""Validate every relative markdown link and in-page anchor across the repository."""
import os, re, sys, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
HEAD = re.compile(r'^(#{1,6})\s+(.*?)\s*$', re.M)

def slug(s):
    """Same algorithm as build.py's slug(): emulate github-slugger."""
    s = s.strip().lower()
    s = re.sub(r'[^\w\s-]', '', s)
    return s.replace(' ', '-')

def anchors(path):
    try: txt = open(path, encoding='utf-8').read()
    except Exception: return set()
    return {slug(m.group(2)) for m in HEAD.finditer(txt)}

# narrative/ is deliberately excluded: those files are templates whose relative links are
# written for their OUTPUT location (docs/), so they do not resolve from narrative/ itself.
# The generated pages are what get checked.
files = []
for pat in ('*.md', 'docs/*.md', 'docs/projects/*.md', 'sources/**/*.md'):
    files += glob.glob(os.path.join(ROOT, pat), recursive=True)
files = sorted(set(files))
bad, checked, ext = [], 0, 0
anchor_cache = {}
for f in files:
    rel = os.path.relpath(f, ROOT)
    txt = open(f, encoding='utf-8').read()
    for m in LINK.finditer(txt):
        target = m.group(2)
        if target.startswith(('http://', 'https://', 'mailto:')):
            ext += 1; continue
        checked += 1
        if target.startswith('#'):
            a = target[1:]
            if f not in anchor_cache: anchor_cache[f] = anchors(f)
            if a not in anchor_cache[f]:
                bad.append(f"{rel}: missing in-page anchor #{a}")
            continue
        path, _, anc = target.partition('#')
        abs_t = os.path.normpath(os.path.join(os.path.dirname(f), path))
        if not os.path.exists(abs_t):
            bad.append(f"{rel}: broken path -> {target}")
            continue
        if anc and abs_t.endswith('.md'):
            if abs_t not in anchor_cache: anchor_cache[abs_t] = anchors(abs_t)
            if slug(anc) not in anchor_cache[abs_t]:
                bad.append(f"{rel}: missing anchor -> {target}")
print(f"files scanned:      {len(files)}")
print(f"relative links:     {checked}")
print(f"external links:     {ext} (not fetched)")
print(f"problems:           {len(bad)}")
for b in bad[:40]: print("  !", b)
if len(bad) > 40: print(f"  ... {len(bad)-40} more")
sys.exit(1 if bad else 0)
