from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

# Load the trained model
with open("vehicle-healthg-pred-model.pkl", "rb") as file:
    model = pickle.load(file)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form input data
        engine_rpm = float(request.form["engine_rpm"])
        lub_oil_pressure = float(request.form["lub_oil_pressure"])
        fuel_pressure = float(request.form["fuel_pressure"])
        coolant_pressure = float(request.form["coolant_pressure"])
        lub_oil_temp = float(request.form["lub_oil_temp"])
        coolant_temp = float(request.form["coolant_temp"])

        # Prepare input for prediction
        input_data = np.array(
            [
                [
                    engine_rpm,
                    lub_oil_pressure,
                    fuel_pressure,
                    coolant_pressure,
                    lub_oil_temp,
                    coolant_temp,
                ]
            ]
        )

        # Make prediction
        prediction = model.predict(input_data)
        confidence = model.predict_proba(input_data)[:, 1]

        # Return the result as JSON
        if prediction[0] == 0:
            return jsonify(
                {"prediction": "Normal", "confidence": f"{confidence[0]:.2%}"}
            )
        else:
            return jsonify(
                {"prediction": "Warning", "confidence": f"{confidence[0]:.2%}"}
            )
    except Exception as e:
        # Error handling
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
