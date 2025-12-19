#!/usr/bin/env python3
"""
Cross-platform script to build HED documentation using Sphinx.

This script:
1. Installs/updates required dependencies from pyproject.toml
2. Builds the Sphinx documentation to HTML format
3. Provides clear status messages and error handling

Usage:
    python scripts/build_docs.py
    Or from root: python -m scripts.build_docs
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Build the Sphinx documentation."""
    # Get the repository root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent

    print("=" * 70)
    print("HED schemas documentation builder")
    print("=" * 70)
    print()

    # Step 1: Install dependencies
    print("Installing/updating documentation dependencies...")
    print("-" * 70)
    requirements_file = repo_root / "docs" / "requirements.txt"
    if not requirements_file.exists():
        print(f"\n❌ Error: {requirements_file} not found", file=sys.stderr)
        return 1
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            cwd=repo_root,
            check=True,
            capture_output=False,
        )
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing dependencies: {e}", file=sys.stderr)
        return 1

    print()

    # Step 2: Build documentation
    print("Building documentation...")
    print("-" * 70)
    source_dir = repo_root / "docs" / "source"
    build_dir = repo_root / "docs" / "_build" / "html"

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "sphinx",
                "-b",
                "html",
                str(source_dir),
                str(build_dir),
            ],
            cwd=repo_root,
            check=True,
            capture_output=False,
        )
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error building documentation: {e}", file=sys.stderr)
        return 1

    print()
    print("=" * 70)
    print("✅ Documentation built successfully!")
    print("=" * 70)
    print(f"\nStatic files are in: {build_dir}")
    print(f"Open {build_dir / 'index.html'} in your browser to view locally.")
    print("\nOr run: python scripts/serve_docs.py")
    print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
