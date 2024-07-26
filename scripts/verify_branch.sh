#!/bin/bash
# Script to verify changes are on the correct branch
# only applies to branches that start with develop-

# Try to use the BRANCH_NAME environment variable first
if [ -z "$BRANCH_NAME" ]; then
    # Environment variable is empty or not set, fallback to git command
    echo "Finding branch name from git"
    branch_name=$(git rev-parse --abbrev-ref HEAD)
else
    # Use the environment variable
    branch_name=$BRANCH_NAME
fi


# Echo the branch name and changed files
echo "branch_name: $branch_name"
echo "files: $@"

branch_prefix=${branch_name%%_*}

# Check if the extracted branch prefix is "admin"
if [[ "$branch_prefix" == "admin" ]]; then
    echo "Any changes allowed on admin branches."
    exit 0
fi

# Verify the branch name is correct after modification
echo "Processed branch_name: $branch_prefix"

# Define base file pattern based on branch name
if [[ "branch_prefix" == "standard" ]]; then
    base_pattern="standard_schema/"
else
    base_pattern="library_schemas/${branch_prefix}/"
fi

# Define the second pattern by appending 'prerelease' to the base pattern
file_pattern="${base_pattern}prerelease/"

# Check if the file paths start with the defined pattern for specified extensions
for file in "$@"; do  # "$@" will contain the list of modified files passed by pre-commit
    extension="${file##*.}"
    # Check files based on their extension
    if [[ "$extension" == "xml" || "$extension" == "mediawiki" || "$extension" == "tsv" ]]; then
        if [[ "$file" != "$file_pattern"* ]]; then
            error_message+="Error: '$file' with extension .$extension should start with '$file_pattern'\n"
        else
            # Call the validation function if the file pattern is correct
            if ! hed_validate_schemas "$file" --add-all-extensions; then
                error_message+="Error: Validation failed for '$file'.\n"
            fi
        fi
    else
        # Allow other files to be modified anywhere under the base pattern directory
        if [[ "$file" != "$base_pattern"* ]]; then
            error_message+="Error: '$file' should not be modified on this branch.  Only files under '$base_pattern' directory\n"
        fi

    fi
done

# Print all accumulated errors and exit if there were any
if [[ -n "$error_message" ]]; then
    echo -e "$error_message"
    exit 1
fi
