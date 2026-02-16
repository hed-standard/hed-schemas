# HED schemas scripts

This directory contains utility scripts for the hed-schemas repository.

## Schema Validation Scripts

### verify_branch.py

Python script that verifies:

- Branch naming conventions (standard\_*, score\_*, lang\_\*, etc.)
- Changes are only in appropriate schema directories
- Changes are in prerelease/ subdirectories
- Schema files pass validation using hed-python tools

**Usage:**

```bash
# Basic usage
python scripts/verify_branch.py file1.xml file2.mediawiki

# Validate all schema extensions
python scripts/verify_branch.py file1.mediawiki --validate-all

# Override branch name
python scripts/verify_branch.py file1.xml --branch standard_new_feature
```

Used by the `verify_source_branch.yaml` workflow to ensure PRs follow repository conventions.

## Documentation Build

### Building Documentation Locally

Navigate to the repository root and use `sphinx-build`:

**Windows:**

```powershell
sphinx-build -b html docs/ docs/_build/html
```

**Unix/Mac:**

```bash
sphinx-build -b html docs/ docs/_build/html
```

This will build the Sphinx documentation to `docs/_build/html/`.

### Serving Documentation Locally

After building, you can serve the documentation with Python's built-in HTTP server:

**Windows:**

```powershell
cd docs\_build\html
python -m http.server 8000
```

**Unix/Mac:**

```bash
cd docs/_build/html
python -m http.server 8000
```

Then open your browser to [http://localhost:8000](http://localhost:8000).

Press Ctrl+C to stop the server.

**Alternative**: You can also open `docs/_build/html/index.html` directly in your web browser.

### Options for HTTP server

```bash
# Use a different port
python -m http.server 8080
```

## Quick Start

To set up your development environment:

```bash
# Install all development dependencies
pip install ".[dev]"

# Build documentation
sphinx-build -b html docs/ docs/_build/html

# Serve documentation
cd docs/_build/html
python -m http.server 8000
```
