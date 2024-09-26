import http.server
import socketserver
import logging
import threading
from prometheus_client import start_http_server, Summary, Counter, generate_latest, CollectorRegistry
import psutil
import time

# Create a registry for the metrics
registry = CollectorRegistry()

# Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'status'], registry=registry)
REQUEST_DURATION = Summary('http_request_duration_seconds', 'Duration of HTTP requests in seconds', ['method'], registry=registry)
CPU_USAGE = Summary('python_cpu_usage_percent', 'CPU usage of the Python application', registry=registry)
MEMORY_USAGE = Summary('python_memory_usage_bytes', 'Memory usage of the Python application', registry=registry)

PORT = 8000
METRICS_PORT = 8001

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        start_time = time.time()

        # Log the request headers
        logging.info(f"GET Request Headers: {self.headers}")
        logging.info("=" * 30)

        # Increment request count
        REQUEST_COUNT.labels(method='GET', status='200').inc()

        # Check for the metrics endpoint
        if self.path == '/python-metrics':
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
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Start the metrics server in a separate thread
    threading.Thread(target=start_metrics_server, daemon=True).start()

    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logging.info(f"Serving at port {PORT}")
        httpd.serve_forever()
