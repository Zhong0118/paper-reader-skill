#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-$HOME/.agents/skills}"
mkdir -p "$TARGET"
rm -rf "$TARGET/paper-reader"
cp -R "$ROOT/skills/paper-reader" "$TARGET/paper-reader"
echo "installed paper-reader -> $TARGET/paper-reader"
