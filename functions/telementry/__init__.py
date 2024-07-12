from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    SimpleSpanProcessor,
    ConsoleSpanExporter,
)
from .baggage import BaggageExporter

console_simple_span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
baggage_simple_span_processor = SimpleSpanProcessor(BaggageExporter())
trace_provider = TracerProvider()

trace_provider.add_span_processor(console_simple_span_processor)
trace_provider.add_span_processor(baggage_simple_span_processor)
trace.set_tracer_provider(trace_provider)

tracer = trace.get_tracer("firebase.functions.tracer")
