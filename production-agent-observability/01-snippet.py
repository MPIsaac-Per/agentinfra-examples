import os
from anthropic import Anthropic
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint=os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"]))
)
tracer = trace.get_tracer("agent.runtime")

anthropic_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Pin the model slug from the operator's verified model registry.
# Slug intentionally omitted here: see companion repo tag v2026.04.25 for the verified value. [unverified]
DEFAULT_MODEL = os.environ["AGENT_MODEL_SLUG"]

def call_model(prompt: str, model: str = DEFAULT_MODEL):
    with tracer.start_as_current_span(f"chat {model}") as span:
        span.set_attribute("gen_ai.operation.name", "chat")
        span.set_attribute("gen_ai.provider.name", "anthropic")
        span.set_attribute("gen_ai.request.model", model)
        try:
            response = anthropic_client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            span.set_attribute("gen_ai.response.id", response.id)
            span.set_attribute("gen_ai.usage.input_tokens", response.usage.input_tokens)
            span.set_attribute("gen_ai.usage.output_tokens", response.usage.output_tokens)
            span.set_status(Status(StatusCode.OK))
            return response
        except Exception as exc:
            span.record_exception(exc)
            span.set_status(Status(StatusCode.ERROR, str(exc)))
            raise
