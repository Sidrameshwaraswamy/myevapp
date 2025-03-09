import pandas as pd
import numpy as np
import random

# Function to generate synthetic dataset
def generate_ev_charging_data(num_samples):
    # Random seed for reproducibility
    np.random.seed(42)
    
    # List of weather conditions for simulation
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Snowy"]
    
    # Random location IDs (you can scale this up with actual GPS data or locations)
    locations = [1, 2, 3, 4, 5]  # Assuming 5 different stations
    
    # Initialize empty lists to hold the data
    time_of_day = []
    day_of_week = []
    temperature = []
    weather_condition = []
    location = []
    electricity_rate = []
    number_of_cars = []
    demand = []  # Target variable
    
    # Generate synthetic data
    for _ in range(num_samples):
        time_of_day.append(random.randint(0, 23))  # Time of day (0-23)
        day_of_week.append(random.randint(0, 6))  # Day of the week (0-6, Monday-Sunday)
        temperature.append(np.round(np.random.uniform(10, 40), 1))  # Temperature between 10°C and 40°C
        weather_condition.append(random.choice(weather_conditions))  # Random weather condition
        location.append(random.choice(locations))  # Random location ID
        electricity_rate.append(np.round(np.random.uniform(0.1, 0.5), 2))  # Random electricity rate between 0.1 and 0.5
        number_of_cars.append(random.randint(1, 50))  # Number of cars charging (1-50)

        # Simple rule-based demand generation for the sake of this example
        # Higher demand with more cars, time of day, and weather effects
        demand_value = (number_of_cars[-1] * 1.5) + (time_of_day[-1] * 0.2) + (temperature[-1] * 0.5)
        if weather_condition[-1] == "Rainy":
            demand_value *= 1.2  # Rainy weather increases demand
        elif weather_condition[-1] == "Snowy":
            demand_value *= 0.8  # Snowy weather decreases demand
        demand_value += np.random.normal(0, 10)  # Add some noise to the demand
        demand.append(np.round(demand_value))

    # Create a DataFrame from the generated data
    df = pd.DataFrame({
        'time_of_day': time_of_day,
        'day_of_week': day_of_week,
        'temperature': temperature,
        'weather_condition': weather_condition,
        'location': location,
        'electricity_rate': electricity_rate,
        'number_of_cars': number_of_cars,
        'demand': demand  # This is the target variable
    })
    
    return df

# Generate a synthetic dataset with 1000 samples
num_samples = 1000
ev_charging_data = generate_ev_charging_data(num_samples)

# Save the dataset to a CSV file
ev_charging_data.to_csv("ev_charging_data.csv", index=False)

# Display the first few rows of the generated dataset
print(ev_charging_data.head())
