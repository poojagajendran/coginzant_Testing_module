

# Selenium Automation Testing with Pytest

##  Project Overview

This project demonstrates end-to-end web automation testing using **Python, Selenium WebDriver, and Pytest**. It covers Selenium fundamentals, pytest test execution, fixtures, parameterization, assertions, HTML reporting, and screenshot capture on test failures.

The automation tests are executed on the **LambdaTest Selenium Playground** application.

---

##  Hands-On Covered

- Selenium WebDriver
- Pytest Test Framework
- Test Discovery
- Fixtures (conftest.py)
- Assertions
- Parameterized Tests
- HTML Test Reports
- Screenshot Capture on Failure
- Dropdown Handling
- Checkbox Handling
- Form Submission Automation

---

##  Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- pytest-html
- WebDriver Manager
- Google Chrome

---

##  Project Structure

```
Selenium_Pytest_Project/
│
├── conftest.py
├── test_playground.py
├── requirements.txt
├── report.html
├── README.md
└── screenshots/
```

---

##  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Selenium_Pytest_Project.git
```

Navigate to the project folder

```bash
cd Selenium_Pytest_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install selenium pytest pytest-html webdriver-manager
```

---

##  Running the Tests

Run all tests

```bash
pytest -v
```

Run a specific test file

```bash
pytest test_playground.py -v
```

Generate HTML Report

```bash
pytest test_playground.py --html=report.html --self-contained-html
```

---

##  Test Cases

###  Simple Form Demo

- Open Simple Form Demo
- Enter text
- Click Submit
- Verify displayed message

---

###  Checkbox Demo

- Open Checkbox Demo
- Select checkbox
- Verify checkbox is selected
- Deselect checkbox
- Verify checkbox is deselected

---

###  Dropdown Demo

- Open Select Dropdown List
- Select "Wednesday"
- Verify selected option

---

###  Parameterized Testing

Executed with three different inputs:

- Hello
- Selenium Automation
- 12345

Each input is executed as an individual test case.

---

##  HTML Report

Generate the HTML report

```bash
pytest test_playground.py --html=report.html --self-contained-html
```

The report contains

- Test Name
- Execution Time
- Pass / Fail Status
- Summary
- Environment Details

---

##  Screenshot on Failure

Whenever a test fails, a screenshot is automatically captured.

Example

```
test_simple_form_submission_failure.png
```

This helps in debugging failed automation tests.

---

##  Fixtures

### Driver Fixture

Creates a new Chrome browser instance for every test.

Scope

```python
scope="function"
```

Automatically closes the browser after execution.

---

### Base URL Fixture

Provides the application URL to all tests.

```python
https://www.lambdatest.com/selenium-playground/
```

---

##  Assertions Used

```python
assert output.text == message
```

```python
assert checkbox.is_selected()
```

```python
assert not checkbox.is_selected()
```

```python
assert dropdown.first_selected_option.text == "Wednesday"
```

---

##  Application Under Test

LambdaTest Selenium Playground

https://www.lambdatest.com/selenium-playground/

---

##  Learning Outcomes

- Selenium WebDriver Fundamentals
- Pytest Framework
- Explicit Waits
- Test Automation
- Browser Automation
- Assertions
- Fixtures
- Parameterized Testing
- HTML Reporting
- Screenshot Capture
- Dropdown Automation
- Checkbox Automation

---

##  Future Enhancements

- Page Object Model (POM)
- Data Driven Testing
- Cross Browser Testing
- Parallel Test Execution
- Jenkins CI/CD Integration
- GitHub Actions
- Allure Reporting

---

##  Author

**Pooja G**

BE Computer Science Engineering (AI & ML)

Rajalakshmi Institute of Technology

Chennai, Tamil Nadu

---

## ⭐ Repository

If you found this project useful, consider giving it a ⭐ on GitHub.
