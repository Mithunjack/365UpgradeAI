from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("best_model.pkl")
expected_features = model.n_features_in_

# Initialize FastAPI app
app = FastAPI()

# ✅ Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Allows all domains (change to specific domain in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define request model
class FeaturesInput(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "FastAPI ML Model is running!"}

@app.post("/predict/")
def predict(data: FeaturesInput):
    try:
        # Check if input length matches the model's expected features
        if len(data.features) != expected_features:
            raise HTTPException(status_code=400, detail=f"Expected {expected_features} features, but got {len(data.features)}.")

        print(f"📥 Received input: {data.features}")  # Debug log
        features = np.array(data.features).reshape(1, -1)
        prediction = model.predict(features)
        print(f"📤 Model prediction: {prediction[0]}")  # Debug log
        return {"prediction": int(prediction[0])}
    except Exception as e:
        print(f"❌ Prediction failed: {e}")  # Debug log
        return {"error": str(e)}
