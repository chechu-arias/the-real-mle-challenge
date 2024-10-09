
import pandas as pd

import config as config


def build_room_type(df: pd.DataFrame) -> pd.DataFrame:

    df["room_type"] = df["room_type"].map(config.ROOM_TYPE_TO_CATEGORICAL)

    return df
