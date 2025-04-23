# Introduction to Machine Learning with `scikit-learn`

This guide introduces basic machine learning concepts using scikit-learn, 
focusing on a simple **wind power time-series forecasting** example. We'll cover 
feature engineering, model training, error metrics, and time-series-specific 
workflows.

---

## Key Concepts & Workflow

### 1. **Feature Engineering for Time Series**
Transform raw time-series data into features that capture temporal patterns. 
For hourly wind power prediction:
- **Lagged Features**: Use values from previous time steps (e.g., wind speed 
nd power from the last hour).
- **Rolling Statistics**: Compute moving averages or standard deviations over 
a window (e.g., 3-hour average wind speed).
- **Time-Based Features**: Extract hour-of-day, day-of-week, or seasonality 
indicators.
- **Cyclical Feature Encoding**: Cyclical features like hour-of-day, wind 
direction need to be encoded specially, like using trigonometric functions,
specifically, `sine` and `cosine`. Read here for more explanations: https://blog.dailydoseofds.com/p/cyclical-feature-engineering 


**Example Code**:
```python
import numpy as np
import pandas as pd

# Synthetic hourly wind and power data (time-series)
hours = 100
data = {
    'timestamp': pd.date_range(start='2023-01-01', periods=hours, freq='H'),
    'wind_speed': np.random.uniform(0, 15, hours),
    'power': np.random.uniform(0, 200, hours)
}
df = pd.DataFrame(data).set_index('timestamp')

# Create lagged features (1-hour lag)
df['wind_speed_lag1'] = df['wind_speed'].shift(1)
df['power_lag1'] = df['power'].shift(1)

# 3-hour rolling average
df['wind_speed_rolling3'] = df['wind_speed'].rolling(3).mean()

# Drop missing values from lag/rolling features
df = df.dropna()
```

---

### 2. **Time-Series Train-Test Split**
Time-series data requires splitting in chronological order to avoid data 
leakage.  **Never shuffle time-series data** — future data should not influence 
past predictions.

```python
# Split into sequential training (80%) and testing (20%)
split_idx = int(0.8 * len(df))
X = df[['wind_speed_lag1', 'power_lag1', 'wind_speed_rolling3']]  # Features
y = df['power']                                                   # Target

X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]
```

---

### 3. **Linear Regression Model**
Linear regression models the relationship between features and target using a 
linear equation:  

**Model Equation**:  
$$
\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_n x_n + \epsilon
$$  
- $\hat{y}$: Predicted power  
- $\beta_0$: Intercept (bias term)  
- $\beta_1, \beta_2, \dots, \beta_n$: Coefficients for features $x_1, x_2, \dots, x_n$  
- $\epsilon$: Error term  

**Objective**: Minimize the **sum of squared residuals** (SSR):  

$$
\text{SSR} = \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$

**Training Code**:
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# Print coefficients (β values)
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
```

---

### 4. **Cross-Validation for Time Series**
Cross-validation (CV) is a technique to evaluate how well a model generalizes 
to unseen data. For time-series problems, standard k-fold CV is 
**inappropriate** because shuffling data breaks temporal order, leading to data 
leakage (future data influencing past predictions). Instead, use 
**time-series-aware splitting**:

#### **What is Cross-Validation?**
- **Goal**: Estimate model performance on unseen data by splitting the dataset 
into multiple "folds."
- **Standard k-fold CV**: Randomly splits data into `k` folds, trains on `k-1` 
folds, and tests on the remaining fold. Repeats `k` times.
- **Problem with Time Series**: Random splitting allows the model to "see" 
future data during training, creating unrealistic performance estimates.

#### **Time-Series Cross-Validation (TSCV)**
Preserves temporal order by splitting data sequentially. Common methods include:
* **TimeSeriesSplit** (scikit-learn):
   - Divides data into `n_splits + 1` chronological segments.
   - Training set grows over time, while the test set moves forward.
   - Example with `n_splits=3`:
     ```
     Train: [0..50] → Test: [51..70]
     Train: [0..70] → Test: [71..90]
     Train: [0..90] → Test: [91..110]
     ```
* **Walk-Forward Validation**:
   - Trains on all past data up to time `t`, tests on `t+1`.
   - Mimics real-world deployment (e.g., daily retraining).

**Code Example**:
```python
from sklearn.model_selection import TimeSeriesSplit, cross_val_score

