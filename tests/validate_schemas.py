import sys
from hed.schema import load_schema, from_string, load_schema_version
from hed.errors import get_printable_issue_string, HedFileError


def main(arg_list=None):
    # Trigger a local cache hit
    _ = load_schema_version("8.2.0")
    validation_issues = []
    saving_failures = []
    if not arg_list:
        arg_list = sys.argv[1:]

    for file_path in arg_list:  # sys.argv[1:] contains all the arguments passed to the script
        print(file_path)
        try:
            if file_path.endswith(".xml") or file_path.endswith(".mediawiki"):
                base_schema = load_schema(file_path)
                issues = base_schema.check_compliance()
                if issues:
                    validation_issues.extend(issues)
                    print(get_printable_issue_string(issues, title=file_path))

                mediawiki_string = base_schema.get_as_mediawiki_string()
                reloaded_schema = from_string(mediawiki_string, schema_format=".mediawiki")

                if reloaded_schema != base_schema:
                    error_text = f"Failed to reload {file_path} as mediawiki.  There is either a problem with the source file, or the saving/loading code."
                    saving_failures.append(error_text)
                    print(error_text)

                xml_string = base_schema.get_as_xml_string()
                reloaded_schema = from_string(xml_string, schema_format=".xml")

                if reloaded_schema != base_schema:
                    error_text = f"Failed to reload {file_path} as xml.  There is either a problem with the source file, or the saving/loading code."
                    saving_failures.append(error_text)
                    print(error_text)
        except HedFileError as e:
            print(f"Saving/loading error: {e.message}")
            if e.issues:
                print(get_printable_issue_string(e.issues, title=file_path))
            continue

    # if saving_failures:
    #     for issue in saving_failures:
    #         print(issue)

    if validation_issues or saving_failures:
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
