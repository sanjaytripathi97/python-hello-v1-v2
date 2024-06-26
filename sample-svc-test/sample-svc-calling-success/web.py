# sample svc calling python code 
import http.server
import socketserver
import logging
import requests

PORT = 8000
SERVICE_URL = "http://webserver-header.web-header.svc.cluster.local:8080/"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s\n" %
                     (self.client_address[0],
                      self.log_date_time_string(),
                      format%args))

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/fetch_headers':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            try:
                # Log the request headers
                logging.info(f"Request Headers: {self.headers}")

                # Make a request to SERVICE_URL
                response = requests.get(SERVICE_URL)
                if response.status_code == 200:
                    logging.info(f"Response Headers: {response.headers}")
                    self.wfile.write(response.text.encode('utf-8'))
                else:
                    logging.error(f"Error fetching headers: {response.status_code}")
                    self.wfile.write(f"Error fetching headers: {response.status_code}".encode('utf-8'))
            except requests.RequestException as e:
                logging.error(f"RequestException: {str(e)}")
                self.wfile.write(f"Error: {str(e)}".encode('utf-8'))

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
