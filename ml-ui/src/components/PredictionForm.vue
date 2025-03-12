<template>
    <div class="container">
      <h2>🔮 Machine Learning Predictor</h2>
  
      <form @submit.prevent="predict">
        <div v-for="(feature, index) in inputFeatures" :key="index" class="input-group">
          <label>Feature {{ index + 1 }}:</label>
          <input 
            type="number"
            step="any"
            v-model="inputFeatures[index]"
            required
            placeholder="Enter a number"
          />
        </div>
  
        <button type="submit">🔍 Predict</button>
      </form>
  
      <div v-if="prediction !== null" class="result">
        <h3>✅ Prediction: {{ prediction }}</h3>
      </div>
  
      <div v-if="error" class="error">
        ❌ {{ error }}
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        inputFeatures: Array(7).fill(""), // ✅ Replace with actual number of features
        prediction: null,
        error: null
      };
    },
    methods: {
      async predict() {
        this.prediction = null;
        this.error = null;
        
        try {
          const response = await axios.post(
            "https://365-data-science-production.up.railway.app/predict/",
            { features: this.inputFeatures.map(Number) },  // ✅ Converts input to float numbers
            { headers: { "Content-Type": "application/json" } }
          );
  
          this.prediction = response.data.prediction;
        } catch (error) {
          console.error("❌ Error making prediction:", error);
          this.error = "Failed to get prediction. Please check your input and try again!";
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 400px;
    margin: auto;
    text-align: center;
    font-family: Arial, sans-serif;
  }
  .input-group {
    margin: 10px 0;
  }
  input {
    display: block;
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  button {
    padding: 10px;
    background: #42b983;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
  }
  .result {
    margin-top: 20px;
    font-size: 18px;
    color: green;
  }
  .error {
    margin-top: 20px;
    font-size: 16px;
    color: red;
  }
  </style>
  