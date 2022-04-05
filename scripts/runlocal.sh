#!/usr/bin/env bash

set -xeuo pipefail

echo 'LOADING SERVER'
flask run --host "${HOST}" --port "${PORT}"
