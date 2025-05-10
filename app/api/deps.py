from jose import jwt, JWTError
from fastapi import Request, HTTPException

SECRET_KEY = "your-secret"  # same as in .env or auth_service

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
    except JWTError:
        raise HTTPException(status_code=401, detail="❌ Invalid token")
