# app/app.py

import streamlit as st
import numpy as np
import pickle
from datetime import datetime
from haversine import haversine

# Load the trained model
with open('app/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Distance calculation
def calculate_distance(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon):
    return haversine((pickup_lat, pickup_lon), (dropoff_lat, dropoff_lon))

# Feature engineering function
def preprocess_input(pickup_datetime, passenger_count, pickup_lat, pickup_lon, dropoff_lat, dropoff_lon):
    pickup_hour = pickup_datetime.hour
    pickup_day = pickup_datetime.weekday()
    is_weekend = 1 if pickup_day >= 5 else 0
    is_night = 1 if pickup_hour < 6 or pickup_hour >= 22 else 0
    distance_km = calculate_distance(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)

    return np.array([[distance_km, pickup_hour, pickup_day, passenger_count, is_weekend, is_night]])

# Streamlit UI
st.set_page_config(page_title="TripFare Predictor", page_icon="🚕")

st.title("🚕 TripFare Predictor")
st.markdown("Predict your taxi fare based on trip details.")

# Input fields
pickup_date = st.date_input("Pickup Date", datetime.now().date())
pickup_time = st.time_input("Pickup Time", datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time)

pickup_lat = st.number_input("Pickup Latitude", value=40.761432, format="%.6f")
pickup_lon = st.number_input("Pickup Longitude", value=-73.979815, format="%.6f")
dropoff_lat = st.number_input("Dropoff Latitude", value=40.641311, format="%.6f")
dropoff_lon = st.number_input("Dropoff Longitude", value=-73.780333, format="%.6f")
passenger_count = st.slider("Passenger Count", 1, 6, value=1)


# Predict button
if st.button("Predict Fare"):
    features = preprocess_input(pickup_datetime, passenger_count, pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)
    fare = model.predict(features)[0]
    st.success(f"Estimated Fare: ${fare:.2f}")

    #cd /Users/eraiyanbu/Desktop/Projects
''' Want to Level It Up?
Here are a few optional next steps you can explore:

1. Add a map (using st.map() or folium)

Let users see pickup/dropoff points.

2. Show feature importance

Use .feature_importances_ from your model to show which features impact fare the most.

3. Deploy to Streamlit Cloud

So others can try your app online. Just push to GitHub and connect it to Streamlit Community Cloud.

4. Add a sidebar for input

Make the UI cleaner by moving inputs to a sidebar using st.sidebar.'''