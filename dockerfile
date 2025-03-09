# Use official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the model and other necessary files to the container
COPY ev_charging_model.pkl /app/ev_charging_model.pkl
# Or for Keras model:
# COPY ev_charging_model.h5 /app/ev_charging_model.h5

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask app (or API code)
COPY app.py /app/app.py

# Expose port for the Flask app
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
