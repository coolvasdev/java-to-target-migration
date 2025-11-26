# Migration Guide: Step 2 - Setup Target Environment

## **Step Overview and Objectives**
In this step, we will set up the target development environment to migrate a Java project to Python. The goal is to establish a Python-based environment that mirrors the functionality of the original Java application and ensures smooth development.

### **Objectives**
1. Install Python and required frameworks/tools.
2. Create a Python project structure that aligns with best practices.
3. Configure build tools for development, testing, and deployment.

---

## **Prerequisites and Dependencies**

### **Prerequisites**
1. **Source Repository Access**: Ensure you have access to the Java project's repository and understand its structure.
2. **Python Installed**: Verify Python (preferably the latest stable version) is installed on your system.
3. **Package Manager Installed**: Ensure `pip` or `pipenv` is available for managing dependencies.

### **Dependencies**
1. **Python Frameworks**: Choose appropriate frameworks based on the Java application functionality:
   - Web applications: Flask or Django
   - CLI tools: Click or Argparse
   - Data processing: Pandas, NumPy, etc.
2. **Build Tools**:
   - `setuptools` or `poetry` for packaging.
   - `pytest` for testing.

---

## **Detailed Implementation Instructions**

### **Task 1: Install Language/Framework**

#### **Step 1.1: Install Python**
1. Download Python from the [official website](https://www.python.org/downloads/).
2. Install Python by following the platform-specific instructions:
   - **Windows**: Run the installer and check the option to "Add Python to PATH."
   - **Mac/Linux**: Use package managers (`brew` for macOS, `apt` for Ubuntu, etc.).
   
   ```bash
   # For Ubuntu/Linux
   sudo apt update
   sudo apt install python3 python3-pip
   ```

3. Confirm installation:
   ```bash
   python3 --version
   pip3 --version
   ```

#### **Step 1.2: Install Framework**
Choose a framework based on your project type:
- **Flask Installation**:
  ```bash
  pip install flask
  ```
- **Django Installation**:
  ```bash
  pip install django
  ```
- Confirm installation:
  ```bash
  flask --version  # For Flask
  django-admin --version  # For Django
  ```

### **Task 2: Setup Project Structure**

#### **Step 2.1: Create a Repository**
1. Clone the source repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a new Python project structure:
   ```bash
   mkdir -p repository/src repository/tests repository/docs
   ```

#### **Step 2.2: Recommended File Structure**
```plaintext
repository/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
├── tests/
│   ├── test_main.py
│   ├── test_utils.py
├── docs/
│   ├── README.md
│   ├── requirements.txt
├── setup.py  # Optional for packaging
```

#### **Step 2.3: Initialize Python Environment**
1. Initialize a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate  # For Windows
   ```

2. Create a requirements file:
   ```bash
   touch docs/requirements.txt
   ```

3. Add initial dependencies:
   ```plaintext
   flask==2.3.3  # Example
   pytest==7.4.0
   ```
   Install dependencies:
   ```bash
   pip install -r docs/requirements.txt
   ```

### **Task 3: Configure Build Tools**

#### **Step 3.1: Set up `pytest` for Testing**
1. Install `pytest`:
   ```bash
   pip install pytest
   ```

2. Create a sample test file:
   ```python
   # tests/test_main.py
   def test_sample():
       assert 1 + 1 == 2
   ```

3. Run tests:
   ```bash
   pytest tests/
   ```

#### **Step 3.2: Create a `setup.py` File (Optional for Packaging)**
1. Add a `setup.py` file:
   ```python
   from setuptools import setup, find_packages

   setup(
       name="repository",
       version="1.0.0",
       packages=find_packages(),
       install_requires=[
           "flask",
           "pytest",
       ],
   )
   ```

2. Build and install locally:
   ```bash
   python setup.py install
   ```

---

## **Code Examples and Snippets**

### **Sample `main.py`**
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **Common Pitfalls and How to Avoid Them**
1. **Missing Virtual Environment**: Always use a virtual environment to avoid dependency conflicts.
   - Fix: Run `python3 -m venv venv` and activate it before installing packages.

2. **Incorrect Framework Choice**: Ensure the target framework aligns with the application's requirements.
   - Fix: Consult documentation (Flask for lightweight, Django for full-stack).

3. **Dependency Issues**: Avoid hard-coding versions unless necessary; use `requirements.txt` or `poetry.lock`.

---

## **Testing Checklist for This Step**
- [ ] Python and pip are installed correctly.
- [ ] Framework is installed and functional (e.g., run `flask --version`).
- [ ] Virtual environment is activated.
- [ ] Project structure aligns with Python best practices.
- [ ] Dependencies are listed in `requirements.txt` and installed.
- [ ] Sample test suite runs successfully via `pytest`.

---

## **Validation Criteria**
1. Python environment is fully set up and functional.
2. Framework is installed and operational.
3. Project structure is complete and matches the desired target structure.
4. Build tools are configured and basic tests pass.

---

## **Troubleshooting Guide**

| **Issue**                       | **Cause**                          | **Solution**                            |
|----------------------------------|-------------------------------------|-----------------------------------------|
| Python not recognized            | PATH not set correctly              | Reinstall Python and check "Add to PATH." |
| Virtual environment not working  | Not activated or missing            | Activate using `source venv/bin/activate`. |
| Dependency installation failure  | Incorrect `requirements.txt` file   | Verify syntax and package names.         |
| Framework commands failing       | Framework not installed properly    | Check installation logs and reinstall.   |

---

## **Resources and References**
- [Python Official Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Django Documentation](https://www.djangoproject.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Setuptools Documentation](https://setuptools.pypa.io/)

---

## **Next Steps**
Proceed to **Step 3: Code Migration**, where you will translate the Java application logic into Python. This includes re-implementing classes, methods, and utilities in Python.

---

### **Estimated Time**: 2-3 hours  
By following this guide, developers can effectively set up a robust Python development environment tailored for their migration needs.