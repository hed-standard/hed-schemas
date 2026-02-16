#!/usr/bin/env python3
"""
Script to verify that changes are on the correct branch and in appropriate directories.

Branch naming conventions:
- standard_*: Only standard_schema/ can be modified
- score_*, lang_*, slam_*, mouse_*, testlib_*: Only corresponding library_schemas/{name}/ can be modified
- admin_*: Any files can be modified (for docs, scripts, CI/CD)

Schema files (.xml, .mediawiki, .tsv) must be in prerelease/ subdirectories.
Released schema directories (hedxml/, hedwiki/, hedtsv/, hedjson/) cannot be modified.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


class BranchVerificationError(Exception):
    """Custom exception for branch verification errors."""

    pass


def get_branch_name() -> str:
    """Get the current branch name from environment variable or git."""
    branch_name = os.environ.get("BRANCH_NAME")

    if not branch_name:
        print("Finding branch name from git")
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            branch_name = result.stdout.strip()
        except subprocess.CalledProcessError as e:
            raise BranchVerificationError(
                f"Failed to get branch name from git: {e}"
            ) from e

    return branch_name


def get_branch_prefix(branch_name: str) -> str:
    """Extract the prefix from branch name (everything before first underscore)."""
    return branch_name.split("_")[0] if "_" in branch_name else branch_name


def get_base_pattern(branch_prefix: str) -> str:
    """Get the base directory pattern for the given branch prefix."""
    if branch_prefix == "standard":
        return "standard_schema/"
    else:
        return f"library_schemas/{branch_prefix}/"


def get_banned_patterns(base_pattern: str) -> list[str]:
    """Get list of banned directory patterns where modifications are not allowed."""
    return [
        f"{base_pattern}hedxml/",
        f"{base_pattern}hedwiki/",
        f"{base_pattern}hedtsv/",
        f"{base_pattern}hedjson/",
    ]


def is_schema_file(filepath: str) -> bool:
    """Check if file is a schema file based on extension."""
    schema_extensions = {".xml", ".mediawiki", ".tsv"}
    return Path(filepath).suffix in schema_extensions


def validate_schema_file(filepath: str, validate_all: bool = False) -> tuple[bool, str]:
    """
    Validate a schema file using hed_validate_schemas command.

    Args:
        filepath: Path to schema file to validate
        validate_all: If True, use --add-all-extensions flag

    Returns:
        Tuple of (success, error_message)
    """
    cmd = ["hed_validate_schemas", filepath]
    if validate_all:
        cmd.append("--add-all-extensions")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return (
                False,
                f"Validation failed for '{filepath}':\n{result.stderr or result.stdout}",
            )
        return True, ""
    except FileNotFoundError:
        return (
            False,
            "hed_validate_schemas command not found. Install hed-python tools.",
        )
    except Exception as e:
        return False, f"Error validating '{filepath}': {e}"


def verify_files(
    files: list[str], branch_name: str, validate_all: bool = False
) -> list[str]:
    """
    Verify that changed files comply with branch naming and location rules.

    Args:
        files: List of file paths to verify
        branch_name: Current branch name
        validate_all: If True, validate all schema extensions

    Returns:
        List of error messages (empty if all validations pass)
    """
    errors = []

    print(f"Branch name: {branch_name}")
    print(f"Files to verify: {len(files)}")

    branch_prefix = get_branch_prefix(branch_name)

    # Admin branches can modify anything
    if branch_prefix == "admin":
        print("Any changes allowed on admin branches.")
        return []

    print(f"Branch prefix: {branch_prefix}")

    base_pattern = get_base_pattern(branch_prefix)
    prerelease_pattern = f"{base_pattern}prerelease/"
    banned_patterns = get_banned_patterns(base_pattern)

    print(f"Base pattern: {base_pattern}")
    print(f"Prerelease pattern: {prerelease_pattern}")

    for filepath in files:
        # Normalize path separators
        filepath = filepath.replace("\\", "/")

        # Schema files must be in prerelease directory
        if is_schema_file(filepath):
            if not filepath.startswith(prerelease_pattern):
                errors.append(
                    f"Error: '{filepath}' is a schema file and must be in '{prerelease_pattern}'"
                )
            else:
                # Validate the schema file
                success, error_msg = validate_schema_file(filepath, validate_all)
                if not success:
                    errors.append(f"Error: {error_msg}")
        else:
            # Check if file is in a banned directory
            is_banned = False
            for banned_pattern in banned_patterns:
                if filepath.startswith(banned_pattern):
                    errors.append(
                        f"Error: '{filepath}' is in restricted directory '{banned_pattern}'. "
                        f"Modifications to released schemas are not allowed."
                    )
                    is_banned = True
                    break

            # Check if file is under the correct base pattern
            if not is_banned and not filepath.startswith(base_pattern):
                errors.append(
                    f"Error: '{filepath}' should not be modified on this branch. "
                    f"Only files under '{base_pattern}' directory should be modified."
                )

    return errors


def main():
    """Main entry point for branch verification."""
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("files", nargs="*", help="List of changed files to verify")
    parser.add_argument(
        "--validate-all",
        action="store_true",
        help="Validate all schema extensions (uses --add-all-extensions flag)",
    )
    parser.add_argument(
        "--branch",
        help="Override branch name (default: from BRANCH_NAME env var or git)",
    )

    args = parser.parse_args()

    try:
        # Get branch name
        if args.branch:
            branch_name = args.branch
        else:
            branch_name = get_branch_name()

        # Check if there are files to verify
        if not args.files:
            print("No files to verify.")
            return 0

        # Verify files
        errors = verify_files(args.files, branch_name, args.validate_all)

        # Report results
        if errors:
            print("\n=== VERIFICATION FAILED ===")
            for error in errors:
                print(error)
            return 1
        else:
            print("\n=== VERIFICATION PASSED ===")
            print("All files are correctly placed and valid.")
            return 0

    except BranchVerificationError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
