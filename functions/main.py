from firebase_functions import https_fn
from api import gateway
from telementry import tracer

@https_fn.on_request()
@tracer.start_as_current_span("reverse_proxy")
def reverse_proxy(req: https_fn.Request) -> https_fn.Response:
    with gateway.app.request_context(req.environ):
        return gateway.app.full_dispatch_request()
