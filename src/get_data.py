## read params
## process data
## return output data

import pandas as pd
import os, yaml, argparse

def read_params(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config

def get_data(config_path):
    config = read_params(config_path)
    data_path = config['data_source']['s3_source']
    df = pd.read_csv(data_path, encoding='utf-8')
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get Data Source Script')
    parser.add_argument('--config', '-c', default='params.yaml', help='config file', required=False)
    args = parser.parse_args()

    config_path = args.config
    data = get_data(config_path)
