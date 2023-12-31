# ---------------------------------------------------------------------------------
# Random Forest Regression
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Import libraries
# ---------------------------------------------------------------------------------
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Create and train the Random Forest Regression model
# ---------------------------------------------------------------------------------
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Make predictions on the test set
# ---------------------------------------------------------------------------------
y_pred = rf_model.predict(X_test)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Evaluate the model
# ---------------------------------------------------------------------------------
crit_mse = mean_squared_error(y_test, y_pred)
crit_r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", crit_mse)
print("R2:", crit_r2)
# ---------------------------------------------------------------------------------
