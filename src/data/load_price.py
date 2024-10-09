
import pandas as pd


def load_price(df: pd.DataFrame) -> pd.DataFrame:

    df['price'] = df['price'].str.extract(r"(\d+).")
    df['price'] = df['price'].astype(int)

    return df
