#!/bin/bash
set -euo pipefail

UPSTREAM_REPO="4v3ngR/kwin-effects-glass"
SPEC_FILE="kwin-effects-glass.spec"
NAME="github-actions[bot]"
EMAIL="github-actions[bot]@users.noreply.github.com"


# Get latest release tag from GitHub API
LATEST_TAG=$(curl -sL "https://api.github.com/repos/$UPSTREAM_REPO/releases/latest" | jq -r ".tag_name")
# Get latest plasma version from GitHub API
LATEST_PLASMA=$(curl -sL "https://api.github.com/repos/KDE/libplasma/tags" | jq -r ".[0].name")

# Get current tag from local spec file
CURRENT_TAG=$(grep "^# Tag:" "$SPEC_FILE" | awk '{print $3}')
# Get current plasma version from local spec file
CURRENT_PLASMA=$(grep "^# Plasma:" "$SPEC_FILE" | awk '{print $3}')

echo "---"
echo "Upstream tag: $LATEST_TAG"
echo "Current spec tag: $CURRENT_TAG"
echo "---"
echo "Upstream plasma version: $LATEST_PLASMA"
echo "Current spec plasma version: $CURRENT_PLASMA"
echo "---"

# Compare and update
if [ "$LATEST_TAG" != "$CURRENT_TAG" ]; then
    echo "New tag found! Updating spec file..."

    # Get version number (remove 'v' prefix and "-*")
    LATEST_TAG_NO_V=${LATEST_TAG#v}
    NEW_VER=${LATEST_TAG_NO_V%%-*}

    # Get release (get everything after '-')
    NEW_REL=${LATEST_TAG#*-}
    # Use 0 if there's nothing after the dash
    if [ "$NEW_REL" = "$LATEST_TAG" ]; then
        NEW_REL=0
    else
        NEW_REL=$((10#$NEW_REL)) # Convert to decimal to avoid being sometimes prefixed by 0
    fi

    # Get changelog
    HEADER="* $(date '+%a %b %d %Y') ${NAME} <${EMAIL}> - ${NEW_VER}-${NEW_REL}"
    LOG=$(curl -sL "https://api.github.com/repos/$UPSTREAM_REPO/compare/$CURRENT_TAG...$LATEST_TAG" | jq -r '.commits[].commit.message | split("\n")[0] | "- " + . | gsub("%"; "%%")')

    if [ -z "$LOG" ] || [ "$LOG" == "null" ]; then
        LOG="- Upstream release $LATEST_TAG"
    fi


    # Replace the "# Tag:" line
    sed -i "s|^# Tag:.*|# Tag: $LATEST_TAG|" "$SPEC_FILE"

    # Replace the "# Plasma:" line
    sed -i "s|^# Plasma:.*|# Plasma: $LATEST_PLASMA|" "$SPEC_FILE"

    # Replace the "Version:" line
    sed -i "s|^Version:.*|Version: $NEW_VER|" "$SPEC_FILE"

    # Replace the "Release:" line
    sed -i "s|^Release:.*|Release: $NEW_REL%{?dist}|" "$SPEC_FILE"

    # Replace "Source0:" line
    sed -i "s|^Source0:.*|Source0: %{url}/archive/$LATEST_TAG.tar.gz|" "$SPEC_FILE"

    # Replace the "%autosetup" line
    sed -i "s|^%autosetup.*|%autosetup -n kwin-effects-glass-$LATEST_TAG_NO_V|" "$SPEC_FILE"

    # Add to the changelog
    sed -n '1,/^%changelog/p' "$SPEC_FILE" > spec.tmp
    echo "$HEADER" >> spec.tmp
    echo "$LOG" >> spec.tmp
    echo "" >> spec.tmp
    sed '1,/^%changelog/d' "$SPEC_FILE" >> spec.tmp
    mv spec.tmp "$SPEC_FILE"

    # Commit and push changes
    git config user.name $NAME
    git config user.email $EMAIL

    git add "$SPEC_FILE"
    git commit -m "Update the spec file to match upstream ($LATEST_TAG)"
    git push
elif [ "$LATEST_PLASMA" != "$CURRENT_PLASMA" ]; then
    echo "Newer Plasma version available! Rebuilding..."

    # Get current release number from local spec file
    CURRENT_REL=$(grep "^Release:" "$SPEC_FILE" | awk '{print $2}' | cut -d '%' -f 1)
    # Bump the release number by incrementing the minor version (e.g. 1.9 -> 1.10)
    BUMPED_REL=$(echo "$CURRENT_REL" | awk -F. '{if (NF>1) print $1 "." $2+1; else print $1+0.1}')

    # Replace the "# Plasma:" line
    sed -i "s|^# Plasma:.*|# Plasma: $LATEST_PLASMA|" "$SPEC_FILE"

    # Replace the "Release:" line
    sed -i "s|^Release:.*|Release: $BUMPED_REL%{?dist}|" "$SPEC_FILE"

    # Commit and push changes
    git config user.name $NAME
    git config user.email $EMAIL

    git add "$SPEC_FILE"
    git commit -m "Rebuild using Plasma ($LATEST_PLASMA)"
    git push
else
    echo "Tags match. No update needed."
fi
