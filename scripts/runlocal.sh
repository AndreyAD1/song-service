#!/usr/bin/env bash

set -xe

echo 'LOADING SERVER'
flask run --host "${HOST}" --port "${PORT}" --reload
