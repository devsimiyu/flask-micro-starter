from datetime import datetime
from flask import Flask, request, Response
from opentelemetry import (
    baggage, 
    trace, 
    context,
    propagate,
)
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.baggage.propagation import W3CBaggagePropagator
from utils import constants

app = Flask(__name__)

@app.before_request
def before_distributed_trace():
    span = trace.get_current_span()
    span.set_attribute(constants.FAAS_INVOKED_PROVIDER_SPAN_ATTRIBUTE, constants.FAAS_INVOKED_PROVIDER_CONFIG)
    span.set_attribute(constants.FAAS_NAME_SPAN_ATTRIBUTE, 'us-central1-reverse_proxy')
    span.set_attribute(constants.FAAS_TRIGGER_SPAN_ATTRIBUTE, 'http')
    span.set_attribute(constants.FAAS_INVOKED_TIME_SPAN_ATTRIBUTE, datetime.now().isoformat())
    span.set_attribute(constants.FAAS_MAX_MEMORY_SPAN_ATTRIBUTE, constants.FAAS_MAX_MEMORY_CONFIG)

@app.after_request
def after_distributed_trace(response: Response):
    propagator = propagate.get_global_textmap()
    span_context = context.get_current()
    headers = dict(propagator.extract(request.headers))
    W3CBaggagePropagator().inject(headers, span_context)
    TraceContextTextMapPropagator().inject(headers, span_context)
    response.headers.update(headers)
    return response

@app.get("/health-check")
def health_check():
    context.attach(baggage.set_baggage('outbox', '10987'))
    return "hello world"
