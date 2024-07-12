from typing import Sequence
from opentelemetry.sdk.trace import ReadableSpan
from opentelemetry.sdk.trace.export import (
    SpanExporter,
    SpanExportResult,
)
from utils.logging import logger

class BaggageExporter(SpanExporter):

    def export(self, spans: Sequence[ReadableSpan]) -> SpanExportResult:
        logger.info('Exporting baggage')
        return super().export(spans)
    
    def shutdown(self) -> None:
        logger.info('Shutting down bagger exporter')
        return super().shutdown()
