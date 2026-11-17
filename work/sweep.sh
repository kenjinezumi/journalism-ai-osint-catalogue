#!/bin/bash
# $1 = owner/repo ; emits one JSON line with verified metadata (REST follows renames)
r="$1"
j=$(gh api "repos/$r" 2>/dev/null)
if [ -z "$j" ]; then echo "{\"query\":\"$r\",\"error\":\"FETCH_FAILED\"}"; exit 0; fi
rel=$(gh api "repos/$r/releases/latest" 2>/dev/null)
echo "$j" | python3 -c "
import sys,json
d=json.load(sys.stdin)
rel=json.loads('''$(echo "$rel" | tr -d '\n' | sed "s/'/ /g")''') if '''$rel'''.strip().startswith('{') else {}
lic=d.get('license') or {}
print(json.dumps({
 'query':'$r','full_name':d.get('full_name'),
 'renamed': (d.get('full_name','').lower()!='$r'.lower()),
 'spdx':lic.get('spdx_id'),'lic_name':lic.get('name'),
 'archived':d.get('archived'),'disabled':d.get('disabled'),
 'pushed_at':(d.get('pushed_at') or '')[:10],'created_at':(d.get('created_at') or '')[:10],
 'updated_at':(d.get('updated_at') or '')[:10],
 'stars':d.get('stargazers_count'),'forks':d.get('forks_count'),
 'open_issues':d.get('open_issues_count'),'lang':d.get('language'),
 'is_fork':d.get('fork'),'parent':((d.get('parent') or {}).get('full_name')),
 'homepage':d.get('homepage'),'desc':(d.get('description') or '')[:200],
 'topics':d.get('topics') or [],
 'rel_tag':rel.get('tag_name'),'rel_date':(rel.get('published_at') or '')[:10] or None,
}, ensure_ascii=False))
" 2>/dev/null || echo "{\"query\":\"$r\",\"error\":\"PARSE\"}"
