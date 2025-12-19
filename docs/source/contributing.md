# Contributing to documentation

This guide explains how to build and contribute to the HED schemas documentation.

## Prerequisites

- Python 3.10 or higher
- Git

## Setting up your environment

1. **Clone the repository**:

   ```bash
   git clone https://github.com/hed-standard/hed-schemas.git
   cd hed-schemas
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\Activate.ps1

   # Unix/Mac
   source .venv/bin/activate
   ```

3. **Install documentation dependencies**:

   ```bash
   pip install -r docs/requirements.txt
   ```

## Building documentation locally

### Method 1: Using the build script (recommended)

The easiest way to build the documentation is using the provided Python script:

```bash
python scripts/build_docs.py
```

This script will:

1. Install/update required dependencies
2. Build the Sphinx documentation
3. Show you where to find the built HTML files

### Method 2: Using Sphinx directly

Navigate to the docs directory and use the make command:

**Windows**:

```powershell
cd docs
make.bat html
```

**Unix/Mac**:

```bash
cd docs
make html
```

The built documentation will be in `docs/_build/html/`.

### Method 3: Using Platform-Specific Scripts

**Windows**:

```powershell
scripts\build-docs.bat
```

**Unix/Mac**:

```bash
./scripts/build-docs.sh
```

## Viewing documentation locally

### Method 1: Using the serve script (recommended)

After building, you can serve the documentation locally:

```bash
python scripts/serve_docs.py
```

This will:

- Start a local HTTP server on port 8000
- Automatically open your browser to http://localhost:8000
- Allow you to view the documentation as it would appear online

Press `Ctrl+C` to stop the server.

**Options**:

```bash
# Use a different port
python scripts/serve_docs.py --port 8080

# Don't automatically open browser
python scripts/serve_docs.py --no-browser
```

### Method 2: Open HTML file directly

Open `docs/_build/html/index.html` in your web browser.

### Method 3: Using Platform-Specific Scripts

**Windows**:

```powershell
scripts\serve-sphinx.bat
```

**Unix/Mac**:

```bash
./scripts/serve-sphinx.sh
```

## Making changes to documentation

### Documentation structure

The documentation source files are in `docs/source/`:

| File                   | Purpose                        |
| ---------------------- | ------------------------------ |
| `index.rst`            | Main documentation index       |
| `introduction.md`      | Overview of HED schemas        |
| `user_guide.md`        | Guide for using schemas        |
| `developer_guide.md`   | Guide for schema development   |
| `schemas_reference.md` | Detailed schema information    |
| `api2.rst`             | Repository structure reference |
| `conf.py`              | Sphinx configuration           |

### Workflow for documentation changes

1. **Create a branch**:

   ```bash
   git checkout -b admin_update_docs
   ```

2. **Edit documentation files** in `docs/source/`

   - Use Markdown (`.md`) for content pages
   - Use reStructuredText (`.rst`) for structural files

3. **Build and preview**:

   ```bash
   python scripts/build_docs.py
   python scripts/serve_docs.py
   ```

4. **Review your changes** in the browser

5. **Rebuild as needed** - The build is fast, so rebuild frequently to check your changes

6. **Commit and push**:

   ```bash
   git add docs/source/
   git commit -m "Update documentation"
   git push origin admin_update_docs
   ```

7. **Create a pull request** on GitHub

## Documentation style guide

### Markdown guidelines

- Use `#` for top-level headings, `##` for sections, `###` for subsections
- Use code blocks with language specification: `` python`,  ``bash\`, etc.
- Use **bold** for emphasis on key terms
- Use `inline code` for commands, file names, and code snippets
- Use bullet lists for unordered items
- Use numbered lists for sequential steps

### Code examples

Always specify the language for code blocks:

````markdown
```python
from hed import schema
schema = schema.load_schema('8.4.0')
```
````

For PowerShell commands:

````markdown
```powershell
pip install -r requirements-dev.txt
```
````

### Links

**Internal links** (to other documentation pages):

```markdown
See the [Developer Guide](developer_guide.md) for more information.
```

**External links**:

```markdown
Visit the [HED Schema Browser](https://www.hedtags.org/hed-schema-browser)
```

**File links** (use relative paths from docs root):

```markdown
[Repository Structure](../../README.md)
```

## Common tasks

### Adding a new page

1. Create a new `.md` file in `docs/source/`
2. Add it to the `toctree` in `index.rst`:
   ```rst
   .. toctree::
      :maxdepth: 2
      :caption: Contents:

      introduction
      user_guide
      your_new_page
   ```
3. Build and verify it appears in the navigation

### Updating schema information

When a new schema version is released:

1. Update version numbers in `schemas_reference.md`
2. Add new links for the new version
3. Update the version table in `introduction.md`
4. Check that all DOI links are correct

### Adding images

1. Place images in `docs/source/_static/images/`
2. Reference in Markdown:
   ```markdown
   ![Alt text](_static/images/your-image.png)
   ```

## Troubleshooting

### Build errors

**Problem**: Module not found errors

```
ModuleNotFoundError: No module named 'myst_parser'
```

**Solution**: Reinstall dependencies

```bash
pip install -r docs/requirements.txt
```

### Warnings

Sphinx may show warnings about:

- Missing references
- Duplicate labels
- Malformed links

Fix these warnings before committing - they indicate potential broken links or incorrect formatting.

### Port already in use

**Problem**: `Address already in use` when running serve_docs.py

**Solution**: Use a different port

```bash
python scripts/serve_docs.py --port 8001
```

Or find and stop the process using port 8000.

## CI/CD integration

Documentation is automatically built and deployed:

- **On every push to main**: Documentation is built and deployed to GitHub Pages
- **On pull requests**: Documentation is built (but not deployed) to verify no errors

The deployed documentation is available at the GitHub Pages URL for the repository.

## Getting help

- **Documentation issues**: Post on [GitHub Issues](https://github.com/hed-standard/hed-schemas/issues)
- **Questions**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Sphinx help**: [Sphinx documentation](https://www.sphinx-doc.org/)
- **MyST (Markdown) help**: [MyST documentation](https://myst-parser.readthedocs.io/)
