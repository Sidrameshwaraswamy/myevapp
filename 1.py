import pandas as pd
data = pd.read_csv("ev_charging_data.csv")

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data[['time_of_day', 'temperature', 'electricity_rate']] = scaler.fit_transform(
    data[['time_of_day', 'temperature', 'electricity_rate']])

data['weather_condition'] = data['weather_condition'].map({'Sunny': 0, 'Cloudy': 1, 'Rainy': 2, 'Snowy': 3})

X = data.drop('demand', axis=1)  # Drop the target column (demand)
y = data['demand']  # Target: EV station demand

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

nn_model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)  # Output layer for regression
])

nn_model.compile(optimizer='adam', loss='mean_squared_error')
nn_model.fit(X_train, y_train, epochs=50, batch_size=32)

from sklearn.metrics import mean_absolute_error

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

loss = nn_model.evaluate(X_test, y_test)
print(f"Loss: {loss}")


nn_model.save('ev_charging_model.h5')
