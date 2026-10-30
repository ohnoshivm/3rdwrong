#!/bin/sh
# Copies only rebuild renders; never copies original-site screenshots.
set -eu
out="$(cd "$(dirname "$0")" && pwd)"
cp "$out/../rebuild-steps/step-017.jpg" "$out/a03-rebuild-y1530.jpg"
cp "$out/../rebuild-steps/step-067.jpg" "$out/a04-rebuild-y6030.jpg"
