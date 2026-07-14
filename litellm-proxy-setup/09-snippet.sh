#!/usr/bin/env bash
set -euo pipefail

: "${LITELLM_MASTER_KEY:?Set LITELLM_MASTER_KEY}"
: "${KEY_OWNER:?Set KEY_OWNER}"
: "${MAX_BUDGET_USD:?Set MAX_BUDGET_USD after approving the limit}"

umask 077
OUTPUT_FILE="${OUTPUT_FILE:-litellm-virtual-key.json}"
curl --fail-with-body --silent --show-error \
  --connect-timeout 5 --max-time 30 \
  -X POST http://127.0.0.1:4000/key/generate \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  --data-binary "$(jq -n \
    --arg owner "$KEY_OWNER" \
    --argjson max_budget "$MAX_BUDGET_USD" \
    '{
    "models": ["claude-sonnet"],
    "duration": "30d",
    "max_budget": $max_budget,
    "budget_duration": "30d",
    "rpm_limit": 60,
    "metadata": {"app": "agent-research", "owner": $owner}
  }')" \
  | jq -e '{key: .key, expires: .expires}' > "$OUTPUT_FILE"

chmod 600 "$OUTPUT_FILE"
printf 'Virtual key written to %s with mode 0600.\n' "$OUTPUT_FILE"
