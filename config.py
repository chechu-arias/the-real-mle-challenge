
from pathlib import Path

DIR_REPO = Path.cwd()

DIR_DATA_RAW = Path(DIR_REPO) / "data" / "raw"
DIR_DATA_PROCESSED = Path(DIR_REPO) / "data" / "processed"
DIR_MODELS = Path(DIR_REPO) / "models"

FILEPATH_RAW_DATA = DIR_DATA_RAW / "listings.csv"

RAW_COLUMNS = [
    'id', 'neighbourhood_group_cleansed', 'property_type', 'room_type', 'latitude', 'longitude',
    'accommodates', 'bathrooms_text', 'bedrooms', 'beds','amenities', 'price'
]

ROOM_TYPE_TO_CATEGORICAL = {
    "Shared room": 1, "Private room": 2, "Entire home/apt": 3, "Hotel room": 4
}
NEIGHB_TO_CATEGORICAL = {"Bronx": 1, "Queens": 2, "Staten Island": 3, "Brooklyn": 4, "Manhattan": 5}

MODEL_FEATURES = ['neighbourhood', 'room_type', 'accommodates', 'bathrooms', 'bedrooms']

MODEL_OUTPUT_TO_CLASS = {'0.0': 'low', '1.0': 'mid', '2.0': 'high', '3.0': 'lux'}

MODEL_PATH = './models/simple_classifier.pkl'

