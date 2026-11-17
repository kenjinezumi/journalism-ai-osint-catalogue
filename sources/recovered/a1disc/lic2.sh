#!/bin/zsh
while read -r r; do
  [[ -z "$r" ]] && continue
  u=$(gh api "repos/$r/license" -q '.html_url' 2>/dev/null)
  t=$(gh api "repos/$r/license" -H "Accept: application/vnd.github.raw" 2>/dev/null | LC_ALL=C tr -d '\000-\010\013\014\016-\037' | tr -s ' \n\r' ' ' | head -c 260)
  echo "=== $r | $u"
  echo "    $t"
done
