import os
from starter.ml.data import data_cleaning_stage


def test_clean_data():
    data_cleaning_stage(root_path='./')

    assert os.path.isfile('./data/clean/census.csv')
