#!/bin/bash
# Publish the Navigator Kits hub + mount each public form as a kit.
#   bash ~/navigator-kits/deploy_navigator_kits.sh
set -e
cd "$HOME/navigator-kits"
if pgrep -x git >/dev/null 2>&1; then echo "✗ git is running — close it and re-run."; exit 1; fi
for L in .git/index.lock .git/HEAD.lock .git/config.lock .git/refs/heads/main.lock; do
  [ -f "$L" ] && rm -f "$L" && echo "→ cleared stale $L"; done

# locate the USC corpus JSON (some forms need it; others degrade to embedded seed)
USC_JSON=""
for J in "$HOME/usc_section_lookup.json" "$HOME/meridian-north-legal-corpus/data/usc_section_lookup.json"; do
  [ -f "$J" ] && USC_JSON="$J" && break
done
[ -n "$USC_JSON" ] && echo "→ USC lookup found: $USC_JSON" || echo "⚠ USC lookup JSON not found — JSON-backed forms will use embedded seed data"

# mount <src-html> <kit-folder> <needs-json:yes|no>
mount_kit(){
  local src="$1" dir="kits/$2" json="$3"
  [ -f "$src" ] || { echo "⚠ skip (missing): $src"; return; }
  mkdir -p "$dir"
  cp "$src" "$dir/index.html"
  if [ "$json" = "yes" ] && [ -n "$USC_JSON" ]; then
    cp "$USC_JSON" "$dir/usc_section_lookup.json"
    mkdir -p "$dir/data"; cp "$USC_JSON" "$dir/data/usc_section_lookup.json"
  fi
  echo "→ mounted $dir"
}

# IMPORTANT: only these specific files are published. The meridian-north-legal-corpus
# repo's README (confidential) and BUILD_SHEET are NOT copied and must not be published.
mount_kit "$HOME/meridian-north-legal-corpus/index.html" "legal-reference-corpus" yes
mount_kit "$HOME/legal_corpus_portal.html"               "usc-time-travel-portal" yes
mount_kit "$HOME/legal_corpus_resolver_v1.html"          "ssa-usc-resolver"       yes
mount_kit "$HOME/legal-corpus-time-travel-demo.html"     "legal-time-travel"      no
mount_kit "$HOME/usc_section_query.html"                 "usc-section-lookup"     yes
mount_kit "$HOME/usc_growth_curve.html"                  "usc-growth-curve"       no
# nsclc_supplement_review.html is the user's PERSONAL health page — intentionally NOT published.

git add index.html README.md deploy_navigator_kits.sh kits
git commit -m "Hub + README: list all live kits with links (pharma, supplements, 7 legal); refresh README" || echo "→ nothing new to commit"
gh auth switch --user meridian-north 2>/dev/null || true
git push origin main
echo ""
echo "✓ Done. Live (~1 min): https://meridian-north.github.io/navigator-kits/"
