#!/bin/bash
set -eu
root="$(cd "$(dirname "$0")/.." && pwd)"
. $root/.venv/bin/activate

function need {
    local tool="$1"
    if ! hash "$tool"; then
        echo "$tool not found, abort"
        exit 1
    fi
}

function check_credentials {
    [ ! -z "$OSC_ACCESS_KEY" ] || (echo "OSC_ACCESS_KEY not set, aborting."; exit 1)
    [ ! -z "$OSC_SECRET_KEY" ] || (echo "OSC_SECRET_KEY not set, aborting."; exit 1)
}

function run_tests() {
    local result=0
    cd "$root/tests"
    for t in *.py; do
        if python "$t"; then
            echo "check $t: OK"
        else
            echo "check $t: KO"
	    result=1
        fi
    done
    exit $result
}

check_credentials
run_tests
