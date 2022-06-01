## read the data from source
## save it in the data/raw for purther process 

import argparse
from get_data import read_params, get_data

def load_and_save(config_path):
    config = read_params(config_path)
    data = get_data(config_path) 

    new_columns = [col.replace(" ", "_") for col in data.columns.values]
    data.columns = new_columns

    raw_dataset_path = config['load_data']['raw_dataset_csv']
    data.to_csv(raw_dataset_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get Data Source Script')
    parser.add_argument('--config', '-c', default='params.yaml', help='config file', required=False)
    args = parser.parse_args()

    config_path = args.config
    data = load_and_save(config_path)