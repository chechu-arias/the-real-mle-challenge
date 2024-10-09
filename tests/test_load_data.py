
import sys
sys.path.append('.')

import numpy as np
import pandas as pd

from src.data.utils import process_bathrooms


def test_add_bathroom_column():
    data = {
        'id': [1, 2, 3],
        'bathrooms_text': ['2 baths', '', '']
    }
    df = pd.DataFrame(data)

    result_df = process_bathrooms(df)

    expected_data = {
        'id': [1, 2, 3],
        'bathrooms_text': ['2 baths', '', ''],
        'bathrooms': [2, np.nan, np.nan]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df, expected_df)
