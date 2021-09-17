import os
from starter.val_model import val_model


def test_model(clean_data, cat_features):
    val_model(clean_data, cat_features, root_dir='./')

    assert os.path.isfile("./model/slice_output.txt")
