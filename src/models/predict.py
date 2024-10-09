
import os
import pickle
import logging
from typing import Optional

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import config as config


def load_model(model_name: str) -> tuple[RandomForestClassifier, str]:

    used_model_name = config.DEFAULT_MODEL_NAME
    used_model_path = config.DEFAULT_MODEL_PATH
    if model_name is not None and os.path.exists(
        config.DIR_MODELS / model_name
    ):
        used_model_name = model_name
        used_model_path = config.DIR_MODELS / model_name

    with open(used_model_path, 'rb') as f:
        model = pickle.load(f)

    logging.info(f"Las predicciones se realizan con: {used_model_path}")

    return model, used_model_name


def predict_category(df: pd.DataFrame, model_name: Optional[str]) -> tuple[list, str]:

    model, used_model_name = load_model(model_name)

    prediction_list = model.predict(df[config.MODEL_FEATURES])

    prediction_class_list = [
        config.MODEL_OUTPUT_TO_CLASS[int(prediction)] for prediction in prediction_list
    ]

    return prediction_class_list, used_model_name
