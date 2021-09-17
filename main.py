import argparse
import hydra
import logging
from starter.ml.data import data_cleaning_stage
from omegaconf import DictConfig

_steps = [
    "data_cleaning",
    "train_test_model",
    "check_score"
]


@hydra.main(config_name='config')
def go(config: DictConfig):
    """
    Run pipeline stages
    """
    logging.basicConfig(level=logging.INFO)

    root_path = hydra.utils.get_original_cwd()

    # Steps to execute
    steps_par = config['main']['steps']
    active_steps = steps_par.split(",") if steps_par != "all" else _steps

    if "data_cleaning" in active_steps:
        logging.info("Cleaning and saving raw_data")
        data_cleaning_stage()


    if "train_test_model" in active_steps:
        logging.info("Train/Test model procedure started")
        pass

    if "check_score" in active_steps:
        logging.info("Score check procedure started")
        pass

if __name__ == "__main__":
    """
    Main entrypoint
    """
    go()
