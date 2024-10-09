
import sys
sys.path.append('.')

from datetime import date as dt

from src.features.build_features import build_training
from src.models.train import train_model


def test_valid_output():
    # This test checks if the model trained has correct format
    df = build_training()
    model_name = train_model(df)

    assert model_name is not None
    assert model_name.startswith(str(dt.today()))
    assert model_name.endswith('simple_classifier.pkl')
