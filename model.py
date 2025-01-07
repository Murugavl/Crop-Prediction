# Import necessary libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data = pd.read_csv('Crop_recommendation.csv')  # Replace 'crop_data.csv' with your dataset file

# view the dataset
data.head()

# shape the dataset
data.shape

# check for null values
data.isnull().sum()

# Split the data into features and labels
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Labels


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

# check the accuracy of the model
accuracy = model.score(X_test, y_test)


# save as the pickle file

with open('crop_prediction.pkl','wb') as file:
    pickle.dump(model, file)

