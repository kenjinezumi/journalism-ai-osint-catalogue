#!/usr/bin/env python3
"""Render the catalogue repository's Markdown into a self-contained static site.

Reads the repository read-only and writes a complete HTML site into <out-dir>.
The Markdown is rendered in-process by markdown-it-py; no network calls, no
external scripts, styles or fonts are involved, so the output is byte-stable
for a given commit and can be served from GitHub Pages as-is.

The site is a rendering of the repository, not a second source of truth: every
page is generated from the tracked .md files, and the interactive directory
table is generated from docs/directory.json in the same build as the Markdown
table it replaces.

Usage: python3 tools/mksite.py <repo-dir> <out-dir>
"""
import os, re, shutil, sys, html
from markdown_it import MarkdownIt

import dirtable

REPO, OUT = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
assert os.path.isdir(REPO), f"not a directory: {REPO}"
assert OUT != REPO, "output directory must not be the repository root"

REPO_URL = "https://github.com/kenjinezumi/journalism-ai-osint-catalogue"
DESCRIPTION = ("An assessed, ranked and evidenced catalogue of 361 open-source "
               "projects, datasets and services used in investigative journalism, "
               "surveillance research and open-source investigation.")

NAV = [("README.html", "Home"),
       ("README.html#directory--all-361-projects", "Directory (361)"),
       ("docs/rankings.html", "All 361 ranked"),
       ("docs/journalism-ai.html", "Journalism &amp; AI"),
       ("docs/surveillance.html", "Surveillance"), ("docs/osint.html", "OSINT"),
       ("docs/methodology.html", "Methodology"), ("docs/stacks.html", "Stacks"),
       ("docs/findings-and-limitations.html", "Findings"),
       ("report.html", "Full report")]

NAV_EXTERNAL = [(REPO_URL, "Source on GitHub")]

CSS = """
:root{--fg:#1f2328;--bg:#ffffff;--mut:#59636e;--line:#d1d9e0;--acc:#0969da;
--code:#f6f8fa;--thead:#f6f8fa;--warn:#9a6700;--warnbg:#fff8c5}
@media(prefers-color-scheme:dark){:root{--fg:#e6edf3;--bg:#0d1117;--mut:#9198a1;
--line:#3d444d;--acc:#4493f8;--code:#151b23;--thead:#151b23;--warn:#d29922;--warnbg:#272115}}
*{box-sizing:border-box}
html{scroll-padding-top:4.2rem}
body{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.topbar{position:sticky;top:0;z-index:20;background:var(--bg);border-bottom:1px solid var(--line);
padding:.5rem .9rem;display:flex;gap:.1rem;flex-wrap:wrap;align-items:center}
.topbar a{color:var(--fg);text-decoration:none;font-size:.82rem;padding:.3rem .55rem;border-radius:6px;white-space:nowrap}
.topbar a:hover{background:var(--code);color:var(--acc)}
.topbar .tag{font-size:.68rem;color:var(--mut);border:1px solid var(--line);border-radius:999px;
padding:.12rem .5rem;margin-right:.5rem;letter-spacing:.04em;text-transform:uppercase}
main{max-width:1100px;margin:0 auto;padding:1.6rem 1.1rem 5rem}
h1,h2,h3,h4{line-height:1.25;margin:1.6em 0 .6em;font-weight:600}
h1{font-size:1.9rem;padding-bottom:.3em;border-bottom:1px solid var(--line);margin-top:.4em}
h2{font-size:1.4rem;padding-bottom:.3em;border-bottom:1px solid var(--line)}
h3{font-size:1.12rem}h4{font-size:1rem}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
p,ul,ol,blockquote,table{margin:0 0 1rem}
ul,ol{padding-left:1.6rem}li{margin:.22rem 0}
code{background:var(--code);padding:.15em .38em;border-radius:5px;font-size:.88em;
font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:var(--code);padding:.9rem 1rem;border-radius:8px;overflow-x:auto}
pre code{background:none;padding:0}
blockquote{border-left:3px solid var(--line);padding:.1rem 0 .1rem 1rem;color:var(--mut)}
table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:.9rem}
th,td{border:1px solid var(--line);padding:.42rem .62rem;text-align:left;vertical-align:top}
th{background:var(--thead);font-weight:600;white-space:nowrap}
tr:nth-child(even) td{background:color-mix(in srgb,var(--code) 55%,transparent)}
hr{border:0;border-top:1px solid var(--line);margin:2rem 0}
h1 a.anc,h2 a.anc,h3 a.anc{opacity:0;margin-left:.35rem;font-size:.8em;text-decoration:none}
h1:hover a.anc,h2:hover a.anc,h3:hover a.anc{opacity:.5}
.note{background:var(--warnbg);color:var(--warn);border:1px solid color-mix(in srgb,var(--warn) 35%,transparent);
border-radius:8px;padding:.55rem .8rem;font-size:.82rem;margin:0 0 1.4rem}
.note b{color:inherit}
.topbar a.ext{margin-left:auto;color:var(--mut)}
.topbar a.ext:hover{color:var(--acc)}
"""

