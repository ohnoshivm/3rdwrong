#!/usr/bin/env bash
set -euo pipefail
TOOLKIT_REPO="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
command -v python3 >/dev/null 2>&1 || { echo 'python3 is required.' >&2; exit 1; }
export PYTHONDONTWRITEBYTECODE=1
exec python3 "$TOOLKIT_REPO/scripts/toolkit_install.py" "$@"
