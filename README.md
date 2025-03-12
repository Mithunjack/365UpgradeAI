# 🚀 Predict student purchase behavior 🚀

## 📖 Overview
This project is a **Machine Learning API** built using **FastAPI**, designed to predict whether students will upgrade to a paid plan based on their platform engagement metrics.

The API is **containerized with Docker** and **deployed on Railway** using **GitHub Actions** for CI/CD automation. Additionally, a **Vue.js frontend** has been implemented for seamless interaction with the API.

## 🎯 Features
✅ **FastAPI for Serving ML Predictions**  
✅ **Pre-trained ML Model (RandomForestClassifier)**  
✅ **MLflow for Model Tracking & Versioning**  
✅ **Dockerized & Deployed on Railway**  
✅ **Automatic Deployment via GitHub Actions**  
✅ **Swagger UI for API Testing (`/docs`)**  
✅ **Vue.js Frontend for User Interaction**

## 📂 Project Structure
```
├── .github/workflows/  # GitHub Actions Workflow
├── main.py         # FastAPI application
├── best_model.pkl  # Trained ML model
├── requirements.txt # Dependencies
├── Dockerfile      # Docker Configuration
├── ml-ui/
│   ├── src/components/PredictionForm.vue  # Vue.js component
│   ├── src/App.vue     # Vue.js main application
│   ├── package.json    # Frontend dependencies
│   ├── netlify.toml    # Netlify Deployment Config
├── README.md           # Documentation
```

## 🔧 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/your-repo-name.git
cd your-repo-name
```

### **2️⃣ Install Dependencies**
```bash
pip install -r backend/requirements.txt
```

### **3️⃣ Run FastAPI Locally**
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```
Now, open **Swagger UI** to test the API:  
👉 `http://127.0.0.1:8000/docs`

## 🐳 Docker Deployment
### **1️⃣ Build the Docker Image**
```bash
docker build -t ml-fastapi backend/.
```

### **2️⃣ Run the Container**
```bash
docker run -p 8000:8000 ml-fastapi
```
The API will be available at:  
👉 `http://127.0.0.1:8000/docs`

## 🚀 Deployment on Railway
This project is **deployed on Railway**, using **GitHub Actions** to automate deployment.

### **🔹 How Deployment Works**
1. **Push Code to GitHub** → GitHub Actions builds Docker image & pushes to Docker Hub.
2. **Railway Pulls & Runs the Container** → New model updates are deployed instantly.
3. **API Becomes Live** → Accessible via Railway’s public URL.

### **🔹 Public API URL**
👉 `https://365-data-science-production.up.railway.app`

## 📡 API Endpoints
### **1️⃣ Root Endpoint**
```http
GET /
```
**Response:**
```json
{"message": "FastAPI ML Model is running!"}
```

### **2️⃣ Prediction Endpoint**
```http
POST /predict/
```
#### **Request (JSON Format):**
```json
{
    "features": [5.1, 3.5, 1.4, 0.2, 10.5, 8.9, 3.2]
}
```
#### **Response:**
```json
{
    "prediction": 1
}
```

## 🔍 Using MLflow for Model Tracking
Instead of manually saving `best_model.pkl`, this project uses **MLflow** for model management.

### **1️⃣ Save Model to MLflow**
```python
import mlflow
import mlflow.sklearn

mlflow.set_experiment("student_purchase_prediction")

with mlflow.start_run():
    mlflow.sklearn.log_model(rf_clf, "random_forest_model")
```

### **2️⃣ Load Model Dynamically in FastAPI**
```python
import mlflow.pyfunc
model = mlflow.pyfunc.load_model("models:/random_forest_model/Production")
```
✅ This ensures **FastAPI always serves the latest version of the model**.

## 🔥 CI/CD with GitHub Actions
The project uses **GitHub Actions** for continuous deployment.

### **🔹 GitHub Actions Workflow**
1. **On Push to `main` Branch:**
   - Builds a **Docker image**
   - Pushes to **Docker Hub**
   - Deploys to **Railway**

### **🔹 Workflow File (`.github/workflows/deploy.yml`)**
```yaml
name: Deploy FastAPI with Docker

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v2

    - name: Log in to Docker Hub
      run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin

    - name: Build & Push Docker Image
      run: |
        docker build -t YOUR_DOCKER_USERNAME/ml-fastapi:latest backend/.
        docker push YOUR_DOCKER_USERNAME/ml-fastapi:latest

    - name: Deploy to Railway
      run: |
        railway redeploy YOUR_SERVICE_ID
```

## 🚀 Frontend Deployment (Vue.js)
The frontend is built with Vue.js and deployed on **Netlify**.

### **🔹 Deploy Vue.js on Netlify**
```bash
npm install -g netlify-cli
npm run build
netlify deploy --prod
```
### **🔹 Public Frontend URL**
👉 `https://frolicking-florentine-149b05.netlify.app/`

## 📌 Future Improvements
🔹 Enhance Vue UI for better user experience  
🔹 Add **JWT authentication** for secure access  
🔹 Deploy MLflow on Railway for better model management  

## 💡 Conclusion
This project demonstrates how to **train, deploy, and automate an ML model using FastAPI, Docker, and Railway**.
With **MLflow integration, automatic deployment, and CI/CD**, the workflow is **fully scalable & production-ready!** 🚀


## 📝 License
This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE) file for details.

