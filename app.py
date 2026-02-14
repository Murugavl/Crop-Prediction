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
def predict():
    # Helper to keep API URLs available after prediction
    api_context = {
        'geo_api_url': os.getenv('GEOCODING_API_URL', 'https://geocoding-api.open-meteo.com/v1/search'),
        'weather_api_url': os.getenv('WEATHER_API_URL', 'https://api.open-meteo.com/v1/forecast')
    }
    
    try:
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        return render_template("index.html", prediction_text = "The Predicted Crop is {}".format(prediction[0]), **api_context)
    except ValueError:
        return render_template("index.html", prediction_text = "Error: Please verify that all inputs are valid numbers.", **api_context)
    except Exception as e:
        return render_template("index.html", prediction_text = "An error occurred: {}".format(str(e)), **api_context)

if __name__ == "__main__":
    flask_app.run(debug=True)