<template>
  <div>
    <h1>Input any Japanese Text</h1>
  </div>
  
  <div>
    <textarea v-model="message" placeholder="add multiple lines"></textarea>
    <button @click="fetchBackendDataFlask">Send by flask</button>
    <button @click="fetchBackendDataFastAPI">Send by fastapi</button>
    <p>{{ anserText }}</p>
  </div>
</template>

<script>
import { fetchDataFastAPI } from './components/testefastapi.js'

export default {
  name: 'App',
  data() {
    return {
      message: '',
      anserText: ''
    }
  },
  methods: {
    async fetchBackendDataFastAPI() {
      try {
        console.log("Frontend side - text to send: ", this.message);
        const msg = await fetchDataFastAPI(this.message);
        console.log("msg: ", msg);
        this.anserText = msg; 
      } catch (error) {
        console.error('Erro ao buscar os dados:', error);
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
