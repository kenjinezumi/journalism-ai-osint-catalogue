import json,re,sys
meta={}
for l in open('meta.jsonl'):
    d=json.loads(l)
    if d.get('error'): continue
    meta[d['query'].lower()]=d
    meta[(d.get('full_name') or '').lower()]=d
inv=json.load(open('inventory.json'))
seg=sys.argv[1]
for d in inv:
    if d['_segment']!=seg: continue
    u=d.get('repo_url','') or ''
    m=re.search(r'github\.com/([\w.\-]+/[\w.\-]+)',u)
    md=meta.get(m.group(1).lower()) if m else None
    bits=[]
    if md:
        bits.append(f"{md['full_name']} spdx={md.get('spdx')} arch={md.get('archived')} push={md.get('pushed_at')} rel={md.get('rel_tag')}@{md.get('rel_date')} tag={md.get('last_tag')} stars={md.get('stars')} iss={md.get('open_issues')}")
    else:
        bits.append(f"NO-GH-META url={u}")
    print(f"- {d['name']} || type={d.get('project_type')} bucket={d.get('bucket')} lic={d.get('licence')} mdl={d.get('model_licence','')} || {bits[0]}")
    print(f"    use: {d.get('journalism_use_case','')[:240]}")
    print(f"    lim: {d.get('limitations','')[:200]} | deps: {d.get('external_deps','')[:120]} | flow: {d.get('data_flows','')[:120]}")
