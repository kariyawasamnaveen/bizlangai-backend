from jose import jwt, JWTError
from fastapi import Request, HTTPException

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET", "default-fallback-secret-key")

def get_current_user(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="❌ No token provided")

    try:
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=["HS256"])
        return {
            "user_id": payload.get("user_id"),
            "role": payload.get("role")
        }
    except JWTError as e:
        print(f"❌ JWT Error: {e} | Token: {token[:15]}... | Secret: {SECRET_KEY}")
        raise HTTPException(status_code=401, detail="❌ Invalid token")
