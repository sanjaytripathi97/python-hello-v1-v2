import http.server
import socketserver
import logging

PORT = 8000

class CustomHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the request headers
        logging.info(f"GET Request Headers: {self.headers}")
        logging.info("=" * 30)  # Print separator line

        if self.path == '/page1':
            self.serve_page1()
        elif self.path == '/page2':
            self.serve_page2()
        else:
            self.serve_index()

    def serve_index(self):
        # Serve the default index.html page
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Read and serve index.html content
        with open('index.html', 'r') as file:
            self.wfile.write(file.read().encode('utf-8'))

    def serve_page1(self):
        # Serve a different page for /page1
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        page1_content = """
        <html>
        <head><title>Page 1</title></head>
        <body>
            <h1>This is Page 1</h1>
            <p>Welcome to the first page!</p>
        </body>
        </html>
        """
        self.wfile.write(page1_content.encode('utf-8'))

    def serve_page2(self):
        # Serve another page for /page2
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        page2_content = """
        <html>
        <head><title>Page 2</title></head>
        <body>
            <h1>This is Page 2</h1>
            <p>Welcome to the second page!</p>
        </body>
        </html>
        """
        self.wfile.write(page2_content.encode('utf-8'))

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
