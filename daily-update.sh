#!/bin/bash
set -euo pipefail

UPSTREAM_REPO="4v3ngR/kwin-effects-glass"
SPEC_FILE="kwin-effects-glass.spec"
NAME="github-actions[bot]"
EMAIL="github-actions[bot]@users.noreply.github.com"


# Get latest release tag from GitHub API
LATEST_TAG=$(curl -sL "https://api.github.com/repos/$UPSTREAM_REPO/releases/latest" | jq -r ".tag_name")
# Get latest plasma version from Fedora Rawhide
LATEST_PLASMA=$(curl -sL "https://mdapi.fedoraproject.org/rawhide/pkg/libplasma" | jq -r '.version')

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

    # Get version number (remove 'v' prefix and suffix)
    LATEST_TAG_NO_V=${LATEST_TAG#v}
    NEW_VER=${LATEST_TAG_NO_V%%-*}

    # Get upstream release (suffix)
    NEW_UPSTREAM_REL=${LATEST_TAG#*-}

    # Create release string
    NEW_REL="$NEW_UPSTREAM_REL.plasma$LATEST_PLASMA%{?dist}"

    # Get changelog (tbh I don't really remember how the LOG parsing works, but it is working (._.;) )
    HEADER="* $(date '+%a %b %d %Y') ${NAME} <${EMAIL}> - ${LATEST_TAG_NO_V}"
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
    sed -i "s|^Release:.*|Release: $NEW_REL|" "$SPEC_FILE"

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

    # Get upstream release (suffix)
    NEW_UPSTREAM_REL=${LATEST_TAG#*-}

    # Create release string
    NEW_REL="$NEW_UPSTREAM_REL.plasma$LATEST_PLASMA%{?dist}"

    # Replace the "# Plasma:" line
    sed -i "s|^# Plasma:.*|# Plasma: $LATEST_PLASMA|" "$SPEC_FILE"

    # Replace the "Release:" line
    sed -i "s|^Release:.*|Release: $NEW_REL|" "$SPEC_FILE"

    # Commit and push changes
    git config user.name $NAME
    git config user.email $EMAIL

    git add "$SPEC_FILE"
    git commit -m "Rebuild using Plasma ($LATEST_PLASMA)"
    git push
else
    echo "Tags match. No update needed."
fi
