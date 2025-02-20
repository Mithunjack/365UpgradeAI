import uvicorn
from fastapi import FastAPI
import joblib
import numpy as np

# Load trained model
model = joblib.load("best_model.pkl")

# Initialize FastAPI app
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

# Ensure the app runs when executed
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
