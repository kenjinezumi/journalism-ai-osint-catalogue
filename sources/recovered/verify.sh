#!/bin/zsh
# usage: verify.sh repo1 repo2 ...
for r in "$@"; do
  out=$(gh api "repos/$r" 2>/dev/null | python3 -c '
import json,sys
try:
    d=json.load(sys.stdin)
except Exception:
    print("PARSE_FAIL"); sys.exit()
lic=(d.get("license") or {}).get("spdx_id")
print("|".join(str(x) for x in [
 d.get("full_name"), lic, d.get("archived"), d.get("language"),
 (d.get("pushed_at") or "")[:10], (d.get("created_at") or "")[:7],
 d.get("stargazers_count"), (d.get("homepage") or "")[:60],
 (d.get("description") or "")[:150]
]))
')
  if [[ -z "$out" ]]; then echo "$r|NOT_FOUND_OR_ERROR"; else echo "$out"; fi
done
