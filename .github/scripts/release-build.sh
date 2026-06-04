#!/bin/env bash
set -e
service=${1:-all}
osc_api_version=${2#v}
oks_api_url=${3:-https://docs.outscale.com/_attachments/oks.yaml}

case "$service" in
    osc|oks|all)
        ;;
    *)
        echo "Unknown service '$service'. Expected one of: osc, oks, all."
        exit 1
        ;;
esac

if [ "$service" != "oks" ] && [ -z "$osc_api_version" ]; then
    echo "run $0 with an OSC API version when building service '$service', abort."
    exit 1
fi

if [ "$service" != "osc" ] && [ -z "$oks_api_url" ]; then
    echo "run $0 with an OKS OpenAPI URL when building service '$service', abort."
    exit 1
fi

root=$(cd "$(dirname $0)/../.." && pwd)
cd "$root"

# build new version number
local_sdk_version=$(cat $root/osc_sdk_python/VERSION)
local_sdk_version_major=$(echo $local_sdk_version | cut -d '.' -f 1)
local_sdk_version_minor=$(echo $local_sdk_version | cut -d '.' -f 2)
local_sdk_version_patch=$(echo $local_sdk_version | cut -d '.' -f 3)
new_sdk_version_minor=$(( local_sdk_version_minor + 1 ))
new_sdk_version="$local_sdk_version_major.$new_sdk_version_minor.0"

if [ "$service" = "osc" ] || [ "$service" = "all" ]; then
    # Update osc-api version
    curl --retry 10 -o "${root}/osc_sdk_python/resources/osc/api.yaml" "https://raw.githubusercontent.com/outscale/osc-api/refs/tags/${osc_api_version}/outscale.yaml"
    uv run python -m osc_sdk_python.codegen.generator osc
    git add "${root}/osc_sdk_python/resources/osc" "${root}/osc_sdk_python/generated/osc"
fi

if [ "$service" = "oks" ] || [ "$service" = "all" ]; then
    # Update oks-api version
    curl --retry 10 -o "${root}/osc_sdk_python/resources/oks/api.yaml" "${oks_api_url}"
    uv run python -m osc_sdk_python.codegen.generator oks
    git add "${root}/osc_sdk_python/resources/oks" "${root}/osc_sdk_python/generated/oks"
fi

# Setup new SDK version
for f in "$root/README.md" "$root/osc_sdk_python/VERSION"; do
    sed -i "s/$local_sdk_version_major\.$local_sdk_version_minor\.$local_sdk_version_patch/$local_sdk_version_major\.$new_sdk_version_minor\.0/g" "$f"
    git add "$f"
done

uv version "$(cat osc_sdk_python/VERSION)"
