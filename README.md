# 🚕 TripFare: Predicting Urban Taxi Fare with Machine Learning

A machine learning project that predicts NYC taxi fare based on trip details using regression models and a Streamlit web application.

---

## 📌 Project Overview

This project focuses on analyzing historical taxi trip records to build a predictive model that accurately estimates the total taxi fare amount. It demonstrates the complete ML workflow from data preprocessing, feature engineering, model training, evaluation, to deployment using Streamlit.

---

## 🔍 Problem Statement

As a data analyst at an urban mobility firm, you aim to enhance fare estimation and promote pricing transparency for passengers. Your goal is to:
- Clean and explore real-world NYC taxi trip data
- Engineer meaningful features (like distance, time of day)
- Train regression models to predict the final fare
- Deploy a user-friendly Streamlit app for real-time fare prediction

---

## 💡 Real-World Applications

- Ride-hailing fare estimation  
- Tourist fare budgeting  
- Driver incentive planning  
- Urban mobility analytics  

---

## 🧠 Skills & Techniques Used

- Exploratory Data Analysis (EDA)
- Feature Engineering (Haversine distance, time-based flags)
- Regression Models: Linear, Ridge, Lasso, Random Forest, Gradient Boosting
- Hyperparameter Tuning (GridSearchCV)
- Model Evaluation (R², MAE, RMSE)
- Streamlit Web App for real-time predictions

---

## 🗂️ Project Structure

TripFare_Project/
├── app/
│ ├── app.py # Streamlit UI
│ └── model.pkl # Trained regression model
├── data/
│ └── raw_taxi_data.csv # NYC taxi dataset
├── Trip Fare Eda Modeling.ipynb # Full ML workflow notebook
├── README.md
└── requirements.txt # Project dependencies
