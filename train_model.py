import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('ev_charging_data.csv')

# Preprocess the data
label_encoder = LabelEncoder()
df['weather_condition'] = label_encoder.fit_transform(df['weather_condition'])

# Split the data into features and target
X = df.drop(columns=['demand'])
y = df['demand']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a .pkl file
with open('ev_charging_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as ev_charging_model.pkl")
