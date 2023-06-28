# ---------------------------------------------------------------------------------
# Artificial Neural Networks
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Import libraries
# ---------------------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Load the data
# ---------------------------------------------------------------------------------
data = pd.read_csv('air_pollution_data.csv')  # Assuming your data is in a CSV file
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Split the data into input features (X) and target variable (y)
# ---------------------------------------------------------------------------------
X = data[['day', 'month', 'year', 'air_temperature', 'wind_speed', 'wind_direction']]
y = data['pollutant_concentration']
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Split the data into training and testing sets
# ---------------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Define the model architecture
# ---------------------------------------------------------------------------------
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Compile the model
# ---------------------------------------------------------------------------------
model.compile(loss='mean_squared_error', optimizer='adam')
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Train the model
# ---------------------------------------------------------------------------------
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Make predictions on the test set
# ---------------------------------------------------------------------------------
y_pred = model.predict(X_test)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Evaluate the model
# ---------------------------------------------------------------------------------
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# ---------------------------------------------------------------------------------