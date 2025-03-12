<template>
  <div id="app">
    <PredictionForm />
  </div>
</template>

<script>
import PredictionForm from "./components/PredictionForm.vue";

export default {
  components: {
    PredictionForm,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 50px;
}
</style>
