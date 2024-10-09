
from pathlib import Path

DIR_REPO = Path.cwd()

DIR_DATA_RAW = Path(DIR_REPO) / "data" / "raw"
DIR_DATA_PROCESSED = Path(DIR_REPO) / "data" / "processed"
DIR_MODELS = Path(DIR_REPO) / "models"

FILEPATH_RAW_DATA = DIR_DATA_RAW / "listings.csv"

RAW_COLUMNS = [
    'id', 'neighbourhood_group_cleansed', 'room_type',
    'accommodates', 'bathrooms_text', 'bedrooms', 'price'
]

ROOM_TYPE_TO_CATEGORICAL = {
    "Shared room": 1, "Private room": 2, "Entire home/apt": 3, "Hotel room": 4
}
NEIGHB_TO_CATEGORICAL = {"Bronx": 1, "Queens": 2, "Staten Island": 3, "Brooklyn": 4, "Manhattan": 5}

ROOM_TYPE_OPTIONS = list(ROOM_TYPE_TO_CATEGORICAL.keys())
NEIGHB_OPTIONS = list(NEIGHB_TO_CATEGORICAL.keys())

MODEL_FEATURES = ['neighbourhood', 'room_type', 'accommodates', 'bathrooms', 'bedrooms']

MODEL_OUTPUT_TO_CLASS = ['Low', 'Mid', 'High', 'Luxury']

DEFAULT_MODEL_PATH = DIR_MODELS / "simple_classifier.pkl"
