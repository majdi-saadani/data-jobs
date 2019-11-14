from pprint import pprint

from DataChallenge import DataChallengeHandler

data_challenge_handler = DataChallengeHandler()



in_folder = "D:\\lifen\\data-jobs\\communications"
out_folder = "D:\\lifen\\data-jobs\\processed"
print(data_challenge_handler.proceed_communication(in_folder, out_folder))
