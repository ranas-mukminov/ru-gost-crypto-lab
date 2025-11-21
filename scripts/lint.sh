#!/usr/bin/env bash
set -euo pipefail

echo "Running ruff..."
ruff check .

echo "Running mypy..."
mypy .

# echo "Running yamllint..."
# yamllint .
