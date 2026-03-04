import pytest

@pytest.mark.smoke
def test_health(api):
    r = api.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body.get("status") in ("ok", "OK", "healthy")
