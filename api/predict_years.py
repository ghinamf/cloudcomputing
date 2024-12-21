import sys
import json
import joblib

# Load model
try:
    model = joblib.load("yearsprediction.pkl")
except Exception as e:
    print("Error loading model:", str(e))
    sys.exit(1)

# Parse input features
features = json.loads(sys.argv[1])

# Predict
try:
    prediction = model.predict([features])
    print(prediction[0])
except Exception as e:
    print("Error during prediction:", str(e))
    sys.exit(1)
