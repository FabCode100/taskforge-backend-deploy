from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(payload: dict):
    return {
        "user_id": "123",
        "token": "fake-token",
        "email": payload.get("email", "")
    }
