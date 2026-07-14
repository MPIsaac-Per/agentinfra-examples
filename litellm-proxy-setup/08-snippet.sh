#!/usr/bin/env bash
set -euo pipefail

docker compose pull
docker compose up -d --wait
curl --fail --silent --show-error http://127.0.0.1:4000/health/readiness
