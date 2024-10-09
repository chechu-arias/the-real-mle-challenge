
import requests

ENDPOINT_URL = "http://localhost:8080/"

response = requests.get(ENDPOINT_URL + "models")
print(response.text)

response = requests.get(ENDPOINT_URL + "train_category_model")
print(response.text)

response = requests.get(ENDPOINT_URL + "models")
print(response.text)

input_inference = {
    "id": 1001,
    "accommodates": 4,
    "room_type": "Entire home/apt",
    "beds": 2,
    "bedrooms": 1,
    "bathrooms": 2,
    "neighbourhood": "Brooklyn",
    "tv": 1,
    "elevator": 1,
    "internet": 0,
    "latitude": 40.71383,
    "longitude": -73.9658,
}

response = requests.post(ENDPOINT_URL + "predict_category", json=input_inference)
print(response.text)

input_inference = {
    "id": 1001,
    "accommodates": 4,
    "room_type": "Entire home/apt",
    "beds": 2,
    "bedrooms": 1,
    "bathrooms": 2,
    "neighbourhood": "Brooklyn",
    "tv": 1,
    "elevator": 1,
    "internet": 0,
    "latitude": 40.71383,
    "longitude": -73.9658,
    "model_name": "2024-10-09_acc_60.05_simple_classifier.pkl"
}

response = requests.post(ENDPOINT_URL + "predict_category", json=input_inference)
print(response.text)
