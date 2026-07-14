# shellcheck shell=bash disable=SC2034
# Copy this fragment to .env and replace every placeholder. Do not execute it.
LITELLM_MASTER_KEY=replace-with-openssl-rand-hex-32
LITELLM_SALT_KEY=replace-with-another-openssl-rand-hex-32
POSTGRES_PASSWORD=replace-with-openssl-rand-hex-32
ANTHROPIC_API_KEY=replace-with-provider-key
OPENAI_API_KEY=replace-with-provider-key
OPENROUTER_API_KEY=replace-with-provider-key
ANTHROPIC_MODEL_ID=anthropic/replace-with-current-model-id
OPENROUTER_MODEL_ID=openrouter/replace-with-current-model-id
OPENAI_MODEL_ID=openai/replace-with-current-model-id
DATABASE_URL=postgresql://litellm:${POSTGRES_PASSWORD}@db:5432/litellm
