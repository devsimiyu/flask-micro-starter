from firebase_functions import https_fn
from api import gateway
from telementry import tracer
from utils import constants

@https_fn.on_request(
    min_instances=constants.FAAS_MIN_INSTANCES_CONFIG,
    max_instances=constants.FAAS_MAX_INSTANCES_CONFIG,
    cpu=constants.FAAS_CPU_CONFIG,
    memory=constants.FAAS_MAX_MEMORY_CONFIG,
    timeout_sec=constants.FAAS_TIMEOUT_CONFIG)
@tracer.start_as_current_span("reverse_proxy")
def reverse_proxy(req: https_fn.Request) -> https_fn.Response:
    with gateway.app.request_context(req.environ):
        return gateway.app.full_dispatch_request()
