#!/bin/bash
set -e

echo "Running Ruff linting..."
ruff check . --fix

echo "Running Black formatting check..."
black .

echo "Running Mypy type checking..."
mypy superbenchmark

echo "All checks passed successfully!"
