# app/api/endpoints/auth.py
from fastapi import APIRouter, HTTPException
from app.utils.hash import hash_password, verify_password
from app.utils.jwt_handler import create_access_token
from app.db.crud import create_user, get_user_by_email

router = APIRouter()

@router.post("/register")
def register(data: dict):
    if get_user_by_email(data["email"]):
        raise HTTPException(status_code=400, detail="❌ Email already exists")

    hashed = hash_password(data["password"])
    create_user(data["username"], data["email"], hashed, data["role"])
    return {"message": "✅ Registered successfully"}

@router.post("/login")
def login(data: dict):
    user = get_user_by_email(data["email"])
    if not user or not verify_password(data["password"], user["password"]):
        raise HTTPException(status_code=401, detail="❌ Invalid credentials")

    token = create_access_token(str(user["_id"]), user["role"])
    return {
        "token": token,
        "role": user["role"],
        "username": user["username"]
    }
