
# Interpolation in Python: An Introduction with `Numpy` and  `SciPy`

Interpolation is a technique used to estimate unknown values between known data
points. It is widely used in data analysis, signal processing, and scientific 
computing. Python provides powerful libraries like `Numpy` and `SciPy` for 
interpolation tasks. It will also be a basic operation you need to do for your
final projects in this course, especially for **Wind resource assessment** and 
**Wind turbine modelling**. 

Below is an overview of common methods with code examples.

---

## 1. **Linear Interpolation with NumPy**
NumPy's `np.interp` function performs simple linear interpolation for 1D 
arrays.

```python
import numpy as np

# Sample data points
x = np.linspace(0, 10, 10)
y = np.sin(x)

# New points to interpolate (including values outside the original range)
x_new = np.linspace(-2, 12, 100)  # Extends beyond [0, 10]

# Perform linear interpolation with out-of-bounds handling
y_new = np.interp(x_new, x, y, left=-1, right=2)  # Set values for x < x.min() and x > x.max()

print(y_new)  # Uses -1 and 2 for out-of-range points

# Sometimes you want nan values for out-of-range points
y_new2 = np.interp(x_new, x, y, left=np.nan, right=np.nan)

print(y_new2)  # Return np.nan for out-of-range points
```

**Key Notes:**
- `x` must be monotonically increasing.
- Use `left` and `right` to define values for extrapolation.

---

## 2. **Advanced Interpolation with SciPy**
SciPy's `interpolate` module offers flexible interpolation and extrapolation 
methods.

### **Example 1: Extrapolation with `interp1d`**
Use `fill_value="extrapolate"` to allow extrapolation beyond the original range:

```python
from scipy import interpolate

# Create interpolation function with extrapolation
f_cubic = interpolate.interp1d(x, y, kind='cubic', fill_value="extrapolate")

# Evaluate at points outside [0, 10]
x_extrap = np.linspace(-2, 12, 100)
y_extrap = f_cubic(x_extrap)  # Works for all x_extrap

print(y_extrap) # there are values below -1 and above 1 due to extrapolation

# To avoid wrong extrapolation, you can disable fill_value, and the default 
# behavior will b: a ValueError is raised any time interpolation is attempted 
# on a value outside of the range of x
f_cubic_no_extrap = interpolate.interp1d(x, y, kind='cubic')

# Evaluate at points outside [0, 10]
x_extrap = np.linspace(-2, 12, 100)
y_no_extrap = f_cubic_no_extrap(x_extrap)  # Will raise a Value Error

```

### **Example 2: Spline Extrapolation**
`UnivariateSpline` extrapolates automatically but may produce unstable results:

```python
spline = interpolate.UnivariateSpline(x, y, s=0)  # s=0 forces interpolation through all points
y_spline_extrap = spline(x_extrap)  # Extends beyond original range (use with caution!)
```

**Key Notes:**
- For `interp1d`, `fill_value="extrapolate"` enables extrapolation for `linear`, `cubic`, etc.
- Splines extrapolate by default but may diverge rapidly outside the original range.

---

## 3. **2D Interpolation with Extrapolation**
For 2D data, specify extrapolation behavior explicitly:

```python
from scipy.interpolate import RectBivariateSpline

# Sample 2D grid
x = np.linspace(0, 5, 10)
y = np.linspace(0, 5, 10)
z = np.random.rand(10, 10)

# Create interpolation function with extrapolation
interp_func = RectBivariateSpline(x, y, z, extrapolate=True)  # Allow extrapolation

# Evaluate outside original grid (e.g., [0, 7])
x_new = np.linspace(-1, 7, 100)
y_new = np.linspace(-1, 7, 100)
z_new = interp_func(x_new, y_new)
```

---

## Handling Out-of-Range Data: Key Considerations
1. **Extrapolation Risks**:
   - Extrapolation assumes trends continue outside the known data, which can 
   lead to errors.
   - Higher-order methods (e.g., cubic splines) may produce unrealistic values 
   when extrapolated.

2. **Workflow Tips**:
   - Use `np.interp` with `left`/`right` for simple constant extrapolation.
   - For SciPy, set `fill_value="extrapolate"` in `interp1d` or 
   `extrapolate=True` in spline methods, if you want to extrapolate.
   - Validate extrapolated results against domain knowledge or physical 
   constraints.
   - Thinnk about what you expect when out-of-range points are asked, sometimes
   raising Error might be a better choice then extrapolation.

---

## When to Use Which?
- **NumPy's `interp`**: Quick linear interpolation with basic extrapolation.
- **SciPy's `interp1d`**: Flexible extrapolation for higher-order methods.
- **Splines**: Use with caution for extrapolation due to potential instability.
- **2D+ Data**: Enable extrapolation with flags like `extrapolate=True`.
- **More options**: Check other methods and tools in `scipy.interpolate`

Always test extrapolated results critically — interpolation is safer than 
extrapolation!