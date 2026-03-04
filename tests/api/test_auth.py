import os
import pytest

@pytest.mark.smoke
def test_login_returns_token(api):
    username = os.getenv("BANK_USER", "demo_user")
    password = os.getenv("BANK_PASS", "demo_pass")

    r = api.post("/auth/login", json={"username": username, "password": password})
    assert r.status_code == 200

    data = r.json()
    assert "access_token" in data
    assert isinstance(data["access_token"], str)
