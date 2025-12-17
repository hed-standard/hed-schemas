Repository Structure
====================

This page describes the structure and organization of the hed-schemas repository.

Directory Organization
----------------------

Root Directories
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

Configuration Files
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

Schema Version Structure
------------------------

Released Versions
~~~~~~~~~~~~~~~~~

Released schema versions are stored in format-specific directories:

* ``hedxml/HED8.4.0.xml`` - Released XML schema
* ``hedwiki/HED8.4.0.mediawiki`` - Released MediaWiki schema
* ``hedjson/HED8.4.0.json`` - Released JSON schema
* ``hedtsv/HED8.4.0/`` - Released TSV schema files

Prerelease Versions
~~~~~~~~~~~~~~~~~~~

All schema development happens in the ``prerelease/`` subdirectory:

* ``prerelease/HED8.5.0.mediawiki`` - Working schema (edit this)
* ``prerelease/HED8.5.0.xml`` - Auto-generated XML
* ``prerelease/HED8.5.0.json`` - Auto-generated JSON  
* ``prerelease/hedtsv/`` - Auto-generated TSV files
* ``prerelease/PRERELEASE_CHANGES.md`` - Documented changes
* ``prerelease/PROPOSED.md`` - Proposed future changes

Workflow Summary
----------------

Schema Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create branch with appropriate prefix (``standard_*``, ``score_*``, etc.)
2. Edit ``.mediawiki`` file in ``prerelease/`` directory
3. Document changes in ``PRERELEASE_CHANGES.md``
4. Push to GitHub
5. CI/CD automatically converts and validates
6. Create pull request
7. Merge after review

Release Workflow
~~~~~~~~~~~~~~~~

1. Update version in schema header
2. Update ``CHANGELOG.md``
3. Move files from ``prerelease/`` to release directories
4. Create git tag
5. Create GitHub release
6. DOI automatically updated via Zenodo

File Naming Conventions
-----------------------

Standard Schema
~~~~~~~~~~~~~~~

* ``HED8.4.0.xml`` - Version number only
* ``HED8.4.0.mediawiki`` - Version number only
* ``HEDLatest.xml`` - Symlink/copy to latest version

Library Schemas
~~~~~~~~~~~~~~~

* ``HED_score_2.1.0.xml`` - Library name and version
* ``HED_lang_1.1.0.mediawiki`` - Library name and version
* ``HED_score_Latest.xml`` - Symlink/copy to latest version

See Also
--------

* :doc:`developer_guide` - Complete schema development guide
* :doc:`user_guide` - Using HED schemas
* :doc:`schemas_reference` - Detailed schema information


Web Services Demos
------------------

Examples demonstrating HED web service usage.

.. mat:autofunction:: web_services_demos.demoEventRemodelingServices

.. mat:autofunction:: web_services_demos.demoEventSearchServices

.. mat:autofunction:: web_services_demos.demoEventServices

.. mat:autofunction:: web_services_demos.demoGetServices

.. mat:autofunction:: web_services_demos.demoLibraryServices

.. mat:autofunction:: web_services_demos.demoSidecarServices

.. mat:autofunction:: web_services_demos.demoSpreadsheetServices

.. mat:autofunction:: web_services_demos.demoStringServices

.. mat:autofunction:: web_services_demos.exampleGenerateSidecar

.. mat:autofunction:: web_services_demos.getDemoData

.. mat:autofunction:: web_services_demos.getHostOptions

.. mat:autofunction:: web_services_demos.getRequestTemplate

.. mat:autofunction:: web_services_demos.getSessionInfo

.. mat:autofunction:: web_services_demos.outputReport

.. mat:autofunction:: web_services_demos.runAllDemos

.. mat:autofunction:: web_services_demos.runDemo


Utilities
---------

Helper functions for common operations.

.. mat:autofunction:: utilities.events2string

.. mat:autofunction:: utilities.filterDirectories

.. mat:autofunction:: utilities.filterFiles

.. mat:autofunction:: utilities.getFileList

.. mat:autofunction:: utilities.rectify_events

.. mat:autofunction:: utilities.separateFiles

.. mat:autofunction:: utilities.str2lines
