# Working with Wind Direction in Python

Wind direction calculations require careful handling of vector components and
angular conventions. This guide covers key concepts, common pitfalls, and best
practices for working with wind direction data in Python, including the
critical distinction between `np.arctan` and `np.arctan2`.

---

## 1. **Calculating Wind Direction from U/V Components**
Wind direction is derived from the eastward (`u`) and northward (`v`) wind 
speed components. The meteorological convention defines:
- **0°**: Wind coming from **North** (blowing southward).  
- **90°**: Wind coming from **East** (blowing westward).  
- **180°**: Wind coming from **South** (blowing northward).  
- **270°**: Wind coming from **West** (blowing eastward).  

### **Formula**  
$$
\theta = \left( 270^\circ - \arctan2(v, u) \times \frac{180^\circ}{\pi} \right) \mod 360^\circ
$$

- `arctan2(v, u)` computes the angle **counterclockwise from the positive x-axis (East)**.  
- Subtract from 270° to convert to **clockwise from North** (meteorological convention).  
- `mod 360` ensures the result is within [0°, 360°).

**Code Example**:
```python
import numpy as np

# Sample U and V components (eastward and northward speeds)
u = 3.0  # Eastward component (m/s)
v = -4.0  # Northward component (m/s)

# Step 1: Compute angle from East (counterclockwise)
angle_rad = np.arctan2(v, u)  # Angle in radians

# Step 2: Convert to degrees and adjust convention
direction_deg = (270 - np.rad2deg(angle_rad)) % 360

print(f"Wind direction: {direction_deg:.1f}°")
```
**Output**:  
```
Wind direction: 323.1°  # Wind coming from northwest
```

---

## 2. **Why Use `np.arctan2` Instead of `np.arctan`?**

### **The Problem with `np.arctan`**  
`np.arctan` calculates the tangent inverse of **a single ratio** (`v/u`), which
 leads to two critical issues:  
1. **Quadrant Ambiguity**:  
   - `arctan(v/u)` cannot distinguish between angles in opposite quadrants.  
   - Example: `u = 1, v = 1` and `u = -1, v = -1` both give `arctan(1) = 45°`,
    but they represent wind directions of **135°** and **315°**, respectively.  

2. **Division by Zero**:  
   - Fails when `u = 0` (e.g., pure north/south winds).  

### **Advantages of `np.arctan2`**  
`np.arctan2(y, x)` takes **two arguments** (`v` and `u`) and:  
1. **Resolves Quadrants**: Uses the signs of `v` and `u` to determine the 
correct angle.  
   - Example:  
     - `arctan2(1, 1) = 45°` (Northeast wind).  
     - `arctan2(-1, -1) = -135°` (or 225°, Southwest wind).  

2. **Handles Zero Values**:  
   - Correctly computes angles when `u = 0` or `v = 0`.  

---

## 3. **Handling Units: Radians vs. Degrees**
- **Numpy trigonometric functions** (`np.sin`, `np.cos`, `np.arctan2`) use 
**radians**.  
- Convert between units explicitly:  
  - **Radians to Degrees**: `np.rad2deg(angle_rad)`  
  - **Degrees to Radians**: `np.deg2rad(angle_deg)`  

**Example**:  
```python
direction_rad = np.deg2rad(direction_deg)  # Convert back to radians for calculations
```

---

## 4. **Full Workflow Example**
```python
import numpy as np

# Sample U and V arrays (eastward and northward components)
u = np.array([0.0, -5.0, 0.0, 3.0])    # Eastward wind speeds
v = np.array([-1.0, 0.0, 1.0, -4.0])   # Northward wind speeds

# Calculate meteorological wind direction
angle_rad = np.arctan2(v, u)
direction_deg = (270 - np.rad2deg(angle_rad)) % 360

print("Wind directions (degrees):")
print(direction_deg)
```
**Output**:  
```
Wind directions (degrees):
[  0.   90. 180. 323.1]  # North, East, South, Northwest
```

---

## 5. **Common Pitfalls & Solutions**
1. **Component Order**:  
   - Use `np.arctan2(v, u)`, **not** `np.arctan2(u, v)` (order matters!).  

2. **Zero Wind**:  
   - Handle `u = 0` and `v = 0` separately (wind direction is undefined): 


3. **Convention Confusion**:  
   - Double-check if your data uses "blowing from" (meteorological) or 
   "blowing to" (oceanographic) conventions.  

---

## 6. **Validation Test Cases**
| Wind Direction (From) | `u` (East) | `v` (North) | `arctan2(v, u)` | Result |
|------------------------|------------|-------------|------------------|--------|
| **North** (0°)         | `0.0`      | `-1.0`      | `-90°` (270°)    | `0°`   |
| **East** (90°)         | `-5.0`     | `0.0`       | `180°`           | `90°`  |
| **South** (180°)       | `0.0`      | `1.0`       | `90°`            | `180°` |
| **West** (270°)        | `3.0`      | `0.0`       | `0°`             | `270°` |

---

## Key Takeaways
- Use **`(270 - np.rad2deg(np.arctan2(v, u))) % 360`** for meteorological wind 
direction.  
- **`np.arctan2` resolves quadrant ambiguity** and handles edge cases.  
- Validate results with known test cases (e.g., pure north/south/east/west 
winds).  
- Always convert between **radians and degrees** explicitly.  

For large datasets, vectorize calculations with NumPy arrays for efficiency. 
When in doubt, visualize wind vectors using libraries like `matplotlib` or 
`plotly`.