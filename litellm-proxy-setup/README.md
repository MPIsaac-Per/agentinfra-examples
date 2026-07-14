# LiteLLM proxy setup

Companion code for [litellm proxy setup](https://mpiv.ai/blog/how-to-set-up-litellm-proxy-for-production-ai-agents-2026).

The compose example binds the proxy to loopback, pins LiteLLM and PostgreSQL by release and digest, keeps provider model IDs in environment configuration, checks readiness, and rotates container logs.

## Assemble the example

```bash
cd litellm-proxy-setup
cp 03-snippet.sh .env
cp 05-snippet.yaml config.yaml
cp 07-snippet.yaml compose.yaml
chmod 600 .env
```

Replace every placeholder in `.env`. Generate independent random values for the master key, salt key, and database password. Select model IDs from current provider registries.

```bash
openssl rand -hex 32
docker compose config --quiet
./08-snippet.sh
```

The first boot allows LiteLLM schema updates. After the database is initialized and the migration has been verified, set `DISABLE_SCHEMA_UPDATE` according to the [current LiteLLM production guidance](https://docs.litellm.ai/docs/proxy/prod) for your deployment process.

## Files

- [`01-snippet.txt`](./01-snippet.txt) — text block (text)
- [`02-snippet.txt`](./02-snippet.txt) — text block (text)
- [`03-snippet.sh`](./03-snippet.sh) is the `.env` template.
- [`04-snippet.sh`](./04-snippet.sh) creates and inspects a PostgreSQL backup.
- [`05-snippet.yaml`](./05-snippet.yaml) is the proxy configuration.
- [`06-snippet.yaml`](./06-snippet.yaml) is an environment fragment for other orchestrators.
- [`07-snippet.yaml`](./07-snippet.yaml) is the Docker Compose definition.
- [`08-snippet.sh`](./08-snippet.sh) pulls, starts, waits, and probes readiness.
- [`09-snippet.sh`](./09-snippet.sh) creates a bounded virtual key and stores it with mode `0600`.
- [`10-snippet.sh`](./10-snippet.sh) blocks an old virtual key after rotation.
- [`11-snippet.sh`](./11-snippet.sh) runs a chat-completions smoke test.
- [`12-snippet.py`](./12-snippet.py) runs the same smoke test through the OpenAI client.

Do not commit `.env`, generated virtual-key files, database dumps, or provider responses.
