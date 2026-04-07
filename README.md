# OpenCart-QA Selenium Python Automation Framework_V1
This project is a professional-grade UI automation framework built to validate e-commerce workflows on the OpenCart platform using:
- Python (Programming Language)
- Selenium WebDriver (Browser Automation)
- Pytest (Test Runner & Assertions)
- Page Object Model (POM) (Design Pattern)
- Data-Driven Testing (DDT) (Excel Integration)
- Allure & Pytest Html - (Reporting)

# PROJECT OVERVIEW:
it is a high-performance, hybrid automation framework engineered to validate complex e-commerce workflows on the OpenCart platform. The project is designed with a focus on scalability and maintainability, ensuring that UI changes require minimal code updates. By integrating Data-Driven logic, this framework allows for exhaustive testing of authentication and registration flows using externalized Excel data.

# It focuses on:
1) **User Registration** : Functional sign-up flow validation with dynamic data.
2) **Authentication** : Standard valid/invalid login verification.
3) **Data-Driven Login** : Exhaustive testing of multiple user scenarios using externalized Excel data.
4) **Account Management** and login Validation workflows by Data driven testing.

# Framework Tools Used: 
- Selenium: Web Driver
- Pytest
- Openpyxl: Excel data manipulation for DDT.
- Pytest-html: Visual HTML report generation.
- Pytest-xdist: Parallel test execution.
- Allure-pytest: Advanced reporting integration.
- Pytest-ordering: Test execution sequence control.

# Project structure
----------------------
```
Project_Root/
├── configurations/                # Global Environment Settings
│   └── config.ini                 # Stores Base URL and Credentials
├── pageObjects/                   # POM Design Pattern Implementation
│   ├── base_page.py               # Reusable Selenium wrappers
│   ├── Home_Page.py               # Homepage navigation logic
│   ├── login_Page.py              # Authentication logic
│   ├── Account_Page.py            # Dashboard components
│   └── AccountRegistrationPage.py  # Sign-up flow management
├── testCases/                     # Pytest Test Suite
│   ├── conftest.py                # Browser setup and teardown fixtures
│   ├── test_001_Reg.py            # Functional sign-up test
│   ├── test_002_Login.py          # Basic authentication test
│   └── test_003_ddtLogin.py       # Data-driven Excel tests
├── testData/                      # External Data Management
│   └── Opencart_LoginData.xlsx    # Test data for DDT
├── utiLites/                      # Reusable Helper Modules
│   ├── readProperties.py          # Configuration parser
│   ├── custom_Logger.py           # Execution tracking
│   ├── XLUtils.py                 # Excel Helper Utilities
│   └── randomString.py            # Dynamic data generator
├── Logs/                          # Runtime Traceability
├── reports/                       # Historical Execution Evidence
│   └── YYYY-MM-DD_HH-MM-SS/       # Unique folder for each run
├── requirements.txt               # Project dependency manifest
├── run.bat                        # One-click Suite Execution
└── install_packages.bat           # One-click Environment Setup
```

## Setup & Execution
1. Clone the repository  
2. Create virtual environment  
3. Install dependencies  
4. Run tests

# Instructions :
1. Clone the repository
   - git clone git@github.com:khajask603/OpenCart-Framework_A1.git
3. Create virtual environment
   - python -m venv .venv
4. python -m venv .venv
   - .venv\Scripts\activate
5. Install dependencies
   - pip install -r requirements.txt
                (or)
   - Double Click the " install_packages.bat " File
6. Run tests
   - pytest -v -s

## Reports & Evidence
- Local HTML Reports : After each run, a new folder is created in reports/ using the format YYYY-MM-DD_HH-MM-SS. Inside, you will find:
    - HtmlReports/report.html: An interactive summary of all test results.
    - screenshots/: Automated screen captures taken specifically at the point of any test failure for rapid debugging.

## Runtime Logging
- Detailed step-by-step execution logs are maintained in Logs/automation.log to provide full traceability for every test action.

## Future Enhancements
- Allure Reporting Integration
- CI/CD using Jenkins & GitHub Actions

## Author

**Khaja Mohiddin**  
 - Senior Test Engineer.
