
import pandas as pd

from src.data.load_data import load_data
from src.features.utils import build_room_type, build_neighbourhood, build_price_category

import config as config


def build_training() -> pd.DataFrame:
    df = load_data()

    df = build_room_type(df)
    df = build_neighbourhood(df)
    df = build_price_category(df)

    return df
    

def build_inference_record(df: pd.DataFrame) -> pd.DataFrame:

    df = build_room_type(df)
    df = build_neighbourhood(df)

    return df
