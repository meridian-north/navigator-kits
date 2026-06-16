#!/bin/bash
# Run on your Mac (gh authed as meridian-north). Creates the PUBLIC repo, pushes, enables Pages.
set -e
REPO="meridian-north/navigator-kits"
gh auth switch --user meridian-north 2>/dev/null || true
# create public repo from this folder and push current branch
gh repo create "$REPO" --public --source=. --remote=origin --push
# enable GitHub Pages from main / root
gh api -X POST "repos/$REPO/pages" -f "source[branch]=main" -f "source[path]=/" \
  || echo "→ If that errored, enable manually: repo Settings → Pages → Branch: main, folder: / (root)"
echo
echo "✓ Pushed. Pages will be live shortly at:"
echo "  https://meridian-north.github.io/navigator-kits/"
echo "  https://meridian-north.github.io/navigator-kits/kits/tickerforum-we-need-another-law/"
