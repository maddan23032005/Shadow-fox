require('dotenv').config(); // ✅ Load .env variables

console.log("✅ Loaded API Key:", process.env.GEMINI_API_KEY ? "Yes" : "No");  // ✅ Gemini API Key check

const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');

// ✅ Use relative paths instead of absolute file paths
const chatRoutes = require('./routes/chat');
const authRoutes = require('./routes/auth');

const app = express();
const PORT = process.env.PORT || 4000;  // ✅ Uses 4000 unless overridden

// ✅ Middleware
app.use(cors());
app.use(express.json());

// ✅ Routes
app.use('/api/chat', chatRoutes);      // Chatbot route
app.use('/api/auth', authRoutes);      // Auth route (Login/Register)

// ✅ Connect MongoDB and Start Server
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    app.listen(PORT, () => {
        console.log(`🚀 Server running on http://localhost:${PORT}`);
    });
}).catch((err) => {
    console.error('❌ MongoDB connection error:', err);
});
