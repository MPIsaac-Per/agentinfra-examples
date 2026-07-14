# Agent infrastructure examples

[![CI](https://github.com/MPIsaac-Per/agentinfra-examples/actions/workflows/ci.yml/badge.svg)](https://github.com/MPIsaac-Per/agentinfra-examples/actions/workflows/ci.yml)
[![CodeQL](https://github.com/MPIsaac-Per/agentinfra-examples/actions/workflows/codeql.yml/badge.svg)](https://github.com/MPIsaac-Per/agentinfra-examples/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/MPIsaac-Per/agentinfra-examples/badge)](https://scorecard.dev/viewer/?uri=github.com/MPIsaac-Per/agentinfra-examples)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Validated companion code for articles on [mpiv.ai/blog](https://mpiv.ai/blog) covering AI agent gateways, observability, and evaluation pipelines.

Each subdirectory corresponds to one published article. Examples that call hosted services require your own credentials and current provider model IDs. Import, schema, shell, and local utility behavior is tested without making external calls.

Validated against Langfuse 4.14, OpenTelemetry 1.43, Anthropic 0.116, OpenAI 2.45, and LiteLLM proxy image v1.90.2 on 2026-07-14. The lockfile and Dependabot preserve that version trail.

## Example status

| Article | Subdirectory | Status |
|---|---|---|
| [LiteLLM proxy setup](https://mpiv.ai/blog/how-to-set-up-litellm-proxy-for-production-ai-agents-2026) | [`litellm-proxy-setup/`](litellm-proxy-setup/) | Validated configuration and operational scripts |
| [Production agent observability](https://mpiv.ai/blog/production-agent-observability-what-operators-actually-need-to-know-2026) | [`production-agent-observability/`](production-agent-observability/) | Current OpenTelemetry and Langfuse v4 examples |
| [Agent eval pipelines](https://mpiv.ai/blog/agent-eval-pipelines-what-operators-actually-need-to-know-2026) | [`agent-eval-pipelines/`](agent-eval-pipelines/) | Current Langfuse v4 and Anthropic examples |
| [LiteLLM vs OpenRouter](https://mpiv.ai/blog/litellm-vs-openrouter-which-wins-for-production-ai-agents-2026) | [`litellm-vs-openrouter/`](litellm-vs-openrouter/) | Article index, no code yet |
| [Langfuse vs Braintrust](https://mpiv.ai/blog/langfuse-vs-braintrust-which-wins-for-agent-observability-2026) | [`langfuse-vs-braintrust/`](langfuse-vs-braintrust/) | Article index, no code yet |

## Development

Requirements: Python 3.11+, [uv](https://docs.astral.sh/uv/), and ShellCheck.

```bash
uv sync --locked --all-extras --dev
uv run ruff check .
uv run ruff format --check .
uv run pytest --cov=. --cov-report=term-missing
shellcheck litellm-proxy-setup/*.sh
uv run pip-audit
```

## Conventions

- One subdirectory per article. Subdirectory name is the article slug (truncated where useful).
- Each subdirectory has its own `README.md` linking back to the article and explaining how to run the code.
- Hosted-service examples require accounts, credentials, and model IDs chosen by the operator.
- Placeholder values are deliberate and fail closed when required environment variables are absent.
- Container images and Python dependencies are versioned. Review upstream release notes before updating them.
- License: MIT unless a subdirectory specifies otherwise.

## Open-source research collection

This repository is one part of Michael Isaac's public agent engineering collection:

- [claude-code-ops-audit](https://github.com/MPIsaac-Per/claude-code-ops-audit), audit methods and DuckDB analysis
- [claude-code-loop-patterns](https://github.com/MPIsaac-Per/claude-code-loop-patterns), tested controls for agent loops
- [mpiv.ai open-source research](https://mpiv.ai/#code), the collection index

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution scope and [SECURITY.md](SECURITY.md) for private vulnerability reporting.

## License

MIT. See [LICENSE](./LICENSE).
