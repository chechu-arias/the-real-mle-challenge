

def load_price(df):

    df['price'] = df['price'].str.extract(r"(\d+).")
    df['price'] = df['price'].astype(int)

    return df
