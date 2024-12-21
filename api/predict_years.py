import sys
import json
import joblib

# Load model
model = joblib.load("years_prediction.pkl")

# Parse input features
features = json.loads(sys.argv[1])

# Predict
prediction = model.predict([features])
print(prediction[0])
