#!/usr/bin/env bash

set -xeuo pipefail

docker-compose -f docker-compose-dev.yml up --build --force-recreate -V -d
