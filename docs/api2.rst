Repository structure
====================

This page describes the structure and organization of the hed-schemas repository.

Directory organization
----------------------

Root directories
~~~~~~~~~~~~~~~~

The repository is organized into the following main directories:

**standard_schema/**
  Contains the HED standard schema in all formats
  
  * ``hedxml/`` - XML format schemas
  * ``hedwiki/`` - MediaWiki format schemas  
  * ``hedjson/`` - JSON format schemas
  * ``hedtsv/`` - TSV format schemas
  * ``prerelease/`` - Working versions under development
  * ``README.md`` - Schema documentation
  * ``CHANGELOG.md`` - Version history
  * ``LICENSE`` - MIT license

**library_schemas/**
  Contains all HED library schemas
  
  * ``score/`` - SCORE clinical EEG vocabulary
  * ``lang/`` - Language experiment vocabulary
  * ``slam/`` - Sensor location and motion vocabulary
  * ``mouse/`` - Mouse/rodent experiment vocabulary
  * ``testlib/`` - Testing vocabulary
  
  Each library has the same subdirectory structure as standard_schema.

**scripts/**
  Utility scripts for schema validation and verification
  
  * ``verify_branch.sh`` - Pre-commit hook for branch validation

**docs/**
  Documentation source files (this documentation)
  
  * ``source/`` - Sphinx documentation source
  * ``make.bat`` - Windows documentation build script
  * ``Makefile`` - Unix documentation build script

**.github/workflows/**
  CI/CD pipeline definitions
  
  * ``validate_schemas.yaml`` - Schema validation
  * ``update_and_convert_schemas.yaml`` - Format conversion
  * ``add_hed_ids.yaml`` - HedId assignment
  * ``verify_source_branch.yaml`` - Branch verification
  * ``codespell.yaml`` - Spell checking
  * ``mdformat.yaml`` - Markdown formatting
  * ``links.yaml`` - Link validation
  * ``deploy-docs.yaml`` - Documentation deployment

Configuration files
~~~~~~~~~~~~~~~~~~~

**library_data.json**
  Defines HedId ranges for each library schema::
  
    {
      "": {"id_range": [10000, 39999]},     // standard
      "score": {"id_range": [40000, 59999]},
      "lang": {"id_range": [60000, 79999]},
      "slam": {"id_range": [80000, 99999]},
      "mouse": {"id_range": [100000, 119999]}
    }

**pyproject.toml**
  Project configuration for documentation build

**CONTRIBUTING.md**
  Guidelines for contributing to HED schemas

Schema version vtructure
------------------------

Released versions
~~~~~~~~~~~~~~~~~

Released schema versions are stored in format-specific directories:

* ``hedxml/HED8.4.0.xml`` - Released XML schema
* ``hedwiki/HED8.4.0.mediawiki`` - Released MediaWiki schema
* ``hedjson/HED8.4.0.json`` - Released JSON schema
* ``hedtsv/HED8.4.0/`` - Released TSV schema files

Prerelease versions
~~~~~~~~~~~~~~~~~~~

All schema development happens in the ``prerelease/`` subdirectory:

* ``prerelease/HED8.5.0.mediawiki`` - Working schema (edit this)
* ``prerelease/HED8.5.0.xml`` - Auto-generated XML
* ``prerelease/HED8.5.0.json`` - Auto-generated JSON  
* ``prerelease/hedtsv/`` - Auto-generated TSV files
* ``prerelease/PRERELEASE_CHANGES.md`` - Documented changes
* ``prerelease/PROPOSED.md`` - Proposed future changes

Workflow summary
----------------

Schema development workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create branch with appropriate prefix (``standard_*``, ``score_*``, etc.)
2. Edit ``.mediawiki`` file in ``prerelease/`` directory
3. Document changes in ``PRERELEASE_CHANGES.md``
4. Push to GitHub
5. CI/CD automatically converts and validates
6. Create pull request
7. Merge after review

Release workflow
~~~~~~~~~~~~~~~~

1. Update version in schema header
2. Update ``CHANGELOG.md``
3. Move files from ``prerelease/`` to release directories
4. Create git tag
5. Create GitHub release
6. DOI automatically updated via Zenodo

File naming conventions
-----------------------

Standard schema
~~~~~~~~~~~~~~~

* ``HED8.4.0.xml`` - Version number only
* ``HED8.4.0.mediawiki`` - Version number only
* ``HEDLatest.xml`` - Symlink/copy to latest version

Library schemas
~~~~~~~~~~~~~~~

* ``HED_score_2.1.0.xml`` - Library name and version
* ``HED_lang_1.1.0.mediawiki`` - Library name and version
* ``HED_score_Latest.xml`` - Symlink/copy to latest version

See also
--------

* :doc:`developer_guide` - Complete schema development guide
* :doc:`user_guide` - Using HED schemas
* :doc:`schemas_reference` - Detailed schema information
