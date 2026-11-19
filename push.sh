#!/usr/bin/env bash
# Pushes this folder to https://github.com/studiorabota/test-dg-2 with Git LFS.
# Create that repo on GitHub first, EMPTY (no README, .gitignore or license).
set -euo pipefail
cd "$(dirname "$0")"

command -v git-lfs >/dev/null || { echo "git-lfs not found. Install it: brew install git-lfs (macOS) / apt install git-lfs"; exit 1; }

git init -b main
git lfs install --local
git add .gitattributes          # tracking rules first, so data + images go into LFS
git add .
git commit -m "Colab + Git LFS demo with windkit modules and images"

echo "Files stored in LFS:"
git lfs ls-files --size

git remote add origin https://github.com/studiorabota/test-dg-2.git
git push -u origin main

echo
echo "Done: https://github.com/studiorabota/test-dg-2"
