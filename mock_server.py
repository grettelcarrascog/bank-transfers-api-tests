from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI(title="Bank Transfers Mock API")

class LoginRequest(BaseModel):
    username: str
    password: str

class TransferRequest(BaseModel):
    from_account_id: str
    to_account_id: str
    amount: float
    currency: str
    description: str | None = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/auth/login")
def login(req: LoginRequest):
    # mock behavior: any user/pass returns a token
    return {"access_token": "mock-token-123"}

@app.post("/transfers", status_code=201)
def create_transfer(req: TransferRequest, idempotency_key: str | None = Header(default=None, alias="Idempotency-Key")):
    if req.amount <= 0:
        raise HTTPException(status_code=422, detail="amount must be greater than 0")

    if req.currency not in ("ARS", "USD"):
        raise HTTPException(status_code=422, detail="invalid currency")

    # mock insufficient funds rule
    if req.amount >= 999999:
        raise HTTPException(status_code=409, detail="insufficient funds")

    # idempotency: if key exists, return a deterministic id
    transfer_id = f"tx-{idempotency_key}" if idempotency_key else f"tx-{uuid.uuid4()}"

    return {"transfer_id": transfer_id, "status": "COMPLETED"}
