#!/bin/env bash
set -e

root=$(cd "$(dirname $0)/../.." && pwd)
new_sdk_version=$(cat $root/sdk_version)
branch_name="autobuild-$new_sdk_version"

if [ -z "$SSH_PRIVATE_KEY" ]; then
    echo "SSH_PRIVATE_KEY is missing, abort."
    exit 1
fi

echo "$SSH_PRIVATE_KEY" > $root/bot.key
GIT_SSH_COMMAND="ssh -i $root/bot.key" git push -f origin $branch_name
