---
Pytest Example
---

The code to generate xml coverage report:
```
pytest --cov-config=tests/.coveragerc --cov-report xml:./tests/reports/coverage.xml --cov=./ ./
```
The code to generate HTML coverage report:
```
pytest --cov-config=tests/.coveragerc --cov-report html:./tests/reports/coverage --cov=./ ./  
```

The code to generate HTML test report:
```
pytest --cov-config=tests/.coveragerc --cov-report html:./tests/reports/coverage --cov=./ ./  
```

[Reporting](https://pytest-cov.readthedocs.io/en/latest/reporting.html)

