import json,sys,subprocess,re
path=sys.argv[1]
rows=[]
for i,l in enumerate(open(path),1):
    l=l.strip()
    if not l: continue
    try: rows.append((i,json.loads(l)))
    except Exception as e: print("BAD JSON line",i,e); sys.exit(1)
REQ=["name","maintainer","primary_category","tags","project_type","description","journalism_use_case","repo_url","docs_url","licence","data_licence_terms","licence_evidence_url","language_stack","deployment","activity_evidence","archived","external_deps","data_flows","limitations","readiness","bucket","evidence_urls"]
seen={}
for i,r in rows:
    miss=[k for k in REQ if k not in r]
    if miss: print(f"line {i} {r.get('name')}: MISSING {miss}")
    u=r.get("repo_url","")
    if u in seen: print(f"line {i} DUPLICATE repo_url with line {seen[u]}: {u}")
    seen[u]=i
    m=re.match(r"https://github\.com/([^/]+)/([^/#?]+?)/?$",u)
    if not m:
        print(f"line {i} {r.get('name')}: non-github or odd repo_url -> {u}")
        continue
    full=f"{m.group(1)}/{m.group(2)}"
    p=subprocess.run(["gh","api",f"repos/{full}","--jq",'[.full_name,(.license.spdx_id//"NONE"),(.archived|tostring),.pushed_at]|@tsv'],capture_output=True,text=True)
    if p.returncode!=0:
        print(f"line {i} {r.get('name')}: GH API FAIL {full} :: {p.stderr.strip()[:120]}")
        continue
    fn,lic,arch,pushed=p.stdout.strip().split("\t")
    decl=r.get("licence","")
    archdecl=r.get("archived","")
    probs=[]
    if lic not in ("NOASSERTION","NONE","") and decl!=lic: probs.append(f"licence declared={decl} api={lic}")
    if lic in ("NOASSERTION","NONE") and decl not in ("not verified",) and r.get("bucket")=="verified-oss" and "licence_evidence_url" not in r: probs.append("noassertion w/o evidence")
    if (arch=="true")!=(archdecl=="yes"): probs.append(f"archived declared={archdecl} api={arch}")
    if fn.lower()!=full.lower(): probs.append(f"redirect {full} -> {fn}")
    print(f"line {i} {r.get('name'):38s} {fn:45s} api_lic={lic:14s} arch={arch:5s} pushed={pushed[:10]} {'| '+'; '.join(probs) if probs else 'OK'}")
