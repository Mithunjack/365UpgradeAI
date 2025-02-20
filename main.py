from fastapi import FastAPI
import joblib
import numpy as np

# Load your trained model (make sure best_model.pkl is in the same folder)
model = joblib.load("best_model.pkl")

# Create FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI ML Model is running!"}

@app.post("/predict/")
def predict(features: list):
    try:
        features = np.array(features).reshape(1, -1)  # Reshape input
        prediction = model.predict(features)  # Make prediction
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
