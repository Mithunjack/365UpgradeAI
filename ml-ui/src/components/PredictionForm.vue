<template>
    <div class="container">
      <h2>🔮 Machine Learning Predictor</h2>
  
      <form @submit.prevent="predict">
        <div v-for="(feature, index) in inputFeatures" :key="index">
          <label>Feature {{ index + 1 }}:</label>
          <input type="number" v-model="inputFeatures[index]" required />
        </div>
  
        <button type="submit">Predict</button>
      </form>
  
      <div v-if="prediction !== null">
        <h3>Prediction: {{ prediction }}</h3>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        inputFeatures: Array(7).fill(""), // Replace with actual number of features
        prediction: null,
      };
    },
    methods: {
      async predict() {
        try {
          const response = await axios.post(
            "https://365-data-science-production.up.railway.app/predict/",
            { features: this.inputFeatures.map(Number) } // Convert strings to numbers
          );
          this.prediction = response.data.prediction;
        } catch (error) {
          console.error("Error making prediction:", error);
          alert("Failed to get prediction. Check backend!");
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
  }
  input {
    display: block;
    margin: 10px auto;
    padding: 5px;
  }
  button {
    padding: 10px;
    background: #42b983;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  