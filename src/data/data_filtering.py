
import pandas as pd


def _filter_nan_records(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(axis=0)

    return df


def _filter_price_records(df: pd.DataFrame) -> pd.DataFrame:

    df = df[df['price'] >= 10]

    return df


def filter_data(df: pd.DataFrame) -> pd.DataFrame:

    df = _filter_price_records(df)
    df = _filter_nan_records(df)

    return df
