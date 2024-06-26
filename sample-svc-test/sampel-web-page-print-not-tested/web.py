import http.server
import socketserver
import logging
import requests

PORT = 8000

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
        elif self.path == '/fetch_picture':
            self.fetch_and_display_image("http://test1.svc.local:8080/picture.jpg")
        elif self.path == '/fetch_fox':
            self.fetch_and_display_image("http://test2.svc.local:8080/fox.jpg")
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def fetch_and_display_image(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content_type = response.headers['Content-Type']
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()
                self.wfile.write(response.content)
            else:
                self.send_error(response.status_code, f'Error fetching image: {url}')
        except requests.RequestException as e:
            self.send_error(500, f'Error: {str(e)}')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    Handler = CustomHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
