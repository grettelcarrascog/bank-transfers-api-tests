import pytest
import uuid

@pytest.mark.regression
def test_create_transfer_happy_path(api):
    payload = {
        "from_account_id": "123",
        "to_account_id": "456",
        "amount": 1000,
        "currency": "ARS",
        "description": "QA portfolio transfer"
    }
    headers = {"Idempotency-Key": str(uuid.uuid4())}

    r = api.post("/transfers", json=payload, headers=headers)
    assert r.status_code in (200, 201)

    data = r.json()
    assert "transfer_id" in data
    assert data.get("status") in ("PENDING", "COMPLETED", "PROCESSING")

@pytest.mark.regression
def test_create_transfer_rejects_negative_amount(api):
    payload = {
        "from_account_id": "123",
        "to_account_id": "456",
        "amount": -10,
        "currency": "ARS"
    }
    r = api.post("/transfers", json=payload)
    assert r.status_code in (400, 422)

@pytest.mark.regression
def test_create_transfer_insufficient_funds(api):
    payload = {
        "from_account_id": "123",
        "to_account_id": "456",
        "amount": 999999999,
        "currency": "ARS"
    }
    r = api.post("/transfers", json=payload)
    assert r.status_code in (400, 409, 422)
