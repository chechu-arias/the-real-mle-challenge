
import numpy as np


def _num_bathroom_from_text(text):
    try:
        if isinstance(text, str):
            bath_num = text.split(" ")[0]
            return float(bath_num)
        else:
            return np.nan
    except ValueError:
        return np.nan


def load_bathrooms(df):

    df['bathrooms'] = df['bathrooms_text'].apply(_num_bathroom_from_text)

    return df
