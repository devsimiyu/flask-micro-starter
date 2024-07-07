from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter
)

trace_provider = TracerProvider()
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())

trace_provider.add_span_processor(span_processor)
trace.set_tracer_provider(trace_provider)

tracer = trace.get_tracer("firebase.functions.tracer")