md = MarkdownIt("gfm-like")
md.disable("linkify")           # linkify-it-py is not installed; bare URLs stay literal


def gh_slug(text):
    """Emulate github-slugger on the heading's rendered text."""
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)      # links -> label
    t = re.sub(r"[`*_~]", "", t)                            # inline markers
    t = t.strip().lower()
    t = re.sub(r"[^\w\s-]", "", t)
    return t.replace(" ", "-")


def rewrite(tokens, depth):
    """Add GitHub-compatible heading ids; point relative .md links at .html."""
    seen = {}
    for i, tok in enumerate(tokens):
        if tok.type == "heading_open":
            inline = tokens[i + 1] if i + 1 < len(tokens) else None
            base = gh_slug(inline.content) if inline is not None else ""
            n = seen.get(base, 0)
            seen[base] = n + 1
            tok.attrSet("id", base if n == 0 else f"{base}-{n}")
        if tok.type == "inline" and tok.children:
            for ch in tok.children:
                if ch.type != "link_open":
                    continue
                href = ch.attrGet("href") or ""
                if href.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path, sep, anc = href.partition("#")
                if path.endswith(".md"):
                    ch.attrSet("href", path[:-3] + ".html" + (sep + anc if sep else ""))
    return tokens


def page(title, body, depth, extra_css=""):
    up = "../" * depth
    nav = "".join(f'<a href="{up}{h}">{t}</a>' for h, t in NAV)
    nav += "".join(f'<a class="ext" href="{h}">{t}</a>' for h, t in NAV_EXTERNAL)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{html.escape(DESCRIPTION, quote=True)}">
<title>{html.escape(title)}</title><style>{CSS}{extra_css}</style></head>
<body><div class="topbar">{nav}</div>
<main>{body}</main></body></html>"""


BANNER = re.compile(r"<!-- SITE_BANNER_START -->.*?<!-- SITE_BANNER_END -->", re.S)

DIR_MARKERS = re.compile(
    r"<!-- DIRECTORY_TABLE_START -->.*?<!-- DIRECTORY_TABLE_END -->", re.S)


def enhance_directory(body):
    """Replace the rendered markdown directory table with the interactive one.

    Both are generated from docs/directory.json and records/*.json in the same
    build, so swapping one for the other cannot change which projects are listed
    or what any cell says. The replacement is bounded by the markers build.py
    writes around the table; if they are missing, the markdown table is left
    exactly as it is rather than guessed at.
    """
    src = os.path.join(REPO, "docs", "directory.json")
    if not DIR_MARKERS.search(body) or not os.path.exists(src):
        print("  ! directory markers or docs/directory.json not found — "
              "README keeps the static markdown table")
        return body, ""
    css, table = dirtable.build(src)
    return DIR_MARKERS.sub(lambda _m: table, body, count=1), css


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(REPO, OUT, ignore=shutil.ignore_patterns(".git"))
    count = 0
    for root, _dirs, files in os.walk(OUT):
        for f in files:
            if not f.endswith(".md"):
                continue
            src = os.path.join(root, f)
            rel = os.path.relpath(src, OUT)
            # narrative/ holds hand-authored TEMPLATES whose relative links are written for
            # their output location (docs/), so they do not resolve from narrative/ itself.
            # Their content appears in full in the generated pages; leave them as raw .md.
            if rel.split(os.sep)[0] == "narrative":
                continue
            depth = rel.count(os.sep)
            text = open(src, encoding="utf-8").read()
            tokens = rewrite(md.parse(text), depth)
            body = md.renderer.render(tokens, md.options, {})
            m = re.search(r"^#\s+(.+)$", text, re.M)
            title = re.sub(r"[`*_]", "", m.group(1)).strip() if m else rel
            extra_css = ""
            if rel == "README.md":
                text = BANNER.sub("", text)          # banner links here; drop it here
                tokens = rewrite(md.parse(text), depth)
                body = md.renderer.render(tokens, md.options, {})
                body, extra_css = enhance_directory(body)
            rendered = page(title, body, depth, extra_css)
            out = os.path.join(root, f[:-3] + ".html")
            open(out, "w", encoding="utf-8").write(rendered)
            if rel == "README.md":
                open(os.path.join(OUT, "index.html"), "w",
                     encoding="utf-8").write(rendered)
            count += 1
    assert os.path.exists(os.path.join(OUT, "index.html")), \
        "README.md did not render — the site would have no landing page"
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    print(f"rendered {count} markdown files -> HTML")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()
