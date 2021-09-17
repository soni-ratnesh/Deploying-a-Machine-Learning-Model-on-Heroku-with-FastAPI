# Script to train machine learning model.
import os
import pandas as pd

from joblib import dump, load
from sklearn.model_selection import train_test_split
from .ml.data import process_data
from .ml.model import train_model, compute_model_metrics


def get_train_test_data(root_path):
    """
    Get data for training and testing

    Parameters
    ----------
    root_path

    Returns
    -------
    train_df , test_df
    """
    data = pd.read_csv(f"{root_path}/data/clean/census.csv")
    train_df, test_df = train_test_split(data, test_size=0.20)

    return train_df, test_df


# Add the necessary imports for the starter code.
# def train_test_model(stages):
#     if os.path.exists()
# Add code to load in the data.


def train_save_model(train, cat_features, root_path):
    """
    
    Parameters
    ----------
    root_path
    train
    cat_features

    Returns
    -------

    """
    x_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )
    # train model
    trained_model = train_model(x_train, y_train)
    # save model
    dump(trained_model, f"{root_path}/model/model.joblib")
    dump(encoder, f"{root_path}/model/encoder.joblib")
    dump(lb, f"{root_path}/model/lb.joblib")

# # Proces the test data with the process_data function.
# X_test, y_test, _, _ = process_data(test, categorical_features=cat_features, label="salary", training=False,
#                                     encoder=encoder, lb=lb)
# trained_model = load("data/model/model.joblib")
# encoder = load("data/model/encoder.joblib")
# lb = load("data/model/lb.joblib")
# 
# y_preds = trained_model.predict(X_test)
# 
# prc, rcl, fb = compute_model_metrics(y_test, y_preds)
