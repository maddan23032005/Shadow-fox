const express = require('express');
const router = express.Router();
const { GoogleGenerativeAI } = require('@google/generative-ai');
require('dotenv').config();

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

// Use a valid model from the list
const model = genAI.getGenerativeModel({ model: 'models/gemini-2.5-pro' });

router.post('/', async (req, res) => {
  try {
    const prompt = `Please format your response using markdown. Include proper indentation and wrap code in triple backticks. Question:\n\n${req.body.message}`;

    const result = await model.generateContent(prompt);
    const response = result.response.text();

    res.json({ bot: response });
  } catch (error) {
    console.error('❌ Gemini Error:', error.message);
    res.status(500).json({ bot: "❌ Error getting response from Gemini API." });
  }
});

module.exports = router;
