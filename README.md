# OpenCart-QA Selenium Python Automation Framework_V1
- This project is a professional-grade UI automation framework built to validate e-commerce workflows on the OpenCart platform using:Python (Programming Language)

Selenium WebDriver (Browser Automation)

Pytest (Test Runner & Assertions)

Page Object Model (POM) (Design Pattern)

Data-Driven Testing (DDT) (Excel Integration)
# PROJECT OVERVIEW:
it is a high-performance, hybrid automation framework engineered to validate complex e-commerce workflows on the OpenCart platform. The project is designed with a focus on scalability and maintainability, ensuring that UI changes require minimal code updates. By integrating Data-Driven logic, this framework allows for exhaustive testing of authentication and registration flows using externalized Excel data.

# Framework structure
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


```
# Environment Setup
-> To quickly set up the automation environment, run install_packages.bat. It will automatically install the following essential plugins: 

Pytest: Framework for test execution and assertions. 
Selenium: WebDriver for browser automation. 
Webdriver-manager: Automatic management of binary drivers for different browsers. 
Pytest-html : Tools for generating professional test reports. 
Openpyxl: Engine used to read and write Excel data for Data-Driven Testing. 
Pytest-xdist: Plugin for running tests in parallel to save execution time.
```
