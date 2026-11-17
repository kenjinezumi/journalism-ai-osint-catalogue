#!/bin/zsh
while read -r r; do
  [[ -z "$r" ]] && continue
  echo "$r -> $(gh api "repos/$r/releases/latest" -q '.tag_name+" @ "+(.published_at[0:10])' 2>/dev/null || echo 'no-release-endpoint')"
done
