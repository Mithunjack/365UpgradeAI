from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("best_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define request model
class FeaturesInput(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "FastAPI ML Model is running!"}

@app.post("/predict/")
def predict(data: FeaturesInput):
    try:
        print(f"📥 Received input: {data.features}")  # Debugging log
        features = np.array(data.features).reshape(1, -1)
        prediction = model.predict(features)
        print(f"📤 Model prediction: {prediction[0]}")  # Debugging log
        return {"prediction": int(prediction[0])}
    except Exception as e:
        print(f"❌ Prediction failed: {e}")  # Debugging log
        return {"error": str(e)}
