"""Trace an Anthropic call with OpenTelemetry GenAI semantic attributes."""

from __future__ import annotations

from typing import Any

from anthropic import Anthropic
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import Status, StatusCode, Tracer


def configure_tracing(*, service_name: str = "agent-runtime") -> tuple[TracerProvider, Tracer]:
    provider = TracerProvider(resource=Resource.create({"service.name": service_name}))
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    return provider, provider.get_tracer("agent.runtime")


def call_model(
    client: Anthropic,
    tracer: Tracer,
    *,
    prompt: str,
    model: str,
) -> Any:
    if not model.strip():
        raise ValueError("model must be a non-empty provider model ID")

    with tracer.start_as_current_span("chat") as span:
        span.set_attribute("gen_ai.operation.name", "chat")
        span.set_attribute("gen_ai.provider.name", "anthropic")
        span.set_attribute("gen_ai.request.model", model)
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
        except Exception as exc:
            span.record_exception(exc)
            span.set_status(Status(StatusCode.ERROR, type(exc).__name__))
            raise

        span.set_attribute("gen_ai.response.id", response.id)
        span.set_attribute("gen_ai.response.model", response.model)
        span.set_attribute("gen_ai.usage.input_tokens", response.usage.input_tokens)
        span.set_attribute("gen_ai.usage.output_tokens", response.usage.output_tokens)
        span.set_status(Status(StatusCode.OK))
        return response
