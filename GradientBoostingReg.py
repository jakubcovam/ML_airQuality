# ---------------------------------------------------------------------------------
# Gradient Boosting Regression
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Import libraries
# ---------------------------------------------------------------------------------
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Load the data
# ---------------------------------------------------------------------------------
data = pd.read_csv('air_pollution_data.csv')
# ---------------------------------------------------------------------------------

# def gradient_boost_reg():

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
# Initialize the Gradient Boosting Regression model
# ---------------------------------------------------------------------------------
gb_model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Train the model
# ---------------------------------------------------------------------------------
gb_model.fit(X_train, y_train)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Make predictions on the test set
# ---------------------------------------------------------------------------------
y_pred = gb_model.predict(X_test)
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Evaluate the model
# ---------------------------------------------------------------------------------
crit_mse = mean_squared_error(y_test, y_pred)
crit_r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", crit_mse)
print("R2:", crit_r2)

# ---------------------------------------------------------------------------------
