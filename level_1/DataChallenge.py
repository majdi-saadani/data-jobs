import json
from os import mkdir, listdir
from os.path import isdir, join


class DataChallengeHandler:

    def log_to_json(self, log_as_string):
        splitter_log = log_as_string.split('|')
        log_json = {}

        for log_attribute in splitter_log:
            key, value = log_attribute.split('=')
            log_json[key] = value

        log_json['sender'] = json.loads(log_json['sender'].replace("'", '"'))
        return log_json

    def file_content_to_json(self, file_path):
        with open(file_path, 'r') as communication_log_file:
            return self.log_to_json(communication_log_file.read())

    def proceed_communication(self, in_folder, out_folder):
        if not isdir(out_folder):
            mkdir(out_folder)

        communication_log_folder = listdir(in_folder)
        # for each files we will read the text and we will change the structure of the data to json
        for log_file in communication_log_folder:
            in_log_file_path = join(in_folder, log_file)
            out_log_file_path = join(out_folder, log_file)

            with open(out_log_file_path, 'w') as proceed_log_file:
                proceed_log_file.write(
                    json.dumps(self.file_content_to_json(in_log_file_path), indent=4))

    def server_proceed_communication(self,received_json, out_folder):
        if not isdir(out_folder):
            mkdir(out_folder)
            out_log_file_path = join(out_folder,'communications-'+received_json.split('|')[0].split('=')[1]+'.json' , log_file)
            with open(out_log_file_path, 'w') as proceed_log_file:
                proceed_log_file.write(
                    json.dumps(self.log_to_json(received_json), indent=4))
