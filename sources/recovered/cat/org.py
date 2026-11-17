#!/usr/bin/env python3
import subprocess, sys, json
def gh(path):
    p = subprocess.run(["gh","api","--paginate",path], capture_output=True, text=True, timeout=180)
    if p.returncode != 0: return []
    out=[]
    txt=p.stdout.strip()
    # gh --paginate concatenates JSON arrays; handle by splitting on '][' 
    txt=txt.replace("][", "],[")
    try:
        if txt.startswith("["):
            for chunk in json.loads("["+txt+"]") if txt.startswith("[[") else [json.loads(txt)]:
                out.extend(chunk)
        else:
            out=json.loads(txt)
    except Exception:
        try: out=json.loads(txt)
        except Exception: return []
    return out
for org in sys.argv[1:]:
    repos = gh(f"orgs/{org}/repos?per_page=100&type=public&sort=pushed")
    if not repos:
        repos = gh(f"users/{org}/repos?per_page=100&type=public&sort=pushed")
    rows=[]
    for d in repos:
        if not isinstance(d,dict): continue
        if d.get("fork"): continue
        lic=(d.get("license") or {}).get("spdx_id") or "NONE"
        rows.append((d.get("pushed_at","")[:10], d.get("stargazers_count",0), d.get("full_name"), lic,
                     "ARCH" if d.get("archived") else "act", (d.get("description") or "")[:120].replace("\n"," ")))
    rows.sort(reverse=True)
    print(f"===== {org} ({len(rows)} non-fork public repos) =====")
    for r in rows[:45]:
        print(" | ".join(str(x) for x in r))
    print()
