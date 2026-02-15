# 🌱 Smart Crop Prediction System

## 🌟 Project Overview
This project is an advanced Machine Learning web application that predicts the most suitable crop for cultivation based on **scientific soil analysis** and **real-time environmental data**.

By integrating **Open-Meteo APIs**, users can simply enter their city name, and the system automatically fetches critical climate parameters (Temperature, Humidity, Rainfall) to provide accurate, data-driven recommendations.

## 🚀 Key Features
- **Intelligent Crop Recommendation**: Uses a robust **Random Forest Classifier** trained on 2,200 agricultural samples.
- **Micro-Climate Analysis**: Integrates directly with weather satellites via Open-Meteo to fetch real-time:
  - 🌡️ Temperature
  - 💧 Humidity
  - 🌧️ Rainfall (Seasonal approximation)
- **Automatic Geolocation**: Just type a city name (e.g., "Coimbatore"), and the system geolocates it instantly.
- **Premium UI/UX**: Features a modern **Glassmorphism Design**, dark mode aesthetics, and smooth animations.
- **Mobile Responsive**: Fully optimized for use on smartphones and tablets in the field.

## 📊 Dataset & Model
- **Dataset**: `Crop_recommendation.csv` containing 2,200 samples for 22 unique crops.
- **Input Features**:
  1. **Nitrogen (N)**: Ratio of Nitrogen content in soil.
  2. **Phosphorus (P)**: Ratio of Phosphorus content in soil.
  3. **Potassium (K)**: Ratio of Potassium content in soil.
  4. **pH**: Soil acidity/alkalinity level.
  5. **Environmental Factors**: Temperature, Humidity, Rainfall (Auto-fetched).
- **Algorithm**: **Random Forest Classifier** (Scikit-Learn).
  - Selected for its high accuracy and ability to handle non-linear relationships in agricultural data.
  - Achieves **~99% Accuracy** on test data.

## 🛠️ Technology Stack
- **Frontend**: HTML5, **Tailwind CSS** (via CDN), JavaScript (ES6+), Google Fonts (Poppins).
- **Backend**: Python, **Flask**.
- **Machine Learning**: Scikit-Learn, Pandas, NumPy.
- **APIs**: Open-Meteo (Geocoding & Weather).
- **Deployment**: Vercel-ready configuration.

## 📸 Screenshots
![Crop-Prediction-Model]

## 📥 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Murugavl/Crop-Prediction.git
   cd Crop-Prediction
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Mac/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Ensure `scikit-learn` version matches the one used to train the model.*

4. **Configuration**
   The project uses a `.env` file for API configuration. A default one is created automatically (Open-Meteo requires no API key for basic usage):
   ```env
   GEOCODING_API_URL=https://geocoding-api.open-meteo.com/v1/search
   WEATHER_API_URL=https://api.open-meteo.com/v1/forecast
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   access the app at `http://localhost:5000`.

## 🐳 Docker Deployment

1. **Build the Image**
   ```bash
   docker build -t crop-prediction-app .
   ```

2. **Run the Container**
   ```bash
   docker run -p 5000:5000 crop-prediction-app
   ```
   Open `http://localhost:5000` in your browser.

## 🤝 Contributing
Contributions are welcome!
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
