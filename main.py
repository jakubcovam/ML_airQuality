# ---------------------------------------------------------------------------------
# Main file
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Import libraries
# ---------------------------------------------------------------------------------
import pandas as pd
import GradientBoostingReg
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Load the data
# ---------------------------------------------------------------------------------
data = pd.read_csv('air_pollution_data.csv', sep=' ', header=None)
# ---------------------------------------------------------------------------------

print(data.loc[1])

# TODO: Change input CSV file (names of rows as day_of_week, hour, etc.)
# TODO: Create functions (def) at each ML
# TODO: Import functions from each ML into main.py
# TODO: Run accuracy criteria calculations from main.py
# TODO: Insert other ML models (Naive Bias, etc.)
# TODO:
