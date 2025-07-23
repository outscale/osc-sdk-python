#!/bin/env bash
set -e
osc_api_version=$1

if [ -z "$osc_api_version" ]; then
    echo "run $0 with version tag as argument, abort."
    exit 1
fi

root=$(cd "$(dirname $0)/../.." && pwd)

# build new version number
local_sdk_version=$(cat $root/osc_sdk_python/VERSION)
local_sdk_version_major=$(echo $local_sdk_version | cut -d '.' -f 1)
local_sdk_version_minor=$(echo $local_sdk_version | cut -d '.' -f 2)
local_sdk_version_patch=$(echo $local_sdk_version | cut -d '.' -f 3)
new_sdk_version_minor=$(( local_sdk_version_minor + 1 ))
new_sdk_version="$local_sdk_version_major.$new_sdk_version_minor.0"

branch_name="autobuild-$new_sdk_version"
git branch -m $branch_name

# Update osc-api version
cd "$root/osc_sdk_python/osc-api"
git reset --hard $osc_api_version
cd ..
git add osc-api
cd "$root"

# Setup new SDK version
for f in "$root/README.md" "$root/osc_sdk_python/VERSION"; do
    sed -i "s/$local_sdk_version_major\.$local_sdk_version_minor\.$local_sdk_version_patch/$local_sdk_version_major\.$new_sdk_version_minor\.0/g" "$f"
    git add "$f"
done

# Setup git && commit
git config user.name "Outscale Bot"
git config user.email "opensource+bot@outscale.com"
commit_msg="🔖 release: osc-sdk-python v$new_sdk_version

 - SDK update for Outscale API $osc_api_version
"
git commit -sm "$commit_msg"
