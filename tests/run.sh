#!/bin/bash
set -eu
root="$(cd "$(dirname "$0")/.." && pwd)"
venv="$root/tests/venv"
creds="$HOME/.oapi_credentials"

function need {
    local tool="$1"
    if ! hash "$tool"; then
        echo "$tool not found, abort"
        exit 1
    fi
}

function prepapre_venv {
    need virtualenv
    if [ -d "$venv" ]; then
        rm -rf "$venv"
    fi
    virtualenv -p python3 "$venv"
    source "$venv/bin/activate"
    pip install -r "$root/requirements.txt"
}

function check_credentials {
    local c=0
    if ! [ -f "$creds" ]; then
        c=$((c + 1))
    fi

    set +u
    if [ -z "$OSC_ACCESS_KEY" ] || [ -z "$OSC_SECRET_KEY" ] || [ -z "$OSC_REGION" ] ; then
        c=$((c + 1))
    fi
    set -u

    if [ "$c" == "2" ]; then
        echo "No authentification method found."
        echo "Your can either set OSC_ACCESS_KEY, OSC_SECRET_KEY and OSC_REGION env variables or fill $creds file with:"
        cat "$root/oapi_credentials.json"
        echo ""
        exit 1
    fi
}

function run_tests() {
    local result=0
    cd "$root/tests"
    for t in *.py; do
        if ! python "$t"; then
            echo "[!!] $t"
            result=1
        else
            echo "[ok] $t"
        fi
    done
    exit $result
}

function submodule_init() {
    pushd "$root"
    git submodule update --init .
    popd
}

function main {
    submodule_init
    check_credentials
    prepapre_venv
    run_tests
}

main
