#!/bin/bash
set -e

# Assuming you are running this from a prepared virtual environment
PROJECT_ROOT=$(cd "$(dirname $0)/.." && pwd)
cd $PROJECT_ROOT

echo -n "$(basename $0): "

if [ -z "$PIP_TOKEN" ]; then
    echo "PIP_TOKEN is missing, abort."
    exit 1
fi

. .venv/bin/activate > /dev/null
python3 -m pip install --upgrade twine
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD=$PIP_TOKEN
python3 -m twine upload --skip-existing --non-interactive dist/*
echo "OK"
