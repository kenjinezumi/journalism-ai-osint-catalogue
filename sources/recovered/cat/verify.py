#!/usr/bin/env python3
import subprocess, sys, json
def gh(path):
    p = subprocess.run(["gh","api",path], capture_output=True, text=True, timeout=60)
    if p.returncode != 0: return None
    try: return json.loads(p.stdout)
    except Exception: return None
rows=[]
for line in open(sys.argv[1]):
    r=line.strip()
    if not r or r.startswith("#"): continue
    d=gh("repos/"+r)
    if d is None:
        print("\t".join([r,"FETCH_FAILED","","","","","","",""])); sys.stdout.flush(); continue
    lic=d.get("license") or {}
    rel=gh("repos/%s/releases/latest"%r)
    reltag = rel.get("tag_name") if rel else "none"
    reldate = (rel.get("published_at") or "")[:10] if rel else "none"
    print("\t".join(str(x) for x in [
        d.get("full_name"), lic.get("spdx_id") or "NONE", (lic.get("name") or "NONE"),
        "ARCHIVED" if d.get("archived") else "active",
        (d.get("pushed_at") or "")[:10], reltag, reldate,
        d.get("language"), d.get("stargazers_count"),
        (d.get("description") or "")[:150].replace("\t"," ")
    ]))
    sys.stdout.flush()
