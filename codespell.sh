#!/bin/bash

# This is a mirror of the codespell.yaml command

# Prepare directory list
DIRS=$(find . -type d -name 'prerelease' | tr '\n' ' ')

# Run codespell on docs/source, root markdown files, and prerelease directories
codespell docs/source *.md $DIRS
