# 📑 Final Report – Crypto Liquidity Ratio Prediction

This final report summarizes the complete workflow, performance results, and insights from the cryptocurrency liquidity prediction project.

---

## 🎯 Problem Statement

To build a Machine Learning model that accurately predicts the **Rolling Liquidity Ratio** of a cryptocurrency using historical price, volume, and volatility data.

---

## 🧱 Project Pipeline

| Step                  | Description                                             |
|-----------------------|---------------------------------------------------------|
| Data Collection       | Combined 2 raw CSVs with market data                   |
| Preprocessing         | Filled missing values, fixed types, cleaned columns    |
| Feature Engineering   | Created domain-specific features (rolling, ratio, etc) |
| Outlier Treatment     | Used capping (1st and 99th percentile)                 |
| Feature Scaling       | Applied `StandardScaler` to numeric inputs             |
| Model Training        | Trained 7 regression models                            |
| Model Evaluation      | Compared with MAE, RMSE, R² Score                      |
| Hyperparameter Tuning | Tuned XGBoost with GridSearchCV                        |
| Deployment            | Built an interactive Streamlit app                     |

---

## 📊 Model Comparison Results

| Model               | MAE (↓)     | RMSE (↓)    | R² Score (↑) |
|--------------------|-------------|-------------|--------------|
| Linear Regression  | 94.9M       | 218.7M      | 0.0276       |
| Ridge Regression   | 95.4M       | 218.7M      | 0.0279       |
| Lasso Regression   | 95.1M       | 218.7M      | 0.0278       |
| Random Forest      | 35.7M       | 114.4M      | 0.7341       |
| Gradient Boosting  | 34.2M       | 89.6M       | 0.8368       |
| AdaBoost           | 145.2M      | 168.7M      | 0.4217       |
| **XGBoost ✅**       | **25.7M**   | **77.9M**   | **0.8765**   |

---

## 🔧 Hyperparameter Tuning

- Used `GridSearchCV` on XGBoost
- Best parameters:
```python
{
  'learning_rate': 0.05,
  'n_estimators': 300,
  'max_depth': 3,
  'subsample': 0.8,
  'colsample_bytree': 0.8
}
```

- Slight improvement seen: `R² ~ 0.83`

---

## 📦 Deployment

- Final XGBoost model saved as `xgboost_model.pkl`
- User interface built using `Streamlit`
- Local testing done via:
streamlit run app.py

---

## 💡 Key Learnings

- Scaling and outlier handling are crucial for model stability
- Feature engineering (rolling, log, relative metrics) had major impact
- Grid search tuning did not drastically improve performance over base XGBoost
- Removing outliers entirely worsened performance — capping was better
- Streamlit made deployment fast and user-friendly

---

## 🏁 Final Conclusion

The model successfully predicts liquidity ratio with a high R² score of **0.87**, proving that market-driven engineered features can effectively model liquidity behavior. The full ML pipeline is now ready for further expansion or integration with live market data.
