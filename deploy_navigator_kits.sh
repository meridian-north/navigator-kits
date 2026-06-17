#!/bin/bash
# Publish the Navigator Kits hub.  bash ~/navigator-kits/deploy_navigator_kits.sh
set -e
cd "$HOME/navigator-kits"
if pgrep -x git >/dev/null 2>&1; then echo "✗ git is running — close it and re-run."; exit 1; fi
for L in .git/index.lock .git/HEAD.lock .git/config.lock .git/refs/heads/main.lock; do
  [ -f "$L" ] && rm -f "$L" && echo "→ cleared stale $L"; done

# mount the Legal Reference Corpus form as a kit (standalone; uses embedded seed data)
if [ -f "$HOME/meridian-north-legal-corpus/index.html" ]; then
  mkdir -p kits/legal-reference-corpus
  cp "$HOME/meridian-north-legal-corpus/index.html" kits/legal-reference-corpus/index.html
  # include the full USC lookup if present (optional; form works without it)
  for J in "$HOME/usc_section_lookup.json" "$HOME/meridian-north-legal-corpus/data/usc_section_lookup.json"; do
    [ -f "$J" ] && cp "$J" kits/legal-reference-corpus/usc_section_lookup.json && echo "→ bundled USC lookup" && break
  done
  echo "→ mounted Legal Reference Corpus kit"
fi
git add index.html deploy_navigator_kits.sh kits 2>/dev/null || git add index.html
git commit -m "Hub: list all public navigator kits (VAERS review, 5-min VAERS, VAERS reader, supplements, legal); formal theme" || echo "→ nothing new to commit"
gh auth switch --user meridian-north 2>/dev/null || true
git push origin main
echo ""
echo "✓ Done. Live (~1 min): https://meridian-north.github.io/navigator-kits/"
