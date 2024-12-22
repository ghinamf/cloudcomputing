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
    with open(MODEL_PATH, "rb") as file:
        model = joblib.load(file)
except FileNotFoundError:
    raise Exception("Model file not found. Please ensure 'yearsprediction.pkl' exists in the same directory as this script.")

# Schema untuk request data
class PredictionRequest(BaseModel):
    features: list

# Route untuk endpoint prediksi
@app.post("/api/jawabarat")
async def predict(request: PredictionRequest):
    try:
        # Validasi jumlah fitur
        if len(request.features) != 1:  # Pastikan hanya satu fitur (tahun)
            raise HTTPException(status_code=400, detail="Jumlah fitur tidak sesuai. Model membutuhkan satu fitur (year).")

        # Format data fitur ke numpy array
        features_array = np.array(request.features).reshape(1, -1)

        # Lakukan prediksi
        prediction = model.predict(features_array)
        
        # Berikan respons
        return {"prediction": int(prediction[0])}  # Pastikan hanya mengirim prediksi pertama
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Middleware CORS untuk mendukung domain berbeda
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain frontend jika memungkinkan
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to West Java Analysis API"}
