DUMP_FILE="litellm-$(date -u +%Y%m%dT%H%M%SZ).dump"
docker compose exec -T db pg_dump -U litellm -Fc litellm > "$DUMP_FILE"
test -s "$DUMP_FILE" || { echo "dump is empty: $DUMP_FILE" >&2; exit 1; }
docker compose exec -T db pg_restore -l < "$DUMP_FILE" \
  | grep -E 'LiteLLM_(VerificationToken|SpendLogs)'
