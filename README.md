# 💹 Crypto Liquidity Ratio Prediction using Machine Learning

This project predicts the **Rolling Liquidity Ratio** of cryptocurrencies using market data and ML models. The deployed app takes crypto market input and provides a liquidity prediction using a trained XGBoost model.

---

## 🚀 Features
- Full data pipeline from collection to deployment
- EDA with outlier capping and feature engineering
- Model comparison with metrics (MAE, RMSE, R²)
- Streamlit app with prediction UI
- Local and cloud deployable

---

## 📁 Project Structure

```plaintext
ML-Crypto-Predictor/
├── app.py                    # Streamlit app
├── scaler.pkl                # Saved StandardScaler
├── xgboost_model.pkl         # Trained model
├── EDA_Report.md             # Exploratory Data Analysis
├── HLD.md                    # High-Level Design
├── LLD.md                    # Low-Level Design
├── Final_Report.md           # Final insights & summary
├── requirements.txt          # Environment dependencies
└── README.md                 # GitHub summary
```




## 🧪 How to Run Locally
git clone https://github.com/Pradunya2000/ML-Crypto-Predictor.git
- cd ML-Crypto-Predictor
- pip install -r requirements.txt
- streamlit run app.py



## 📊 Final Model Results

| Metric | Value |
|--------|-------|
| MAE    | 25.7M |
| RMSE   | 77.9M |
| R²     | 0.876 |



## 🧠 Tech Stack

- Python
- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Seaborn
- Streamlit (for UI)


## ✅ requirements.txt

- Streamlit
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Matplotlib
- Seaborn
