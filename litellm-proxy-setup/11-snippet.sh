#!/usr/bin/env bash
set -euo pipefail

: "${LITELLM_VIRTUAL_KEY:?Set LITELLM_VIRTUAL_KEY}"

curl --fail-with-body --silent --show-error \
  --connect-timeout 5 --max-time 60 \
  http://127.0.0.1:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_VIRTUAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet",
    "messages": [{"role": "user", "content": "Reply with the single word: ok"}]
  }' | jq -e '.choices[0].message.content'
