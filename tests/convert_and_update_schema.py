import os.path
import sys
from collections import defaultdict
from hed.schema import from_string, load_schema_version
from hed.errors import get_printable_issue_string, HedFileError, SchemaWarnings


from hed.schema.schema_io.df2schema import load_dataframes
from hed.schema.schema_io.ontology_util import update_dataframes_from_schema, save_dataframes
from hed.schema.hed_schema_io import load_schema, from_dataframes
import argparse


def validate_schema(file_path):
    validation_issues = []
    try:
        base_schema = load_schema(file_path)
        issues = base_schema.check_compliance()
        issues = [issue for issue in issues if issue["code"] != SchemaWarnings.SCHEMA_PRERELEASE_VERSION_USED]
        if issues:
            error_message = get_printable_issue_string(issues, title=file_path)
            validation_issues.extend(error_message)

        mediawiki_string = base_schema.get_as_mediawiki_string()
        reloaded_schema = from_string(mediawiki_string, schema_format=".mediawiki")

        if reloaded_schema != base_schema:
            error_text = f"Failed to reload {file_path} as mediawiki.  There is either a problem with the source file, or the saving/loading code."
            validation_issues.append(error_text)

        xml_string = base_schema.get_as_xml_string()
        reloaded_schema = from_string(xml_string, schema_format=".xml")

        if reloaded_schema != base_schema:
            error_text = f"Failed to reload {file_path} as xml.  There is either a problem with the source file, or the saving/loading code."
            validation_issues.append(error_text)
    except HedFileError as e:
        print(f"Saving/loading error: {e.message}")
        error_text = e.message
        if e.issues:
            error_text = get_printable_issue_string(e.issues, title=file_path)
        validation_issues.append(error_text)

    return validation_issues


def main():
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('filenames', nargs='*', help='List of files to process')
    parser.add_argument('--set-ids', action='store_true', help='Set IDs for each file')

    args = parser.parse_args()

    filenames = args.filenames
    set_ids = args.set_ids

    # Trigger a local cache hit (this ensures trying to load withStandard schemas will work properly)
    _ = load_schema_version("8.2.0")

    # Find and group the changed files
    schema_files = defaultdict(set)
    for file_path in filenames:
        basename, extension = os.path.splitext(file_path.lower())
        if extension == ".xml" or extension == ".mediawiki":
            schema_files[basename].add(extension)
            continue
        elif extension == ".tsv":
            tsv_basename = basename.rpartition("_")[0]
            schema_files[tsv_basename].add(extension)
        else:
            print(f"Ignoring file {file_path}")

    all_issues = []
    for basename, extensions in schema_files.items():
        single_schema_issues = []
        for extension in extensions:
            full_path = basename + extension
            issues = validate_schema(full_path)
            if issues:
                print(f"Issues validating {full_path}")
                for issue in issues:
                    print(issue)
            single_schema_issues += issues

        # Todo: make this not reload the schema potentially
        # todo: this should probably check all 3 versions, even if they weren't altered
        if len(extensions) > 1 and not single_schema_issues:
            paths = [basename + extension for extension in extensions]
            schemas = [load_schema(path) for path in paths]
            all_equal = all(obj == schemas[0] for obj in schemas[1:])
            if not all_equal:
                all_issues.append(f"Multiple schemas of type {basename} were modified, and are not equal.\n"
                                  f"Only modify one source schema type at a time(mediawiki, xml, tsv), or modify all 3 at once.")

        all_issues += single_schema_issues

    if all_issues:
        print("Did not attempt to update schemas due to validation failures")
        return 1

    # todo: update this for storing spreadsheets in a sub folder
    # If we are here, we have validated the schemas
    for basename, extensions in schema_files.items():
        # Skip any with multiple extensions or not in pre-release
        if len(extensions) > 1 or "prerelease" not in basename:
            continue
        source_filename = basename + list(extensions)[0]
        source_df_filename = basename + ".tsv"
        schema = load_schema(source_filename)
        print(f"Trying to convert/update file {source_filename}")
        source_dataframes = load_dataframes(source_df_filename)
        # todo: We need a more robust system for if some files are missing
        #  (especially for library schemas which will probably lack some)
        if any(value is None for value in source_dataframes.values()):
            source_dataframes = schema.get_as_dataframes()

        result = update_dataframes_from_schema(source_dataframes, schema, assign_missing_ids=set_ids)

        schema_reloaded = from_dataframes(result)
        schema_reloaded.save_as_mediawiki(basename + ".mediawiki")
        schema_reloaded.save_as_xml(basename + ".xml")
        #directory = os.path.join(os.path.split(converting_filename)[0], "spreadsheets")
        #os.makedirs(directory, exist_ok=True)
        # tsv_name = os.path.join(directory, base_file + ".tsv")
        save_dataframes(source_df_filename, result)


    print("Did not update any schemas")
    return 0


if __name__ == "__main__":
    exit(main())
