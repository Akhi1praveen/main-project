from flask import Flask, request, jsonify
from flask_cors import CORS
import util
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/flood_predict', methods=['POST'])
def flood_predict():
    try:
        print("Received request data:", request.form)

        Rainfall = float(request.form['Rainfall'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        River_Discharge = float(request.form['River_Discharge'])
        Water_Level = float(request.form['Water_Level'])
        Elevation = float(request.form['Elevation'])
        Historical_Floods = int(request.form['Historical_Floods'])

        # Get prediction
        prediction = util.predict_flood(Rainfall, Temperature, Humidity, River_Discharge, Water_Level, Elevation, Historical_Floods)

        # Convert NumPy int64 to Python int
        if isinstance(prediction, (np.int64, np.int32)):
            prediction = int(prediction)

        response = jsonify({'flood_predicted': prediction})
        return response

    except Exception as e:
        print("Error:", str(e))  # Print error in Flask console
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("Starting python flask server for flood prediction...")
    util.load_artifacts()
    app.run(debug=True)  # Enable debug mode

