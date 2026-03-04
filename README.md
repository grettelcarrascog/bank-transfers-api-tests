# Bank Transfers API Tests

API test automation project in Python (pytest) for a simplified banking transfers domain.

The suite uses a small FastAPI mock server so tests can run locally and in CI without relying on external environments.
To run the tests locally, start the mock server and then execute the pytest suites.

## What’s covered

- Smoke: health check, login
- Regression: transfer creation (happy path), negative amount, insufficient funds
- Idempotency-Key header handling

## How to run locally

Start the mock API (Terminal 1):

```bash
uvicorn mock_server:app --host 127.0.0.1 --port 8000
```
Run tests (Terminal 2):
```
export BASE_URL=http://127.0.0.1:8000
pytest -m smoke
pytest -m regression
```
## Project structure
```
config/            environment configuration
src/client/        API client wrapper
tests/api/         API test cases
mock_server.py     mock banking API
.github/workflows  CI pipeline (GitHub Actions)
```
## Author
Grettel Carrasco — QA Analyst
