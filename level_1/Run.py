from os.path import dirname, abspath, join

from DataChallenge import DataChallengeHandler

if __name__ == "__main__":
    data_challenge_handler = DataChallengeHandler()
    root_folder = dirname(dirname(abspath(__file__)))
    in_folder = join(root_folder, "communications")
    out_folder = join(root_folder, "processed")
    print(data_challenge_handler.proceed_communication(in_folder, out_folder))