tscv = TimeSeriesSplit(n_splits=3)
scores = cross_val_score(
    model, 
    X, 
    y, 
    cv=tscv,                   # Use time-series splitter
    scoring='neg_mean_squared_error'
)
print(f"Cross-validated MSE: {-scores.mean():.2f}")
```

#### **Why Use Time-Series CV?**
- **Avoids Data Leakage**: Ensures test data always comes **after** training 
data.
- **Robust Performance Estimates**: Reflects real-world scenarios where models 
predict future values.
- **Hyperparameter Tuning**: Safely optimize parameters without overfitting to 
temporal patterns.

**Key Notes**:
- Use larger `n_splits` for small datasets (but ensure test folds have enough 
data).
- Early training folds may be too small for complex models (e.g., deep 
learning).
- For long-term forecasting, use `gap` parameter to separate training and test 
periods.

---

### 5. **Error Metrics and Equations**
Evaluate regression performance using:  

#### **Mean Squared Error (MSE)**  
$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2
$$  
- Penalizes large errors quadratically.  

#### **Mean Absolute Error (MAE)**  
$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
$$  
- Represents average absolute error (robust to outliers).  

#### **Root Mean Squared Error (RMSE)**  
$$
\text{RMSE} = \sqrt{\text{MSE}}
$$  
- Interpretable in target variable units (e.g., kW for power).  

**Calculation Code**:
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"MSE: {mse:.2f}, MAE: {mae:.2f}, RMSE: {rmse:.2f}")
```

---

## Complete Wind Power Forecasting Example

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Generate synthetic time-series data
np.random.seed(42)
hours = 200
timestamps = pd.date_range(start='2023-01-01', periods=hours, freq='H')
wind_speed = np.random.uniform(0, 15, hours)
power = 10 * wind_speed + np.random.normal(0, 15, hours)  # Linear relationship + noise

# Create DataFrame with lagged features
df = pd.DataFrame({'timestamp': timestamps, 'wind_speed': wind_speed, 'power': power})
df.set_index('timestamp', inplace=True)
df['wind_speed_lag1'] = df['wind_speed'].shift(1)
df['power_lag1'] = df['power'].shift(1)
df = df.dropna()

# Split into sequential training (80%) and testing (20%)
split_idx = int(0.8 * len(df))
X_train, X_test = df[['wind_speed_lag1', 'power_lag1']].iloc[:split_idx], df[['wind_speed_lag1', 'power_lag1']].iloc[split_idx:]
y_train, y_test = df['power'].iloc[:split_idx], df['power'].iloc[split_idx:]

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
# Note that this is randomly generated data, and linear regression performs badly
y_pred = model.predict(X_test)
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} kW")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f} kW")

# Coefficients for interpretation
print(f"Model equation: power = {model.intercept_:.2f} + {model.coef_[0]:.2f} * wind_speed_lag1 + {model.coef_[1]:.2f} * power_lag1")
```

---

## Key Takeaways
1. **Time-Series Splitting**: Always split data chronologically to avoid 
leakage.
2. **Linear Regression**: Models linear relationships with interpretable 
coefficients.
3. **Error Metrics**:
   - **MSE** for emphasizing large errors.
   - **MAE** for robustness to outliers.
   - **RMSE** for interpretability in target units.
4. **Feature Engineering**: Lagged and rolling features are critical for 
time-series forecasting.

For improved accuracy:
- Add weather forecast data (e.g., predicted wind speed).
- Consider other availale data (e.g., wind direction, wind shear)
- Experiment with models like **ARIMA**, **Prophet**, or **LSTM** (for complex 
temporal patterns).
- Use **feature scaling** for non-linear models (e.g., SVM, neural networks).
- Experiement with different feature selections/engineering, different ML models, and parameter tuning.


This note provides a foundation for time-series regression tasks. Adjust 
feature engineering and model selection based on data complexity!