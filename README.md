# Bank Transfers API Tests

[![API Tests](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)

API test automation project in Python (**pytest**) built as a complement
to manual QA practice, for a simplified banking transfers domain.  
The suite includes a lightweight **FastAPI mock server** so tests can run
**locally and in CI** without relying on external environments.

## Tech Stack

- Python, pytest
- FastAPI (mock server)
- GitHub Actions (CI)

## What's Covered

- **Smoke:** health check, login
- **Regression:** transfer creation (happy path), negative amount, insufficient funds
- **Idempotency:** `Idempotency-Key` header handling

## How to Run Locally

**Requirements:** Python 3.10+

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the mock API (Terminal 1):
```bash
uvicorn mock_server:app --host 127.0.0.1 --port 8000
```

Run tests (Terminal 2):
```bash
export BASE_URL=http://127.0.0.1:8000
pytest -m smoke
pytest -m regression
```

## Project Structure
```
config/                 environment configuration
src/client/             API client wrapper
tests/api/              API test cases
mock_server.py          mock banking API
.github/workflows/      CI pipeline (GitHub Actions)
```

## Notes

- Tests validate status codes, response payloads, and business rules.
- Designed to be reliable and reproducible: no dependency on shared QA environments.
- CI runs smoke + regression on push/PR via GitHub Actions.
- HTML reports are available in GitHub Actions → workflow run → Artifacts → `pytest-reports` (includes `smoke-report.html` and `regression-report.html`).

## Author

**Grettel Carrasco** — QA Analyst  
Manual QA with automation skills in API testing (Python/pytest).
