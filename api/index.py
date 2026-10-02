import json
import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load Model & Feature Names
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "housing_model.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "model", "model_columns.json")

model = joblib.load(MODEL_PATH)
with open(COLUMNS_PATH, "r") as f:
    model_columns = json.load(f)


class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus_semi_furnished: int
    furnishingstatus_unfurnished: int


@app.post("/api/predict")
def predict(features: HouseFeatures):
    data = features.dict()

    # Match column names created by pandas get_dummies
    formatted_data = {
        "area": data["area"],
        "bedrooms": data["bedrooms"],
        "bathrooms": data["bathrooms"],
        "stories": data["stories"],
        "mainroad": data["mainroad"],
        "guestroom": data["guestroom"],
        "basement": data["basement"],
        "hotwaterheating": data["hotwaterheating"],
        "airconditioning": data["airconditioning"],
        "parking": data["parking"],
        "prefarea": data["prefarea"],
        "furnishingstatus_semi-furnished": data[
            "furnishingstatus_semi_furnished"
        ],
        "furnishingstatus_unfurnished": data["furnishingstatus_unfurnished"],
    }

    # Ensure array follows exact feature ordering from training
    input_vector = [[formatted_data[col] for col in model_columns]]

    prediction = model.predict(input_vector)[0]
    return {"prediction": float(prediction)}
