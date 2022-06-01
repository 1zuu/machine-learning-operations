## load train / test files
## train algorithm
## save the metrics, params, and model

import os, argparse, sys, warnings, json, joblib

import numpy as np
import pandas as pd 

from get_data import read_params
from urllib.parse import urlparse
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_and_evaluate(config_path):
    config = read_params(config_path)

    train_path = config['split_data']['train_path']
    test_path = config['split_data']['test_path']
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    Y = train[config['base']['target_column']]
    Ytest = test[config['base']['target_column']]
    X = train.drop(config['base']['target_column'], axis=1)
    Xtest = test.drop(config['base']['target_column'], axis=1)

    # train the model
    model = ElasticNet(alpha=config['estimators']['ElasticNet']['params']['alpha'], 
                       l1_ratio=config['estimators']['ElasticNet']['params']['l1_ratio'],
                       random_state=config['base']['random_state'])

    model.fit(X, Y)

    # evaluate the model
    predictions = model.predict(Xtest)
    actual = Ytest

    mse = mean_squared_error(actual, predictions)
    mae = mean_absolute_error(actual, predictions)
    r2 = r2_score(actual, predictions)

    #####################################################
    scores_file = config["reports"]["scores"]
    with open(scores_file, "w") as f:
        scores = {
            "mse": mse,
            "mae": mae,
            "r2": r2
        }
        json.dump(scores, f, indent=4)

    params_file = config["reports"]["params"]
    with open(params_file, "w") as f:
        params = {
            "alpha": config['estimators']['ElasticNet']['params']['alpha'],
            "l1_ratio": config['estimators']['ElasticNet']['params']['l1_ratio'],
        }
        json.dump(params, f, indent=4)
    #####################################################

    # save the model
    model_path = config['model_dir']
    joblib.dump(model, os.path.join(model_path, "model.joblib"))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train and Evaluate Model Script')
    parser.add_argument('--config', '-c', default='params.yaml', help='config file', required=False)
    args = parser.parse_args()

    config_path = args.config
    train_and_evaluate(config_path)
