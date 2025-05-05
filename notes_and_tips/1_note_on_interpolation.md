
# Interpolation in Python: An Introduction with `NumPy` and  `SciPy`

Interpolation is a technique used to estimate unknown values between known data
points. It is widely used in data analysis, signal processing, and scientific 
computing. Python provides powerful libraries like `NumPy` and `SciPy` for 
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

## 4. **Interpolation on higher dimensions**
For higher (arbitrary) dimensions, use `RegularGridInterpolator` if the 
provided data points are on a regular or rectilinear grid.

The data must be defined on a rectilinear grid; that is, a rectangular grid 
with even or uneven spacing. Linear, nearest-neighbor, spline interpolations 
are supported. After setting up the interpolator object, the interpolation 
method may be chosen at each evaluation.

```python
from scipy.interpolate import RegularGridInterpolator
import numpy as np

# Example on 3D datas
def f(x, y, z):  
    return 2 * x**3 + 3 * y**2 - z

x = np.linspace(1, 4, 11)
y = np.linspace(4, 7, 22)
z = np.linspace(7, 9, 33)

xg, yg ,zg = np.meshgrid(x, y, z, indexing='ij', sparse=True)

# data is now a 3-D array with data[i, j, k] = f(x[i], y[j], z[k])
data = f(xg, yg, zg)


# define an interpolating function from this data:
interp_func2 = RegularGridInterpolator((x, y, z), data)

# Evaluate the interpolating function at the two poins
pts = np.array([[2.1, 6.2, 8.3],
                [3.3, 5.2, 7.1]])

# You can choose different method when evaluating
# Supported are “linear”, “nearest”, “slinear”, “cubic”, “quintic” and “pchip”.

# Use linear interpolation method
values_interped_linear = interp_func2(pts, method='linear')

# Use cubic spline interpolation method
values_interped_cubic = interp_func2(pts, method='cubic')

# Compare the different values
print(values_interped_linear)
print(values_interped_cubic)
```
For higher (arbitrary) dimensions, use `RegularGridInterpolator` if the 
provided data points are on a regular or rectilinear grid.


## 5. **Practical Examples**
Here we provide two practical examples that are quite relevant for two of the
final projects:

### Interpolation over mutiple files
This example is relevant for the **Wind turbine modelling** project, especially
the 2nd functional requirement:
   - Compute lift coefficient ($C_l$) and drag coefficient ($C_d$) as function 
   of span position ($r$) and angle of attack ($\alpha$)

Assume you have a list of 2D tables of some varialbe over the $x$ and $y$ 
dimension, each table corresponds to a position $r$ in the 3rd dimension, and 
you want to interpolate to find the variable for a point in the 3D space, i.e.,
defined by $x$, $y$ and $r$. 

The following code demonstrates how to do this:

```python
from scipy.interpolate import RegularGridInterpolator
import numpy as np

# these ranges should be strictly ascending or desending
x_range = np.linspace(0, 10, num=11)
y_range = np.linspace(0, 20, num=21)
r_range = np.linspace(0, 100, num= 51)

# Using synthetic data randomly generated as an example for a list of 2D tables
xy_table_list = []
for r in r_range:
   xy_table_list.append(
      np.random.rand(len(x_range), len(y_range)))

# Construct a 3D array with xyr_array[i, j, k] defines the variable for 
# point: x_range[i], y_range[j], r_range[k]
xyr_array = np.zeros((len(x_range), len(y_range), len(r_range)))

for k in range(len(r_range)):
   xyr_array[:, :, k] = xy_table_list[k]

# Construct the interpolate function using `RegularGridInterpolator`
interp_func = RegularGridInterpolator(
   (x_range, y_range, r_range), xyr_array)

# You may wrap the interp_func inside a function:
def get_variable(x, y, r):
   return interp_func((x, y, r), method='linear')

# Test for some points
for index in [[0, 0, 0], [10, 12, 38], [10, 20, 50]]:
   i, j, k = index
   var_real = xy_table_list[k][i, j]
   var_interp = get_variable(x_range[i], y_range[j], r_range[k])
   print(f'For x_range[{i}], x_range[{i}], x_range[{i}], the original variable'
      + f'is : {var_real}, interpolated value is: {var_interp}')
   assert np.isclose(var_real, var_interp)
```


### Interpolation over mutiple time series
This example is relevant for the **Wind resource assessment** project, especially
the 3rd functional requirement:
   - Compute wind speed and wind direction time series at 10 m and 100 m 
   heights for a given location inside the box bounded by the four locations, 
   such as the Horns Rev 1 site, using interpolation.

Assume you have 4 grid point on the x-y plane, each has a time-series of a 
variable (like wind speed) for the same period and with the same time step, 
you need to find the cooresponding time-series for a point in between.

The following code demonstrate how to do this:

```python
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import matplotlib.pyplot as plt

# Grid points on the x-y coordinate
x = [0, 1]   # x/y array should be strictly ascending or desending
y = [0, 1]

# Assume each points hold a time-series with 100 time steps
# here ts_for_4_points[i, j, t] are ts(t) at x[i], y[j]
num_time_steps = 100
ts_for_4_points = np.random.rand(2, 2, num_time_steps)

# Build the interpolation function
interp_func = RegularGridInterpolator((x, y), ts_for_4_points)

# Test for the first point
assert np.all(np.isclose(interp((0, 0)), ts_for_4_points[0, 0, :]))

# interpolate for a point [0.5, 0.5] in between
ts_interp = interp_func((0.5, 0.5), method='linear')

fig = plt.figure()
plt.plot(ts_for_4_points[0, 0, :])
plt.plot(ts_for_4_points[1, 0, :])
plt.plot(ts_for_4_points[0, 1, :])
plt.plot(ts_for_4_points[1, 1, :])
plt.plot(ts_interp)
plt.legend(['point 0', 'point 1', 'point 2', 'point 3',
            'interped'])
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
- **Unstructured data**:
   - `griddata` - Interpolate unstructured N-D data, choosing from 3 methods:
   'linear’, ‘nearest’, ‘cubic’.
   - `NearestNDInterpolator` - Nearest neighbor interpolator on unstructured 
   data in N dimensions
   - `LinearNDInterpolator` - Piecewise linear interpolator on unstructured 
   data in N dimensions.
- **More options**: Check other methods and tools in `scipy.interpolate`.


Always test extrapolated results critically — interpolation is safer than 
extrapolation!