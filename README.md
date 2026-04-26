# agentinfra-examples

Runnable companion code for articles on [mpiv.ai/blog](https://mpiv.ai/blog) covering AI agent infrastructure: LiteLLM proxy setups, agent observability with Langfuse / Braintrust / Helicone, evaluation pipelines, multi-provider gateways.

Each subdirectory corresponds to one published article. The subdirectory is created when the article first references it; code is added as needed to make the article's instructions reproducible by a reader following along.

## Subdirectories (current + planned)

| Article | Subdirectory | Status |
|---|---|---|
| [How to Set Up LiteLLM Proxy for Production AI Agents (2026)](https://mpiv.ai/blog/how-to-set-up-litellm-proxy-for-production-ai-agents-2026) | `litellm-proxy-setup/` | _Code samples coming — open an issue if you'd like a specific snippet packaged_ |
| [LiteLLM vs OpenRouter: Which Wins for Production AI Agents (2026)](https://mpiv.ai/blog/litellm-vs-openrouter-which-wins-for-production-ai-agents-2026) | `litellm-vs-openrouter/` | Planned |
| [Production Agent Observability (2026)](https://mpiv.ai/blog/production-agent-observability-what-operators-actually-need-to-know-2026) | `production-agent-observability/` | Planned |
| [Langfuse vs Braintrust (2026)](https://mpiv.ai/blog/langfuse-vs-braintrust-which-wins-for-agent-observability-2026) | `langfuse-vs-braintrust/` | Planned |
| [Agent Eval Pipelines (2026)](https://mpiv.ai/blog/agent-eval-pipelines-what-operators-actually-need-to-know-2026) | `agent-eval-pipelines/` | Planned |

## Conventions

- One subdirectory per article. Subdirectory name is the article slug (truncated where useful).
- Each subdirectory has its own `README.md` linking back to the article and explaining how to run the code.
- Code is intended to be runnable as-is on a fresh machine with the listed prerequisites — no proprietary infra, no commercial-tier cloud accounts beyond what the article itself calls out.
- License: MIT unless a subdirectory specifies otherwise.

## License

MIT — see [LICENSE](./LICENSE).
