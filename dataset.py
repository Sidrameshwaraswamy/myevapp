import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
n_samples = 1000

data = {
    'time_of_day': np.random.randint(0, 24, size=n_samples),  # Random hour of the day
    'day_of_week': np.random.randint(0, 7, size=n_samples),  # Random day of the week
    'temperature': np.random.uniform(5, 35, size=n_samples),  # Random temperature between 5°C and 35°C
    'weather_condition': np.random.choice(['Sunny', 'Cloudy', 'Rainy', 'Snowy'], size=n_samples),  # Random weather
    'location': np.random.randint(1, 10, size=n_samples),  # Random location ID
    'electricity_rate': np.random.uniform(0.1, 0.3, size=n_samples),  # Electricity rate between 0.1 and 0.3 currency units
    'number_of_cars': np.random.randint(50, 500, size=n_samples),  # Number of EVs in the area
    'demand': np.random.uniform(1, 100, size=n_samples)  # Demand is the target variable
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV for use in training
df.to_csv('ev_charging_data.csv', index=False)

print(df.head())
