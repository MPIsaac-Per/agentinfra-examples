# Agent evaluation pipelines

Companion code for [agent eval pipelines](https://mpiv.ai/blog/agent-eval-pipelines-what-operators-actually-need-to-know-2026).

These examples are import-safe and tested against Langfuse 4.14 and Anthropic 0.116. Hosted calls require `LANGFUSE_*` and `ANTHROPIC_API_KEY` credentials plus provider model IDs selected by the operator.

## Files

- [`01-snippet.py`](./01-snippet.py) runs a Langfuse dataset experiment with an injected model ID.
- [`02-snippet.py`](./02-snippet.py) validates judge output and calibrates a candidate judge against a reference.
- [`03-snippet.py`](./03-snippet.py) queries one observation through the Langfuse v4 API and promotes it to a dataset.

References: [Langfuse experiments](https://langfuse.com/docs/evaluation/evaluation-methods/experiments) and [query via SDK](https://langfuse.com/docs/api-and-data-platform/features/query-via-sdk/).
