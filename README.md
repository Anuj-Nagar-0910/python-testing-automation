# 🚀 Python Test Automation Framework

![Build Status](https://github.com/Anuj-Nagar-0910/python-testing-automation/actions/workflows/ci.yml/badge.svg)

[![Allure Report](https://img.shields.io/badge/Allure-Report-blue)](https://Anuj-Nagar-0910.github.io/python-testing-automation)

[![codecov](https://codecov.io/gh/Anuj-Nagar-0910/python-testing-automation/branch/main/graph/badge.svg)](https://codecov.io/gh/Anuj-Nagar-0910/python-testing-automation)
---

## 📌 Project Overview

This project demonstrates a **Python-based automated testing framework** using:

- ✅ Pytest (Test Execution)
- ✅ Allure (Advanced Reporting)
- ✅ GitHub Actions (CI/CD Pipeline)
- ✅ CAN Simulation (python-can)

---

## 🧠 Key Features

- Automated test execution on every code push
- Interactive Allure reports hosted on GitHub Pages
- Structured logging (Input / Expected / Actual)
- CI/CD integration with GitHub Actions
- Scalable test architecture

---

## 📁 Project Structure

```md
python-testing-automation/
│
├── demos/
│   ├── src/
│   ├── tests/
│   ├── conftest.py
│   ├── requirements.txt
│
├── .github/workflows/
│   └── ci.yml
│
├── README.md
````

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/anuj-nagar-0910/python-testing-automation.git
cd python-testing-automation/demos
````

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Tests

```bash
pytest
```

---

### 4. Generate Allure Report (Local)

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🌐 CI/CD Pipeline

This project uses **GitHub Actions** to:

* Automatically run tests on push
* Generate Allure reports
* Publish reports via GitHub Pages

---

## 📊 View Allure Report

👉 [Click Here to View Report](https://anuj-nagar-0910.github.io/python-testing-automation/)

---

## 🧪 Sample Test Scenario

* CAN message transmission
* Validation of arbitration ID
* Payload verification
* Logging of Input / Expected / Actual values

---

## 🛠️ Tools & Technologies

* Python 3.11
* Pytest
* Allure Reporting
* GitHub Actions
* python-can

---

## 🎯 Future Enhancements

* UDS diagnostic testing
* Real CAN hardware integration
* Parallel execution
* Dashboard analytics

---

## 👨‍💻 Author

**Anuj Nagar**

---

## ⭐ If you found this useful, consider giving a star!



