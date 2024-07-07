from flask import Flask
from opentelemetry import trace

app = Flask(__name__)

@app.get("/health-check")
def health_check():
    span = trace.get_current_span()
    span.set_attribute("sample_attr", "gateway health check invoked")
    return "hello world"
