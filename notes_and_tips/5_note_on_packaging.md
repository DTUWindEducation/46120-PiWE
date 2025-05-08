# **Organize a Python Package with `pyproject.toml` and `__init__.py`** 

This guide combines modern packaging (using **Hatchling** and `pyproject.toml`)
 with best practices for structuring `__init__.py` to create a clean, 
 maintainable Python package.

---

## **1. Package Structure & `pyproject.toml` Setup**  
Choose one of two directory layouts and configure `pyproject.toml` accordingly.

**Note: for the final projects of this course, you should choose the 2nd 
option, i.e., package inside  `src/` folder.**

---

### **Option 1: Flat Layout (Package in Root Directory)**  
**Structure**:  
```
my_package_folder/
├── pyproject.toml
└── my_package/      # Package directory (same name as project name in .toml file)
    ├── __init__.py  # Required for package initialization
    ├── module.py    # Example module
    └── utils/
        ├── __init__.py
        └── helpers.py
```

**`pyproject.toml` (Hatchling)**:  
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my_package"
version = "0.1.0"
description = "My package"
authors = [{ name = "Your Name" }]
readme = "README.md"
license = "MIT"
dependencies = []  # Add your dependencies here

# Explicitly set source directory (default is "src/")
[tool.hatch.build]
sources = ["."]  # Look in root for packages
```

---

### **Option 2: `src/` Layout (Recommended for Isolation)**  
**Structure**:  
```
my_package_folder/
├── pyproject.toml
└── src/
    └── my_package/  # Package directory inside src/ fikder
        ├── __init__.py
        ├── module.py
        └── utils/
            ├── __init__.py
            └── helpers.py
```

**`pyproject.toml` (Hatchling)**:  
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my_package"
version = "0.1.0"
# ... (same metadata as above) ...

# No extra config needed! Hatchling defaults to "src/" for packages.
```

---

## **2. Writing `__init__.py` for Clarity and Control**  
The `__init__.py` file defines your package’s public API. Below are common patterns:

---

### **Case 1: Minimal `__init__.py` (Empty)**  
**Use Case**: Let users import submodules directly.  

**File**:  
```python
# my_package/__init__.py (empty)
```

**Imports**:  
```python
from my_package.module import some_function  # Explicit submodule import
from my_package.utils.helpers import helper  # Nested submodule
```

---

### **Case 2: Expose Key Symbols**  
**Use Case**: Simplify imports for common functions/classes.  

**File**:  
```python
# my_package/__init__.py
from .module import some_function, MainClass
from .utils.helpers import helper

# Optional: Define version
__version__ = "0.1.0"

# Optional: Limit star imports
__all__ = ["some_function", "MainClass", "helper"]
```

**Imports**:  
```python
from my_package import some_function, MainClass  # Direct access
from my_package import helper  # Imported from nested submodule
```

---

### **Case 3: Subpackage Initialization**  
**Use Case**: Initialize nested packages (e.g., `utils/`).  

**File**:  
```python
# my_package/utils/__init__.py
from .helpers import helper  # Expose helper from utils

__all__ = ["helper"]
```

**Imports**:  
```python
from my_package.utils import helper  # Clean import
```

**Note: for the final projects of this course, we recommend Case 2, so that 
you do do from my_package import some_function.**

---

## **3. Key Takeaways**  
1. **`pyproject.toml` Configuration**:  
   - Use `sources = ["."]` for flat layouts.  
   - `src/` layout requires no extra config (Hatchling default).  

2. **`__init__.py` Roles**:  
   - Empty files mark directories as packages.  
   - Non-empty files define the public API and simplify imports.  
   - Use `__all__` to control `from my_package import *`.  

3. **Versioning**:  
   - Define `__version__` in the root `__init__.py` for consistency.  

4. **Best Practices**:  
   - Prefer `src/` layout to avoid accidental local imports.  
   - Use `__init__.py` to expose a curated API, not to dump all code.  

---

## **4. Full Example Workflow**  

### **Step 1: Install the Package**  
```bash
# Install in editable mode (development)
pip install -e .
```

### **Step 2: Usage**  
```python
# Import from exposed API (if defined in __init__.py)
from my_package import some_function

# Import from submodules directly
from my_package.utils.helpers import helper
```

---

## **Summary Table**  
| **Aspect**               | **Flat Layout**          | **`src/` Layout**          |  
|--------------------------|--------------------------|----------------------------|  
| **Directory**            | `my_package/` in root    | `src/my_package/`          |  
| **`pyproject.toml`**     | `sources = ["."]`        | No extra config            |  
| **Advantage**            | Simplicity               | Isolation from dev files   |  
| **`__init__.py` Role**   | Define API/version       | Same                       |  

---

By combining `pyproject.toml` (Hatchling) with thoughtful `__init__.py` design, you create a package that’s easy to distribute, import, and maintain.