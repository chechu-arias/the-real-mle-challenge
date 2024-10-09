
import pickle
from sklearn.ensemble import RandomForestClassifier

import config as config


def load_model() -> RandomForestClassifier:

    with open(config.MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    return model


def predict_category(df):

    model = load_model()

    prediction_list = model.predict(df[config.MODEL_FEATURES])

    prediction_class_list = [
        config.MODEL_OUTPUT_TO_CLASS[str(prediction)] for prediction in prediction_list
    ]

    return prediction_class_list
