#!/usr/bin/env bash
set -euo pipefail

# Ensure we are in the project root
cd "$(dirname "$0")/.."
export PYTHONPATH=${PYTHONPATH:-}:.


echo "Running lint checks..."
# Check if ruff is installed
if command -v ruff &> /dev/null; then
    ruff check .
else
    echo "Warning: ruff not found, skipping lint."
fi

echo "Running tests..."
# Check if pytest is installed
if command -v pytest &> /dev/null; then
    pytest -q
else
    echo "pytest not found. Trying to run with python -m unittest..."
    # This might fail for pytest-specific features like fixtures
    python3 -m unittest discover tests/unit
fi
