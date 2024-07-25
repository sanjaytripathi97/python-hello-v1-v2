import http.server
import socketserver
import logging

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Log the request headers
        logging.info(f"GET Request Headers: {self.headers}")
        logging.info("=" * 30)  # Print separator line

        # Call the superclass method to handle the request
        super().do_GET()

    def do_POST(self):
        # Log the request headers
        logging.info(f"POST Request Headers: {self.headers}")
        logging.info("=" * 30)  # Print separator line

        # Log the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info(f"POST Request Body: {post_data.decode('utf-8')}")
        logging.info("=" * 30)  # Print separator line

        # Respond to the POST request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"POST request received")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
