
import pandas as pd

import config as config
from src.features.build_features import build_training, build_inference_record
from src.models.predict import predict_category

if __name__ == '__main__':

    df = build_training()
    df = build_inference_record(df)
    prediction = predict_category(df)
    print(prediction)
