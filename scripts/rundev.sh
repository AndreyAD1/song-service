#!/usr/bin/env bash

set -xe

docker-compose -f docker-compose-dev.yml up --build --force-recreate -V -d
