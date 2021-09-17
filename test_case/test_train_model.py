
import os
from starter.train_model import get_train_test_data, train_save_model


def test_get_train_test_data():
    train_df, test_df = get_train_test_data(root_path='./')

    assert train_df.shape[0] > 0
    assert train_df.shape[1] == 12

    assert test_df.shape[0] > 0
    assert test_df.shape[1] == 12


def test_train_save_model(clean_data, cat_features):

    train_save_model(clean_data, cat_features, root_path='./')

    assert os.path.isfile("./model/model.joblib")
    assert os.path.isfile("./model/encoder.joblib")
    assert os.path.isfile("./model/lb.joblib")
