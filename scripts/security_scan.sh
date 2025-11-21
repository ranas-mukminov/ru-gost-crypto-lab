#!/usr/bin/env bash
set -euo pipefail

echo "Running bandit..."
bandit -r tools/ -c pyproject.toml

echo "Running pip-audit..."
# pip-audit # requires internet, might fail in restricted env
echo "Skipping pip-audit in lab environment (uncomment in production)"
