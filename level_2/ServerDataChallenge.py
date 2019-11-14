from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from DataChallenge import DataChallengeHandler


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
  data_challenge_handler = DataChallengeHandler()

  def do_POST(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send message back to client
        message = "The server will process the unprocceded data"

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf8').replace('{"communication": "','').replace('"}','')
        print(post_data)

        out_folder = "D:\\lifen\\data-jobs\\processed"
        data_challenge_handler = DataChallengeHandler()

        data_challenge_handler.server_proceed_communication(post_data , out_folder)


        return
def run():

  print('starting server...')
  server_address = ('127.0.0.1', 5000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()