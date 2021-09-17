from joblib import load
from .ml.data import process_data
from .ml.model import inference


def run_inference(data, cat_features, root_path):
    """
    Load model and run inference
    Parameters
    ----------
    root_path
    data
    cat_features

    Returns
    -------
    prediction
    """
    model = load(f"{root_path}/model/model.joblib")
    encoder = load(f"{root_path}/model/encoder.joblib")
    lb = load(f"{root_path}/model/lb.joblib")

    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(model, X)
    prediction = lb.inverse_transform(pred)[0]

    return prediction
