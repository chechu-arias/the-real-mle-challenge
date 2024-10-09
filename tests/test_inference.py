
import sys
sys.path.append('.')

from datetime import date as dt

from src.features.build_features import build_training
from src.models.predict import predict_category

import config as config


def test_valid_output():
    # This test checks if the prediction output has correct format
    df = build_training()
    prediction, model_used = predict_category(df, model_name=None)

    assert isinstance(prediction, list)
    assert len(prediction) == len(df)
    assert model_used == config.DEFAULT_MODEL_NAME
