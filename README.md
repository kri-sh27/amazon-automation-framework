# Amazon Automation Framework

## Overview

This project is a Hybrid Test Automation Framework developed using **Python, Selenium, Pytest, and Page Object Model (POM)** to automate Amazon shopping workflows.

The framework automates the following scenarios:

### Test Case 1

* Navigate to Amazon
* Search for an iPhone device
* Open the selected product
* Retrieve and print the product price
* Add the product to the cart

### Test Case 2

* Navigate to Amazon
* Search for a Samsung Galaxy device
* Open the selected product
* Retrieve and print the product price
* Add the product to the cart

Both test cases are executed in **parallel** using Pytest-XDist to demonstrate concurrency and execution efficiency.

---

# Framework Architecture

This framework follows a **Hybrid Framework** approach by combining:

* Page Object Model (POM)
* Object Repository
* Externalized Configuration Management
* Parallel Test Execution
* Reporting and Logging

## Design Patterns Used

### 1. Page Object Model (POM)

All page-specific actions and web elements are encapsulated within dedicated page classes.

Benefits:

* Improved code readability
* Reusable page methods
* Reduced code duplication
* Easier maintenance

---

### 2. Object Repository

All locators are maintained in an external `locators.properties` file.

Example:

```properties
home.search_box=id=twotabsearchtextbox
product.add_to_cart=id=add-to-cart-button
```

Locators are dynamically loaded at runtime using a custom locator parser.

Benefits:

* Separation of test logic and UI locators
* No locator hardcoding in Python files
* Easy maintenance
* Faster updates when UI changes

---

### 3. Hybrid Framework

The framework combines the strengths of multiple automation approaches.

Key Advantages:

✅ Easy maintenance

✅ Separation of test logic and locators

✅ Non-developers can update locators without modifying code

✅ No code changes required for locator updates

✅ Highly scalable for enterprise-level automation suites

✅ Reusable and modular framework design

✅ Demonstrates framework engineering skills rather than simple scripting

---

# Project Structure

```text
amazon-automation-framework/
│
├── config/
│   ├── config.properties
│   ├── locators.properties
│   └── lambdatest.properties
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_results_page.py
│   └── product_page.py
│
├── tests/
│   ├── test_iphone.py
│   └── test_galaxy.py
│
├── utilities/
│   ├── config_reader.py
│   ├── locator_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
│
├── reports/
├── screenshots/
├── logs/
│
├── .github/
│   └── workflows/
│       └── automation.yml
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
single Command to create the folder structure 

``` bash

mkdir -p amazon-automation-framework/{config,pages,tests,utilities,reports,screenshots,logs,.github/workflows} && \
touch amazon-automation-framework/config/{config.properties,locators.properties,lambdatest.properties} && \
touch amazon-automation-framework/pages/{base_page.py,home_page.py,search_results_page.py,product_page.py} && \
touch amazon-automation-framework/tests/{test_iphone.py,test_galaxy.py} && \
touch amazon-automation-framework/utilities/{config_reader.py,locator_reader.py,driver_factory.py,logger.py,screenshot.py} && \
touch amazon-automation-framework/.github/workflows/automation.yml && \
touch amazon-automation-framework/{conftest.py,pytest.ini,requirements.txt,README.md}

```


---

# Technology Stack

| Component          | Technology                 |
| ------------------ | -------------------------- |
| Language           | Python 3.x                 |
| Automation Tool    | Selenium WebDriver         |
| Test Framework     | Pytest                     |
| Parallel Execution | Pytest-XDist               |
| Reporting          | Pytest HTML Report, Allure |
| Design Pattern     | Page Object Model          |
| Framework Type     | Hybrid Framework           |
| Version Control    | Git                        |
| CI/CD              | GitHub Actions             |
| Cloud Execution    | LambdaTest (Optional)      |

---

# Installation

Clone the repository:

```bash
git clone https://github.com/kri-sh27/amazon-automation-framework
```

Navigate to project directory:

```bash
cd amazon-automation-framework
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate virtual environment:

### Windows

```bash
myenv\Scripts\activate
```

### Linux/Mac

```bash
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Execute Tests

Run all tests:

```bash
pytest -v
```

Run tests in parallel:

```bash
pytest -n 2
```

Generate HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

View Allure Report:

```bash
allure serve allure-results
```

---

# Configuration Management

Framework configuration is maintained externally.

## config.properties

```properties
url=https://www.amazon.in
browser=chrome
execution=local
```

## locators.properties

```properties
home.search_box=id=twotabsearchtextbox
home.search_button=id=nav-search-submit-button
```

This approach ensures that locator updates can be managed independently of test code changes.

---

# Logging

The framework captures execution logs inside:

```text
logs/framework.log
```

Benefits:

* Easier debugging
* Better traceability
* Improved defect analysis

---

# Screenshot Capture

Screenshots are automatically captured upon test failure.

Location:

```text
screenshots/
```

Benefits:

* Faster root cause analysis
* Improved debugging
* Better defect reporting

---

# CI/CD Integration

GitHub Actions pipeline is included to support automated execution on every code push.

Workflow File:

```text
.github/workflows/automation.yml
```

Pipeline Activities:

* Checkout source code
* Setup Python environment
* Install dependencies
* Execute tests
* Publish reports

---

# LambdaTest Integration (Bonus)

The framework is designed to support execution on LambdaTest Cloud Grid.

Benefits:

* Cross-browser testing
* Cloud execution
* Scalable parallel testing
* Remote execution support

---


## LambdaTest Cloud Execution

The framework supports execution on LambdaTest Selenium Grid.

Features:
- Cloud-based browser execution
- Cross-browser compatibility testing
- Parallel execution
- Remote test monitoring
- Scalable infrastructure

Run:

pytest -n 2

The tests will execute in parallel on LambdaTest Cloud.

---

# Future Enhancements

* Data Driven Testing
* API Integration Testing
* Database Validation
* Docker Support
* Jenkins Pipeline Integration
* AWS Execution Support
* Test Retry Mechanism
* Extent Reporting
* Slack Notifications

---

# Author

Krishnat Hogale

QA Automation Engineer | Selenium | Python | API Testing | CI/CD | AWS | DevOps
