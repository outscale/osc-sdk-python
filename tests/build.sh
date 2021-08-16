#!/bin/bash
set -e

# Assuming you are running this from a prepared virtual environment
PROJECT_ROOT=$(cd "$(dirname $0)/.." && pwd)
cd $PROJECT_ROOT

echo -n "$(basename $0): "

. .venv/bin/activate > /dev/null
python3 -m pip install --upgrade pip build
python3 -m build
echo "OK"
