# Disable the old key after the overlap window. Reversible.
curl -sS -X POST http://localhost:4000/key/block \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"key": "sk-...the-old-key..."}'
