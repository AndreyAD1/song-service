#!/usr/bin/env bash

set -xeuo pipefail

COMPOSE_FILE="docker-compose-dev.yml"
CMD="docker-compose -f ${COMPOSE_FILE}"

function docker_compose_down() {
  if [[ $? -ne 0 ]]; then
    ${CMD} logs app
  fi
  ${CMD} down
  ${CMD} rm -f
}

docker_compose_down
trap docker_compose_down EXIT

${CMD} up -d --build
${CMD} exec -T app pytest -v -W ignore:::marshmallow.fields