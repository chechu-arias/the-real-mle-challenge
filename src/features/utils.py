
import numpy as np
import pandas as pd

import config as config


def build_neighbourhood(df: pd.DataFrame) -> pd.DataFrame:

    df["neighbourhood"] = df["neighbourhood"].map(config.NEIGHB_TO_CATEGORICAL)

    return df


def build_room_type(df: pd.DataFrame) -> pd.DataFrame:

    df["room_type"] = df["room_type"].map(config.ROOM_TYPE_TO_CATEGORICAL)

    return df


def build_price_category(df: pd.DataFrame) -> pd.DataFrame:

    df['category'] = pd.cut(
        df['price'],
        bins=[10, 90, 180, 400, np.inf],
        labels=[0, 1, 2, 3]
    )

    df = df.dropna(axis=0)

    return df