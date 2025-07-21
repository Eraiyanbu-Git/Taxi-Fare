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

# 🛒 Shopper Spectrum  
**Customer Segmentation and Product Recommendations in E-Commerce**

---

## 🔎 Key Components

### 1️⃣ RFM Customer Segmentation (Unsupervised Learning)

- **Recency**: Days since last purchase  
- **Frequency**: Number of purchases  
- **Monetary**: Total amount spent  

**Algorithm Used**: KMeans clustering  
**Optimal K Selection**: Elbow Method & Silhouette Score  

**Segment Labels:**

| Segment     | Description                                |
|-------------|--------------------------------------------|
| High-Value  | Frequent, recent, and high-spending        |
| Regular     | Moderate in all RFM dimensions             |
| Occasional  | Low frequency and spend                    |
| At-Risk     | Long inactive, low spend and frequency     |

---

### 2️⃣ Product Recommendation System (Collaborative Filtering)

- Customer × Product pivot table
- Cosine Similarity between products
- Recommends **Top 5** similar items based on input product

---

## 🎯 Streamlit Web App Features

### 🔍 1. Customer Segmentation  
**Input:**
- Recency  
- Frequency  
- Monetary  

**Output:**  
- Predicted customer segment (e.g. High-Value)

---

### 🛍️ 2. Product Recommendation  
**Input:**  
- Product name  

**Output:**  
- Top 5 similar product recommendations

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/shopper-spectrum.git
   cd shopper-spectrum

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
3. Launch Streamlit app
    ```bash
    cd app
    streamlit run app.py

🧩 Real-World Applications
🎯 Targeted Marketing Campaigns

🛍 Personalized Product Recommendations

💡 Customer Retention Strategy

📦 Smart Inventory Planning

**✨ Author** :
Eraiyanbu Arulmurugan




