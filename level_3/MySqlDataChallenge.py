import json
import pymysql


class DataChallengeToMysqlHandler:
    def log_to_json(self, log_as_string):
        splitter_log = log_as_string.split("|")
        log_json = {}

        for log_attribute in splitter_log:
            key, value = log_attribute.split("=")
            log_json[key] = value

        log_json["sender"] = json.loads(log_json["sender"].replace("'", '"'))
        return log_json

    def mysql_proceed_communication(self, received_json):
        data = DataChallengeToMysqlHandler()
        data = data.log_to_json(received_json)
        con = pymysql.connect(host="localhost", user="root", passwd="", db="lifen")
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO production (id, telecom, created_at,sender_name , sender_category) VALUES (%s,%s,%s,%s,%s)",
            (
                data["id"],
                data["telecom"],
                data["created_at"],
                data["sender"]["name"],
                data["sender"]["profession"],
            ),
        )
        con.commit()
        con.close()
        print("Done")
