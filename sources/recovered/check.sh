#!/bin/bash
# usage: check.sh repo1 repo2 ...
for r in "$@"; do
  out=$(gh api "repos/$r" 2>/dev/null | python3 -c '
import sys,json
try:
  d=json.load(sys.stdin)
except Exception:
  print("PARSE_FAIL"); sys.exit()
lic=(d.get("license") or {})
print("\t".join(str(x) for x in [
 d.get("full_name"),
 lic.get("spdx_id"),
 lic.get("name"),
 d.get("pushed_at"),
 d.get("archived"),
 d.get("stargazers_count"),
 d.get("language"),
 d.get("created_at","")[:10],
 (d.get("description") or "")[:120],
]))
')
  if [ -z "$out" ]; then echo -e "$r\tNOT_FOUND"; else echo "$out"; fi
done
