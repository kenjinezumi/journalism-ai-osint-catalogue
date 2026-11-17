#!/bin/zsh
while read -r r; do
  [[ -z "$r" ]] && continue
  j=$(gh api "repos/$r/license" 2>/dev/null)
  if [[ -z "$j" ]]; then echo "=== $r : NO_LICENSE_FILE_DETECTED"; continue; fi
  name=$(echo "$j" | jq -r '.name'); url=$(echo "$j" | jq -r '.html_url')
  body=$(echo "$j" | jq -r '.content' | base64 -d 2>/dev/null | tr -s ' \n' ' ' | head -c 420)
  echo "=== $r | file=$name | $url"
  echo "    $body"
done
