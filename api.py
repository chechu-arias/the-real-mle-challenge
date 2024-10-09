import os
import time
import logging

import uvicorn
import pandas as pd
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import config as config
from src.models.train import train_model
from src.models.predict import predict_category
from src.features.build_features import build_training, build_inference_record
from src.DTO.category_classifier import InputCategoryClassifierEndpoint


logger = logging.getLogger("riesgos-alimentarios-api")

app = FastAPI()


@app.get("/train_category_model")
def train_category_endpoint(
    request: Request
) -> JSONResponse:

    start = time.time()
    client_host = request.client.host

    df = build_training()
    new_model_name = train_model(df)

    out_json = {"model_name": new_model_name}

    logger.info(
        f'{client_host} | classification processed in {round(time.time() - start, 2)} seconds'
    )

    return JSONResponse(content=jsonable_encoder(out_json))


@app.post("/predict_category")
def predict_category_endpoint(
    data: InputCategoryClassifierEndpoint, request: Request
) -> JSONResponse:

    start = time.time()
    client_host = request.client.host

    df = pd.DataFrame.from_records([data.dict()])
    df = build_inference_record(df)
    prediction = predict_category(df, data.model_name)

    out_json = {
        "id": data.id,
        "price_category": prediction[0]
    }

    logger.info(
        f'{client_host} | classification processed in {round(time.time() - start, 2)} seconds'
    )

    return JSONResponse(content=jsonable_encoder(out_json))


@app.get("/models")
def list_models() -> JSONResponse:

    path_string = config.DIR_MODELS

    out_json = {
        "models": [
            name for name in os.listdir(path_string) if name.endswith(".pkl")
        ]
    }

    return JSONResponse(content=jsonable_encoder(out_json))


if __name__ == '__main__':
    uvicorn.run(app=app)
