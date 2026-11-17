#!/bin/zsh
while read -r r; do
  [[ -z "$r" ]] && continue
  out=$(gh api "repos/$r" 2>/dev/null | jq -c '{full:.full_name,lic:(.license.spdx_id//"none"),arch:.archived,pushed:.pushed_at[0:10],lang:.language,stars:.stargazers_count,hp:.homepage,desc:.description[0:120]}')
  if [[ -z "$out" ]]; then echo "{\"full\":\"$r\",\"ERROR\":1}"; else echo "$out"; fi
done
