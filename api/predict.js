const xgboost = require('@xgboost/xgboost-node');
const path = require('path');

let model = null;

(async () => {
    model = await xgboost.loadModel(path.join(__dirname, 'xgboost_model.json'));
})();

module.exports = async (req, res) => {
    if (req.method !== 'POST') {
        return res.status(405).send({ error: "Only POST method is allowed" });
    }

    const { symptoms } = req.body;
    if (!Array.isArray(symptoms) || symptoms.length !== 24) {
        return res.status(400).send({ error: "Invalid input" });
    }

    try {
        const prediction = model.predict([symptoms]);
        res.status(200).send({ prediction: prediction[0] });
    } catch (error) {
        console.error(error);
        res.status(500).send({ error: "Failed to process the request" });
    }
};
