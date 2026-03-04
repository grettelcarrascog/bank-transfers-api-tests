# Bank Transfers API Tests

API testing project built with Python and pytest to validate core scenarios of a banking transfer service.

Automation is used here as a complement to QA analysis, helping validate repeatable scenarios and regression flows for financial APIs.

## What is tested

The test suite validates key behaviors of a bank transfer API:

- Health endpoint availability
- Authentication flow
- Successful bank transfer creation
- Validation of invalid amounts
- Business rule validation (insufficient funds)
- Idempotency behavior for transfers

## Tech stack

- Python
- Pytest
- Requests
- FastAPI (mock server)
- GitHub Actions

## Run locally

Start the mock API server:

```
uvicorn mock_server:app --host 127.0.0.1 --port 8000
```

Run tests:

```
pytest -v
```

Run smoke tests:

```
pytest -m smoke
```

## Project structure

```
config/            environment configuration
src/client/        API client wrapper
tests/             automated test suites
tests/api/         API test scenarios
mock_server.py     mock banking API
.github/workflows  CI pipeline configuration
```

## Author

Grettel Carrasco  
QA Analyst
