# Production agent observability

Companion code for [production agent observability](https://mpiv.ai/blog/production-agent-observability-what-operators-actually-need-to-know-2026).

The Python examples are import-safe and tested against OpenTelemetry 1.43, Langfuse 4.14, and Anthropic 0.116. They omit prompt and completion contents from OpenTelemetry attributes. The collector fragment hashes current and legacy GenAI content attributes before export.

## Files

- [`01-snippet.py`](./01-snippet.py) emits low-cardinality OpenTelemetry spans with current GenAI semantic attributes.
- [`02-snippet.py`](./02-snippet.py) uses Langfuse v4 `observe`, `propagate_attributes`, and observation update methods with injected agent functions.
- [`03-snippet.yaml`](./03-snippet.yaml) is a collector processor fragment for content redaction and tail sampling.

References: [OpenTelemetry generative AI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) and [Langfuse Python instrumentation](https://langfuse.com/docs/observability/sdk/python/instrumentation).
