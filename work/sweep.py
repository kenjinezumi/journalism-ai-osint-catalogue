#!/usr/bin/env python3
import json,subprocess,sys
from concurrent.futures import ThreadPoolExecutor

def gh(path):
    p=subprocess.run(['gh','api',path],capture_output=True,text=True)
    if p.returncode!=0: return None
    try: return json.loads(p.stdout)
    except Exception: return None

def one(r):
    d=gh(f'repos/{r}')
    if not d or 'full_name' not in d:
        return {'query':r,'error':'FETCH_FAILED'}
    rel=gh(f'repos/{r}/releases/latest') or {}
    tags=gh(f'repos/{r}/tags?per_page=1') or []
    lic=d.get('license') or {}
    return {'query':r,'full_name':d.get('full_name'),
      'renamed': d.get('full_name','').lower()!=r.lower(),
      'spdx':lic.get('spdx_id'),'lic_name':lic.get('name'),
      'archived':d.get('archived'),'disabled':d.get('disabled'),
      'pushed_at':(d.get('pushed_at') or '')[:10],'created_at':(d.get('created_at') or '')[:10],
      'stars':d.get('stargazers_count'),'forks':d.get('forks_count'),
      'open_issues':d.get('open_issues_count'),'lang':d.get('language'),
      'is_fork':d.get('fork'),'parent':((d.get('parent') or {}).get('full_name')),
      'homepage':d.get('homepage'),'desc':(d.get('description') or '')[:200],
      'topics':d.get('topics') or [],
      'rel_tag':rel.get('tag_name'),'rel_date':(rel.get('published_at') or '')[:10] or None,
      'last_tag':(tags[0].get('name') if tags else None)}

repos=[l.strip() for l in open('candidates.txt') if l.strip()]
out=open('meta.jsonl','w')
with ThreadPoolExecutor(max_workers=12) as ex:
    for i,res in enumerate(ex.map(one,repos)):
        out.write(json.dumps(res,ensure_ascii=False)+'\n')
        if i%50==0: out.flush(); print(i,file=sys.stderr,flush=True)
out.close()
print('DONE',len(repos),file=sys.stderr)
