import http.server
import socketserver
import logging

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Log the request headers
        logging.info(f"Headers: {self.headers}")
        logging.info("=" * 30)  # Print separator line

        # Call the superclass method to handle the request
        super().do_GET()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
