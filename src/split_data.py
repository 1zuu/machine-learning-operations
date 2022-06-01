# split the raw data
# save it int data/processed folder

import os, argparse
import pandas as pd
from get_data import read_params
from sklearn.model_selection import train_test_split

def split_and_saved(config_path):
    config = read_params(config_path)

    raw_data_path = config['load_data']['raw_dataset_csv']
    data = pd.read_csv(raw_data_path)

    random_state = config['base']['random_state']
    test_size = config['split_data']['test_size']
    train, test = train_test_split(data, test_size=test_size, random_state=random_state)

    train_path = config['split_data']['train_path']
    test_path = config['split_data']['test_path']
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split Raw Data Script')
    parser.add_argument('--config', '-c', default='params.yaml', help='config file', required=False)
    args = parser.parse_args()

    config_path = args.config
    split_and_saved(config_path)