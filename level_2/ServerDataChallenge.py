from http.server import BaseHTTPRequestHandler, HTTPServer
from os.path import dirname, abspath, join

from DataChallenge import DataChallengeHandler


class HttpServerRequestHandler(BaseHTTPRequestHandler):
    data_challenge_handler = DataChallengeHandler()

    def do_POST(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Send message back to client

        content_length = int(self.headers["Content-Length"])
        post_data = (
            self.rfile.read(content_length)
            .decode("utf8")
            .replace('{"communication": "', "")
            .replace('"}', "")
        )
        root_folder = dirname(dirname(abspath(__file__)))
        out_folder = join(root_folder, "processed")
        data_challenge_handler = DataChallengeHandler()

        data_challenge_handler.server_proceed_communication(post_data, out_folder)

        return


def run():
    print("starting server...")
    server_address = ("127.0.0.1", 5000)
    httpd = HTTPServer(server_address, HttpServerRequestHandler)
    print("running server...")
    httpd.serve_forever()


run()
