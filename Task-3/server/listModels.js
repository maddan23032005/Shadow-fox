const axios = require('axios');
require('dotenv').config();

const API_KEY = process.env.GEMINI_API_KEY;
const URL = 'https://generativelanguage.googleapis.com/v1/models?key=' + API_KEY;

async function listModels() {
  try {
    const response = await axios.get(URL);
    const models = response.data.models;

    console.log('✅ Available Gemini Models:\n');
    models.forEach(model => {
      console.log(`🧠 ${model.name}`);
    });
  } catch (error) {
    console.error('❌ Failed to fetch models:', error.message);
  }
}

listModels();
