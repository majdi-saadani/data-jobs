from ServerDataChallengeToMysql import testHTTPServer_RequestHandler

if __name__ == "__main__":

    sql_challenger_server = testHTTPServer_RequestHandler()
    sql_challenger_server.run()
