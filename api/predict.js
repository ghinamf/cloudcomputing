const xgboost = require('@xgboost/xgboost-node'); // Install via npm
const path = require('path');

// Load the XGBoost model
let model = null;
(async () => {
    model = await xgboost.loadModel(path.join(__dirname, '../xgboost_model.json'));
})();

module.exports = async (req, res) => {
    if (req.method !== 'POST') {
        return res.status(405).json({ error: "Only POST method is allowed" });
    }

    try {
        // Ensure the request body is parsed
        const { symptoms } = JSON.parse(req.body || '{}');
        
        if (!Array.isArray(symptoms) || symptoms.length !== 24) {
            return res.status(400).json({ error: "Invalid input. Expected 24 symptoms." });
        }

        // Predict using the loaded model
        const prediction = model.predict([symptoms]);
        res.status(200).json({ prediction: prediction[0] });
    } catch (error) {
        console.error("Error in prediction function:", error);
        res.status(500).json({ error: "Failed to process the request" });
    }
};
