
import pandas as pd

from src.data.raw_data import load_raw_data
from src.data.bathroom import load_bathrooms
from src.data.load_price import load_price
from src.data.data_filtering import filter_data


def load_data() -> pd.DataFrame:

    df = load_raw_data()

    df = load_bathrooms(df)
    df = load_price(df)
    df = filter_data(df)

    return df
