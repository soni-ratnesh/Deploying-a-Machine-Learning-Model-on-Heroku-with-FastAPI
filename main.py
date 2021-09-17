
import os
import yaml

from fastapi import FastAPI
from schema import ModelInput
from pandas import DataFrame
from starter.inferance_model import run_inference


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

with open('config.yml') as f:
    config = yaml.load(f)

app = FastAPI()


@app.get("/")
async def get_items():
    return {"message": "Greetings!"}


@app.post("/")
async def inference(input_data: ModelInput):

    input_data = input_data.dict()

    change_keys = config['infer']['update_keys']
    columns = config['infer']['columns']
    cat_features = config['data']['cat_features']

    for new_key, old_key in change_keys:
        input_data[new_key] = input_data.pop(old_key)

    input_df = DataFrame(data=input_data.values(), index=input_data.keys()).T
    input_df = input_df[columns]

    prediction = run_inference(input_df, cat_features)

    return {"prediction": prediction}

