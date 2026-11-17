#!/bin/zsh
# usage: verify.sh reposfile  (one owner/repo per line, # comments ok)
# emits TSV: repo, spdx, license_name, archived, pushed_at, created_at, lang, latest_release_tag, latest_release_date, stars, desc
while read -r r; do
  [[ -z "$r" || "$r" == \#* ]] && continue
  j=$(gh api "repos/$r" 2>/dev/null)
  if [[ -z "$j" || "$j" == *"Not Found"* ]]; then echo "$r\tFETCH_FAILED"; continue; fi
  rel=$(gh api "repos/$r/releases/latest" 2>/dev/null)
  echo "$j" | python3 -c "
import sys,json
d=json.load(sys.stdin)
lic=d.get('license') or {}
rel=None
try:
    rel=json.loads(open('/dev/stdin').read())
except Exception: pass
print('\t'.join(str(x) for x in [
 d.get('full_name'), lic.get('spdx_id','NONE'), (lic.get('name') or 'NONE'),
 d.get('archived'), (d.get('pushed_at') or '')[:10], (d.get('created_at') or '')[:10],
 d.get('language'), d.get('stargazers_count'),
 (d.get('description') or '')[:160].replace('\t',' ')
]))
"
  echo "$rel" | python3 -c "
import sys,json
try:
    d=json.load(sys.stdin)
    print('   REL\t'+str(d.get('tag_name'))+'\t'+str(d.get('published_at'))[:10])
except Exception:
    print('   REL\tnone\tnone')
"
done < "$1"
