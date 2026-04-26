umask 077
curl -sS -X POST http://localhost:4000/key/generate \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "models": ["claude-sonnet"],
    "duration": "30d",
    "max_budget": 25.00,
    "budget_duration": "30d",
    "rpm_limit": 60,
    "metadata": {"app": "agent-research", "owner": "michael"}
  }' | jq '{key: .key, expires: .expires}'
