#  E-Commerce API QA Automation Framework

This project simulates testing of a RESTful e-commerce API. Built using Python, Pytest and Requests with Allure reporting and GitHub Actions CI integration.

## 🔧 Stack
- Python 3.11
- Pytest
- Requests
- Allure
- GitHub Actions

##  Run Tests
```bash
pip install -r requirements.txt
pytest
allure serve reports/
```

##  Structure
```
tests/ - Test cases
utils/ - Helper functions
data/ - Test data
.github/ - CI config
reports/ - Allure reports
```
