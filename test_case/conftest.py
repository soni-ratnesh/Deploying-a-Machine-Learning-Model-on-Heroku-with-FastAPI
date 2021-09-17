import pytest
import pandas as pd

from starter.ml.data import clean_dataset


@pytest.fixture
def raw_data():
    """
    Get dataset
    """
    df = pd.read_csv("data/raw/census.csv", skipinitialspace=True)

    return df


@pytest.fixture
def clean_data(raw_data):
    """
    Get dataset
    """
    df = clean_dataset(raw_data)
    return df
