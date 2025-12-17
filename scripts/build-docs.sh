#!/usr/bin/env bash
# Wrapper script for Unix-like systems - calls cross-platform Python script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/build_docs.py"
