
import pandas as pd

import config as config
from src.features.build_features import build_training
from src.models.predict import predict_category

if __name__ == '__main__':

    df = build_training()
    prediction, model_used = predict_category(df, model_name=None)
    print(prediction)
