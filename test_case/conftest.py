import pytest
import yaml
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


@pytest.fixture
def cat_features():
    """
    Get dataset
    """
    with open('config.yml') as f:
        config = yaml.load(f)

    return config['data']['cat_features']


@pytest.fixture
def train_data(clean_data):
    """
    Get dataset
    """
    df = clean_data.drop('salary', axis=1)
    return df


@pytest.fixture
def test_data(clean_data):
    """
    Get dataset
    """
    df = clean_data['salary']
    return df


@pytest.fixture
def inference_data_low():
    data_dict = {'age': 19,
                 'workclass': 'Private',
                 'fnlgt': 77516,
                 'education': 'HS-grad',
                 'marital-status': 'Never-married',
                 'occupation': 'Own-child',
                 'relationship': 'Husband',
                 'race': 'Black',
                 'sex': 'Male',
                 'hours-per-week': 40,
                 'native-country': 'United-States'
                 }
    df = pd.DataFrame(data=data_dict.values(),
                      index=data_dict.keys()).T
    return df


@pytest.fixture
def inference_data_high():
    data_dict = {'age': 33,
                 'workclass': 'Private',
                 'fnlgt': 149184,
                 'education': 'HS-grad',
                 'marital-status': 'Never-married',
                 'occupation': 'Prof-specialty',
                 'relationship': 'Not-in-family',
                 'race': 'White',
                 'sex': 'Male',
                 'hours-per-week': 60,
                 'native-country': 'United-States'
                 }
    df = pd.DataFrame(data=data_dict.values(),
                      index=data_dict.keys()).T
    return df
