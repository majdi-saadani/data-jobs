from http.server import BaseHTTPRequestHandler, HTTPServer

from MySqlDataChallenge import DataChallengeToMysqlHandler


class HttpServerRequestHandler(BaseHTTPRequestHandler):
    sql_challenge_handler = DataChallengeToMysqlHandler()

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
        sql_challenge_handler = DataChallengeToMysqlHandler()
        sql_challenge_handler.mysql_proceed_communication(post_data)

        return


def run():
    print("starting server...")
    server_address = ("127.0.0.1", 5000)
    httpd = HTTPServer(server_address, HttpServerRequestHandler)
    print("running server...")
    httpd.serve_forever()


run()
