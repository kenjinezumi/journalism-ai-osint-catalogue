import json,sys
meta={}
for l in open('meta.jsonl'):
    d=json.loads(l)
    if d.get('error'): continue
    meta[d['query'].lower()]=d; meta[(d.get('full_name') or '').lower()]=d
for r in sys.argv[1:]:
    d=meta.get(r.lower())
    if not d: print(f"{r}: NO META"); continue
    print(f"{d['full_name']} | spdx={d.get('spdx')} | arch={d.get('archived')} | push={d.get('pushed_at')} | rel={d.get('rel_tag')}@{d.get('rel_date')} tag={d.get('last_tag')} | stars={d.get('stars')} iss={d.get('open_issues')} | {(d.get('desc') or '')[:90]}")
