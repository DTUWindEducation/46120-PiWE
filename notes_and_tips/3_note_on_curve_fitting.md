# Introduction to Curve Fitting with `SciPy`

Curve fitting is the process of finding a mathematical model that best
describes a dataset. Unlike interpolation (which passes through all data 
points), curve fitting optimizes model parameters to minimize the difference
between the model and noisy or incomplete data. SciPy's `curve_fit` function is 
a powerful tool for this task.

Curve fitting is widely used in scientific computing. For example, based on a
time series of wind speed over one/multiple year(s), you can fit a Weibull 
distribution, which is widely used in AEP calculation.

---

## 1. **Key Concepts**
- **Goal**: Find parameters of a function $f(x, \theta)$ that minimize the
 residual sum of squares (RSS) between the model and data.
- **Model Equation**: $y = f(x, \theta) + \epsilon$, where $\theta$ are parameters and $\epsilon$ is noise.
- **Applications**: Physics, engineering, finance (e.g., exponential decay, sinusoidal trends).

**Note**: If you have read the note on machine learning, you will discover the
linear regression model used there is just a specific form of curve fitting, 
assuming the function to be a linear function of the considered features. In
a sense, many machine learning model can be viewed as a kind of **curve 
fitting**, maybe using a complex function that has many parameters (like 
multi-layer of neural networks with many weighting parameters) to be 
learned/tuned to minimize the prediction error.

---

## 2. **Workflow with `scipy.optimize.curve_fit`**
### Step 1: Define the Model Function
Define a Python function representing the mathematical model. Parameters are
also passed as arguments.

```python
import numpy as np
from scipy.optimize import curve_fit

# Example: Exponential decay model
def model_func(x, a, b, c):
    """Model: y = a * exp(-b * x) + c"""
    return a * np.exp(-b * x) + c
```

### Step 2: Generate or Load Data
Use synthetic or real data. Example using synthetic data with noise added:

```python
x_data = np.linspace(0, 4, 50)

# Note that in the following true model, the true values of a, b, c are:
# 2.5, 1.3 and 0.5
y_data = 2.5 * np.exp(-1.3 * x_data) + 0.5  # True model

y_noisy = y_data + 0.2 * np.random.normal(size=x_data.size)  # Add noise
```

### Step 3: Fit the Model
Use `curve_fit` to find optimal parameters:
```python
params_opt, params_cov = curve_fit(
    f=model_func,
    xdata=x_data,
    ydata=y_noisy,
    p0=[1, 1, 1]  # Initial guess for [a, b, c]
)

a_opt, b_opt, c_opt = params_opt # fitted value for the parameters

print(f"Optimal parameters: a={a_opt:.2f}, b={b_opt:.2f}, c={c_opt:.2f}")
```

You can compare the fitted values and the true values for the parameters

### Step 4: Evaluate Fit Quality
Calculate residuals and error metrics:

```python
y_pred = model_func(x_data, *params_opt)

# Residuals
residuals = y_noisy - y_pred

# Error metrics
mse = np.mean(residuals**2) 
rmse = np.sqrt(mse)
print(f"MSE: {mse:.4f}, RMSE: {rmse:.4f}")
```

---

## 3. **Advanced Features**
### Parameter Uncertainty
The covariance matrix `params_cov` provides uncertainty estimates:

```python
# Standard deviation of parameters
params_std = np.sqrt(np.diag(params_cov))
print(f"Parameter uncertainties: ±{params_std}")
```

### Bounds on Parameters
Constrain parameter ranges using the `bounds` argument:

```python
params_opt, _ = curve_fit(
    model_func,
    x_data, y_noisy,
    p0=[1, 1, 1],
    bounds=([0, 0, 0], [3, 5, 1])  # [lower_bounds], [upper_bounds]
)
```

---

## 4. **Complete Example: Fitting a Gaussian Curve**

```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Model: Gaussian function
def gaussian(x, amplitude, mean, std):
    return amplitude * np.exp(-((x - mean) / std)**2 / 2)

# Generate noisy data
x = np.linspace(-5, 5, 100)
y_true = gaussian(x, 3, 0, 1)
y_noisy = y_true + 0.5 * np.random.randn(x.size)

# Fit
params_opt, params_cov = curve_fit(
    gaussian, x, y_noisy,
    p0=[2, 0, 1]  # Initial guess: [amplitude, mean, std]
)

# Results
amp, mu, sigma = params_opt
print(f"Amplitude: {amp:.2f}, Mean: {mu:.2f}, Std: {sigma:.2f}")

# Plot
plt.scatter(x, y_noisy, label="Noisy Data")
plt.plot(x, gaussian(x, *params_opt), 'r-', label="Fitted Curve")
plt.legend()
plt.show()
```

---

## 5. **When to Use Curve Fitting vs. Interpolation**
| **Curve Fitting** | **Interpolation** |
|--------------------|--------------------|
| Noisy data | Precise data points |
| Known/assumed model (e.g., exponential, polynomial) | No assumed model |
| Parameter estimation | Smooth curve through points |
| Forecasting beyond data range | Interpolation within data range |

---

## Key Takeaways
1. **Model Selection**: Choose a model that reflects the underlying process (e.g., exponential for decay, Gaussian for distributions).
2. **Initial Guesses**: Provide reasonable `p0` to avoid convergence issues.
3. **Uncertainty**: Use `params_cov` to assess parameter reliability.
4. **Validation**: Visualize fits and calculate residuals to detect model mismatch.