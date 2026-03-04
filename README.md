cat > README.md << 'EOF'
# Bank Transfers API Tests (Python + Pytest)

API test automation framework focused on **bank transfer** scenarios (core flows + business rules), built with **Python + pytest**.
Includes a **FastAPI mock server** so the suite can run locally and in CI without external dependencies.

## What this repo demonstrates
- **API automation framework** structure (client + fixtures + config)
- **Test design** for banking transfers (happy path + validations + business rules)
- **Smoke vs Regression** suites (pytest markers)
- **CI pipeline** with GitHub Actions
- **HTML test reports** generated on every run (CI artifacts)

## Project structure
