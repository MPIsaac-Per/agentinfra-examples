# Contributing

## Development setup

Requirements: Python 3.11+, [uv](https://docs.astral.sh/uv/), Docker Compose for proxy validation, and ShellCheck.

```bash
git clone https://github.com/MPIsaac-Per/agentinfra-examples.git
cd agentinfra-examples
uv sync --locked --all-extras --dev
```

Run the same checks as CI:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest --cov=. --cov-report=term-missing
shellcheck litellm-proxy-setup/*.sh
uv run pip-audit
```

## Change requirements

- Link current official documentation for each external API used.
- Pin dependency ranges and container releases; pin example container images by digest.
- Keep imports free of credential checks, network calls, and process-wide configuration.
- Use fakes for unit tests and mark any optional live test clearly.
- Do not commit credentials, generated keys, provider responses, traces, prompts, or customer data.
- State operator-controlled values such as model IDs, network exposure, and budgets explicitly.

Open an issue before adding a new article directory or hosted-service dependency. Small contract corrections can go directly to a pull request.

By participating, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
