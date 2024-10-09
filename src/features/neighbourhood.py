
import config as config

def build_neighbourhood(df):

    df["neighbourhood"] = df["neighbourhood"].map(config.NEIGHB_TO_CATEGORICAL)

    return df