import http.server
import socketserver
import logging
import threading
from prometheus_client import start_http_server, Summary, Counter, generate_latest, CollectorRegistry
import psutil
import time
import json
from collections import deque
from datetime import datetime

# Create a registry for the metrics
registry = CollectorRegistry()

# Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'status'], registry=registry)
REQUEST_DURATION = Summary('http_request_duration_seconds', 'Duration of HTTP requests in seconds', ['method'], registry=registry)
CPU_USAGE = Summary('python_cpu_usage_percent', 'CPU usage of the Python application', registry=registry)
MEMORY_USAGE = Summary('python_memory_usage_bytes', 'Memory usage of the Python application', registry=registry)

PORT = 8000
METRICS_PORT = 8001

# In-memory log buffer
class LogBuffer:
    def __init__(self, maxlen=100):
        self.logs = deque(maxlen=maxlen)
        self.lock = threading.Lock()

    def add(self, log_entry):
        with self.lock:
            self.logs.append(log_entry)

    def get_all(self):
        with self.lock:
            return list(self.logs)

# Global log buffer instance
log_buffer = LogBuffer()

# Custom logging handler to capture logs
class BufferHandler(logging.Handler):
    def emit(self, record):
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S'),
            'level': record.levelname,
            'message': self.format(record)
        }
        log_buffer.add(log_entry)

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        start_time = time.time()

        # Log the request headers
        logging.info(f"GET Request Headers: {self.headers}")
        logging.info("=" * 30)

        # Increment request count
        REQUEST_COUNT.labels(method='GET', status='200').inc()

        # Check for the API logs endpoint
        if self.path == '/api/logs':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            logs = log_buffer.get_all()
            self.wfile.write(json.dumps(logs).encode('utf-8'))
        # Check for the metrics endpoint
        elif self.path == '/python-metrics':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; version=0.0.4; charset=utf-8')
            self.end_headers()
            self.wfile.write(generate_latest(registry))
        else:
            # Call the superclass method to handle the request
            super().do_GET()

        # Calculate duration and record it
        duration = time.time() - start_time
        REQUEST_DURATION.labels(method='GET').observe(duration)

    def do_POST(self):
        start_time = time.time()

        # Log the request headers
        logging.info(f"POST Request Headers: {self.headers}")
        logging.info("=" * 30)

        # Log the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"POST Request Body: {post_data.decode('utf-8')}")
        logging.info("=" * 30)

        # Increment request count
        REQUEST_COUNT.labels(method='POST', status='200').inc()

        # Respond to the POST request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"POST request received")

        # Calculate duration and record it
        duration = time.time() - start_time
        REQUEST_DURATION.labels(method='POST').observe(duration)

def start_metrics_server():
    start_http_server(METRICS_PORT, registry=registry)

if __name__ == "__main__":
    # Configure logging with buffer handler
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Add buffer handler to capture logs
    buffer_handler = BufferHandler()
    buffer_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(buffer_handler)

    # Start the metrics server in a separate thread
    threading.Thread(target=start_metrics_server, daemon=True).start()

    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logging.info(f"Serving at port {PORT}")
        httpd.serve_forever()
