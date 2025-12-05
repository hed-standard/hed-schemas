#!/usr/bin/env python
"""Convert HED schema from XML to JSON format with proper attribute inheritance.

This script generates JSON schema files that correctly propagate inherited
attributes like extensionAllowed from parent to child tags.

Usage:
    python xml_to_json.py <xml_file> [output_json_file]

Example:
    python xml_to_json.py ../standard_schema/hedxml/HED8.4.0.xml ../standard_schema/hedjson/HED8.4.0.json
"""

import argparse
import json
import sys
from pathlib import Path

# Add hed-python to path if needed
try:
    from hed import schema as hedschema
    from hed.schema.hed_schema_constants import HedKey
except ImportError:
    print("Error: hed-python (hedtools) is required. Install with: pip install hedtools")
    sys.exit(1)


# Attributes that should be included in JSON output (with inheritance)
TAG_ATTRIBUTES = [
    'extensionAllowed',
    'requireChild',
    'unique',
    'reserved',
    'tagGroup',
    'topLevelTagGroup',
    'recommended',
    'required',
    'suggestedTag',
    'relatedTag',
    'valueClass',
    'unitClass',
    'defaultUnits',
    'takesValue',
]

# Additional attributes that may be present
EXTRA_ATTRIBUTES = [
    'hedId',
    'rooted',
    'annotation',
    'deprecatedFrom',
    'inLibrary',
]


def get_tag_children(tag_entry):
    """Get list of direct child tag names."""
    children = []
    for child in tag_entry.children.values():
        children.append(child.short_tag_name)
    return children


def build_tag_dict(tag_entry):
    """Build JSON dictionary for a single tag with inherited attributes.

    Note: Boolean attributes like extensionAllowed use inherited values (from ancestors).
    Other attributes like suggestedTag only use direct values from this tag.
    """
    tag_dict = {
        'short_form': tag_entry.short_tag_name,
        'long_form': tag_entry.long_tag_name,
        'description': tag_entry.description or '',
        'parent': tag_entry.parent.short_tag_name if tag_entry.parent else None,
        'children': get_tag_children(tag_entry),
        'attributes': {}
    }

    # Build attributes dictionary
    attrs = tag_dict['attributes']

    # Boolean attributes - check inherited value (these should propagate from ancestors)
    for attr_name in ['extensionAllowed', 'requireChild', 'unique', 'reserved',
                      'tagGroup', 'topLevelTagGroup', 'recommended', 'required', 'takesValue']:
        # has_attribute checks inherited attributes for DataProperty/ObjectProperty
        attrs[attr_name] = tag_entry.has_attribute(attr_name)

    # List/tag reference attributes - use DIRECT values only (not inherited)
    # These are AnnotationProperty in the ontology, not inherited by design
    for attr_name in ['suggestedTag', 'relatedTag', 'valueClass', 'unitClass']:
        value = tag_entry.attributes.get(attr_name)  # Direct attribute only
        if value:
            # These come as comma-separated strings
            attrs[attr_name] = [v.strip() for v in value.split(',') if v.strip()]
        else:
            attrs[attr_name] = []

    # Default units - single value, direct attribute only
    default_units = tag_entry.attributes.get('defaultUnits')
    attrs['defaultUnits'] = default_units

    # Extra attributes that are explicitly set (not inherited)
    hed_id = tag_entry.attributes.get('hedId')
    if hed_id:
        attrs['hedId'] = hed_id

    rooted = tag_entry.attributes.get('rooted')
    if rooted:
        attrs['rooted'] = rooted

    annotation = tag_entry.attributes.get('annotation')
    if annotation:
        # Annotation can be a single string or list
        if isinstance(annotation, list):
            attrs['annotation'] = annotation
        else:
            annotations = [a.strip() for a in annotation.split(',') if a.strip()]
            if len(annotations) == 1:
                attrs['annotation'] = annotations[0]
            else:
                attrs['annotation'] = annotations

    deprecated_from = tag_entry.attributes.get('deprecatedFrom')
    if deprecated_from:
        attrs['deprecatedFrom'] = deprecated_from

    in_library = tag_entry.attributes.get('inLibrary')
    if in_library:
        attrs['inLibrary'] = in_library

    return tag_dict


def convert_schema_to_json(hed_schema):
    """Convert a HedSchema object to JSON-compatible dictionary."""
    output = {
        'version': hed_schema.version_number,
    }

    # Add header attributes
    for key, value in hed_schema.header_attributes.items():
        if key != 'version':
            output[key] = value

    # Add prologue
    if hed_schema.prologue:
        output['prologue'] = hed_schema.prologue

    # Build tags dictionary (flat, keyed by short_form)
    tags_dict = {}
    for tag_entry in hed_schema.tags.all_entries:
        tag_dict = build_tag_dict(tag_entry)
        tags_dict[tag_entry.short_tag_name] = tag_dict

    output['tags'] = tags_dict

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Convert HED schema from XML to JSON with proper attribute inheritance'
    )
    parser.add_argument('xml_file', help='Input XML schema file')
    parser.add_argument('output_json', nargs='?', help='Output JSON file (defaults to same name with .json extension)')
    parser.add_argument('--indent', type=int, default=2, help='JSON indentation (default: 2)')

    args = parser.parse_args()

    xml_path = Path(args.xml_file)
    if not xml_path.exists():
        print(f"Error: XML file not found: {xml_path}")
        sys.exit(1)

    # Determine output path
    if args.output_json:
        json_path = Path(args.output_json)
    else:
        json_path = xml_path.with_suffix('.json')

    print(f"Loading schema from: {xml_path}")

    # Load schema using hed-python
    hed_schema = hedschema.load_schema(str(xml_path))

    print(f"Schema version: {hed_schema.version_number}")
    print(f"Library: {hed_schema.library or '(standard)'}")
    print(f"Total tags: {len(list(hed_schema.tags.all_entries))}")

    # Convert to JSON
    json_data = convert_schema_to_json(hed_schema)

    # Count tags with extensionAllowed=true (including inherited)
    ext_allowed_count = sum(
        1 for tag_dict in json_data['tags'].values()
        if tag_dict['attributes'].get('extensionAllowed', False)
    )
    print(f"Tags with extensionAllowed=true (including inherited): {ext_allowed_count}")

    # Write JSON
    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=args.indent, ensure_ascii=False)

    print(f"JSON schema written to: {json_path}")


if __name__ == '__main__':
    main()
