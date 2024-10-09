
import numpy as np
import pandas as pd

import config as config


def _num_bathroom_from_text(text: str) -> float:
    try:
        if isinstance(text, str):
            bath_num = text.split(" ")[0]
            return float(bath_num)
        else:
            return np.nan
    except ValueError:
        return np.nan


def process_bathrooms(df: pd.DataFrame) -> pd.DataFrame:

    df['bathrooms'] = df['bathrooms_text'].apply(_num_bathroom_from_text)

    return df


def process_price(df: pd.DataFrame) -> pd.DataFrame:

    df['price'] = df['price'].str.extract(r"(\d+).")
    df['price'] = df['price'].astype(int)

    return df
