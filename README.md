# OpenCart-QA Selenium Python Automation Framework_V1
This project is a professional-grade UI automation framework built to validate e-commerce workflows on the OpenCart platform using:
- Python (Programming Language)
- Selenium WebDriver (Browser Automation)
- Pytest (Test Runner & Assertions)
- Page Object Model (POM) (Design Pattern)
- Data-Driven Testing (DDT) (Excel Integration)
- Allure & Pytest Html - (Reporting)

# PROJECT OVERVIEW:
it is a hybrid automation framework engineered to validate complex e-commerce workflows on the OpenCart platform. The project is designed with a focus on scalability and maintainability, ensuring that UI changes require minimal code updates. By integrating Data-Driven logic, this framework allows for exhaustive testing of authentication and registration flows using externalized Excel data.

- **Note on Test Environment:** This framework targets the Naveen Automation Labs demo as Alternative  instance of OpenCart. This environment was selected to ensure stable execution by bypassing       production-level security measures (Cloudflare & CAPTCHA) that are intentionally designed to block Selenium-based automation.

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
OpenCart_Automation_Framework/
├── configurations/                # Global Environment Settings
│   └── config.ini                 # Base URL, Credentials, and Environment variables
├── logs/                          # Runtime Traceability (.log files)
├── page_objects/                  # Page Object Model Implementation
│   ├── base_page.py               # Reusable Selenium wrappers (Switches, Waits, JS)
│   ├── home_page.py               # Homepage navigation & locators
│   ├── login_page.py              # Authentication components
│   ├── account_page.py            # User dashboard interactions
│   └── registration_page.py       # Sign-up flow management
├── reports/                       # Historical Execution Evidence
│   └── 2026-04-11_20-45-10/       # Unique Run ID (Auto-generated)
│       ├── html_reports/          # Clean, isolated interactive reports
│       │   └── report.html
│       └── screenshots/           # Failure evidence for debugging
├── test_cases/                    # Pytest Test Suite
│   ├── conftest.py                # Browser fixtures and Report hooks
│   ├── test_001_registration.py   # Functional sign-up test
│   ├── test_002_login.py          # Basic authentication test
│   └── test_003_ddt_login.py      # Data-driven Excel tests
├── test_data/                     # External Data Management
│   └── login_data.xlsx            # Source for DDT (Data-Driven Testing)
├── utilities/                     # Reusable Helper Modules
│   ├── read_properties.py         # Config.ini parser
│   ├── custom_logger.py           # Logging configuration
│   ├── excel_utils.py             # Openpyxl wrappers for Excel
│   └── data_generator.py          # Random strings for dynamic testing
├── requirements.txt               # Project dependency manifest
├── run.bat                        # One-click execution (Standard/Smoke)
└── install_packages.bat           # Environment setup script
```

## Setup & Execution
1. Clone the repository  
2. Create virtual environment  
3. Install dependencies  
4. Run tests

# Instructions :
1. Clone the repository
   - git clone git@github.com:PONNADAPADMINI/OpenCart-Framework_A1.git
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

**Padmini Ponnada**  
 - Senior Test Engineer.
