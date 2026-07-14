#!/usr/bin/env bash
set -euo pipefail

# Disable the old key after the overlap window. Reversible.
: "${LITELLM_MASTER_KEY:?Set LITELLM_MASTER_KEY}"
: "${OLD_VIRTUAL_KEY:?Set OLD_VIRTUAL_KEY}"

curl --fail-with-body --silent --show-error \
  --connect-timeout 5 --max-time 30 \
  -X POST http://127.0.0.1:4000/key/block \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  --data-binary "$(jq -n --arg key "$OLD_VIRTUAL_KEY" '{key: $key}')"
