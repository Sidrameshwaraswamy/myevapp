import pickle
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

# Load the trained model from the .pkl file
with open('ev_charging_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Simulating a simple user store (in production, use a real database)
users = {"user1": "password123", "user2": "mypassword"}

# Secret key for session management (secure this in production)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_secret_key')

@app.route('/')
def home():
    # If the user is logged in, render the home page with their username
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username not in users:
            users[username] = password
            flash(f"Account created for {username}. You can now log in.", 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose another one.', 'danger')
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
def predict():
    # Ensure user is logged in before making a prediction
    if 'username' not in session:
        return redirect(url_for('login'))

    try:
        # Get features from the form (e.g., user input)
        features = [
            int(request.form['time_of_day']),
            int(request.form['day_of_week']),
            float(request.form['temperature']),
            request.form['weather_condition'],
            int(request.form['location']),
            float(request.form['electricity_rate']),
            int(request.form['number_of_cars']),
        ]

        # Convert weather_condition to numeric using label encoding
        label_encoder = {"Sunny": 0, "Cloudy": 1, "Rainy": 2, "Snowy": 3}
        features[3] = label_encoder[features[3]]

        # Convert features to a numpy array for the model
        import numpy as np
        features = np.array(features).reshape(1, -1)

        # Make the prediction using the loaded model
        demand_prediction = model.predict(features)

        # Display the prediction result on the home page
        return render_template('index.html', prediction=demand_prediction[0])

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
