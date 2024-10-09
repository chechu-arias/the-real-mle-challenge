
import pandas as pd

import config as config


def build_neighbourhood(df: pd.DataFrame) -> pd.DataFrame:

    df["neighbourhood"] = df["neighbourhood"].map(config.NEIGHB_TO_CATEGORICAL)

    return df