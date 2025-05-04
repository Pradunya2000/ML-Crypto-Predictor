import streamlit as st
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load("xgboost_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💹 Crypto Liquidity Predictor")

st.write("Enter values or click 'Use Sample Data'")

# Create empty placeholders
if 'use_sample' not in st.session_state:
    st.session_state.use_sample = False

# Button to autofill
if st.button("Use Sample Data"):
    st.session_state.use_sample = True

# Inputs
if st.session_state.use_sample:
    price = st.number_input("Price", value=40000.0)
    volume_24h = st.number_input("24h Volume", value=1e9)
    market_cap = st.number_input("Market Cap", value=1e12)
    price_change = st.number_input("Price Change", value=200.0)
    volume_change = st.number_input("Volume Change", value=2e8)
    rolling_avg_price_7d = st.number_input("7-Day Avg Price", value=39000.0)
    rolling_avg_volume_7d = st.number_input("7-Day Avg Volume", value=8e8)
    rolling_std_price_7d = st.number_input("7-Day Price Std Dev", value=1000.0)
    price_volatility_index = st.number_input("Price Volatility Index", value=5e9)
else:
    price = st.number_input("Price")
    volume_24h = st.number_input("24h Volume")
    market_cap = st.number_input("Market Cap")
    price_change = st.number_input("Price Change")
    volume_change = st.number_input("Volume Change")
    rolling_avg_price_7d = st.number_input("7-Day Avg Price")
    rolling_avg_volume_7d = st.number_input("7-Day Avg Volume")
    rolling_std_price_7d = st.number_input("7-Day Price Std Dev")
    price_volatility_index = st.number_input("Price Volatility Index")

# Prediction
if st.button("Predict"):
    input_data = np.array([[price, volume_24h, market_cap, price_change, volume_change,
                            rolling_avg_price_7d, rolling_avg_volume_7d,
                            rolling_std_price_7d, price_volatility_index]])

    prediction = model.predict(input_data)[0]
    st.success(f"📈 Predicted Rolling Liquidity Ratio: {prediction:.4f}")
