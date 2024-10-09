
import sys
sys.path.append('.')

from datetime import date as dt

import pytest
import requests

import config as config

BASE_URL = "http://localhost:8080"


def test_models_endpoint_valid():
    url = f"{BASE_URL}/models"

    response = requests.get(url)

    assert response.status_code == 200

    response_json = response.json()
    assert 'models' in response_json
    assert isinstance(response_json['models'], list)


def test_train_endpoint_valid():
    url = f"{BASE_URL}/train_category_model"

    response = requests.get(url)

    assert response.status_code == 200

    response_json = response.json()
    assert 'model_name' in response_json
    assert isinstance(response_json['model_name'], str)
    assert response_json['model_name'] is not None
    assert response_json['model_name'].startswith(str(dt.today()))
    assert response_json['model_name'].endswith('simple_classifier.pkl')


def test_predict_endpoint_valid():
    url = f"{BASE_URL}/predict_category"

    payload = {
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


    response = requests.post(url, json=payload)

    assert response.status_code == 200

    response_json = response.json()
    assert 'id' in response_json
    assert 'price_category' in response_json
    assert 'model' in response_json
    assert isinstance(response_json['price_category'], str)
    assert response_json['price_category'] in config.MODEL_OUTPUT_TO_CLASS


def test_predict_endpoint_invalid():
    url = f"{BASE_URL}/predict_category"

    invalid_payload = {
        "id": 1,
        # Missing other required fields
    }

    response = requests.post(url, json=invalid_payload)

    assert response.status_code == 422

    response_json = response.json()
    assert 'detail' in response_json
    assert isinstance(response_json['detail'], list) and len(response_json['detail']) > 0
    assert 'msg' in response_json['detail'][0]
    assert 'Field required' in response_json['detail'][0]['msg']
