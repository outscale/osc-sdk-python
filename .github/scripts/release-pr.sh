#!/bin/env bash
set -e
osc_api_version=$1

if [ -z "$osc_api_version" ]; then
    echo "run $0 with version tag as argument, abort."
    exit 1
fi

if [ -z "$GH_TOKEN" ]; then
    echo "GH_TOKEN is missing, abort."
    exit 1
fi

root=$(cd "$(dirname $0)/../.." && pwd)

new_sdk_version=$(cat $root/osc_sdk_python/VERSION)
major=$(echo $new_sdk_version | cut -d '.' -f 1)
branch_name="autobuild-$new_sdk_version"

# https://docs.github.com/en/free-pro-team@latest/rest/reference/pulls#create-a-pull-request
result=$(curl -s -X POST -H "Authorization: token $GH_TOKEN" -d "{\"head\":\"$branch_name\",\"base\":\"master\",\"title\":\"SDK v$new_sdk_version\",\"body\":\"Automatic build of SDK v$new_sdk_version version based on Outscale API v$osc_api_version\"}" "https://api.github.com/repos/outscale/osc-sdk-python/pulls")

errors=$(echo $result | jq .errors)

if [ "$errors" != "null" ]; then
    echo "errors while creating pull request, abort."
    exit 1
fi
