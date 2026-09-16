#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-paper-reader-skill}"
VISIBILITY="${2:-public}"

if [[ "$VISIBILITY" != "public" && "$VISIBILITY" != "private" ]]; then
  echo "usage: $0 [repo-name] [public|private]" >&2
  exit 2
fi

command -v gh >/dev/null 2>&1 || { echo "GitHub CLI (gh) is required" >&2; exit 1; }
gh auth status >/dev/null

if [[ ! -d .git ]]; then
  git init -b main
  git add .
  git commit -m "feat: initial paper-reader skill"
fi

if git remote get-url origin >/dev/null 2>&1; then
  echo "origin already exists: $(git remote get-url origin)" >&2
  echo "push manually or remove/rename the existing origin first" >&2
  exit 1
fi

gh repo create "$REPO_NAME" "--$VISIBILITY" --source=. --remote=origin --push
