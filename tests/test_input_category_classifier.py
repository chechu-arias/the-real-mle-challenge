
import sys
sys.path.append('.')

import pytest

from pydantic import ValidationError
from src.DTO.category_classifier import InputCategoryClassifierEndpoint

import config as config


def test_valid_input():
    # This test checks if the model accepts valid data
    valid_data = {
        "id": 1,
        "accommodates": 4,
        "room_type": "Private room",
        "beds": 2,
        "bedrooms": 1,
        "bathrooms": 1,
        "neighbourhood": "Bronx",
        "tv": 1,
        "elevator": 1,
        "internet": True,
        "latitude": 37.7749,
        "longitude": -122.4194
    }

    model = InputCategoryClassifierEndpoint(**valid_data)

    assert model.room_type == valid_data['room_type']
    assert model.neighbourhood == valid_data['neighbourhood']


def test_invalid_room_type():
    # This test checks if the model raises a validation error for an invalid room_type
    invalid_data = {
        "id": 1,
        "accommodates": 4,
        "room_type": "Luxury room",  # Invalid room_type
        "beds": 2,
        "bedrooms": 1,
        "bathrooms": 1,
        "neighbourhood": "Bronx",
        "tv": 1,
        "elevator": 1,
        "internet": True,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "classification_name": "default_model"
    }

    with pytest.raises(ValidationError) as excinfo:
        InputCategoryClassifierEndpoint(**invalid_data)

    assert "room_type must be one of" in str(excinfo.value)


def test_invalid_neighbourhood():
    # This test checks if the model raises a validation error for an invalid neighbourhood
    invalid_data = {
        "id": 1,
        "accommodates": 4,
        "room_type": "Private room",
        "beds": 2,
        "bedrooms": 1,
        "bathrooms": 1,
        "neighbourhood": "Unknown Place",  # Invalid neighbourhood
        "tv": 1,
        "elevator": 1,
        "internet": True,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "classification_name": "default_model"
    }

    with pytest.raises(ValidationError) as excinfo:
        InputCategoryClassifierEndpoint(**invalid_data)

    assert "neighbourhood must be one of" in str(excinfo.value)
