# from flask import Flask, request, jsonify
# import joblib
# import numpy as np
# import logging
# logging.basicConfig(level=logging.DEBUG)

# app = Flask(__name__)

# # Load model
# linear_model = 'yearsprediction.pkl'
# with open(linear_model, 'rb') as file:
#     model = joblib.load(file)
# # xgboost_model = joblib.load("xgboost_model.pkl")

# @app.route("/public/jawabarat", methods=["POST"])
# def predict_jawabarat():
#     app.logger.info("Request received: %s", request.get_json())
#     data = request.get_json()
#     features = np.array(data['features']).reshape(1, -1)
#     prediction = model.predict(features)
#     return jsonify({'prediction': prediction.tolist()})

# # @app.route("/api/mentalhealth", methods=["POST"])
# # def predict_mentalhealth():
# #     data = request.json["features"]
# #     prediction = xgboost_model.predict([data])
# #     return jsonify({"prediction": prediction.tolist()})

# if __name__ == "__main__":
#     app.run(debug=True)
