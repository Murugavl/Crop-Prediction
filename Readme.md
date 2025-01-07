# Crop Prediction Using Deep Learning

## Project Overview
This project aims to develop a machine learning model that predicts the most suitable crops for cultivation based on various environmental and soil factors. By integrating historical data, geolocation, and weather information, the model provides accurate predictions to help farmers make informed decisions.

## Features
- Utilizes Deep Neural Networks (DNN) for crop prediction.
- Considers soil contents (Nitrogen, Phosphorus, Potassium, pH), temperature, humidity, and rainfall as input features.
- Leverages weather and geolocation APIs for real-time data.
- Includes a user-friendly web interface for data input and prediction display.

## Dataset
- The dataset contains 2,200 samples across 22 different crops.
- Each crop has 100 samples.
- Features include soil contents (N, P, K, pH), temperature, humidity, and rainfall.

## Model Architecture
- Three hidden layers with 64, 128, and 64 neurons, respectively.
- SeLU activation function for input and hidden layers.
- Softmax activation function for the output layer.
- Categorical cross-entropy loss function.
- ADAM optimizer.
- 100 epochs with an 80:20 train-test split ratio.

## Results
- Achieved approximately 99% accuracy on both training and test datasets.

## User Input
- Soil contents: Nitrogen (N), Phosphorus (P), Potassium (K), and pH levels.
- Geolocation: State and District.
- Month (Season) of cultivation.
- Temperature and humidity values retrieved through weather APIs.

## Web Interface
- Interactive interface for users to input data.
- Real-time predictions based on the input data.

## Installation and Usage
1. Clone the repository:
   ```
   git clone https://github.com/Murugavl/Crop-Prediction.git
   ```
2. Navigate to the project directory:
   ```
   cd Crop-Prediction
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```
   python app.py
   ```
5. Access the web interface at `http://localhost:5000`.

## File Structure
- `dataset/`: Contains datasets used for training and validation.
- `model/`: Includes the model architecture and saved model weights.
- `app.py`: Main script for running the application.
- `index.html`: File related to the web interface.
- `requirements.txt`: Lists the dependencies required to run the project.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



