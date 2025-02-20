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
if [[ "$branch_prefix" == "standard" ]]; then
    base_pattern="standard_schema/"
else
    base_pattern="library_schemas/${branch_prefix}/"
fi

# Valid location for schemas
file_pattern="${base_pattern}prerelease/"

# Banned locations for ANY changes
declare -a banned_patterns=(
    "${base_pattern}hedxml/"
    "${base_pattern}hedwiki/"
    "${base_pattern}hedtsv/"
)

for file in "$@"; do  # "$@" will contain the list of modified files passed by pre-commit
    extension="${file##*.}"
    # First check schemas in the correct location, and validate them.
    if [[ "$extension" == "xml" || "$extension" == "mediawiki" || "$extension" == "tsv" ]]; then
        if [[ "$file" != "$file_pattern"* ]]; then
            error_message+="Error: '$file' with extension .$extension should start with '$file_pattern'\n"
        else
            if [ -n "$VALIDATE_ALL" ]; then
                # Verify all schemas match
                if ! hed_validate_schemas "$file" --add-all-extensions; then
                    error_message+="Error: Validation failed for '$file'.\n"
                fi
            else
                if ! hed_validate_schemas "$file"; then
                    error_message+="Error: Validation failed for '$file'.\n"
                fi
            fi
        fi
    else
        is_banned=false

        # Check against each banned pattern
        for banned_pattern in "${banned_patterns[@]}"; do
            if [[ "$file" == "$banned_pattern"* ]]; then
                error_message+="Error: '$file' is in a restricted directory '$banned_pattern'. Modifications are not allowed in this directory.\n"
                is_banned=true
                break
            fi
        done

        # Check if the file is not under the base pattern and not already banned
        if [[ "$file" != "$base_pattern"* && "$is_banned" == false ]]; then
            error_message+="Error: '$file' should not be modified on this branch. Only files under '$base_pattern' directory should be modified.\n"
        fi
    fi
done

# Print all accumulated errors and exit if there were any
if [[ -n "$error_message" ]]; then
    echo -e "$error_message"
    exit 1
fi
