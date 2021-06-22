#!/bin/env bash
set -e
osc_api_version=$1

if [ -z "$osc_api_version" ]; then
    echo "run $0 with version tag as argument, abort."
    exit 1
fi

root=$(cd "$(dirname $0)/../.." && pwd)

# build new version number
local_sdk_version=$(cat setup.py |grep "version="|cut -d "'" -f 2)
local_sdk_version_major=$(echo $local_sdk_version | cut -d '.' -f 1)
local_sdk_version_minor=$(echo $local_sdk_version | cut -d '.' -f 2)
local_sdk_version_patch=$(echo $local_sdk_version | cut -d '.' -f 3)
new_sdk_version_minor=$(( local_sdk_version_minor + 1 ))
new_sdk_version="$local_sdk_version_major.$new_sdk_version_minor.0"

echo "$new_sdk_version" > $root/sdk_version

branch_name="autobuild-$new_sdk_version"
git branch -m $branch_name

# Update osc-api version
cd "$root/osc_sdk_python/osc-api"
git reset --hard $osc_api_version
cd ..
git add osc-api
cd "$root"

# Setup new SDK version
for f in README.md setup.py osc_sdk_python/authentication.py; do 
    sed -i 's/$local_sdk_version_major\.$local_sdk_version_minor\.local_sdk_version_patch/$local_sdk_version_major\.$new_sdk_version_minor\.0/' $f
    git add "$root/$f"
done

# Setup git && commit
git config user.name "Outscale Bot"
git config user.email "opensource+bot@outscale.com"
commit_msg="osc-sdk-python v$new_sdk_version

 - SDK update for Outscale API v$osc_api_version
"
git commit -sm "$commit_msg"
