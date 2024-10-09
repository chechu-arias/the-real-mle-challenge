
import pandas as pd

from src.data.utils import process_bathrooms, process_price
from src.data.data_filtering import filter_data

import config as config


def _load_raw_data() -> pd.DataFrame:
    df = pd.read_csv(config.FILEPATH_RAW_DATA, usecols=config.RAW_COLUMNS)

    df.rename(
        columns={'neighbourhood_group_cleansed': 'neighbourhood'},
        inplace=True
    )

    return df


def load_data() -> pd.DataFrame:

    df = _load_raw_data()
    df = process_bathrooms(df)
    df = process_price(df)
    df = filter_data(df)

    return df
