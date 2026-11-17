#!/usr/bin/env python3
import subprocess, sys, json
def gh(path):
    p = subprocess.run(["gh","api","--paginate",path], capture_output=True, text=True, timeout=180)
    if p.returncode != 0: return []
    txt=p.stdout.strip().replace("][", "],[")
    try:
        if txt.startswith("[["): 
            out=[]
            for c in json.loads("["+txt+"]"): out.extend(c)
            return out
        return json.loads(txt)
    except Exception: return []
for org in sys.argv[1:]:
    repos = gh(f"orgs/{org}/repos?per_page=100&type=public&sort=pushed") or gh(f"users/{org}/repos?per_page=100&type=public&sort=pushed")
    rows=[]
    for d in repos:
        if not isinstance(d,dict) or d.get("fork"): continue
        st=d.get("stargazers_count",0); desc=(d.get("description") or "")
        pushed=(d.get("pushed_at") or "")[:10]
        if st<8 and not (pushed>"2025-06" and len(desc)>25): continue
        if st<3: continue
        lic=(d.get("license") or {}).get("spdx_id") or "NONE"
        rows.append((pushed, st, d.get("full_name"), lic, "ARCH" if d.get("archived") else "act", desc[:115].replace("\n"," ")))
    rows.sort(reverse=True)
    print(f"===== {org} =====")
    for r in rows[:28]: print(" | ".join(str(x) for x in r))
    print()
