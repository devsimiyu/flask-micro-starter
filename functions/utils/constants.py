from enum import Enum
from opentelemetry.semconv.trace import SpanAttributes
from firebase_functions.params import IntParam, StringParam
from firebase_functions.options import MemoryOption

FAAS_NAME_SPAN_ATTRIBUTE = 'faas.name'
FAAS_TRIGGER_SPAN_ATTRIBUTE = SpanAttributes.FAAS_TRIGGER
FAAS_INVOKED_TIME_SPAN_ATTRIBUTE = 'faas.time'
FAAS_INVOKED_PROVIDER_SPAN_ATTRIBUTE = 'faas.invoked_provider'
FAAS_MAX_MEMORY_SPAN_ATTRIBUTE = 'faas.max_memory'

FAAS_ENVIRONMENT_CONFIG = StringParam('ENVIRONMENT', default='local')
FAAS_MAX_MEMORY_CONFIG = MemoryOption.MB_512.value
FAAS_TIMEOUT_CONFIG = IntParam('TIMEOUT').value
FAAS_MIN_INSTANCES_CONFIG = FAAS_ENVIRONMENT_CONFIG.equals('local').then(1, 0)
FAAS_MAX_INSTANCES_CONFIG = FAAS_ENVIRONMENT_CONFIG.equals('local').then(1, 10)
FAAS_CPU_CONFIG = IntParam('CPU').value
FAAS_INVOKED_PROVIDER_CONFIG = 'gcp'
