import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create flask app
flask_app = Flask(__name__)
# Alias for Vercel
app = flask_app 
model = pickle.load(open("crop_prediction.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html", 
                         geo_api_url=os.getenv('GEOCODING_API_URL', 'https://geocoding-api.open-meteo.com/v1/search'),
                         weather_api_url=os.getenv('WEATHER_API_URL', 'https://api.open-meteo.com/v1/forecast'))

@flask_app.route("/predict", methods = ["POST"])
@flask_app.route("/predict", methods = ["POST"])
def predict():
    try:
        # Check if request is JSON (for AJAX) or Form data
        if request.is_json:
            data = request.get_json()
            float_features = [float(data[x]) for x in data]
        else:
            float_features = [float(x) for x in request.form.values()]
            
        features = [np.array(float_features)]
        prediction = model.predict(features)
        
        return jsonify({'prediction': prediction[0]})
        
    except ValueError:
        return jsonify({'error': "Please verify that all inputs are valid numbers."}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    flask_app.run(debug=True)