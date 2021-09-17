import argparse
import hydra
import logging
from starter.ml.data import data_cleaning_stage
from starter.train_model import get_train_test_data, train_save_model
from omegaconf import DictConfig

_steps = [
    "data_cleaning",
    "train_model",
    "check_score"
]


@hydra.main(config_name="config.yml")
def go(config: DictConfig):
    """
    Run pipeline stages
    """
    logging.basicConfig(level=logging.INFO)

    root_path = hydra.utils.get_original_cwd()
    # Steps to execute
    steps_par = config['main']['steps']
    active_steps = steps_par.split(",") if steps_par != "all" else _steps

    cat_features = config['data']['cat_features']

    if "data_cleaning" in active_steps:
        logging.info("Cleaning and saving raw_data")
        data_cleaning_stage(root_path)

    train_df, test_df = get_train_test_data(root_path)

    if "train_model" in active_steps:
        logging.info("Train/Test model procedure started")
        train_save_model(train_df, cat_features, root_path)

    if "check_score" in active_steps:
        logging.info("Score check procedure started")
        pass

if __name__ == "__main__":
    """
    Main entrypoint
    """
    go()
