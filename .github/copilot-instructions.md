# HED-Schemas repository developer instructions

> **Local environment**: If `.status/local-environment.md` exists in this repository, read it first — it contains machine-specific details (OS, shell, virtual environment paths) that override generic assumptions.

When you create summaries of what you did, always put them in a `.status/` directory at the root of the repository.

## Project overview
HED (Hierarchical Event Descriptors) is a framework for systematically describing events and experimental metadata. This repository (`hed-schemas`) contains the **official HED vocabulary schemas** in multiple formats (MediaWiki, XML, JSON, TSV). These schemas define the standardized terms used by researchers to annotate their datasets.

### Related repositories
- **[hed-python](https://github.com/hed-standard/hed-python)**: Python tools for HED validation, analysis, and transformation (`hedtools` package)
- **[hed-specification](https://github.com/hed-standard/hed-specification)**: Formal specification defining HED annotation rules and schema structure
- **[hed-examples](https://github.com/hed-standard/hed-examples)**: Example datasets and use cases
- **[hed-matlab](https://github.com/hed-standard/hed-matlab)**: MATLAB tools for HED processing
- **[hed-javascript](https://github.com/hed-standard/hed-javascript)**: JavaScript validation tools (BIDS validator)
- **[hedtags.org](https://www.hedtags.org)**: Main documentation and resources site

### Online resources
- **Schema Browser**: [hedtags.org/hed-schema-browser](https://www.hedtags.org/hed-schema-browser) - Interactive schema exploration
- **Online Tools**: [hedtools.org](https://hedtools.org) - Web-based schema validation, conversion, and annotation tools
- **Documentation**: [hedtags.org/hed-schemas](https://www.hedtags.org/hed-schemas) - Full schema documentation

## Repository structure

### Standard schema (`standard_schema/`)
The base HED vocabulary used across all domains:
- **Current Version**: 8.4.0 (prerelease: 8.5.0)
- **HedId Range**: 10000-39999
- **DOI**: 10.5281/zenodo.7876037
- Contains fundamental terms for describing events, properties, agents, actions, and experimental structures

### Library schemas (`library_schemas/`)
Specialized vocabularies for specific domains:

1. **score** (HedId: 40000-59999)
   - Clinical neurological annotation vocabulary
   - Based on SCORE standard for EEG/clinical event description
   - Current: 2.1.0, Prerelease: 2.2.0
   - DOI: 10.5281/zenodo.7897596

2. **lang** (HedId: 60000-79999)
   - Linguistic stimuli annotation vocabulary
   - Current: 1.1.0, Prerelease: 1.2.0
   - DOI: 10.5281/zenodo.13987483

3. **slam** (HedId: 80000-99999)
   - Sensor Location and Motion vocabulary
   - Prerelease: 1.0.0

4. **mouse** (HedId: 100000-119999)
   - Mouse/rodent experiment vocabulary
   - Prerelease: 1.0.0

5. **testlib** (HedId: auto-assigned)
   - Testing vocabulary (copy of standard schema)
   - For development/testing purposes only

### Schema formats and directories

Each schema is stored in **four equivalent formats**:
1. **MediaWiki** (`.mediawiki`) - in `hedwiki/` directory
   - Human-readable text format
   - Primary editing format for schema developers
   - Easy to review in GitHub and text editors
   
2. **XML** (`.xml`) - in `hedxml/` directory
   - Format used by all HED tools for validation and analysis
   - Includes XSD schema definition files
   - Never edited directly - generated from MediaWiki or TSV
   
3. **JSON** (`.json`) - in `hedjson/` directory
   - Flat dictionary structure for easy lookups
   - Optimized for AI tools and programmatic access
   - Generated from XML/MediaWiki
   
4. **Tabular TSV** (`.tsv`) - in `hedtsv/` directory
   - Spreadsheet-compatible format
   - Each schema entity type (tags, units, etc.) in separate TSV file
   - May contain additional ontology mapping information

**CRITICAL**: All four formats contain the same semantic information. Conversion between formats is lossless.

## Schema development workflow

### Branch naming convention
Branch names determine which schema can be modified:
- `standard_*`: Only `standard_schema/` can be modified
- `score_*`, `lang_*`, `slam_*`, `mouse_*`: Only corresponding library schema can be modified
- `admin_*`: Any files can be modified (for docs, scripts, CI/CD)

### Development process

1. **Propose Changes**:
   - Post an [issue](https://github.com/hed-standard/hed-schemas/issues) describing proposed changes
   - Discuss with HED Working Group
   - Changes documented in schema's `PROPOSED.md` file

2. **Make Changes in Prerelease**:
   - Create branch with appropriate prefix (e.g., `standard_add_new_term`)
   - **ALL changes go to `prerelease/` subdirectory first**
   - Edit the `.mediawiki` file in `prerelease/` (primary editing format)
   - Document changes in `prerelease/PRERELEASE_CHANGES.md`

3. **Automated Conversion & Validation**:
   - GitHub Actions automatically convert `.mediawiki` → `.xml`, `.json`, `.tsv`
   - Schemas validated on every push
   - Changed files only are processed for efficiency

4. **Release Process**:
   - Update version number following semantic versioning
   - Update `CHANGELOG.md` with comprehensive change documentation
   - Move schema from `prerelease/` to release directories (`hedxml/`, `hedwiki/`, etc.)
   - Tag release and publish DOI via Zenodo

### Semantic versioning rules
HED schemas follow **semantic versioning** (major.minor.patch):
- **Major**: Breaking changes (removed terms, changed meaning)
- **Minor**: Backward-compatible additions (new terms, new attributes)
- **Patch**: Non-functional changes (description improvements, typos)

### Schema metadata
Key schema attributes in header:
- `version`: Current version number
- `withStandard`: Version of standard schema (for library schemas)
- `library`: Library schema name
- `hedId`: Range assigned from `library_data.json`

## Development tools & commands

### Python tools from hed-python
Install tools for schema validation and conversion:
```powershell
pip install git+https://github.com/hed-standard/hed-python.git@main
```

Key commands:
- `hed_validate_schemas <files>`: Validate schema files
- `hed_update_schemas <files>`: Convert between formats
- `hed_cache_schemas --clear`: Clear cached schemas

### CI/CD pipeline

GitHub Actions in `.github/workflows/` (these are the **actual** current workflows):

- **validate_schemas.yaml**: Validates all changed schema files on every push/PR to any branch. Uses Python 3.10 and `hed_validate_schemas`.
- **verify_source_branch.yaml**: On PRs, runs `scripts/verify_branch.py` to enforce branch naming and `prerelease/` placement. Uses Python 3.12.
- **ruff.yaml**: Python lint/format check (pushes/PRs to `main`). Runs `uvx ruff check .` and `uvx ruff format --check .`.
- **typos.yaml**: Spell checking (pushes/PRs to `main`). Runs `uvx typos`.
- **mdformat.yaml**: Markdown formatting check (pushes/PRs to `main`). Checks `docs/` and all `README.md` files. The `.status/` directory is excluded.
- **docs.yaml**: Builds Sphinx documentation and deploys to GitHub Pages (pushes to `main`). Also runs on PRs to verify the build.
- **links.yaml**: Weekly link checker on built HTML docs (scheduled + manual).

### Local validation commands

Run these locally to replicate CI checks before pushing. All tools use `uvx` and require no installation:

```bash
# Schema validation (changed files only — mirrors CI)
pip install git+https://github.com/hed-standard/hed-python.git@main
hed_validate_schemas <path/to/changed.mediawiki>

# Python linting (mirrors ruff.yaml)
uvx ruff check .
uvx ruff format --check .

# Spell checking (mirrors typos.yaml)
uvx typos

# Markdown formatting check (mirrors mdformat.yaml)
uvx --with mdformat-myst mdformat --check --wrap no --number docs/ *.md

# Find and check all README files (mirrors mdformat.yaml)
# On Linux/macOS:
find . -name "README.md" -not -path "./.git/*" -not -path "./.venv/*" -not -path "./.status/*" | \
  xargs uvx --with mdformat-myst mdformat --check --wrap no --number

# Build docs locally
pip install ".[docs]"
sphinx-build -b html docs/ docs/_build/html
```

### Python version requirements

- Schema validation (`validate_schemas.yaml`): Python **3.10**
- All other CI jobs (ruff, typos, mdformat, docs): Python **3.12**
- `pyproject.toml` `requires-python`: `>=3.10,<3.15`

### Pre-commit hooks
Use `scripts/verify_branch.py` to enforce:
- Changes only in appropriate schema directories
- Changes only in `prerelease/` directories
- No modifications to released schemas

## Schema structure & ontology

### Core schema elements
1. **Tags** (Hierarchical vocabulary):
   - Organized in tree structure (e.g., `Event/Action/Move/Reach`)
   - Each tag has: name, description, attributes, HedId
   - Can have value classes (e.g., `Age/#`) or unit classes

2. **Unit Classes & Units**:
   - Define measurement units (time, angle, frequency, etc.)
   - Units have: name, symbol, conversion factors
   - Unit classes define which units are compatible

3. **Value Classes**:
   - Define types of values allowed (text, numeric, dateTime, etc.)

4. **Schema Attributes**:
   - Modify tag behavior (required, unique, topLevelTagGroup, etc.)
   - Define relationships (property domains/ranges for ontology)

5. **Properties**:
   - Define relationships between tags and attributes
   - Used for ontology mapping (OWL/RDF export)

### Ontology integration
Schemas include prefixes and annotations for mapping to external ontologies:
- **Prefixes**: `rdfs:`, `skos:`, `dc:`, `ncit:`, `owl:`, etc.
- **Annotations**: Map HED terms to ontology URIs (e.g., `ncit:C25499`)
- **Properties**: Define relationships (Domain, Range, etc.)
- Enables export to OWL/RDF for semantic web integration

## Key configuration files

### library_data.json
Defines HedId ranges for each library schema:
```json
{
    "": {"id_range": [10000, 39999]},  // standard schema
    "score": {"id_range": [40000, 59999]},
    "lang": {"id_range": [60000, 79999]},
    "slam": {"id_range": [80000, 99999]},
    "mouse": {"id_range": [100000, 119999]}
}
```

### pyproject.toml
Build configuration (this is NOT a Python package repository):
- Defines project metadata
- `[tool.typos]` spell-check configuration (excluded file patterns and allowed words)
- `[tool.ruff]` linting configuration
- Documentation build settings (`[project.optional-dependencies] docs`)

## Documentation

### Sphinx documentation
Source: `docs/`
Build: `docs/make.bat` (Windows) or `docs/Makefile` (Unix)
Output: `docs/_build/html/`

Key documentation files:
- `developer_guide.md`: Guide for schema developers
- `schemas_overview.md`: Overview of all HED schemas
- `api.rst`: Repository structure reference
- `index.rst`: Main documentation landing page

### Schema-specific documentation
Each schema directory contains:
- `README.md`: Schema overview and usage
- `CHANGELOG.md`: Detailed version history
- `CONTRIBUTORS.md`: List of contributors
- `LICENSE`: MIT license
- `prerelease/PRERELEASE_CHANGES.md`: Pending changes
- `prerelease/PROPOSED.md`: Proposed future changes

## Common workflows

### Adding a new term
1. Create branch: `standard_new_term` (or appropriate library prefix)
2. Edit `standard_schema/prerelease/HED8.5.0.mediawiki` (or library prerelease)
3. Add term in hierarchical position with description and attributes
4. Document in `prerelease/PRERELEASE_CHANGES.md`
5. Push - CI will auto-convert to XML/JSON/TSV and validate
6. Create PR, get reviews, merge

### Modifying existing term
1. Create branch with appropriate prefix
2. Edit prerelease `.mediawiki` file
3. Update description, attributes, or position
4. Document change type (minor/patch) in `PRERELEASE_CHANGES.md`
5. Push and create PR

### Creating new schema version
1. Update version number in prerelease schema
2. Consolidate `PRERELEASE_CHANGES.md` into `CHANGELOG.md`
3. Move files from `prerelease/` to release directories
4. Create git tag
5. Update Zenodo DOI

### Validating local schema changes

```powershell
# Install hed-python tools
pip install git+https://github.com/hed-standard/hed-python.git@main

# Validate a schema file
hed_validate_schemas standard_schema/prerelease/HED8.5.0.mediawiki

# Convert MediaWiki to other formats
hed_update_schemas standard_schema/prerelease/HED8.5.0.mediawiki
```

See "Local Validation Commands" under CI/CD Pipeline for the full set of checks that mirror CI.

## Common pitfalls to avoid

1. **Don't edit released schemas**: Only edit files in `prerelease/` directories
2. **Don't edit XML/JSON/TSV directly**: Always edit `.mediawiki` and let CI convert
3. **Branch naming matters**: Use correct prefix or CI will reject your changes
4. **HedId uniqueness**: Never reuse HedIds - they are permanent identifiers
5. **Semantic versioning**: Understand major/minor/patch implications before changing version
6. **Breaking changes**: Removing or significantly changing terms requires major version bump
7. **Library schema coordination**: Library schemas must specify compatible standard schema version
8. **Format equivalence**: All formats contain same information - choose editing format wisely
9. **Case sensitivity**: HED is case-insensitive but maintain consistent capitalization
10. **Markdown heading style**: Use sentence case — capitalize only the first word and proper nouns/acronyms (e.g., `## Schema development workflow`, not `## Schema Development Workflow`)

## Getting Help

- **Issues**: [github.com/hed-standard/hed-schemas/issues](https://github.com/hed-standard/hed-schemas/issues)
- **Working Group**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Documentation**: [hedtags.org](https://www.hedtags.org)
- **Resources**: [hedtags.org/hed-resources](https://www.hedtags.org/hed-resources)
- **Schema Developer Guide**: [hedtags.org/hed-resources/HedSchemaDevelopersGuide.html](https://www.hedtags.org/hed-resources/HedSchemaDevelopersGuide.html)
