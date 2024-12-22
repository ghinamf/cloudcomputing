from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Load model dari file .pkl
MODEL_PATH = os.path.join(os.path.dirname(__file__), "yearsprediction.pkl")
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise Exception("Model file not found. Please ensure 'yearsprediction.pkl' exists in the same directory as this script.")

# Schema untuk request data
class PredictionRequest(BaseModel):
    features: list

# Endpoint prediksi
@app.post("/api/jawabarat")
async def predict(request: PredictionRequest):
    try:
        print("Received Request:", request.features)  # Log input request
        if len(request.features) != 1:
            raise HTTPException(status_code=400, detail="Invalid number of features. Model requires one feature (year).")

        features_array = np.array(request.features).reshape(1, -1)
        prediction = model.predict(features_array)
        print("Prediction Result:", prediction[0])  # Log hasil prediksi

        return {"prediction": int(prediction[0])}
    except Exception as e:
        print("Error:", str(e))  # Log error
        raise HTTPException(status_code=500, detail=str(e))


# CORS untuk mendukung frontend
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Anda dapat mengganti dengan domain frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to West Java Analysis API"}
