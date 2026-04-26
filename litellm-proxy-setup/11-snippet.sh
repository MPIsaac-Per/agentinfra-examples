curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer sk-...the-issued-key..." \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet",
    "messages": [{"role": "user", "content": "Reply with the single word: ok"}]
  }'
