
import pandas as pd

import config as config


def load_raw_data() -> pd.DataFrame:
    df = pd.read_csv(config.FILEPATH_RAW_DATA, usecols=config.RAW_COLUMNS)

    df.rename(
        columns={'neighbourhood_group_cleansed': 'neighbourhood'},
        inplace=True
    )

    return df