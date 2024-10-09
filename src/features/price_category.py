
import numpy as np
import pandas as pd


def build_price_category(df: pd.DataFrame) -> pd.DataFrame:

    df['category'] = pd.cut(
        df['price'],
        bins=[10, 90, 180, 400, np.inf],
        labels=[0, 1, 2, 3]
    )

    df = df.dropna(axis=0)

    return df
