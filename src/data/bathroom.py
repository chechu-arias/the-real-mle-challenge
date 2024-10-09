
import numpy as np
import pandas as pd


def _num_bathroom_from_text(text: str) -> float:
    try:
        if isinstance(text, str):
            bath_num = text.split(" ")[0]
            return float(bath_num)
        else:
            return np.nan
    except ValueError:
        return np.nan


def load_bathrooms(df: pd.DataFrame) -> pd.DataFrame:

    df['bathrooms'] = df['bathrooms_text'].apply(_num_bathroom_from_text)

    return df
