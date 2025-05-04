# 🛠 Low-Level Design (LLD) – Crypto Liquidity Ratio Prediction

This document outlines the detailed step-by-step logic and processing used in the project.

---

## 1. 📥 Data Collection

- Two datasets collected: `coin_gecko_2022-03-16.csv` and `coin_gecko_2022-03-17.csv`
- Combined using `pandas.concat()` to form a single dataset

---

## 2. 🧼 Data Preprocessing

- Converted `date` column to datetime format
- Identified and filled missing values in columns like:
  - `1h`, `24h`, `7d` → filled using `.mean()` or `.bfill()`
- Checked data types and converted non-numeric columns where needed
- Removed or handled duplicate entries if any

---

## 3. 🧠 Feature Engineering

Created the following new features:
| Feature Name               | Description                                             |
|---------------------------|---------------------------------------------------------|
| `price_change`            | Difference between current and previous price           |
| `volume_change`           | Difference in 24h trading volume                        |
| `rolling_avg_price_7d`    | 7-day moving average of price                           |
| `rolling_avg_volume_7d`   | 7-day moving average of volume                          |
| `rolling_std_price_7d`    | 7-day rolling standard deviation of price (volatility)  |
| `rolling_liquidity_ratio` | 24h volume / abs(price_change)                          |
| `price_volatility_index`  | price_change * volume_change                            |
| `log_price`, `log_volume` | Log-transformed price and volume                        |
| `relative_volume`         | 24h volume / 7-day avg volume                           |
| `price_momentum`          | price_change / volatility                               |

---

## 4. ⚠️ Outlier Treatment

- Applied **outlier capping** using 1st and 99th percentile:
```python
df[col] = np.clip(df[col], lower_bound, upper_bound)
```
- This preserved overall data while minimizing noise

---

## 5. 📊 Feature Selection

- Used `RandomForestRegressor.feature_importances_` to rank features
- Top features:
  - `relative_volume`
  - `log_volume`
  - `log_price`

---

## 6. ⚖️ Feature Scaling

- Applied `StandardScaler` on selected numeric columns
- Target variable `rolling_liquidity_ratio` was **not scaled**
- Only `X_train` and `X_test` were scaled

---

## 7. 🧠 Model Building

Tested 7 regression models:
- Linear Regression
- Ridge & Lasso Regression
- Random Forest
- Gradient Boosting
- XGBoost ✅ (Best)
- AdaBoost

Saved the best model using:
```python
joblib.dump(best_model, "xgboost_model.pkl")
```

---

## 8. 🧪 Model Evaluation

Metrics used:
- MAE: Mean Absolute Error
- RMSE: Root Mean Squared Error
- R² Score

| Metric | Best Model (XGBoost) |
|--------|----------------------|
| MAE    | ~25.7M               |
| RMSE   | ~77.9M               |
| R²     | ~0.876               |

---

## 9. 🧪 Hyperparameter Tuning (GridSearchCV)

- Tuned `XGBoostRegressor` with grid search
- Final best parameters used for improved accuracy
- Observed slight performance improvement (~0.83 R²)

---

## 10. 💻 Deployment

- Built an interactive **Streamlit UI**
- Inputs:
  - Price, volume, market cap, volatility, etc.
- Model loads `.pkl` file and outputs predicted liquidity
- Local deployment tested with:
```bash
streamlit run app.py
```

---

## ✅ Final Output

- Fully working ML pipeline
- Clean UI for user prediction
- Ready-to-use `.pkl` model and documentation
```