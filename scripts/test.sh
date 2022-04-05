#!/usr/bin/env bash

set -xeuo pipefail

COMPOSE_FILE="docker-compose-dev.yml"
CMD="docker-compose -f ${COMPOSE_FILE}"

function docker_compose_down() {
  ${CMD} down
  ${CMD} rm -f
}

trap docker_compose_down EXIT

${CMD} up -d --build --force-recreate
if ! ${CMD} exec -T app pytest -v -W ignore:::marshmallow.fields
then
  ${CMD} logs app
fi