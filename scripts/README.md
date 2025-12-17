# HED Schemas Scripts

This directory contains utility scripts for the hed-schemas repository.

## Documentation Build Scripts

### Building Documentation Locally

**Python (cross-platform):**

```bash
python scripts/build_docs.py
```

**Windows:**

```cmd
scripts\build-docs.bat
```

**Unix/Mac:**

```bash
./scripts/build-docs.sh
```

This will:

1. Install documentation dependencies from `docs/requirements.txt`
2. Build the Sphinx documentation to `docs/_build/html/`
3. Show you where to find the built HTML files

### Serving Documentation Locally

After building, you can serve the documentation locally:

**Python (cross-platform):**

```bash
python scripts/serve_docs.py
```

**Windows:**

```cmd
scripts\serve-sphinx.bat
```

**Unix/Mac:**

```bash
./scripts/serve-sphinx.sh
```

This will:

1. Start a local HTTP server on port 8000
2. Open your browser to view the documentation
3. Allow you to view the documentation as it would appear online

Press Ctrl+C to stop the server.

### Options for serve_docs.py

```bash
# Use a different port
python scripts/serve_docs.py --port 8080

# Don't automatically open browser
python scripts/serve_docs.py --no-browser
```

## Schema Validation Scripts

### verify_branch.sh

Pre-commit hook that verifies:

- Branch naming conventions (standard\_*, score\_*, lang\_\*, etc.)
- Changes are only in appropriate schema directories
- Changes are in prerelease/ subdirectories

Used by `.pre-commit-config.yaml` and the `verify_source_branch.yaml` workflow.

## Quick Start

To set up your development environment:

```bash
# Install all development dependencies
pip install -r requirements-dev.txt

# Build documentation
python scripts/build_docs.py

# Serve documentation
python scripts/serve_docs.py
```
